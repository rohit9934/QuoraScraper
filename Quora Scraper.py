#created with love by @rohit9934
import webbrowser, pyperclip, requests, bs4, sys
import time
headers = {'user-agent': 'my-app/0.0.1'}
def ConvertToUrl(change):
    new=change.replace(' ','+')
    url= "https://www.quora.com/search?q=" +new
    return url
def QuestionUrl(my):
    url="https://www.quora.com"+ my
    return url
print("Hi and Welcome to Quora Scraper, Ask your Question")
St= input()
url= ConvertToUrl(St)
res=requests.get(url, headers=headers, timeout=15)
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text, 'html.parser')
elem=soup.find_all("span" ,class_="question_text")
Links=soup.find_all("a", class_="question_link")
Questions=[]
for i in range(len(Links)):
    Convert= QuestionUrl(Links[i]['href'])
    Questions.append(Convert)
#QuestionLinks=[] #List of Urls of Questions
print("Please Choose the Question number you want to see")
for i in range(len(elem)):
    print("%d. "%(i+1), elem[i].text)
print("\n")
print("Now Enter your Question Number\n")
n=int(input())
QuestionUrl= Questions[n-1]
result= requests.get(QuestionUrl, headers=headers, timeout=15)
NewSoup= bs4.BeautifulSoup(result.text, 'html.parser')
Answers=NewSoup.find_all("span", class_="ui_qtext_rendered_qtext")
AnsNO=0
print(Answers[AnsNO].text)
print("\n")
print("Do you want another Answer? Y or N ?")
k = input()


#To Ask for more Answers
while k=='Y':
    if k == 'Y':
        AnsNO+=1
        print(Answers[AnsNO].text)
    print("Do you want another Answer? Y or N ?")
    k=input()
print("Do you want to get to Question Main Page For More Answers, Y or N ?")
go= input()
if go=='Y':
    webbrowser.open(QuestionUrl)




