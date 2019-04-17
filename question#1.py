#reading the input_sentence.txt file
try:
    with open("input_numbers.txt","r") as input_sentence:
        sentence = input_sentence.read()
except FileNotFoundError:
    sentence = None

#converting string into list to sperate each numbers
list1 = list(sentence.split(","))

#converting the string seperated list into list of integer
list2= []
for i in range(len(list1)):
    list2.append(int(list1[i]))

#sort / sorted function cannot be used as it ommits 0
#sorting function that sort number on ascending order
def sort_ascending(lists):
    for i in range(len(lists)):
        for j in range(1, len(lists)-i):
            # swap if prev value is less than current value
            # change < to > to reverse the order
            if lists[j-1] > lists[j]:
                # do a tuple swap
                (lists[j-1], lists[j]) = (lists[j], lists[j-1])

#calling the sorting function
sort_ascending(list2)

#writing the sorted value in file
with open('output_numbers.txt','w') as f:
    for i in list2:
        #to remove comma after last element
        if i == list2[-1]:
            print(i,file=f)
        else:
            print(i,file=f, end=',')

print("The output_number.txt file has been created")
