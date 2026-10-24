"""Run after selecting your final domain: python scripts/configure_domain.py https://your-domain"""
from pathlib import Path
from urllib.parse import urlsplit
import sys,re,html,json
if len(sys.argv)!=2:raise SystemExit('Pass your final HTTPS origin as the only argument.')
u=urlsplit(sys.argv[1]);host=u.hostname or ''
if u.scheme!='https' or not host or '.' not in host or u.username or u.password or u.query or u.fragment or u.path not in ('','/') or u.port:raise SystemExit('Use a valid HTTPS domain only, without credentials, port, path, query, or fragment.')
origin='https://'+host.encode('idna').decode();url=origin+'/'
public=Path(__file__).resolve().parents[1]/'public';p=public/'index.html';s=p.read_text()
s=re.sub(r'<link rel="canonical"[^>]*>','',s)
s=re.sub(r'<meta property="og:(?:url|image)"[^>]*>','',s)
logo=re.search(r'<span class="original-logo-window"><img src="([^"]+)"',s).group(1)
s=s.replace('</head>','<link rel="canonical" href="'+html.escape(url,quote=True)+'"><meta property="og:url" content="'+html.escape(url,quote=True)+'"><meta property="og:image" content="'+html.escape(url+logo,quote=True)+'"></head>')
def schema(m):
 d=json.loads(m.group(1));d['url']=url;d['logo']=url+logo;return '<script type="application/ld+json">'+json.dumps(d)+'</script>'
s=re.sub(r'<script type="application/ld\+json">(.*?)</script>',schema,s,flags=re.S);p.write_text(s)
(public/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>'+html.escape(url)+'</loc></url></urlset>')
(public/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+origin+'/sitemap.xml\n')
print('Configured canonical URL, sharing URL/image, Organization URL/logo, sitemap and robots.txt for '+origin)
