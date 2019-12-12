"""
Build a TinyDB from a DocumentCloud documents.json file

See the TinyDB docs for info about using the resulting database.
https://tinydb.readthedocs.io/en/latest/index.html

E.g.:

What are the Chicago document sources and how many docs for each?

```
  >>> from collections import Counter
  >>> from tinydb import TinyDB, Query
  >>> db = TinyDB('db.json')
  >>> q = Query()
  >>> docs = db.search(q.source.matches('Chicago'))
  >>> counter = Counter([doc['source'] for doc in docs])
```
"""
import json
import os
import sys
from tinydb import TinyDB


def makedb(docsfile, dbfile):
    db = TinyDB(dbfile)
    with open(docsfile) as f:
        data = json.load(f)
        db.insert_multiple(data)
    print('Done!')


if __name__=='__main__':
    try:
        docsfile = sys.argv[1]
        dbfile = sys.argv[2]
    except IndexError:
        print('\nUsage: makedb.py docsfile dbfile')
        sys.exit(0)
    if os.path.exists(dbfile):
        print('\n!! DB file already exists. Delete it first in order to recreate.')
        sys.exit(0)
    makedb(docsfile, dbfile)
