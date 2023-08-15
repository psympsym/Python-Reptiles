import os
import requests

if __name__ == '__main__':
    head = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/117.0.0.0 Safari/537.36 Edg/117.0.0.0"
    }

    post_url = "https://fanyi.baidu.com/sug"
    while True:
        word = input("\033[5;31m输入:\033[0m")
        os.system('cls')
        if word == 'exit()':
            break
        data = {
            'kw': word
        }
        response = requests.post(url=post_url, headers=head, data=data)
        dic_obj = response.json()
        max_len = len(max((obj.get('k') for obj in dic_obj.get("data")), key=len))
        for obj in dic_obj.get("data", 'none'):
            string = (f"\033[1;33m{obj.get('k'):<{max_len}}\033[0m -> "
                      f"\033[1;35m{obj.get('v')}\033[0m")
            print(string)
