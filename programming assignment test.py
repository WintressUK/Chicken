#%%
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

#%%
#Question 1

#first, obtain all category links and put them in a list

url = 'https://sitescrape.awh.durham.ac.uk/comp42315/publicationfull_type_animationandgraphics.htm'

page = requests.get(url, verify=False)
soup = BeautifulSoup(page.content, "html.parser")

options = soup.find_all('p', class_='TextOption')
links = options[1].find_all('a')

linklist = ['https://sitescrape.awh.durham.ac.uk/comp42315/publicationfull_type_animationandgraphics.htm']

for link in links:
    tempurl = link.get('href')
    linklist.append('https://sitescrape.awh.durham.ac.uk/comp42315/' + tempurl)
    
print(linklist)

#if statements and stuff

#%%
#now scrape all link pages in the linklist for publication title, year, and author list

titleslist = []
yearlist = []
authorslist = []
authorsnumberlist = []

for url in linklist:
    currentpage = requests.get(url, verify=False)
    currentsoup = BeautifulSoup(currentpage.content, "html.parser")
    w3_cell = currentsoup.find_all('div', class_="w3-cell-row")
    time.sleep(1)
    
    if w3_cell==None:
        print("the void (cell void)")
        
    for cell in w3_cell:
        title = cell.find(class_="PublicationTitle")
        
        if title==None:
            print("the void (title void)")
        else:
            titleslist.append(title.text)
        
        smalltext = cell.find_all(class_="TextSmall")
        
        if smalltext==None:
            print("the void (smalltext void)")
        else:
            yearcontainer = smalltext[0]
            authors = smalltext[1]
            
            #print(yearcontainer.text)
            
        yearcontainer = yearcontainer.text.replace(",", "")
        yearcontainer = yearcontainer.split()
        yearcontainer = int(yearcontainer[-1])
        yearlist.append(yearcontainer) #need to add checking for a valid year here, a year void
        
        authors = authors.text.split(',')
        popped = authors.pop()
        popped = popped.split('and') #could add if len(popped)==2, to make sure you're just getting two extra authors here
        authors.extend(popped)
        authors = tuple(authors)
        authorslist.append(authors)
        
        authorsnumberlist.append(len(authors))

#next: i also need to check this for duplicates/remove duplicates because some journal pubs r in multiple categories so some of my stuff is nonsensical

#%%
#create the desired table
#i could just remove duplicates in the table tbh

print(len(titleslist),len(yearlist), len(authorslist), len(authorsnumberlist))

#all of these lists have the same length. now i need to group them

biglist = []

for i in range(len(titleslist)):
    first = titleslist[i]
    second = yearlist[i]
    third = tuple(authorslist[i])
    fourth = authorsnumberlist[i]
    newlist = [first,second,third,fourth]
    biglist.append(newlist)
    
#remove all the duplicates

for i in range(len(biglist)):
    biglist[i] = tuple(biglist[i])
    
biglist = set(biglist) #make it a set to remove all duplicates
biglist = list(biglist)
print(len(biglist))

#make the final dataframe
cols = ['Publication Title', 'Year', 'Authors', 'Number of Authors']
df = pd.DataFrame(biglist, columns = cols)
print(df)