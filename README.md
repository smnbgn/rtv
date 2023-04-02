# 365.rtvslo.si media downloader

This is a Python script that downloads individual audio/video files from the website 365.rtvslo.si of the Slovenian public broadcaster. Conversion from video to audio is supported.

## Requirements
- Python 3 (add to the PATH environment variable)

    Installation: https://phoenixnap.com/kb/how-to-install-python-3-windows
- FFmpeg (add to the PATH environment variable)

    Installation: https://phoenixnap.com/kb/ffmpeg-windows
- Google Chrome
- Seleniumwire Python library

    Installation:
    ```
    pip install selenium-wire
    ```


## Example usage
Download video:
```
python rtv.py https://365.rtvslo.si/arhiv/odmevi/174947419
```
Download audio only:
```
python rtv.py https://365.rtvslo.si/arhiv/odmevi/174947419 -audio
```



