# Instagram Termux Downloader (ITDL)

<div align="center">

```
██╗████████╗██████╗ ██╗     
██║╚══██╔══╝██╔══██╗██║     
██║   ██║   ██║  ██║██║     
██║   ██║   ██║  ██║██║     
██║   ██║   ██████╔╝███████╗
╚═╝   ╚═╝   ╚═════╝ ╚══════╝
```

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Termux](https://img.shields.io/badge/Termux-Support-purple.svg)](https://termux.com/)

🚀 A powerful Instagram video/reel downloader for Termux with metadata support

</div>

## ✨ Features

- 📥 Download Instagram videos and reels
- 📝 Save post descriptions and metadata
- 🎯 Simple command-line interface
- 🚄 Fast and efficient downloads
- 📱 Optimized for Termux
- 🎨 Beautiful progress display
- 📂 Organized file storage

## 🔧 Installation

1. Update Termux packages:
```bash
pkg update && pkg upgrade
```

2. Install Python:
```bash
pkg install python
```

3. Install required package:
```bash
pip install instaloader
```

4. Set up storage permissions:
```bash
termux-setup-storage
```

5. Clone the repository:
```bash
git clone https://github.com/krivadna/termuxinstadownloader.git
cd termuxinstadownloader
```

## 💫 Usage

```bash
python itdlbykalki.py <instagram_post_url>
```

Example:
```bash
python itdlbykalki.py https://www.instagram.com/reel/XXXXXXXXXXXX/
```

## 📂 File Locations

Downloaded files are saved in:
```
~/storage/downloads/instagram_downloads/
```

## 📋 Requirements

- Python 3.x
- Termux
- Internet connection
- Storage permission
- instaloader package

## 🔍 Troubleshooting

If you encounter issues:

1. Ensure storage permissions are granted:
```bash
termux-setup-storage
```

2. Check if the download directory exists:
```bash
ls ~/storage/downloads/instagram_downloads
```

3. Verify internet connection:
```bash
ping google.com
```

4. Update the package:
```bash
pip install --upgrade instaloader
```

## 🚀 Features in Detail

- **Video Downloads**: Download Instagram videos and reels in high quality
- **Metadata Saving**: Captures post descriptions, hashtags, and other metadata
- **Progress Display**: Shows download progress and file information
- **Error Handling**: Comprehensive error messages and troubleshooting guidance
- **Organized Storage**: Creates dedicated directories for downloads
- **Color Coding**: Beautiful color-coded terminal output


## 💼 Professional Services

Contact for:
- 🔧 Custom implementations
- 🎯 Specific feature requests
- 💻 Integration support
- 🛠️ Technical consultation

## 🛡️ Disclaimer

This tool is for educational purposes only. Please respect Instagram's terms of service and content creators' rights.



## ⭐ Show your support

Give a ⭐️ if this project helped you!

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


<div align="center">
  <sub>Built with ❤️ by Cyber Kalki</sub>
</div>

<!-- Custom Footer -->
<p align="center">
  <img src="https://raw.githubusercontent.com/krivadna/krivadna/refs/heads/main/footer.svg" width="100%" alt="Cyberpunk Footer"/>
</p>
