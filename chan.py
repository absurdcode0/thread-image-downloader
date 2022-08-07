import requests, os, re

board = ''           # Enter your board e.g adv, g, a etc
post_id = ''         # Enter Post ID (Number next to the Time)

# Enter where you want to download
path = os.path.join(os.sep, 'C:', os.sep, 'Path', 'To', 'X',)  # Windows Example prints C:\Users\Path\To\X
# Linux Example prints /home/name/documents, just an exmaple edit this ^
dir_lin = os.path.join(os.sep, 'home', 'name', 'Documents')             

r = requests.get(f'https://a.4cdn.org/{board}/thread/{post_id}.json')
r = r.json()

def get_title():
    try:
        for x in r['posts']:
            title = x['sub']
            break
        title = re.sub(r'[^\w]', ' ', title)
        title = title.strip()
        titled_folder(title)
    except KeyError:
        board_folder(post_id)
def board_folder(folder_title):
        new_dir = folder_title
        fullname = f"{board}-{new_dir}"
        if os.path.isdir(new_dir):
            os.makedirs(fullname)
            os.chdir(rf"{path}{os.sep}{fullname}")
        else:
            os.makedirs(fullname)
            os.chdir(rf"{path}{os.sep}{fullname}")
def titled_folder(folder):
    if os.path.isdir(folder):
        os.makedirs(rf"{path}{os.sep}{folder}-{post_id}")
        os.chdir(rf"{path}{os.sep}{folder}-{post_id}")
    else:
        os.makedirs(rf"{path}{os.sep}{folder}")
        os.chdir(rf"{path}{os.sep}{folder}")

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
