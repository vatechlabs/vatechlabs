"""Configure canonical, OG URLs, JSON-LD and sitemap for all legal pages."""
# SITE-WIDE DOMAIN CONFIG V3
from pathlib import Path
from urllib.parse import urlsplit
import html, json, re, sys
if len(sys.argv) != 2:
    raise SystemExit('Usage: py scripts/configure_domain.py https://www.vatechlabs.com')
u = urlsplit(sys.argv[1])
if (u.scheme != 'https' or not u.hostname or '.' not in u.hostname or u.username or u.password
    or u.path not in ('','/') or u.query or u.fragment or u.port):
    raise SystemExit('Pass an HTTPS domain without path, query, port, or credentials')
origin='https://'+u.hostname.encode('idna').decode('ascii')
public=Path(__file__).resolve().parents[1]/'public'
pages=['index.html','privacy-policy.html','terms-of-use.html','disclaimer.html','cookie-policy.html']
home=(public/'index.html').read_text(encoding='utf-8')
m=re.search(r'<span class="original-logo-window"><img src="([^"]+)"',home)
if not m: raise SystemExit('Original logo not found')
logo=origin+'/'+m.group(1)
for name in pages:
    p=public/name
    if not p.is_file(): raise SystemExit('Missing page: '+str(p))
    s=p.read_text(encoding='utf-8')
    url=origin+('/' if name=='index.html' else '/'+name)
    s=re.sub(r'<link rel="canonical"[^>]*>','',s)
    s=re.sub(r'<meta property="og:(?:url|image)"[^>]*>','',s)
    tags=(f'<link rel="canonical" href="{html.escape(url,quote=True)}">'
          f'<meta property="og:url" content="{html.escape(url,quote=True)}">'
          f'<meta property="og:image" content="{html.escape(logo,quote=True)}">')
    if '</head>' not in s: raise SystemExit('Missing </head> in '+name)
    s=s.replace('</head>',tags+'</head>',1)
    if name=='index.html':
        def update(m):
            d=json.loads(m.group(1));d['url']=origin+'/';d['logo']=logo
            return '<script type="application/ld+json">'+json.dumps(d,ensure_ascii=False)+'</script>'
        s=re.sub(r'<script type="application/ld\+json">(.*?)</script>',update,s,flags=re.S)
    p.write_text(s,encoding='utf-8')
urls=[origin+('/' if n=='index.html' else '/'+n) for n in pages]
(public/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('  <url><loc>'+html.escape(u)+'</loc></url>\n' for u in urls)+'</urlset>\n',encoding='utf-8')
(public/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+origin+'/sitemap.xml\n',encoding='utf-8')
print('Configured site-wide canonical URLs, sharing metadata, sitemap and robots:',origin)
