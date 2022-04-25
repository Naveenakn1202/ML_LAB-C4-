import csv
a=[]
with open('datasheet1.csv','r') as csvfile:
    for row in csv.reader(csvfile):
        a.append(row)
    print(a)
    print("")
    
num_attributes = len(a[0])-1
s=['0']*num_attributes

g=[["?" for i in range(len(s))] for i in range(len(s))]


for i in range(0,len(a)):
    if a[i][num_attributes]=='yes':
        for j in range(0,num_attributes):
            if s[j]=='0' or s[j]==a[i][j]:
                s[j]=a[i][j]
            else:
                s[j]='?'
    else:
        for j in range(0,num_attributes):
            if(s[j] == a[i][j] or s[j] =='?'):
                g[j][j]='?'
                continue
            else:
                g[j][j] = s[j]
for j in range(0,num_attributes):
    if s[j]!=g[j][j] or s[j]=='?':
        g[j][j]='?'
        
indices = [i for i, val in enumerate(g) if val == ['?', '?', '?', '?', '?', '?']]     
for i in indices:
    g.remove(['?', '?', '?', '?', '?', '?'])
print("Specific hypothesis:",s)                
print("General hypothesis:",g)