# 📼 clip-cc-dataset

The `clip-cc-dataset` is a lightweight Python package for accessing and optionally downloading the **CLIP-CC** dataset — a curated collection of **200 YouTube video links with human-written summaries**, intended for research and experimentation in multimodal AI tasks like video comprehension, summarization, and representation learning.

## 📂 Dataset Contents

- `metadata.jsonl`: A JSON Lines file bundled with the package. Each line is a JSON object:

  ```json
  {
    "id": "001",
    "file_link": "https://www.youtube.com/watch?v=abc123",
    "summary": "A man explains the basics of machine learning with real-world examples."
  }
  ```

- No video files are distributed with this package.
- You can optionally download and clip videos to 90 seconds using the built-in helper.

---

## ⚙️ Installation

Clone or install the package using `pip`:

```bash
# Clone manually
git clone https://github.com/yourusername/clip-cc-dataset.git
cd clip-cc-dataset
pip install .

# OR install directly from a Git repo
pip install git+https://github.com/yourusername/clip-cc-dataset.git
```

### 🧱 Dependencies

The downloader requires:
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)
- [`ffmpeg`](https://ffmpeg.org/)

Install with:

```bash
pip install yt-dlp ffmpeg-python
```

Ensure `ffmpeg` is available in your system PATH:

```bash
ffmpeg -version
```

---

## 📦 Package Structure

```bash
clip_cc_dataset/
├── loader.py       # Loads metadata.jsonl
├── downloader.py   # Downloads & clips videos (optional)
metadata/
└── metadata.jsonl  # Video link + summary
```

---

## 🧪 Usage

### 🔍 Load Metadata

```python
from clip_cc_dataset.loader import load_metadata

data = load_metadata()
print(data[0])
# {'id': '001', 'file_link': 'https://youtube.com/…', 'summary': '…'}
```

---

### ⬇️ Download & Clip Videos (Optional)

```python
from clip_cc_dataset.downloader import download_and_clip_dataset

download_and_clip_dataset(
    output_dir="downloads/temp",        # raw download location
    dest_dir="downloads/clips",         # final clipped output
    target_ids={"001", "092"},          # optional: only process these IDs
    cookiefile_path="cookies.txt",      # optional: use for login-restricted videos
    clip_duration=90                    # optional: default = 90 seconds
)
```

This:
- Downloads videos using `yt-dlp`
- Clips the first `90` seconds using `ffmpeg`
- Cleans up intermediate files

---

## 💡 Tips

- If some videos are restricted, export cookies from your browser as `cookies.txt` and pass the path.
- To test without `ffmpeg`, modify format string in `downloader.py` to `'format': 'mp4'` (not recommended for quality).

---

## 📚 Example Applications

- Video summary training and evaluation
- Clip-based representation learning
- Zero-shot video classification
- Grounded video captioning

---

## 📜 License

Specify your license here (e.g., MIT, Apache 2.0).

---

## 👤 Author

**Your Name**  
Email: you@example.com  
GitHub: [@yourusername](https://github.com/yourusername)