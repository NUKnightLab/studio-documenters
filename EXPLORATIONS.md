# Getting started with the data

## documents.json

The documents.json file comes from DocumentCloud. It is a dump of all the metadata for the documents in the project.

### simple approaches

... that probably won't work well for this file.

Normally, I would say Firefox does a nice job of formatting json files if you just open it in the browser .. However, this file:

 1. is formatted as a list, not an object. At least for me, I am finding that FF doesn't really like this format so much.
 2. is a big file!

.. so, you'll probably want to skip right ahead to something more useful.

To pretty print a json file, you can use python's json tool:

```
$ python -m json.tool documents.json
```
But again, this is a pretty big file, so you won't do much with this.


### jq

[jq](https://stedolan.github.io/jq/) is a really handy command-line tool if you ever need to dig into some json files.

Here are a couple of queries to get you started.

What are the sources of the docs. Note: we need to do this `[]|` pipe thing because of the list format of the data. See the [jq docs](https://stedolan.github.io/jq/) for more info.

```
jq '.[]|.source' documents.json
```

Sort them

```
jq '.[]|.source' documents.json | sort
```

Remove duplicates and get the count of each source

```
jq '.[]|.source' documents.json | sort | uniq -c
```

### In code

At some point, you will want to do more than just see what's there. You will want to be able to do some in-code investigations. You can load up documents.json in python:

```
>>> import json
>>> docs = json.load(open('documents.json'))
```

Which will give you a list of dictionary objects. However, for the sake of more sophisticated querying, there is a TinyDB version of the data called db.json (created with the makedb tool).

As an example, what are the Chicago document sources and how many docs for each?

```
  >>> from collections import Counter
  >>> from tinydb import TinyDB, Query
  >>> db = TinyDB('db.json')
  >>> q = Query()
  >>> docs = db.search(q.source.matches('Chicago'))
  >>> counter = Counter([doc['source'] for doc in docs])
```
