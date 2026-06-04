import requests
from bs4 import BeautifulSoup
from app.parsers.base_parser import BaseParser
from app.parsers.normalizer import clean_text
class ClutchParser(BaseParser):
    source_name='clutch'
    def search(self, query: str, region: str, limit: int = 20) -> list[dict]:
        results=[]; url=f"https://clutch.co/search?query={query.replace(' ','+')}"
        try:
            r=requests.get(url,timeout=15,headers={"User-Agent":"Mozilla/5.0"}); soup=BeautifulSoup(r.text,'html.parser')
            cards=soup.select('li.provider-row, div.provider-row')
            for card in cards[:limit]:
                name_el=card.select_one('h3, h2, a'); link_el=card.select_one('a[href]')
                name=clean_text(name_el.get_text()) if name_el else 'Unknown company'; source_url=link_el['href'] if link_el else url
                if source_url.startswith('/'): source_url='https://clutch.co'+source_url
                results.append({"company_name":name,"website":None,"title":f"Potential B2B service company: {name}","region":region,"raw_text":clean_text(card.get_text(' ',strip=True)),"source":self.source_name,"source_url":source_url,"budget":None,"industry":query})
        except Exception:
            pass
        return results[:limit]
