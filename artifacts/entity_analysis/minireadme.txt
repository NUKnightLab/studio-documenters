Usage Instructions:

For information on installing flask and virtual environments:
https://flask.palletsprojects.com/en/1.1.x/installation/#python-version
https://flask.palletsprojects.com/en/1.1.x/quickstart/

1. INSTALL FLASK WITH PIP using above link

2. Create virtual environment: 
$ python -m venv venv

3. Move formattedsearch, hello, and long_data.json.zip into venv

4. Enter venv and unzip long_data.json

5. To run on localhost:
$ export FLASK_APP=hello.py
$ flask run

6. To access, go to web browser and search localhost:5000/