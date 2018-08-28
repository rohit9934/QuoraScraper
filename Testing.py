import speech_recognition as sr
import requests,datetime, bs4, webbrowser, pyperclip
import time,random
import win32com.client
#Next Task, Learn regex for Talk
speaker = win32com.client.Dispatch("SAPI.SpVoice")
def Speak(s):
    speaker.Speak(s)
def Listening():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    return r.recognize_google(audio)
def ConvertToUrl(s):
    url="https://www.youtube.com/results?search_query="
    s=s.replace(' ','+')
    url=url+s
    return url
#Listen Songs will play song directly from youtube
def ListenSongs(s):
    url=ConvertToUrl(s)
    headers = {'user-agent': 'my-app/0.40.1'}
    res=requests.get(url, headers=headers, timeout=15)
    soup=bs4.BeautifulSoup(res.text, 'html.parser')
    songs=soup.findAll('div',{'class':'yt-lockup-video'})
    song=songs[0].contents[0].contents[0].contents[0]
    link=song['href']
    #print(link)
    webbrowser.open('https://www.youtube.com'+link)
#In this, i have parsed top 50 imdb movies using beautiful soup
#and it will show me.
def Time(): #This Function will print the time
    s=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    Speak(s)
def RecommendMovie():
    url="http://www.imdb.com/chart/top"
    headers = {'user-agent': 'my-app/0.40.1'}
    res=requests.get(url, headers=headers, timeout=15)
    soup=bs4.BeautifulSoup(res.text, 'html.parser')
    movies= soup.find_all('h3',class_="lister-item-header")
    ratings=soup.find_all('div',class_="ratings-bar")
   # print(movies[0].text[3:])
    #print(ratings[0].text[3:7])
    n=random.randint(1,50)
    Speak(movies[n].text[3:])
    Speak("is a Great Movie you don't want to miss, Rohit")
    Speak("with IMDB Ratings of "+ratings[n].text[3:7])
#Prototype
Speak("Good Evening Rohit, Which song you wanna listen?")
Speak("Good Evening Rohit, Do you want a movie recommendation!")
s=Listening()
#Speak("The current time is ")
#Speak(Time())
#print("Playing "+s+" For you Rohit")
#Speak("Playing "+s+" For you Rohit")
#Speak("OK, Rohit you said "+s)
#ListenSongs(s)
RecommendMovie()


