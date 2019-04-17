#taking user input for array and integer
user_input = input("Enter a array elements separated by comma:\n")
#converting the user provided elements to list/array 
array_list=list(int(x) for x in user_input.split(','))
integer = int(input("Enter a number:\n"))

#function to check similarity of list/array and integer number
def similarity_check(array,integer):
    integer = str(integer)
    counter = 0
    index=0
    
    #removing the leading zeros
    if array[0] == 0:
        for i in range(len(array)):
            if array[i]>0:
                index = i
                break
    array = array[index:]

    #checking the similarity
    if len(array) == len(integer):
        for i in range(len(integer)):
            if array[i] == int(integer[i]):
                counter += 1
    if counter == len(array):
        return 1
    else:
        return 0

print(similarity_check(array_list,integer))


