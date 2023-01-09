import torch
import whisper
from download_video import VideoDownload

model = whisper.load_model("base")


VideoDownload.download_ytvid_as_mp3("yourvideourl", "audio")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("GPU available: {}".format(torch.cuda.is_available()))

result = model.transcribe("audio.mp3")
print(result["text"])
with open("text.txt", "w") as f:
    f.write(result["text"])
