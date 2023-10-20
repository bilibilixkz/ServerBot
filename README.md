# ServerBot

A simple tool to deploy a QQ bot for Minecraft server status monitoring.

---

## Deployment Guide
1. Download the entire project as zip from [https://github.com/bilibilixkz/ServerBot/archive/refs/heads/master.zip](https://github.com/bilibilixkz/ServerBot/archive/refs/heads/master.zip)
2. Unzip the file
3. Download and install Python 3
4. Run `python -m pip -r requirements.txt`, and you might want to set the PyPI mirror manually by using `-i` to speed up this step (sometimes a number 3 is required after "python" and "pip")
5. Install and run go-cqhttp, an official deployment guide of it is available at [https://docs.go-cqhttp.org/guide/quick_start.html](https://docs.go-cqhttp.org/guide/quick_start.html)
6. Edit config.py with any text editor to configuration
7. Run `python main.py`