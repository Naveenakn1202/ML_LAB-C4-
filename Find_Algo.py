import csv

def updatehypothesis(x,h):
    if h == []:
        for i in range(0,len(x)):
            h.append("$")

        print("Initial State : ", h)
        return x
    
    for i in range(0,len(x)):
        if x[i].upper() != h[i].upper() :
            h[i] = "?"
            
    print("Most Specific Hypothesis : ", h)       
    return h

if __name__ == "__main__":
    data = []
    h = []
    
    with open('datasheet1.csv','r') as file :
        reader = csv.reader(file)
        print("Data Set : ")
        
        for row in reader:
            data.append(row)
            print(row)

    if data:
        for x in data:
            if x[-1].upper() == "YES":
                x.pop()
                h = updatehypothesis(x,h)
    
    print("Maximally Specific Hypothesis : " , h)