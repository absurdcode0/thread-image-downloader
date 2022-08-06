import requests, os, re

board = 'r9k' # Select your board e.g adv, g, a etc
post_id = '69701095' # Enter Post ID (Number next to the Time)
DIR = r'C:\Path\to\file'
r = requests.get(f'https://a.4cdn.org/{board}/thread/{post_id}.json')
r = r.json()

def get_title():
    try:
        for x in r['posts']:
            title = x['sub']
            has_title = True
            break
        title = re.sub(r'[^\w]', ' ', title)
        titled_folder(title.strip())
    except KeyError:
        board_folder(post_id)
def board_folder(folder_title):
        new_dir = folder_title
        fullname = f"{board} {new_dir}"
        if os.path.isdir(new_dir):
            os.makedirs(fullname)
            os.chdir(rf"{DIR}\{fullname}")
        else:
            os.makedirs(fullname)
            os.chdir(rf"{DIR}\{fullname}")
def titled_folder(folder):
    if os.path.isdir(folder):
        os.makedirs(rf"{DIR}\{folder}_{post_id}")
        os.chdir(rf"{DIR}\{folder}_{post_id}")
    else:
        os.makedirs(rf"{DIR}\{folder}")
        os.chdir(rf"{DIR}\{folder}")

def main():
    for item in r['posts']:
        try:
            ext = item['ext']
            id = item['tim']
            full = f"{id}{ext}"
            image_url = f'https://is2.4chan.org/{board}/{id}{ext}'
                    
            img_data = requests.get(image_url).content

            with open(full, 'wb') as handler:
                handler.write(img_data)
                print("image downloaded")
        except KeyError:
            continue        
get_title()
main()
