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
        request = driver.wait_for_request(['videos-f.jwpsrv', 'jwpsrv-vh'], timeout=30)
        return str(request)
    except Exception as e:
        print(e)

    # Advertisement video "https://videos-e.jwpsrv.com/content/conversions/Pd1viDFY/videos/9cYJSeiC-30497135.mp4-2.ts"

    input("Inspect")
    return None


if __name__ == '__main__':
    print(f'{Fore.MAGENTA}Starting scrape{Fore.RESET}')
    with open('video_links.json', 'r') as f:
        video_list = json.load(f)

    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=.\\local_chrome_sessions")
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)

    for meded_url, video_link in video_list.items():
        if video_link == 'NOT FOUND':
            link = get_video_link(driver, meded_url)
            print(meded_url, link)
    driver.close()


