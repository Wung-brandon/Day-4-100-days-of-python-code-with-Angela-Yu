""" import random

toast = random.randint(0,1)
if toast == 1:
    print('Heads')
else:
    print('Tail') """

# LINEAR SEARCH ALGORITHM

def linear_search(number_list,number_to_find):
    for index,element in enumerate(number_list):
        #print(element)
        if element == number_to_find:
            return index
    return -1

if __name__ == '__main__':
    numbers_list = [2,4,6,8,3,6,9,34,12,56,89]
    print(len(numbers_list))
    number_to_find = 34
    index = linear_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using linear search")