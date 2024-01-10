#Assignment -5
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys = ["name", "salary"]

Ret= {k:sample_dict[k]for k in keys}
print(Ret)

res = dict()
for k in keys:
    res.update({k: sample_dict[k]})
    print(res)
print(res)    
    
#Assignment -6
for k in keys:
    sample_dict.pop(k)
print(sample_dict)



#Assignment -7
sample_dict = {'a': 100, 'b': 200, 'c': 300}

for j in sample_dict.values():
    if j == 200:
        print(f"yes! {j} is present in Dictionary")
        
for k,v in sample_dict.items():
    if v == 200:
        print(f"yes! {v} is present in Dictionary")
        
for k in sample_dict.keys():        
    if(sample_dict.get(k)==200):
        print(f"Wow!!{sample_dict.get(k)} is present in our Dictionary")
        
if 200 in sample_dict.values():
    print("200 is present in Dict")
