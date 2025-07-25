<img src="assets/CLIP-CC.gif" alt="CLIP-CC Process Flow" width="100%"/>

<div align="center">
  <p align="center">
    <em>A Comprehensive Dataset for Video Comprehension and Multimodal AI Research</em>
    <br />
  </p>
</div>

<div align="center">

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-teal?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-teal?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Dataset](https://img.shields.io/badge/🤗_Dataset-Hugging_Face-ff9500?style=for-the-badge&logo=huggingface&logoColor=white)](https://huggingface.co/datasets/IVSL-SDSU/Clip-CC)

</div>

<p align="center">
  <a href="https://arxiv.org/abs/placeholder-link">📰 Research Paper</a>
  ·
  <a href="https://colab.research.google.com/drive/1FH81YpNAy3dM_wtdnDV9eDe2ZH5vMoab?usp=sharing">📓 Interactive Notebook</a>
</p>

---

## 🤔 What is CLIP-CC?

The **CLIP-CC Dataset** is a carefully curated collection of **200 YouTube video links with human-written summaries**, specifically designed for research and experimentation in multimodal AI tasks. This dataset addresses the growing need for high-quality video comprehension benchmarks that can effectively evaluate the narrative understanding capabilities of Large Video Language Models (LVLMs).

### 🔬 How CLIP-CC is Made

<table align="center" width="100%" style="border-collapse: collapse;">
<tr>
<td width="33%" align="center" style="padding: 12px; vertical-align: top;">
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; padding: 20px; color: white; box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3); height: 300px; display: flex; flex-direction: column;">
<h3 style="margin: 0 0 15px 0; font-size: 1.2em; text-align: center; min-height: 30px; display: flex; align-items: center; justify-content: center;">🎬 Step 1: Curate & Clip</h3>
<div style="font-size: 0.85em; opacity: 0.9; flex-grow: 1;">
<p style="margin: 0 0 10px 0;"><strong>Source:</strong> YouTube's Rotten Tomatoes Movieclips channel</p>
<p style="margin: 0 0 8px 0;"><strong>Selection Criteria:</strong></p>
<ul style="margin: 0; padding-left: 15px; font-size: 0.9em; line-height: 1.4;">
<li>Action-rich scenes with complex events</li>
<li>≥2 recurring actors for multi-character tracking</li>
<li>Multiple scenes/shots for temporal understanding</li>
<li>Characters leave and return (tests identity memory)</li>
<li>Cannot be understood from a single frame alone</li>
</ul>
<p style="margin: 10px 0 0 0;"><strong>Output:</strong> ~90 second clips</p>
</div>
</div>
</td>
<td width="33%" align="center" style="padding: 12px; vertical-align: top;">
<div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 15px; padding: 20px; color: white; box-shadow: 0 8px 25px rgba(240, 147, 251, 0.3); height: 300px; display: flex; flex-direction: column;">
<h3 style="margin: 0 0 15px 0; font-size: 1.2em; text-align: center; min-height: 30px; display: flex; align-items: center; justify-content: center;">🎙️ Step 2: Human Narration</h3>
<div style="font-size: 0.85em; opacity: 0.9; flex-grow: 1;">
<p style="margin: 0 0 10px 0;"><strong>Narration Process:</strong></p>
<ul style="margin: 0; padding-left: 15px; font-size: 0.9em; line-height: 1.4;">
<li>Human watches clip and narrates in real-time</li>
<li>Present tense, factual description style</li>
<li>Consistent entity labels throughout</li>
<li>Audio recording of live narration</li>
<li>Professional transcription to text format</li>
</ul>
<p style="margin: 10px 0 0 0;"><strong>Output:</strong> Raw text transcript</p>
</div>
</div>
</td>
<td width="33%" align="center" style="padding: 12px; vertical-align: top;">
<div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); border-radius: 15px; padding: 20px; color: white; box-shadow: 0 8px 25px rgba(79, 172, 254, 0.3); height: 300px; display: flex; flex-direction: column;">
<h3 style="margin: 0 0 15px 0; font-size: 1.2em; text-align: center; min-height: 30px; display: flex; align-items: center; justify-content: center;">🤖 Step 3: LLM Clean-up</h3>
<div style="font-size: 0.85em; opacity: 0.9; flex-grow: 1;">
<p style="margin: 0 0 10px 0;"><strong>Refinement Process:</strong></p>
<ul style="margin: 0; padding-left: 15px; font-size: 0.9em; line-height: 1.4;">
<li>Feed raw transcript to GPT-4o/ChatGPT</li>
<li>Fix grammar and sentence structure only</li>
<li>Preserve all original content (no drops)</li>
<li>Maintain narrative flow and accuracy</li>
<li>Quality assurance with diff check review</li>
</ul>
<p style="margin: 10px 0 0 0;"><strong>Output:</strong> Final dataset entry</p>
</div>
</div>
</td>
</tr>
</table>

