#import webbrowser
# webbrowser.open('https://inventwithpython.com/')

import requests, bs4
res = requests.get('https://www.nhl.com/stats/')
# res = requests.get('https://nostarch.com')
res.raise_for_status()
mySoup = bs4.BeautifulSoup(res.text, 'html.parser')
type(mySoup)

# exampleFile = open(noStarchSoup)

# exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')

divelems = mySoup.select('div')
pelems = mySoup.select('p')
divElem = mySoup.select('div')[0]
# print(type(divelems)) # elems is a list of Tag objects.
# print(len(divelems))
# print(divelems[0])
# print(divelems[0].getText())
# print(divelems[1].getText())

# print(divElem.get('class'))

divFind = mySoup.find('div', {'class': 'd3-l-wrap'})
mainFind = divFind.findChildren("main", recursive=False)

children = divFind.findChildren("main", recursive=False)

for child in children:
    print(child)


# for i in range (0,15):
#     # print(mySoup.select('div')[i])
#     print(mySoup.select('div')[i].get('class'))

# # pElem = mySoup.select('p')[0]

