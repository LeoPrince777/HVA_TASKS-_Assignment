#Assignment -8
sample_dict = {
"name": "Kelly",
"age":25,
"salary": 8000,
"city": "New york"
}

sample_dict["location"] = sample_dict.pop('city')
print(sample_dict)

#Assignment -9
sample_dict = {
'Physics': 82,
'Math': 65,
'history': 75}

mini = min(sample_dict)
print(mini)
print(min(sample_dict.keys()))
print(min(sample_dict.values()))
print(min(sample_dict.items()))

#Assignment -10
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},  1st Dict
    'emp2': {'name': 'Emma', 'salary': 8000},   2nd
    'emp3': {'name': 'Brad', 'salary': 500}
}

print(sample_dict['emp3']['salary'])

sample_dict['emp3']['salary'] = 8500
print(sample_dict['emp3'])



