"""
NAME: reptile_test1.py <br/>
Description:  <br/>
@author ranyk <br/>
@version V1.0 <br/>
@date 2024-02-19
"""
import requests

url = 'https://v3-web.douyinvod.com/a1942007941a2efda4d8c6b5f6803547/65d367a1/video/tos/cn/tos-cn-ve-15/owcZi7n5QeAQIeBw0hDCnqAOAZ9Zb9rHlnuWgE/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=978&bt=978&cs=0&ds=6&ft=bvTKJbQQqUuxfdoZPo0OqY8hFgpi-ofxejKJMUbD1N0P3-I&mime_type=video_mp4&qs=0&rc=aGc1OGZpPDhnZTc6Zjw2ZEBpMzVwN2Y6Zmh3cTMzNGkzM0BeMjBfMmExXzUxMDZgYjI1YSNhbXJrcjRfNS5gLS1kLS9zcw%3D%3D&btag=e00030000&dy_q=1708349513&feature_id=f0150a16a324336cda5d6dd0b69ed299&l=202402192131526E6B35BD20B93A19E87A'


if __name__ == '__main__':
    response = requests.get(url=url)
    content = response.content
    open('../videos/videos.mp4', 'ab').write(content)
