print("#### Assignment -1 #####\n")
str1 = "James"
print(str1[::2])

s = str1[0]+str1[2]+str1[4]
print(s)

print("#### Assignment -2 #####\n")
s = int(len(str1)/2)
s1 = str1[0]+str1[s]+str1[-1]
print("s1:",s1)

#str2 = "JhonDipPeta"
str2 = "JaSonAy"
st = int((len(str2)-3)/2)
print(st)
st1 = str2[2:5]
print(st1)

s1 = "Ault"
s2 = "Kelly"
s3 = s1[0:2]+s2[:]+s1[-2:]
print("#### Assignment -3 #####\n",s3)


print("#### Assignment -4 #####\n")
s4 = "America"
s5 = "Japan"
m4 = int(len(s4)/2)
print(m4)
m5 = int(len(s5)/2)
print(m5)
s6 = s4[0]+s5[0]+s4[m4]+s5[m5]+s4[-1]+s5[-1]
print(s6)

print("#### Assignment -5 #####\n")
T1 =""        
T = "PyNaTive"
for i in T:
    if i in T.lower():
        T1+=i
for j in T:
    if j in T.upper():
        T1+=j
print(T1)
 
print("#### Assignment -6 #####\n") 
import re 
ct = "P@#yn26at^&i5ve"
count_albha  = len(re.findall('[A-Za-z]',ct))
count_digit  = len(re.findall('[0-9]',ct))
count_Special = len(re.findall('[~*<>#@^&!]',ct))
print(count_albha,count_digit,count_Special)

#ct = "P@#yn26at^&i5ve"
count = len([i for i in ct if i.isalpha()])
#res   = len([ele for ele in test_str if ele.isalpha()])
print(count)


print("Total counts of chars, digits, and symbols")
count=""
count1=""
count2=""
ct = "P@#yn26at^&i5ve"
for j in ct:
    if j.isalpha():
        count= count+j
        ct1 = len(count)
print("char:",ct1)
count1=""
for k in ct:
    if k.isdigit():
        count1= count1+k
        ct2= len(count1)
print("Digits:", ct2)
count2=""
sp = "~*<>#@^&!"
for l in ct:
    if l in sp:
        count2= count2+l
        ct3= len(count2)
print("symbols:", ct3)

 
print("#### Assignment -7 #####\n")

x1 = "Abc" 
x2 = "Xyz"
mid_x1 = int(len(x1)/2)
#print(x1m)
mid_x2 = int(len(x2)/2)
#print(x2m)
Fin_str = x1[0]+x2[-1]+x1[mid_x1]+x2[mid_x2]+x1[-1]+x2[0]
print(Fin_str)
        
print("#### Assignment -8 #####\n")
s1 = "Yna" 
s2 = "PYnative"
if s1 in s2:
    print("True")     
else:
    print("False")
    
    
print("#### Assignment -9 #####\n")    

wd = "Welcome to USA. usa awesome, isn't it?"
wd1 ="USA"
t_wd = wd.lower()
cnt = t_wd.count(wd1.lower())
print(cnt)

if wd1 in t_wd:
    cnt+=1
print(cnt)



print("#### Assignment -10 #####\n")

str1 = "PYnative29@#8496"
count =0
total =0
for i in str1:
    if i.isdigit():
        total = int(i)+total
        count=count+1
print(count)
avg = total/count
print("Sum and Average: ", total, avg)


        

        
