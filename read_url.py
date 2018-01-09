import urllib.request
from bs4 import BeautifulSoup
from PyPDF2 import PdfFileReader

#response = urllib.request.urlopen('https://www.canlii.org/fr/qc/qccq/doc/2017/2017qccq2179/2017qccq2179.html')
#response = urllib.request.urlopen('http://7ba0a889.ngrok.io/2017qccq2179.html')
#response = urllib.request.urlopen('http://127.0.0.1/2017qccq2179.html')

response = open("2017qccq2179.html",'r',encoding = 'utf-8')
#response = PdfFileReader(open('2017qccq2179.pdf','r'))


html = response.read()
soup = BeautifulSoup(html,"lxml")
response.close()

print(soup.getText())




