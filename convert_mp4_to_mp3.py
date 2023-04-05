from concurrent.futures import ThreadPoolExecutor
import os


def change_extension(file, new_ext):
    pre, ext = os.path.splitext(file)
    return pre + new_ext


folder = os.getcwd()
mp4_files = [each for each in os.listdir(folder) if each.endswith('.mp4')]
mp4_files = list(map(lambda file: '.\\' + file, mp4_files))


def do_encode(mp4_file):
    mp3_file = change_extension(mp4_file, '.mp3')
    cmd = f"ffmpeg -hide_banner -loglevel error -i \"{mp4_file}\" \"{mp3_file}\""
    print(f"Converting: {mp4_file}")
    os.system(cmd)


processes = []
with ThreadPoolExecutor() as executor:
    for mp4_file in mp4_files:
        processes.append(executor.submit(do_encode, mp4_file))
