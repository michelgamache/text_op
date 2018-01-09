import urllib.request
from bs4 import BeautifulSoup
from PyPDF2 import PdfFileReader

#response = urllib.request.urlopen('https:...')


response = open("2017qccq2179.html",'r',encoding = 'utf-8')
#response = PdfFileReader(open('.pdf','r'))


html = response.read()
soup = BeautifulSoup(html,"lxml")
response.close()

print(soup.getText())




