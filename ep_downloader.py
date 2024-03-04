import yt_dlp
import os

def download_m3u8(master_url, series_info, episode_data, output_dir='.', overwrites=False):
    dl_path = f'{output_dir}/{series_info["title"]} E{episode_data["number"]:03} - {episode_data["name"]}.%(ext)s'

    opts = {
        'format': 'bestvideo/best',
        'outtmpl': dl_path,
        'overwrites' : overwrites
    }

    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download(master_url)