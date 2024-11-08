import os
import random
import tempfile
import requests
import ctypes

class Furry:
    def __init__(self):
        self.temp_dir = os.path.join(tempfile.gettempdir(), "furry")
        os.makedirs(self.temp_dir, exist_ok=True)

    def download_images(self):
        while True:
            self._download_and_save_image()

    def _download_and_save_image(self):
        is_nsfw = random.choice([True, False])
        if is_nsfw:
            picType = "nsfw"
            otherType = random.choice([
                'waifu',
                'neko',
                'trap',
                'blowjob'
            ])
        else:
            picType = "sfw"
            otherType = random.choice([
                'waifu',
                'neko', 
                'shinobu',
                'megumin',
                'bully',
                'cuddle',
                'cry',
                'hug',
                'awoo',
                'kiss',
                'lick',
                'pat',
                'smug',
                'bonk',
                'yeet',
                'blush',
                'smile',
                'wave',
                'highfive',
                'handhold',
                'nom',
                'bite',
                'glomp',
                'slap',
                'kill',
                'kick',
                'happy',
                'wink',
                'poke',
                'dance',
                'cringe'
            ])
        
        base = f'https://api.waifu.pics/{picType}/{otherType}'
        try:
            req_url = requests.get(base)
            if not req_url.ok:
                return

            data = req_url.json()
            url = data.get('url', '')
            if not url:
                return

            if url.lower().endswith('.png') or url.lower().endswith('.jpg'):
                file_size = int(requests.head(url).headers.get('content-length', 0))
                
                if file_size > 0:
                    filename = os.path.join(self.temp_dir, os.path.basename(url))
                    with open(filename, 'wb') as f:
                        response = requests.get(url, stream=True)
                        for block in response.iter_content(1024):
                            if not block:
                                break
                            f.write(block)

                    self.randomize_wallpapers()
                else:pass
            else:pass
        except Exception as e:pass

    def randomize_list(self, lst):
        randomized_list = lst[:]
        random.shuffle(randomized_list)
        return randomized_list

    def randomize_wallpapers(self):
        images = [os.path.join(self.temp_dir, img) for img in os.listdir(self.temp_dir)
                  if img.lower().endswith('.png') or img.lower().endswith('.jpg')]
        if images:
            selected_image = random.choice(images)
            try:
                ctypes.windll.user32.SystemParametersInfoW(20, 0, selected_image, 0)
            except Exception as e:pass

if __name__ == "__main__":
    instance = Furry()
    instance.download_images()
