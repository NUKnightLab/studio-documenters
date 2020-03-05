import numpy as np
import json
from documentcloud import DocumentCloud

import numpy as np

client = DocumentCloud()

def entity_comp(entity):
	return entity.relevance

def search_json():
	with open('long_data.json') as f:
		entities_dict = json.load(f)

	# Using DocumentCloud API to pull document data
	obj = client.documents.get('5839910-Illinois-Medical-District-Commission-2016-05-17')
	entities = obj.get_entities()
	# Sort by relevance - a property of entities pulled from the API
	entities.sort(key=entity_comp,reverse=True)

	names = []
	orgs = []
				
	# Seperating entities into people and organizations. Keep top 10 most relevant people and 
	# top 5 most relevant organizations
	person_entities = [x for x in entities if x.type == 'person']
	organization_entities = [x for x in entities if x.type == 'organization']
	for i in range(min(10,len(person_entities))):		
		names.append(person_entities[i].title)
	for i in range(min(5,len(organization_entities))):		
		orgs.append(organization_entities[i].title)
			
	# Looks for entity as dictionary key in long_data.json.
	# Take all related articles and attach them to dictionary with entity name as key
	# repeat for organizations
	ppl_articles_dict = {}
	for i in range(min(10, len(person_entities))):
		entity = person_entities[i]
		try:
			others = entities_dict[entity.title]			
			for j in range(len(others) - 1):			
				try:
					ppl_articles_dict[entity.title].append(others[j + 1])
				except:
					ppl_articles_dict[entity.title] = [others[j + 1]]			
		except:
			pass

	org_articles_dict = {}
	for i in range(min(5, len(organization_entities))):
		entity = organization_entities[i]
		try:
			others = entities_dict[entity.title]			
			for j in range(len(others) - 1):			
				try:
					org_articles_dict[entity.title].append(others[j + 1])
				except:
					org_articles_dict[entity.title] = [others[j + 1]]			
		except:		
			pass	

	# Returns name of article, names of entities (people and orgs), and linked dictionaries
	return obj.title, names, orgs, ppl_articles_dict, org_articles_dict
		