from flask import Flask
import sys
from formattedsearch import search_json

app = Flask(__name__)

@app.route('/')
def hello_world():

	# Retrieve list of other documents using formattedsearch
	article_name, names, orgs, ppl_articles_dict, org_articles_dict = search_json()

	# Setting up javascript to expand and collapse list
	html = '''<script> 
				function toggleFunc(id) {
				  var x = document.getElementById("myDIV" + id);
				  var btn = document.getElementById("button" + id)
				  if (x.style.display === "none") {
				    x.style.display = "block";
				    btn.innerHTML = "Hide Related Documents";
				  } else {
				    x.style.display = "none";
				    btn.innerHTML = "Show Related Documents";
				  }
				}
			</script>'''

	# Page Title
	html += "<h1> Entity Analysis for Article: " + article_name + "</h1>"

	# Goes through list of people
	counter = 0
	html += "<h2> Most Relevant People and Associated Documents </h2>"
	for ent in ppl_articles_dict.keys():
		dict_obj = ppl_articles_dict[ent]
		# Decide if this article is in the dictionary or not
		if article_name in [x[0] for x in dict_obj]:
			dict_size = len(dict_obj) - 1
		else:
			dict_size = len(dict_obj)
		# [Entity name] - [Number of related documents], and button to expand and collapse
		html += "<div style='width:600px; display:flex; justify-content:space-between'><h4>" + ent + " - " + str(dict_size) +" related docs</h4><button id = 'button" + str(counter) + "' onClick='toggleFunc(" + str(counter) + ")'>Show Related Documents</button></div>"
		# Within the collapsible zone, have list of related documents
		html += "<ol style='display:none;' id='myDIV" + str(counter) + "'>"
		counter += 1
		for i in dict_obj:
			if i[0] == article_name:
				continue
			html += "<li><a target=_blank href="+i[1]+">"+i[0]+"</a></li>"
		html += "</ol>"

	# Repeat for organizations
	html += "<h2> Most Relevant Organizations and Associated Documents </h2>"
	for ent in org_articles_dict.keys():
		dict_obj = org_articles_dict[ent]
		if article_name in [x[0] for x in dict_obj]:
			dict_size = len(dict_obj) - 1
		else:
			dict_size = len(dict_obj)
		html += "<div style='width:600px; display:flex; justify-content:space-between'><h4>" + ent + " - " + str(dict_size) +" related docs</h4><button id = 'button" + str(counter) + "' onClick='toggleFunc(" + str(counter) + ")'>Show Related Documents</button></div>"
		html += "<ol style='display:none;' id='myDIV" + str(counter) + "'>"
		counter += 1
		for i in dict_obj:
			if i[0] == article_name:
				continue
			html += "<li><a target=_blank href="+i[1]+">"+i[0]+"</a></li>"
		html += "</ol>"

	html += "</body>"

	return html
