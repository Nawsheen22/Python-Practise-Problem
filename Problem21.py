'''Input a list like ["apple","banana","car","dog","orange","cat"] and sort them by their length and print them using dictionary where the output will be like-
3 : ['car','dog','cat']
5 : ['apple']
6 : ['banana','orange']'''


Old_List=["apple","banana","car","dog","orange","cat"]

New_list=(sorted(Old_List,key=len))


dictionary_Storage={}


for x in New_list:
    length=len(x)
    if length not in dictionary_Storage:
      dictionary_Storage[length]=[]
    dictionary_Storage[length].append(x)

print(dictionary_Storage)



