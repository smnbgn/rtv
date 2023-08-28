from urllib.parse import urlparse
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re
import time
import os
import sys

if (len(sys.argv) < 2) or (len(sys.argv) > 3):
    print("Usage: python rtv.py URL [-audio]")
    sys.exit()

# Get the command line arguments
url = sys.argv[1]
if (len(sys.argv) == 3) and (sys.argv[2] == '-audio'):
  audio = True
else:
  audio = False

options = Options()
options.add_argument('headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--log-level=3");
options.add_argument("--mute-audio")
driver = webdriver.Chrome(options=options)

driver.get(url)

#Wait for the site to load fully
time.sleep(5)

title_element = driver.find_elements(By.XPATH, "//a[@class='show-title-link']")[0]
title = title_element.text
title = re.sub(r'[^a-zA-Z0-9čžšČŽŠćĆ\s]+', '', title)

try:
  subtitle_element = driver.find_elements(By.XPATH, "//div[@class='rtv4d-title-meta']/h1")[0]
  subtitle = subtitle_element.text
  subtitle = re.sub(r'[^a-zA-Z0-9čžšČŽŠćĆ\s]+', '', subtitle)
  filename = title + ' - ' + subtitle
except:
  filename = title
print(filename)

# Click on the video to generate requests
driver.find_elements(By.CLASS_NAME, 'jwplayer')[0].click()

time.sleep(60) # Wait for 60s to skip commercials

for request in driver.requests:
  if request.response and urlparse(url).netloc not in urlparse(request.url).netloc:
    if '.mp3?exp' in request.url:
      os.system('ffmpeg -y -i \"' + request.url + '\" -c copy \"' + filename + '.mp3\"') 
    elif ('playlist.m3u8?' in request.url) and audio:
      os.system('ffmpeg -y -acodec libmp3lame -aq 2 \"' + filename + '.mp3\" -i \"' + request.url + '\"')
    elif 'playlist.m3u8?' in request.url:
      os.system('ffmpeg -i \"' + request.url + '\" -bsf:a aac_adtstoasc -vcodec copy -c copy -crf 50 \"' + filename + '.mp4\"') 
