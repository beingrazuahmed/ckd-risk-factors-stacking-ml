#!/usr/bin/env python3
"""Report basic CKD dataset dimensions, source labels and missing values."""
import argparse
import pandas as pd
from pathlib import Path

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--path',default='data/uci_ckd.csv')
    p.add_argument('--expected-rows',type=int,default=400)
    args=p.parse_args()
    path=Path(args.path)
    if not path.is_file():raise SystemExit(f'CSV missing: {path}')
    df=pd.read_csv(path)
    print('Data dimensions:',df.shape)
    print('Column names:',list(df.columns))
    print('Class counts:',df.iloc[:,-1].value_counts(dropna=False).to_dict())
    print('Top missing-count fields:',df.isna().sum().sort_values(ascending=False).head(10).to_dict())
    if df.shape!=(args.expected_rows,25):raise SystemExit('Unexpected dataset shape; check source before running analysis.')
    if not {'ckd','notckd','not ckd'}.issuperset(set(df.iloc[:,-1].astype(str).str.strip().str.lower())):
        raise SystemExit('Unrecognized target class values.')
    print('Basic source shape and labels verified. This is not a clinical data-quality or external-validation audit.')

if __name__=='__main__':main()
