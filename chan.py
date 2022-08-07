from sys import argv
from requests import get
from os import chdir, makedirs, path

url = argv[1]
url = url.split("/") #['https:', '', 'boards.4channel.org', 'g', 'thread', '111111']
board = url[3]
thread_id = url[-1]

#workpath = os.path.dirname(os.path.realpath(__file__))

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
def main():
    for item in r['posts']:
        try:
            ext = item['ext']
            id = item['tim']
            full = f"{id}{ext}"
            image_url = f'https://is2.4chan.org/{board}/{id}{ext}'
                    
            img_data = get(image_url).content

            with open(full, 'wb') as handler:
                handler.write(img_data)
                print("image downloaded")
        except KeyError: # if no image
            continue        
board_folder(board)
if __name__ == '__main__':
    main() 