<div align="center">
<table style="border: 2px solid #7c3aed; border-radius: 12px; background: linear-gradient(145deg, #f3e8ff, #e9d5ff); padding: 25px; margin: 20px auto; max-width: 800px;">
<tr>
<td align="center">

**📊 Dataset Statistics**

<table width="100%" style="margin: 15px 0;">
<tr>
<td width="50%" align="center" style="padding: 10px;">

**🎬 Content**
- **200** curated video clips
- **~90 seconds** each
- **100%** YouTube sourced

</td>
<td width="50%" align="center" style="padding: 10px;">

**📝 Summaries**
- **402 words** average
- **349 words** median
- **99-1,011** word range

</td>
</tr>
<tr>
<td width="50%" align="center" style="padding: 10px;">

**🎭 Complexity**
- Multi-scene narratives
- Character identity tracking
- Action-dense sequences

</td>
<td width="50%" align="center" style="padding: 10px;">

**📊 Distribution**
- **57.5%** detailed (300+ words)
- **24.0%** long (200-300 words)
- **17.5%** medium (100-200 words)

</td>
</tr>
</table>

*Sourced from Rotten Tomatoes Movieclips • 3-step curation process*

</td>
</tr>
</table>
</div>

Perfect for evaluating video captioning models, multimodal language models, and narrative understanding systems using advanced metrics like [VCS (Video Comprehension Score)](https://github.com/Multimodal-Intelligence-Lab/Video-Comprehension-Score).

---

## 📂 Dataset Contents & Key Features

### 📊 Dataset Structure

<table align="center" width="100%" style="border-collapse: collapse;">
<tr>
<td width="50%" align="center" style="padding: 15px;">
<div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); border-radius: 15px; padding: 20px; color: white; box-shadow: 0 8px 25px rgba(79, 172, 254, 0.3);">
<h3 style="margin: 0 0 10px 0; font-size: 1.2em;">📋 Metadata Format</h3>
<p style="margin: 0; font-size: 0.9em; opacity: 0.9;">JSON Lines format with video links and summaries</p>
</div>
</td>
<td width="50%" align="center" style="padding: 15px;">
<div style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); border-radius: 15px; padding: 20px; color: white; box-shadow: 0 8px 25px rgba(250, 112, 154, 0.3);">
<h3 style="margin: 0 0 10px 0; font-size: 1.2em;">🎥 Video Access</h3>
<p style="margin: 0; font-size: 0.9em; opacity: 0.9;">Optional download and 90-second clipping utilities</p>
</div>
</td>
</tr>
</table>

**📋 Example Entry (`metadata.jsonl`):**

```json
{
  "id": "001",
  "file_link": "https://www.youtube.com/watch?v=abc123",
  "summary": "A man explains the basics of machine learning with real-world examples."
}
```

---

## ⚡ Getting Started

Choose the installation method that best fits your workflow. All methods provide access to the complete CLIP-CC dataset with 200 video entries and human-written summaries.

<div align="center">
<table style="border: 2px solid #059669; border-radius: 12px; background: linear-gradient(145deg, #d1fae5, #a7f3d0); padding: 15px; margin: 20px 0;">
<tr>
<td align="center">

**⚡ Quick Start Tip:** Most research only needs metadata - video downloading is completely optional!

</td>
</tr>
</table>
</div>

### 📦 Installation Methods

<table align="center" width="100%">
<tr>
<td width="33%" align="center" style="vertical-align: top;">

### 🎯 **Manual Installation**
*Full control and development*

<details>
<summary><b>🖱️ Click to expand steps</b></summary>

<br>

**Terminal:**
```bash
git clone https://github.com/hdubey-debug/CLIP-CC.git
cd CLIP-CC
pip install .
```

**Colab/Jupyter:**
```python
!git clone https://github.com/hdubey-debug/CLIP-CC.git
%cd CLIP-CC
!pip install .
```

<div align="center">

🔧 **Full source access**  
🛠️ **Modification ready**  
📁 **Local development**

</div>

</details>

</td>
<td width="33%" align="center" style="vertical-align: top;">

