#!/usr/bin/env python3
"""Check that notebook outputs, local CSVs, and absolute paths are not committed."""
import json,re,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
issues=[]
for p in (root/'notebooks').glob('*.ipynb'):
    try:nb=json.loads(p.read_text(encoding='utf-8'))
    except Exception as e:issues.append(f'{p}: invalid JSON: {e}');continue
    for i,c in enumerate(nb.get('cells',[])):
        if c.get('cell_type')!='code':continue
        if c.get('outputs'):issues.append(f'{p}: stored code outputs in cell {i}')
        text=''.join(c.get('source',[]))
        if re.search(r'[A-Za-z]:\\(?:Users|Documents|Desktop|Downloads)\\',text,re.I):issues.append(f'{p}: hardcoded Windows private path in cell {i}')
        if re.search(r'data:image/|base64,',text,re.I):issues.append(f'{p}: embedded binary data in cell {i}')
        if c.get('execution_count') is not None:issues.append(f'{p}: saved execution count in cell {i}')
for p in (root/'data').rglob('*'):
    if p.is_file() and p.name!='.gitkeep':issues.append(f'Local data present in upload package: {p}')
for p in root.rglob('*'):
    if p.is_file() and p.suffix.lower() in {'.csv','.xlsx','.xls','.rar','.zip','.arff','.pkl','.joblib'} and p != root/'figures'/'figure_manifest.csv':
        issues.append(f'Unintended local dataset / model artifact: {p}')
print('\n'.join(issues) if issues else 'PASS: no saved notebook outputs, personal source paths or local datasets in package.')
sys.exit(1 if issues else 0)
