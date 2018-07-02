import urllib2,cookielib,PyPDF2,re

pdfFileObj = open('docs/3492.0.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    #pageObj =  pdfReader.getPage(0)
    #print pageObj.extractText()
text = ''
for page in pdfReader.pages:
        #print page.extractText()
    try:
        text += page.extractText()
    except Exception as e:
        print "err"


print text
