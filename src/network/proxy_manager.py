thonpython
class ProxyManager:
    def __init__(self, proxies=None):
        self.proxies = proxies or []

    def get_proxy(self):
        return self.proxies[0] if self.proxies else None