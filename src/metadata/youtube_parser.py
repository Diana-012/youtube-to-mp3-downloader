thonpython
from pytube import YouTube

class YouTubeMetadata:
    def __init__(self, proxy=None):
        self.proxy = proxy

    def extract_metadata(self, url: str) -> dict:
        yt = YouTube(url, proxies={"http": self.proxy, "https": self.proxy} if self.proxy else None)

        return {
            "embed": {
                "iframeUrl": f"https://www.youtube.com/embed/{yt.video_id}",
                "width": 1280,
                "height": 720
            },
            "title": yt.title,
            "description": yt.description,
            "lengthSeconds": yt.length,
            "author": yt.author,
            "keywords": yt.keywords,
            "publishDate": str(yt.publish_date),
            "viewCount": yt.views,
            "thumbnails": [t.url for t in yt.thumbnail_url.split()]
        }