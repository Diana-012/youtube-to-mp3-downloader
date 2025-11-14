thonpython
def normalize_url(url: str) -> str:
    if "youtu.be/" in url:
        code = url.split("youtu.be/")[-1]
        return f"https://www.youtube.com/watch?v={code}"
    return url.strip()