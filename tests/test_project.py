import unittest, tempfile
from pathlib import Path
import pandas as pd
from project import ROOT, generate, clean, predict, FEATURES
from import_uci import build

class ProjectTests(unittest.TestCase):
    def test_generation(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'data.csv'; a=generate(p); b,meta=clean(p)
            self.assertEqual(len(a),1200); self.assertEqual(meta['removed_rows'],0)
            self.assertEqual(list(b.columns),['customer_id',*FEATURES])
    def test_prediction(self):
        r=predict([380,11,11,.35]); self.assertIn('name',r); self.assertIsInstance(r['review_flag'],bool)
    def test_invalid(self):
        for v in [[-1,1,2,.5],[1,1,2,1.1],[1,1,100,.5],[1,0,2,.5],[1,1.2,2,.5]]:
            with self.assertRaises(ValueError): predict(v)
    def test_importer(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'raw.csv'; out=Path(tmp)/'out.csv'
            pd.DataFrame({'InvoiceNo':['1','2','C3'],'StockCode':['A','B','B'],'Quantity':[2,1,-1],'InvoiceDate':['2011-12-01','2011-12-02','2011-12-03'],'UnitPrice':[5,8,8],'CustomerID':[12345,12345,12345]}).to_csv(p,index=False)
            build(p,out); d=pd.read_csv(out); self.assertEqual(d.iloc[0].spend_90d,18); self.assertEqual(d.iloc[0].orders_90d,2)

if __name__=='__main__': unittest.main()
