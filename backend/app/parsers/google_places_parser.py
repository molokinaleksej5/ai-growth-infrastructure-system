import requests
from app.config import settings
from app.parsers.base_parser import BaseParser
class GooglePlacesParser(BaseParser):
    source_name='google_places'
    def search(self, query: str, region: str, limit: int = 20) -> list[dict]:
        if not settings.google_places_api_key: return []
        url='https://maps.googleapis.com/maps/api/place/textsearch/json'; params={"query":f"{query} in {region}","key":settings.google_places_api_key}
        data=requests.get(url,params=params,timeout=20).json(); out=[]
        for item in data.get('results',[])[:limit]:
            out.append({"company_name":item.get('name'),"website":None,"title":f"Company found via Google Places: {item.get('name')}","region":region,"raw_text":item.get('formatted_address'),"source":self.source_name,"source_url":f"https://www.google.com/maps/place/?q=place_id:{item.get('place_id')}","budget":None,"industry":query})
        return out
