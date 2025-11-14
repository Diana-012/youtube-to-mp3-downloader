thonpython
import json
import os
import logging
from converters.audio_extractor import AudioExtractor
from converters.url_normalizer import normalize_url
from metadata.youtube_parser import YouTubeMetadata
from metadata.validators import validate_youtube_url
from network.proxy_manager import ProxyManager

logging.basicConfig(level=logging.INFO)

def load_urls(path: str):
    with open(path, "r") as f:
        return json.load(f)

def main():
    input_path = os.path.join(os.path.dirname(__file__), "../data/sample_input.json")
    urls = load_urls(input_path)

    proxy_manager = ProxyManager()
    proxy = proxy_manager.get_proxy()

    extractor = AudioExtractor(proxy=proxy)
    parser = YouTubeMetadata(proxy=proxy)

    results = []

    for url in urls:
        norm = normalize_url(url)
        if not validate_youtube_url(norm):
            logging.warning(f"Invalid URL skipped: {norm}")
            continue

        logging.info(f"Processing: {norm}")

        metadata = parser.extract_metadata(norm)
        file_path = extractor.download_audio(norm)

        results.append({
            "filePath": file_path,
            "information": metadata
        })

    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()