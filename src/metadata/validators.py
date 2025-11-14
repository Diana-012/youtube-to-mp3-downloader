thonpython
import re

YT_REGEX = re.compile(r"(https?://)?(www\.)?(youtube\.com|youtu\.be)/")

def validate_youtube_url(url: str) -> bool:
    return bool(YT_REGEX.search(url))