### 🚀 **Pip Installation**
*Quick and simple*

<details>
<summary><b>🖱️ Click to expand steps</b></summary>

<br>

**Terminal:**
```bash
pip install git+https://github.com/hdubey-debug/CLIP-CC.git
```

**Colab/Jupyter:**
```python
!pip install git+https://github.com/hdubey-debug/CLIP-CC.git
```

<div align="center">

⚡ **30-second setup**  
🔥 **Zero configuration**  
✅ **Instant access**

</div>

</details>

</td>
<td width="33%" align="center" style="vertical-align: top;">

### 🤗 **Hugging Face**
*Seamless dataset integration*

<details>
<summary><b>🖱️ Click to expand steps</b></summary>

<br>

**Terminal:**
```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("IVSL-SDSU/Clip-CC")

# Access a sample entry
print(dataset["train"][0])
```

**Colab/Jupyter:**
```python
# If path issues occur, upgrade packages:
!pip install --upgrade datasets fsspec

from datasets import load_dataset
dataset = load_dataset("IVSL-SDSU/Clip-CC")
print(dataset["train"][0])
```

<div align="center">

🤗 **Native HF integration**  
📊 **Dataset ecosystem**  
🔄 **Auto-versioning**

</div>

</details>

</td>
</tr>
</table>

### 💻 Basic Usage

Once installed, start using CLIP-CC in seconds:

<table align="center" width="100%">
<tr>
<td width="50%" align="center" style="vertical-align: top;">

### 🐍 **Python Package (Manual & Pip)**

<div style="background: linear-gradient(145deg, #dbeafe, #bfdbfe); padding: 20px; border-radius: 12px; border: 2px solid #3b82f6;">

```python
# Import CLIP-CC (works for both manual and pip installation)
from clip_cc.loader import load_metadata

# Load dataset
data = load_metadata()

# Explore
print(f"Dataset size: {len(data)} videos")
print(f"Sample: {data[0]}")

# Access summaries
for entry in data[:3]:
    print(f"Video {entry['id']}: {entry['summary']}")
```

</div>

</td>
<td width="50%" align="center" style="vertical-align: top;">

### 🤗 **Hugging Face**

<div style="background: linear-gradient(145deg, #fef3c7, #fde68a); padding: 20px; border-radius: 12px; border: 2px solid #f59e0b;">

```python
# Load with Hugging Face
from datasets import load_dataset

dataset = load_dataset("IVSL-SDSU/Clip-CC")

# Explore
print(f"Dataset: {dataset}")
print(f"Sample: {dataset['train'][0]}")

# Access summaries
for i in range(3):
    entry = dataset['train'][i]
    print(f"Video {entry['id']}: {entry['summary']}")
```

</div>

</td>
</tr>
</table>

---

## 🎥 Video Downloader & Clipper

<div align="center">
<table style="border: 2px solid #dc2626; border-radius: 12px; background: linear-gradient(145deg, #fed7d7, #fca5a5); padding: 15px; margin: 20px 0;">
<tr>
<td align="center">

**⚠️ Video Downloading is Optional** - Most research only needs the metadata (summaries + links)!

</td>
</tr>
</table>
</div>

### 🔧 Setup & Usage

<div align="center">
<table style="border: 2px solid #dc2626; border-radius: 12px; background: linear-gradient(145deg, #fed7d7, #fca5a5); padding: 15px; margin: 20px 0;">
<tr>
<td align="center">

**⚠️ Video Downloading is Terminal Only** - Colab/Jupyter environments don't support the browser cookies needed for age-restricted videos.

</td>
</tr>
</table>
</div>

### 💻 **Terminal Only**

<div style="background: linear-gradient(145deg, #ede9fe, #ddd6fe); padding: 20px; border-radius: 12px; border: 2px solid #7c3aed; max-width: 600px; margin: 0 auto;">

**1. Install Dependencies:**
```bash
pip install yt-dlp ffmpeg-python
```

**2. Check FFmpeg:**
```bash
ffmpeg -version
```

**3. Download & Clip Videos:**
```python
from clip_cc.downloader import download_and_clip_dataset

# Download one specific video (ID: 001)
download_and_clip_dataset(
    output_dir="downloads/clips",
    target_ids={"001"},
    use_browser_cookies=True,  # Uses Chrome/Firefox cookies directly
    clip_duration=90
)

print("✅ Videos downloaded and clipped!")
```

</div>

