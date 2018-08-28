import random,requests, bs4, webbrowser, pyperclip
url="http://www.imdb.com/search/title?groups=top_250&sort=user_rating"
headers = {'user-agent': 'my-app/0.40.1'}
res=requests.get(url, headers=headers, timeout=15)
soup=bs4.BeautifulSoup(res.text, 'html.parser')
movies= soup.find_all('h3',class_="lister-item-header")
ratings=soup.find_all('div',class_="ratings-bar")
print(movies[0].text[3:])
print(ratings[0].text[3:7])
print(random.randint(1,50))

