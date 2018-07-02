import urllib2,cookielib,PyPDF2,re,csv
import pandas as pd

csv = pd.read_csv('docs/filtered_URL.csv',sep = ';')


for index,row in csv.iterrows():
    try:

        print row['att1'],row["url"],row["sino_sentences"]
        url = row["url"]

        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}

        req = urllib2.Request(url, headers=hdr)

        try:
            page = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            print e.fp.read()

        content = page.read()
        with open('docs/'+str(row['att1'])+'.pdf','wb') as output:
          output.write(content)
    #print content'''

        pdfFileObj = open('docs/'+str(row['att1'])+'.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        #pageObj =  pdfReader.getPage(0)
        #print pageObj.extractText()
        text = ''
        for page in pdfReader.pages:
            #print page.extractText()
            try:
                text += page.extractText()
            except Exception as ee:
                print ""

        regex = r"(Mr. [A-z ]*)\.( Mr. President,| Madam Speaker,| Madam Chair,| Mr. Speaker,)"
        matches = re.findall(regex, text)
        items = set()
        for match in matches:
            #print match
            res = re.sub(',.*','',str(match))#.replace('(u','').replace('\'','')
            print res
            if(items.__contains__(res)):
                continue
            else:
                items.add(res)

        print items.__str__()
        with open("out.csv", "a") as myfile:
            myfile.write(str(row['att1'])+';'+items.__str__()+"\n")
        #spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])

    except Exception as pe:
        print pe.message
