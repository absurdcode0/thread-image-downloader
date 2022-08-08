from sys import argv
from requests import get
from os import chdir, makedirs, path
from pathlib import Path

url = argv[1]
url = url.split("/") #['https:', '', 'boards.4channel.org', 'g', 'thread', '111111']
board = url[3]
thread_id = url[-1]

images = []
r = get(f'https://a.4cdn.org/{board}/thread/{thread_id}.json')
r = r.json()


def board_folder(folder_title):
        if path.isdir(folder_title):
            chdir(rf"{folder_title}")
            thread_folder(thread_id)
        else:
            makedirs(folder_title)
            chdir(rf"{folder_title}")
            thread_folder(thread_id)

def thread_folder(postno):
    makedirs(postno)
    chdir(rf"{postno}")
def get_image():
    for item in r['posts']:
        try:
            ext = item['ext']
            id = item['tim']
            full = f"{id}{ext}"
            images.append(full)
        except KeyError: # if no image
            continue
def main():
    for image in images:
        image_url = f'https://i.4cdn.org/{board}/{image}' 
        filename = Path(image)
        response = get(image_url)
        filename.write_bytes(response.content)
        print("image downloaded")
board_folder(board)
get_image()
main() 
