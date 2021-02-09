from functools import reduce

# lambda keyword
double = lambda x: x * 2
print(double(5))

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x % 2 == 0), my_list))
print("======new_lst=======",new_list)


# map() function
def addition(n):
    return n + n


numbers = (1, 2, 3, 3)
result = map(addition, numbers)
print("========result=========", result)
print("======type of result=======", type(result))
print("=============", list(result))

# reduce() function
# from functools import reduce required
numbers = [3, 4, 6, 9, 34, 12]


def custom_sum(first, second):
    return first + second


result = reduce(custom_sum, numbers)
print(result)

# filter() function
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']


def filterVowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if (letter in vowels):
        return True
    else:
        return False


filteredVowels = filter(filterVowels, letters)
print("=======filteredvowels=======", filteredVowels)

print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)

# join() function
list1 = ['1', '2', '3', '4']
s = "-"
s = s.join(list1)
print(s)

list1 = ['g', 'e', 'e', 'k', 's']
print("".join(list1))
