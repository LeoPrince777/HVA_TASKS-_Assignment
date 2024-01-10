sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict['class'])
print(sampleDict['class']['student']['marks'])
print(sampleDict['class']['student']['name'])
#print(sampleDict['class']['student']['name']['marks']['history'] )  TypeError: string indices must be integers
print(sampleDict['class']['student']['marks']['history'])
print(sampleDict['class']['student']['marks']['physics'])


employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
#res =dict()
#res.fromkeys(employees,defaults)
res = dict.fromkeys(employees,defaults)
print (res)