import unittest, json, ast, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

class RepoTests(unittest.TestCase):
    def test_notebooks_valid_and_clean(self):
        for file in (ROOT/'notebooks').glob('*.ipynb'):
            nb=json.loads(file.read_text(encoding='utf-8'))
            self.assertEqual(nb['nbformat'],4)
            self.assertGreater(len(nb['cells']),3)
            for cell in nb['cells']:
                if cell['cell_type']=='code':
                    self.assertEqual(cell['outputs'],[])
                    self.assertIsNone(cell['execution_count'])
                    ast.parse(''.join(cell['source']))

    def test_only_one_source_of_truth(self):
        full=json.loads((ROOT/'notebooks'/'CKD_Full_Research_Workflow.ipynb').read_text())
        self.assertEqual(len([x for x in full['cells'] if x['cell_type']=='code']),9)

    def test_public_data_not_bundled(self):
        self.assertEqual(sorted(x.name for x in (ROOT/'data').iterdir()),['.gitkeep'])
        self.assertTrue((ROOT/'.gitignore').is_file())

    def test_source_and_credit_documented(self):
        t=(ROOT/'README.md').read_text()
        for term in ['10.3329/ijss.v25i2.85732','10.24432/C5G020','REPRODUCIBILITY.md','METHODS_AND_LIMITATIONS.md','MIT','CC BY-NC-SA','not an approved clinical']:
            self.assertIn(term,t)

    def test_uci_schema_mapper(self):
        sys.path.insert(0,str(ROOT/'scripts'))
        from fetch_uci_ckd import normalize_uci_data,SOURCE_COLUMNS
        import pandas as pd
        X=pd.DataFrame({x:[0,1] for x in SOURCE_COLUMNS})
        X=pd.concat([X]*200,ignore_index=True)
        y=pd.DataFrame({'class':['ckd','notckd']*200})
        out=normalize_uci_data(X,y)
        self.assertEqual(out.shape,(400,25))
        self.assertEqual(sorted(out['class'].unique()),['ckd','not ckd'])

    def test_alternate_uci_cell_count_aliases(self):
        sys.path.insert(0,str(ROOT/'scripts'))
        from fetch_uci_ckd import normalize_uci_data,SOURCE_COLUMNS
        import pandas as pd
        X=pd.DataFrame({x:[0,1] for x in SOURCE_COLUMNS})
        X=X.rename(columns={'wc':'wbcc','rc':'rbcc'})
        X=pd.concat([X]*200,ignore_index=True)
        y=pd.DataFrame({'class':['ckd','notckd']*200})
        self.assertEqual(normalize_uci_data(X,y).shape,(400,25))

    def test_figures_licensing_separate(self):
        self.assertIn('CC BY-NC-SA',(ROOT/'LICENSING.md').read_text())
        self.assertIn('CC BY 4.0',(ROOT/'DATA_AVAILABILITY.md').read_text())

if __name__=='__main__':unittest.main()
