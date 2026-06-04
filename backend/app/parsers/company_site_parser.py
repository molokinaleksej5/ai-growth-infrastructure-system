import re, requests
from bs4 import BeautifulSoup
from app.parsers.normalizer import clean_text, normalize_url
class CompanySiteParser:
    def parse(self, url: str) -> dict:
        url=normalize_url(url)
        try:
            r=requests.get(url,timeout=20,headers={"User-Agent":"Mozilla/5.0"}); soup=BeautifulSoup(r.text,'html.parser')
            text=soup.get_text(' ',strip=True); emails=list(set(re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",text)))
            links=list(set(a['href'] for a in soup.find_all('a',href=True) if 'linkedin.com' in a['href']))
            return {"website":url,"title":clean_text(soup.title.text if soup.title else ''),"description":clean_text(text[:5000]),"emails":emails[:10],"linkedin_links":links[:10]}
        except Exception as e: return {"website":url,"error":str(e)}
