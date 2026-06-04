import re
def clean_text(text: str | None) -> str:
    if not text: return ""
    return re.sub(r"\s+", " ", text).strip()
def normalize_url(url: str | None) -> str | None:
    if not url: return None
    url=url.strip()
    if not url.startswith('http'): url='https://'+url
    return url
def normalize_company_name(name: str | None) -> str:
    return clean_text(name)[:255] if name else 'Unknown company'
def normalize_lead_item(item: dict) -> dict:
    return {"company_name":normalize_company_name(item.get('company_name')), "website":normalize_url(item.get('website')), "title":clean_text(item.get('title'))[:500], "region":clean_text(item.get('region')), "raw_text":clean_text(item.get('raw_text')), "source":clean_text(item.get('source')), "source_url":normalize_url(item.get('source_url')), "budget":clean_text(item.get('budget')), "industry":clean_text(item.get('industry'))}
