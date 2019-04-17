#reading the input_sentence.txt file
try:
    with open("input_sentence.txt","r") as input_sentence:
        sentence = input_sentence.read()
except FileNotFoundError:
    sentence = None
    
#removing the \n from sentence because while reading file \n is added
#to last while the line finishes
sentence = sentence[:-1]

#converting string to list to check duplicate and unique strings
list1 = list(sentence.split(" "))

#finding the duplicate strings
duplicate = []
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] == list1[j] and list1[i] not in duplicate:
            duplicate.append(list1[i])
            break
        
#finding the unique strings
unique = []
for i in range(len(list1)):
    if list1[i] not in duplicate:
        unique.append(list1[i])
        
#finding all the duplicate strings
duplicate_word = []
for i in range(len(list1)):
    if list1[i]  in duplicate:
        duplicate_word.append(list1[i])

#printing the unique strings
print('Unique Words:',end=' ')
for i in range(len(unique)):
    print(unique[i],end=',')
print() #to print new line

#printing the duplicate words along with its count
print('Duplicate Words:',end=' ')
for i in range(len(duplicate)):
    print(duplicate[i],'-',duplicate_word.count(duplicate[i]),end=' ')         
print() #to print new line

duplicate.extend(unique)
#priting the strings after removing duplicates
print('Duplicate Eliminated:',end=' ')
for i in range(len(duplicate)):
    print(duplicate[i],end=' ')
