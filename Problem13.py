#you want to print only those that has 'a' in its name



Oldlist=["Mango","Apple","Singara","PineApple","Mimi"]

Newlist=[]

for x in Oldlist:
    if "a" or "A" in x:
        Newlist.append(x)

        print(x)

#list library are : remove , insert , append , index insertion

Colourlist=["Pink","Yellow","Orange","Green","Chocolate"]

Colourlist.append("Strawberry")
print(Colourlist)

Colourlist.insert(3,"Chicken")
print(Colourlist)
Colourlist.remove("Pink")
print(Colourlist)
Colourlist[3]="Yuyuyu"  #Must be within the present list

print(Colourlist)



colorlist1=["Magenta"]
colorlist2=["Pink"]

zz=colorlist1+colorlist2
print(zz)




