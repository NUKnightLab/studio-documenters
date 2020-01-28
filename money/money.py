import os
import re
import RAKE
from summarize import summarize
from dotenv import load_dotenv
load_dotenv()

DOCS_DIR = os.environ['DOCS_DIR']
PARA = re.compile('\n\n.*?\n\n', re.S|re.M)
MONEY = re.compile('\$[\d,\.]+')

rake = RAKE.Rake(RAKE.SmartStopList())

def get_money_docs():
    docs = {}
    all_keywords = set()
    all_moneys = set()
    for f in os.listdir(DOCS_DIR):
        doc = open(os.path.join(DOCS_DIR, f)).read()
        paras = []
        doc_moneys = set()
        for p in PARA.findall(doc):
            moneys_ = MONEY.findall(p)
            if moneys_:
                paras.append(p)
                all_moneys.update(moneys_)
                doc_moneys.update(moneys_)
        if paras:
            data = {}
            data['moneyrefs'] = [p.strip() for p in paras]
            data['moneys'] = doc_moneys
            keywords = []
            for k,v in rake.run(doc):
                k = k.replace('\n', ' ')
                if not k.replace('$','').replace(',','').replace('.','').isnumeric():
                    keywords.append(k)
            data['keywords'] = keywords
            all_keywords.update(keywords)
            data['summary'] = summarize(doc)
            docs[f] = data
    
    r = {
        'docs': docs,
        'keywords': all_keywords,
        'moneys': all_moneys
    }
    return r
