import json  

# Sample data to write  
data = {  
    "name": "Alice",  
    "age": 30,  
    "city": "New York",  
    "is_student": False  
}  

# Writing to a JSON file  
with open('data.json', 'w') as json_file:  
    json.dump(data, json_file)  

# Reading from the JSON file  
with open('data.json', 'r') as json_file:  
    loaded_data = json.load(json_file)  

# Display the loaded data  
print(loaded_data)