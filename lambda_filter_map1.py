#Write a Python program to square the elements of a list using map() function.
#Sample List: [4, 5, 2, 9]
#Square the elements of the list:
#[16, 25, 4, 81]
def numbers(nums):
    square_numbers=map(lambda x:x*2,nums)
    return list(numbers)
mylist=[4,5,2,9]
result=numbers(mylist)
print (result)