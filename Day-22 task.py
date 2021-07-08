# 1.Read a jpeg image and print the image file

from PIL import Image
img = Image.open("zz.jpg")
print(img.format)
import matplotlib.pyplot as plt
plt.imshow(img)

# 2.Merge two pdf files using python script

import PyPDF2

pdf1File = open('Day 6 - python.pdf', 'rb')
pdf2File = open('Day 8 - python.pdf', 'rb')

pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('MergedFiles.pdf', 'wb')
pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()
pdf1File.close()
pdf2File.close()
pdf3 = open("MergedFiles.pdf", 'rb')
pdf3Reader = PyPDF2.PdfFileReader(pdf3)
print(pdf3Reader)
pdf3.close()

# 3.Scrape a website and store the data into DB

import requests
from bs4 import BeautifulSoup
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="deepak#$1238220994412")
mydb = mysql.connector.connect(host="localhost", user="root", password="deepak#$1238220994412", database="Doctors")
dbse = mydb.cursor()
url_to_scrape = 'https://google.com/'
plain_html_text = requests.get(url_to_scrape)
soup = BeautifulSoup(plain_html_text.text, "html.parser")
print(soup.prettify())
