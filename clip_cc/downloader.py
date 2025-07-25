import os
import json
import subprocess
from yt_dlp import YoutubeDL

def _get_default_metadata_path():
    """
    Returns the internal metadata.jsonl path included in the package.
    """
    return os.path.join(os.path.dirname(__file__), "..", "metadata", "metadata.jsonl")

def download_video(url, output_path, cookiefile_path=None, use_browser_cookies=False):
    ydl_opts = {
        'outtmpl': output_path,
        'quiet': True,
        'format': 'bv*[vcodec^=avc1]+ba[ext=m4a]/mp4',
    }
    
    if use_browser_cookies:
        # Try to use browser cookies directly
        try:
            ydl_opts['cookiesfrombrowser'] = ('chrome',)  # Try Chrome first
            print("🍪 Attempting to use Chrome browser cookies directly")
        except:
            try:
                ydl_opts['cookiesfrombrowser'] = ('firefox',)  # Try Firefox as fallback
                print("🍪 Attempting to use Firefox browser cookies directly")
            except:
                print("⚠️ Could not access browser cookies")
    elif cookiefile_path:
        # Check if cookie file exists
        if os.path.exists(cookiefile_path):
            ydl_opts['cookiefile'] = cookiefile_path
            print(f"🍪 Using cookies from: {cookiefile_path}")
            # Read first few lines to verify format
            try:
                with open(cookiefile_path, 'r') as f:
                    first_line = f.readline().strip()
                    if first_line.startswith('# Netscape HTTP Cookie File'):
                        print("✅ Cookie file appears to be in correct Netscape format")
                    else:
                        print("⚠️ Cookie file may not be in Netscape format")
                        print(f"First line: {first_line[:50]}...")
            except:
                print("⚠️ Could not read cookie file")
        else:
            print(f"⚠️ Cookie file not found at: {cookiefile_path}")

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def clip_video_ffmpeg(input_path, output_path, duration=90):
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

def download_and_clip_dataset(
    output_dir,
    target_ids=None,
    cookiefile_path=None,
    use_browser_cookies=False,
    clip_duration=90
):
    """
    Downloads and clips videos from the internal metadata file.

    Args:
        output_dir: Temp folder to save raw downloaded videos
        target_ids: Optional set of video IDs to filter
        cookiefile_path: Optional path to YouTube cookies
        use_browser_cookies: Use browser cookies directly (Chrome/Firefox)
        clip_duration: Duration in seconds (default: 90)
    """
    jsonl_path = _get_default_metadata_path()
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
                download_video(url, temp_path, cookiefile_path=cookiefile_path, use_browser_cookies=use_browser_cookies)
                print(f"✂️ Clipping {video_id} to {clip_duration} seconds...")
                clip_video_ffmpeg(temp_path, final_path, duration=clip_duration)
                print(f"✅ Saved: {final_path}")
            except Exception as e:
                print(f"⚠️ Error processing {video_id}: {e}")
            finally:
                if os.path.exists(temp_path):
                    os.remove(temp_path)
    
    if os.path.exists(temp_dir):
        os.removedirs(temp_dir)