**Parameters:**
- `output_dir`: Where to save the clipped videos
- `target_ids`: Specific video ID(s) to download (use `None` to download all 200 videos)
- `use_browser_cookies`: Use browser cookies directly (recommended for age-restricted videos)
- `cookiefile_path`: Alternative cookie file path (if browser cookies don't work)
- `clip_duration`: Video length in seconds (default: 90)

**What this does:**
- Downloads videos using `yt-dlp` to a temporary folder
- Clips the first 90 seconds using `ffmpeg`
- Saves final clipped videos to `output_dir`
- Automatically cleans up intermediate files

### 🔧 Troubleshooting Downloads

<details>
<summary><strong>Age-Restricted Videos (Most Common Issue)</strong></summary>

**Problem:** `Sign in to confirm your age` error

**Solution: Use Browser Cookies (Terminal Only)**

**Method 1: Browser cookies (Recommended)**
```python
# Uses your browser's cookies directly (Chrome/Firefox)
# Make sure you're signed into YouTube in your browser first
download_and_clip_dataset(
    output_dir="clips",
    target_ids={"002"},  # Or None for all videos
    use_browser_cookies=True,  # Uses Chrome or Firefox cookies directly
    clip_duration=90
)
```

**Method 2: Export cookies file (Alternative)**
1. **Export cookies from your browser:**
   - Install browser extension "Get cookies.txt LOCALLY" (Chrome/Firefox)
   - Visit YouTube and sign in to your account
   - Click the extension and download `cookies.txt` file
   - **Important:** Make sure it's in Netscape format

2. **Use cookies in download:**
   ```python
   download_and_clip_dataset(
       output_dir="clips",
       target_ids={"002"},  # Or None for all videos
       cookiefile_path="cookies.txt",
       clip_duration=90
   )
   ```

**Note:** Method 1 (browser cookies) works much more reliably than cookie files.

</details>

<details>
<summary><strong>Other Common Issues</strong></summary>

**FFmpeg Issues:**
- Ensure `ffmpeg` is installed and in PATH
- Test with: `ffmpeg -version`

**Network Issues:**
- Check internet connection for YouTube access
- Some videos may be region-restricted or removed

**Video Not Found:**
- Video may have been removed from YouTube
- The download will skip missing videos and continue with others

</details>

---

## 🤖 VCS Ecosystem Integration

CLIP-CC is designed to work seamlessly with [VCS (Video Comprehension Score)](https://github.com/Multimodal-Intelligence-Lab/Video-Comprehension-Score) for comprehensive video understanding evaluation.

<div align="center">
<table style="border: 2px solid #7c3aed; border-radius: 12px; background: linear-gradient(145deg, #f3e8ff, #e9d5ff); padding: 20px; margin: 20px 0;">
<tr>
<td align="center">

[![VCS Metrics](https://img.shields.io/badge/🤖_Companion_Library-VCS_Metrics-9333ea?style=for-the-badge&logo=python&logoColor=white)](https://github.com/Multimodal-Intelligence-Lab/Video-Comprehension-Score)

**📊 Perfect Integration: CLIP-CC + VCS**
- 🎥 **CLIP-CC provides the data** → Rich video dataset with human summaries
- 🔍 **VCS provides the evaluation** → Advanced narrative comprehension metrics  
- 🏆 **Together: Complete research pipeline** → From data loading to evaluation

</td>
</tr>
</table>
</div>


---

## 📚 Citation

If you use CLIP-CC Dataset in your research, please cite:

```bibtex
@software{vcs_metrics_2024,
  title = {VCS Metrics: Video Comprehension Score for Text Similarity Evaluation},
  author = {Dubey, Harsh and Ali, Mukhtiar and Mishra, Sugam and Pack, Chulwoo},
  year = {2024},
  institution = {South Dakota State University},
  url = {https://github.com/Multimodal-Intelligence-Lab/Video-Comprehension-Score},
  note = {Python package for narrative similarity evaluation}
}
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### 🌟 **Made with ❤️ by the VCS Team**

**Authors**: Harsh Dubey, Mukhtiar Ali, Sugam Mishra, and Chulwoo Pack  
**Institution**: South Dakota State University  
**Year**: 2024

[⭐ Star this repo](https://github.com/hdubey-debug/CLIP-CC) • [🐛 Report Bug](https://github.com/hdubey-debug/CLIP-CC/issues) • [💡 Request Feature](https://github.com/hdubey-debug/CLIP-CC/issues) • [💬 Community Q&A](https://github.com/hdubey-debug/CLIP-CC/discussions)