import os
import json
import subprocess
from yt_dlp import YoutubeDL

def download_video(url, output_path, cookiefile_path=None):
    """
    Download a YouTube video using yt-dlp.
    """
    ydl_opts = {
        'outtmpl': output_path,
        'quiet': True,
        'format': 'bv*[vcodec^=avc1]+ba[ext=m4a]/mp4',
    }
    if cookiefile_path:
        ydl_opts['cookiefile'] = cookiefile_path

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def clip_video_ffmpeg(input_path, output_path, duration=90):
    """
    Clip a video to a specific duration using FFmpeg.
    """
    command = [
        'ffmpeg',
        '-y',
        '-i', input_path,
        '-t', str(duration),
        '-c', 'copy',
        output_path
    ]
    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to clip {input_path}: {e}")
        raise

def download_and_clip_from_jsonl(jsonl_path, output_dir, target_ids=None, cookiefile_path=None):
    """
    Download and clip videos based on a JSONL metadata file.
    
    Args:
        jsonl_path: Path to metadata.jsonl
        output_dir: Directory where final clips will be saved
        target_ids: Set of video IDs to process (optional)
        cookiefile_path: Optional path to YouTube cookies file
    """
    os.makedirs(output_dir, exist_ok=True)
    temp_dir = os.path.join(output_dir, "temp_raw")
    os.makedirs(temp_dir, exist_ok=True)

    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            entry = json.loads(line)
            video_id = entry["id"]
            url = entry["file_link"]

            if target_ids and video_id not in target_ids:
                continue

            temp_path = os.path.join(temp_dir, f"{video_id}_raw.mp4")
            final_path = os.path.join(output_dir, f"{video_id}.mp4")

            print(f"⬇️ Downloading {video_id}...")
            try:
                download_video(url, temp_path, cookiefile_path=cookiefile_path)
                print(f"✂️ Clipping {video_id} to 90 seconds using FFmpeg...")
                clip_video_ffmpeg(temp_path, final_path, duration=90)
                print(f"✅ Saved: {final_path}")
            except Exception as e:
                print(f"⚠️ Error processing {video_id}: {e}")
            finally:
                if os.path.exists(temp_path):
                    os.remove(temp_path)
