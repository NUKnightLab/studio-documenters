"""
Script to fetch OCR text files from the URLs in a DocumentCloud documents.json
"""
import json
import os
import sys
import requests

CACHEDIR = 'data/DocumentCloud/text'
DOCSFILE = 'data/DocumentCloud/documents.json'


def fetch(url, verbose=False):
    n = len('https://assets.documentcloud.org-documents-')
    path = os.path.join(CACHEDIR, url[n:].replace('/', '-'))
    if os.path.exists(path):
        if verbose:
            print('exists', path)
        text = open(path).read()
        return text
    else:
        print('fetching', url)
        text = requests.get(url).text
        with open(path, 'w') as f:
            f.write(text)
        return text


def fetch_missing(verbose=False):
    with open(DOCSFILE) as f:
        data = json.load(f)
        for doc in data:
            url = doc['resources'].get('text')
            if not url:
                print('No OCR text available for Document Cloud document:',
                    doc['canonical_url'])
                continue
            fetch(url, verbose)


if __name__=='__main__':
    verbose = '-v' in sys.argv
    fetch_missing(verbose=verbose)
