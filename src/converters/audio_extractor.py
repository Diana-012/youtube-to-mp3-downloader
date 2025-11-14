thonpython
import os
import logging
from pytube import YouTube

class AudioExtractor:
    def __init__(self, output_dir="downloads", proxy=None):
        self.output_dir = output_dir
        self.proxy = proxy
        os.makedirs(self.output_dir, exist_ok=True)

    def download_audio(self, url: str) -> str:
        yt = YouTube(url, proxies={"http": self.proxy, "https": self.proxy} if self.proxy else None)
        audio_stream = yt.streams.filter(only_audio=True).first()
        if not audio_stream:
            raise RuntimeError("No audio stream available.")

        output_path = audio_stream.download(output_path=self.output_dir)
        mp3_path = output_path.replace(".mp4", ".mp3")

        os.rename(output_path, mp3_path)
        logging.info(f"Downloaded MP3: {mp3_path}")
        return mp3_path