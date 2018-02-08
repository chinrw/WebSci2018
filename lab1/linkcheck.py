import json
from urllib import request
from urllib.error import URLError

from django.contrib.staticfiles.templatetags.staticfiles import static


class LinkCheck:
    def __init__(self):
        pass

    @staticmethod
    def send_request(url):
        try:
            response = request.urlopen(url)
        except URLError:
            print("Cannot reach")
            return False
        else:
            print("Reachable")
            response.close()
            return True
        finally:
            pass


def select_5_from_json(num, data):
    content = []
    i = num * 5
    while len(content) < 5:
        while "user" not in data[i]:
            i += 1
        user_icon = data[i]["user"]["profile_image_url"]
        if not LinkCheck.send_request(data[i]["user"]["profile_image_url"]):
            url = static('lab1/icon.png')
            user_icon = url
        content.append({'icon': user_icon, 'text': data[i]["text"]})
        print(data[i]["text"])
        i += 1
    return content


if __name__ == "__main__":
    LinkCheck.send_request("http://www.worldpara.com")
