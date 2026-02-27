from bs4 import BeautifulSoup
import requests
import pandas as pd

web='https://gaana.com/playlist/gaana-dj-tamil-top-50-2'

request=requests.get(web)
print(request.status_code)


soup=BeautifulSoup(request.text, 'html.parser')
name=soup.find_all('a',class_="t_over _plyCr",href=True)

q=[]
for x in name:
    c=x.get('href')
    q.append(c)

# print(q)
names=[]
year=[]
time=[]
singer=[]
for x in q:
    # print('https://gaana.com'+ x)
    r='https://gaana.com'+ x
    b=requests.get(r)

    t=BeautifulSoup(b.text, 'html.parser')
    sname=t.find('h1',class_="title").text
    names.append(sname)
    syear=t.find('span',class_='_date').text
    year.append(syear)
    stime=t.find('span',class_='_duration').text
    time.append(stime)
    snger=t.find('ul',class_='singers').text
    singer.append(snger)
# print(singer)


name=[]
movie=[]
for x in names:
    b=x.replace('(','').replace(")","").replace('"','')
    # print(b)
    e=b.split('From')
    # print(e)
    name.append(e[0])
    try:
        movie.append(e[1])
    except IndexError:
        movie.append('NOT FOUND')

dict={
    'SONG NAME':name,
    'MOVIE':movie,
    'SINGER NAME':singer,
    'YEAR':year,
    'DURATION':time
    
}
df=pd.DataFrame(dict)
# print(df)
df.to_excel('DATA.xlsx',index=False)
df.to_csv('DATA.csv', index=False)
print("file saved") 
df = pd.read_csv('DATA.csv')
print("\nRead CSV:")
print(df)