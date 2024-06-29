from Document import Document
from Group import Group
import json

with open("proprieties.json") as file:
    data = json.load(file)
list_of_names = []
list_of_priorities = []
for x in data["data"]:
    doc = Document(x)
    list_of_names.append(doc.getName())
    list_of_priorities.append(doc.getPriority())

group = Group("My Files", "RED", list_of_names, list_of_priorities)
group.orderByAlpha()
group.orderByPriority()