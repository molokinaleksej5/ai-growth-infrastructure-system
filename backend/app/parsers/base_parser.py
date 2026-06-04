from abc import ABC, abstractmethod
class BaseParser(ABC):
    source_name='base'
    @abstractmethod
    def search(self, query: str, region: str, limit: int = 20) -> list[dict]: pass
