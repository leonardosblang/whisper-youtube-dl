from yt_dlp import YoutubeDL

class VideoDownload:
    def download_ytvid_as_mp3(url, name):
        video_info = YoutubeDL().extract_info(url=url, download=False)
        filename = f"{name}.mp3"
        options = {
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': filename,
        }
        with YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
        print("Download complete... {}".format(filename))
