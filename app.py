import config
from openstates import openStates

apikey = config.openstate

o = openStates(apikey)

names = o.search_people("Smith")

for index in range(0, len(names)):
    print(
        names[index].get("name"),
        names[index].get("party"),
        names[index]["jurisdiction"]["name"],
    )
    
print(names)
