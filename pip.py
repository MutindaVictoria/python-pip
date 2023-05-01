#Write a Python function that takes two arguments (a and b) and returns their sum.
def add_sum(a,b):
    addition=a+b
    return addition

#Write a Python function that takes a string as input and returns the string reversed.
def word(names):
    statement=list(set(names))
    reversed_elements=statement[::-1]
    return reversed_elements

#Write a Python function that takes a list of integers as input and 
#returns the sum of all the integers in the list.
def num_addition(*nums):
    added=0
    for i in nums:
        added+=i
    return added

#Write a Python function that takes a list of integers as input and 
#returns a new list with all the even numbers removed.
def even_numbers_removed(nums):
    newlist=[]
    for i in nums:
        if i%2!=0:
            newlist.append(i)
    return newlist

#Write a Python function that takes a list of integers as input and 
#returns the highest value in the list.
def number_highest_value(num):
    a=max(num)
    return(a)

#Write a Python function that takes a list of strings as input and 
#returns a new list with all the strings capitalized.
def wordCasing(word):
    return word.capitalize() if len(word)>3 else word.lower()

title = ['tHe', 'souND', 'AND', 'the', 'fUrY']
result = list(map(wordCasing, title))
result[0] =result[0].capitalize()
