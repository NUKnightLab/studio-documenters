"""
Script to fetch OCR text files from the URLs in a DocumentCloud documents.json
"""
import json
import os
import shutil
import sys
import requests

CACHEDIR = 'data/DocumentCloud/text'
DOCSFILE = 'data/DocumentCloud/documents.json'
SUBSET_DIR = 'data/DocumentCloud/subset'


def copyfile(url, dest, verbose=False):
    n = len('https://assets.documentcloud.org-documents-')
    fn = url[n:].replace('/', '-')
    path = os.path.join(CACHEDIR, fn)
    dest = os.path.join(dest, fn)
    if os.path.exists(path):
        shutil.copyfile(path, dest)
    else:
        print('File does not exist:', path)


def create_subset(string_match='', verbose=False):
    with open(DOCSFILE) as f:
        data = json.load(f)
        for doc in data:
            if string_match.lower() in doc['source'].lower():
                print(doc['source'])
                url = doc['resources'].get('text')
                copyfile(url, SUBSET_DIR)


if __name__=='__main__':
    verbose = '-v' in sys.argv
    match = sys.argv[-1] if len(sys.argv) > 1 and sys.argv[-1] != '-v' else ''
    create_subset(string_match=match, verbose=verbose)
