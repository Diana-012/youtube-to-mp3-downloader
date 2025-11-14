thonpython
import requests

class Requester:
    def __init__(self, proxy=None, timeout=10):
        self.proxy = proxy
        self.timeout = timeout

    def get(self, url: str):
        return requests.get(
            url,
            proxies={"http": self.proxy, "https": self.proxy} if self.proxy else None,
            timeout=self.timeout
        )