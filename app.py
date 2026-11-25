"""Local web prototype. Run python app.py and visit http://127.0.0.1:8000."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs
import html, json
import joblib
from project import ROOT, predict, FEATURES

ARTIFACT=joblib.load(ROOT/'models/segmenter.joblib')

def page(result=None, error=None):
    output=''
    if error: output=f'<div class="error">{html.escape(error)}</div>'
    if result:
        output=f'<section><h2>{html.escape(result["name"])}</h2><p>{html.escape(result["action"])}</p><p>Segment {result["segment"]} | Centroid margin: {result["centroid_margin"]} | Review: {"Yes" if result["review_flag"] else "No"}</p></section>'
    fields=[('spend_90d','Spend in last 90 days (GBP illustrative)','380','0.01'),('orders_90d','Orders in last 90 days','11','1'),('recency_days','Days since last purchase','11','1'),('favorite_product_share','Favorite product share (0–1)','0.35','0.01')]
    form=''.join(f'<label>{label}<input name="{name}" type="number" min="0" {"max=1" if name=="favorite_product_share" else ""} step="{step}" value="{value}" required></label>' for name,label,value,step in fields)
    return f'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Retail customer segmentation</title><style>body{{font:16px system-ui;background:#edf3f5;color:#16354a;margin:0}}main{{max-width:640px;margin:36px auto;padding:24px;background:white;border-radius:14px}}h1{{font-size:28px}}label{{display:block;margin:16px 0}}input{{display:block;box-sizing:border-box;width:100%;padding:10px;margin-top:6px;border:1px solid #91a9b4;border-radius:6px}}button{{background:#176d71;color:white;border:0;padding:12px 20px;border-radius:6px;font:inherit}}section,.error{{padding:12px;background:#e1f1ec;margin-top:18px;border-radius:8px}}.error{{background:#ffe4e0}}small{{color:#526775}}</style><main><small>PROJECT 27 / UNSUPERVISED LEARNING</small><h1>Customer segmentation</h1><p>Enter purchase behavior to find the nearest customer segment.</p><form method="post">{form}<button>Find segment</button></form>{output}<p><small>Training source: {html.escape(ARTIFACT['source'])}. Educational demonstration only. No personal details required or saved.</small></p></main></html>'''

class Handler(BaseHTTPRequestHandler):
    def send_page(self, body, status=200):
        self.send_response(status); self.send_header('Content-Type','text/html; charset=utf-8'); self.end_headers(); self.wfile.write(body.encode())
    def do_GET(self):
        if self.path=='/': self.send_page(page())
        else: self.send_error(404)
    def do_POST(self):
        if self.path!='/': self.send_error(404); return
        try:
            n=int(self.headers.get('Content-Length','0'))
            if n<1 or n>8192: raise ValueError('Invalid request size')
            fields=parse_qs(self.rfile.read(n).decode()); result=predict([fields[f][0] for f in FEATURES],ARTIFACT)
            self.send_page(page(result))
        except (KeyError,ValueError,UnicodeError) as e: self.send_page(page(error='Invalid values. '+str(e)),400)

if __name__=='__main__':
    print('Open http://127.0.0.1:8000'); ThreadingHTTPServer(('127.0.0.1',8000),Handler).serve_forever()
