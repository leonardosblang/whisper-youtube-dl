import torch
import transcribe
import whisper
from download_video import VideoDownload


class Whisper:
    def __init__(self, model):
        self.model = whisper.load_model(model)
        self.audio = None

    def download_video(self, url):
        self.audio = VideoDownload.download_ytvid_as_mp3(url, "audio")

    def transcribe(self):
        result = self.model.transcribe("audio.mp3")
        return result["text"]


