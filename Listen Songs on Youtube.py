import requests, bs4, webbrowser, pyperclip
import time
def ConvertToUrl(s):
    url="https://www.youtube.com/results?search_query="
    s=s.replace(' ','+')
    url=url+s
    return url
print("Enter Song you want to Listen")
s= "Perfect"
url=ConvertToUrl(s)
headers = {'user-agent': 'my-app/0.40.1'}
res=requests.get(url, headers=headers, timeout=15)
soup=bs4.BeautifulSoup(res.text, 'html.parser')
songs=soup.findAll('div',{'class':'yt-lockup-video'})
song=songs[0].contents[0].contents[0].contents[0]
link=song['href']
print(link)
webbrowser.open('https://www.youtube.com'+link)
