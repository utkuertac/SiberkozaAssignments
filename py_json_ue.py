# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample JSON
user_ueJSON ='{"first_name_ue": "Utku", "last_name_ue": "Ertaç", "age_ue": 22}'

# Parse to dict
user_ue = json.loads(user_ueJSON)

print(user_ue)
print(user_ue['first_name_ue'])

car_ue = {'make_ue': 'Ford', 'model_ue': 'Mustang', 'year_ue': 1970}

car_ueJSON = json.dumps(car_ue)

print(car_ueJSON)
