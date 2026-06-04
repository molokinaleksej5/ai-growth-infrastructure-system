from app.parsers.base_parser import BaseParser
class DirectoryParser(BaseParser):
    source_name='business_directory_demo'
    def search(self, query: str, region: str, limit: int = 20) -> list[dict]:
        return [{"company_name":f"{region} Digital Services Company","website":"https://example-directory-company.com","title":f"B2B company from directory: {query}","region":region,"raw_text":f"Business directory company related to {query}, region {region}","source":self.source_name,"source_url":"https://example-directory.com/company","budget":None,"industry":query}][:limit]
