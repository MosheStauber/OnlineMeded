import json
import youtube_dl
import os
from tempfile import TemporaryDirectory
from multiprocessing import Pool
import subprocess


def download_video(url: str, video_path: str):
    if url.startswith('https://videos-'):
        url_format = url + '-{}.ts'
    else:  # url.startswith('https://jwpsrv')
        url_format = url[:url.find('index')] + 'segment{}_0_av.ts'

    print(f'Working on {url_format}: {video_path}')

    with TemporaryDirectory() as temp_dir:
        video_list_file = os.path.join(temp_dir, 'flist.txt')
        with open(video_list_file, 'w') as f:
            part_number = 1
            while True:
                video_part = os.path.join(temp_dir, str(part_number))
                ydl_opts = {'outtmpl': video_part}
                try:
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url_format.format(part_number)])
                    f.write(f"file '{video_part}'\n")
                    part_number += 1
                except Exception as e:
                    print(e)
                    break

        subprocess.call(["ffmpeg.exe", "-f", "concat", "-safe", "0", "-i", video_list_file, "-c:v", "copy", '-threads', '4', video_path])


if __name__ == '__main__':
    with open('video_links.json', 'r') as f:
        video_list = json.load(f)

    root_video_dir = 'Videos'

    pool_args = []
    with Pool(3) as pool:
        for meded_url, video_link in video_list.items():
            category, video_name = meded_url.split('/')[-2:]
            video_dir = os.path.join(root_video_dir, category)
            os.makedirs(video_dir, exist_ok=True)
            base_url = video_link.split('.m3u8')[0]
            pool_args.append((base_url, os.path.join(video_dir, video_name + '.mp4')))

        pool.starmap(download_video, pool_args)
