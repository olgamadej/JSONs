import json

#Load the JSON data from a file
with open('updatedfrench.json', 'r', encoding='utf-8') as file:
	data = json.load(file)

#Create ids for all objects
for i, entry in enumerate(data, start=1):
	entry['id'] = i

#Save the updated JSON data back to the file
with open('withids.json', 'w', encoding='utf-8') as file:
	json.dump(data, file, ensure_ascii=False, indent=4)
