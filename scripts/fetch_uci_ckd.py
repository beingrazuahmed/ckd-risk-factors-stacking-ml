#!/usr/bin/env python3
"""Fetch and normalize UCI CKD dataset ID 336 without bundling patient records in Git."""
from pathlib import Path
import argparse
import pandas as pd

SOURCE_COLUMNS = ['age','bp','sg','al','su','rbc','pc','pcc','ba','bgr','bu','sc','sod','pot','hemo','pcv','wc','rc','htn','dm','cad','appet','pe','ane']
OUTPUT_COLUMNS = [
    'age','blood pressure','specific gravity','albumin','sugar','red blood cells',
    'pus cell','pus cell clumps','bacteria','blood glucose random','blood urea',
    'serum creatinine','sodium','potassium','hemoglobin','packed cell volume',
    'white blood cell count','red blood cell count','hypertension','diabetes mellitus',
    'coronary artery disease','appetite','pedal edema','anemia','class'
]

def normalize_uci_data(features, targets):
    X=features.copy()
    X.columns=[str(x).strip().lower() for x in X.columns]
    X=X.rename(columns={"wbcc":"wc", "rbcc":"rc"})
    expected=set(SOURCE_COLUMNS)
    if set(X.columns)==expected:
        X=X.loc[:,SOURCE_COLUMNS].copy()
    elif list(X.columns)==OUTPUT_COLUMNS[:-1]:
        X=X.loc[:,OUTPUT_COLUMNS[:-1]].copy()
    else:
        raise ValueError(f'Unexpected UCI feature names: {list(X.columns)}. Cannot safely reorder data. Review source schema.')
    y=targets.iloc[:,0] if isinstance(targets,pd.DataFrame) else targets
    y=y.astype('string').str.strip().str.lower().str.replace(r'\s+', ' ',regex=True)
    allowed={'ckd','notckd','not ckd'}
    if not set(y.dropna().unique()).issubset(allowed):
        raise ValueError(f'Unexpected CKD target labels: {sorted(y.dropna().unique())}')
    y=y.replace({'notckd':'not ckd'})
    df=X.reset_index(drop=True).copy()
    df.columns=OUTPUT_COLUMNS[:-1]
    df['class']=y.reset_index(drop=True)
    if len(df)!=400 or len(df.columns)!=25:
        raise ValueError(f'UCI data expected 400 rows and 25 columns, got {df.shape}')
    if df['class'].isna().any():raise ValueError('UCI target has missing values.')
    return df

def main():
    parser=argparse.ArgumentParser(description='Fetch official UCI CKD dataset 336 into an untracked local CSV')
    parser.add_argument('--out',default='data/uci_ckd.csv',help='Path under which to save normalized 25-column CSV')
    parser.add_argument('--force',action='store_true',help='Overwrite existing local file')
    args=parser.parse_args()
    out=Path(args.out).expanduser()
    if out.exists() and not args.force:raise SystemExit(f'File already exists: {out} (pass --force only if overwrite is intentional)')
    try:
        from ucimlrepo import fetch_ucirepo
    except ImportError as e:
        raise SystemExit('Install requirements first: python -m pip install -r requirements.txt') from e
    dataset=fetch_ucirepo(id=336)
    df=normalize_uci_data(dataset.data.features,dataset.data.targets)
    out.parent.mkdir(parents=True,exist_ok=True)
    df.to_csv(out,index=False)
    print(f'Saved official UCI CKD data to {out} ({df.shape[0]} rows, {df.shape[1]} columns)')
    print('Source: Rubini, Soundarapandian & Eswaran (2015), doi:10.24432/C5G020 (CC BY 4.0).')

if __name__=='__main__':main()
