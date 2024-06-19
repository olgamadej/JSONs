import json

#Load the JSON data from a file
with open('french.json', 'r', encoding='utf-8') as file:
	data = json.load(file)

#Ensure all 'subject' fields are arrays
for entry in data:
	if 'subject' in entry and isinstance(entry['subject'], str):
		entry['subject'] = [entry['subject']]

#Save the updated JSON data back to the file
with open('updatedfrench.json', 'w', encoding='utf-8') as file:
	json.dump(data, file, ensure_ascii=False, indent=4)