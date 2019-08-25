import time
import json
import youtube_dl
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from seleniumwire import webdriver
from colorama import Back, Fore


def download_video(url, name, download_dir):
    if not os.path.exists(download_dir):
        os.mkdir(download_dir)

    fname = os.path.join(download_dir, name)
    ydl_opts = {
        'outtmpl': f'{fname}.%(ext)s',
        'format': 'mp4'
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return f'{fname}.mp4'


def get_video_link(chrome_driver, url):
    chrome_driver.get(url)

    del driver.requests

    wait = WebDriverWait(driver, 30)
    player = wait.until(ec.visibility_of_element_located((By.ID, "acquire_video_jwp")))
    player.click()

    try:
        request = driver.wait_for_request(['videos-f.jwpsrv', 'jwpsrv-vh'], timeout=90)
        return str(request)
    except Exception as e:
        print(e)

    return None


if __name__ == '__main__':
    print(f'{Fore.MAGENTA}Starting scrape{Fore.RESET}')
    with open('video_list.json', 'r') as f:
        video_list = json.load(f)

    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=.\\local_chrome_sessions")
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)

    root_url = 'https://onlinemeded.org'
    with open('video_links.txt', 'w') as f:
        for video in video_list:
            topic, name = video.split('/')[2:]
            video_url = root_url + video
            link = get_video_link(driver, video_url)
            text = f'{video_url}: {link if link else "NOT FOUND"}'
            print(text)
            f.write(text+'\n')
            f.flush()

    driver.close()


