#Create a dictionary
sample_dict = {
  "name": "Pulkit",
  "age": 23,
  "city": "Agra",
}

# Accessing values in a dictionary
print(sample_dict["name"])
print(sample_dict)

# Create a list with the same information to show the difference between list and a dictionary
sample_list = ["Pulkit", 23, "Agra"]
print(sample_list[0])

# Get the list of keys
print(sample_dict.keys())

# Get the list of values
print(sample_dict.values())

for key in sample_dict.keys():
	print(key, sample_dict[key])
	
# Check if the key exists in the dictionary or not
if "country" in sample_dict:
	print(sample_dict["country"])
else:
	print("key does not exist")
	
# Add a key-value pair to the dictionary
sample_dict["Profession"] = "Software Engineer"
print(sample_dict)

# Delete a key-value pair
del(sample_dict["Profession"])
print(sample_dict)

# Change a value in the dictionary
sample_dict["city"] = "Bangalore"
print(sample_dict)

# Store a list as a value in the dictionary
sample_dict["marks"] = [99,87, 85, 92, 90]
print(sample_dict)

# Access a value in the list stored in the dictionary
print(sample_dict["marks][1])

# Create a nested dictionary
classroom = {
  "PulkitChawla" : {
    "age": 23,
    "marks": [89, 85, 90, 86, 90]
  },
  "Kanishk": {
    "age": 13,
    "marks": [90, 95, 85, 87, 80]
  }
}

# Go through basic dictionary operations for nested dictionary
print(classroom.keys())
print(classroom.values())

for i in classroom.keys():
	print(classroom[i])

classroom["PulkitChawla"]["age"] = 30

