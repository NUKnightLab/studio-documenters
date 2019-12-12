# Documenters.org
Explorations for the Documenters.org project


## Tools

Recreate the DocumentCloud documents database

```
 $ rm data/DocumentCloud/db.json
 $ python -m tools.makedb data/DocumentCloud/documents.json data/DocumentCloud/db.json
```

Fetch OCR docs from DocumentCloud

```
 $ python -m tools.fetchdocs [-v]
```
