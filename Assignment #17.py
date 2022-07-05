# Q1. Assign the value 7 to the variable guess_me. Then, write the conditional tests (if, else, and elif) to
#     print the string 'too low' if guess_me is less than 7, 'too high' if greater than 7, and 'just right' if equal to 7.

guess_me = 7
if guess_me < 7:
    print("too low")
elif guess_me > 7:
    print("too high")
else :
    print("just right")


# Q2. Assign the value 7 to the variable guess_me and the value 1 to the variable start. Write a while
#     loop that compares start with guess_me. Print too low if start is less than guess me. If start equals
#     guess_me, print 'found it!' and exit the loop. If start is greater than guess_me, print 'oops' and exit
#     the loop. Increment start at the end of the loop.

guess_me = 7
start = 1
while start <= guess_me:
    if start < guess_me:
        print("too low")
    elif start == guess_me:
        print("found it!")
    else :
        print("oops")
    start +=1


# Q3. Print the following values of the list [3, 2, 1, 0] using a for loop.

l = [i for i in range(3,-1,-1)]
print(l)


# Q4. Use a list comprehension to make a list of the even numbers in range(10)

evens = [i for i in range(10) if i%2==0]
print(f"List Comprehension: {evens}")


# Q5. Use a dictionary comprehension to create the dictionary squares. Use range(10) to return the
#     keys, and use the square of each key as its value.

d = {i:i**2 for i in range(10)}
print(f"Dictionary Comprehension: {d}")


# Q6. Construct the set odd from the odd numbers in the range using a set comprehension (10).

odd_set = {i for i in range(10)}
print(f"Set Comprehension: {odd_set}")


# Q7. Use a generator comprehension to return the string 'Got' and a number for the numbers in
#     range(10). Iterate through this by using a for loop.

gen = (i for i in range(10))
for genval in gen:
    print('Got',genval)


# Q8. Define a function called good that returns the list ['Harry', 'Ron', 'Hermione'].

def good():
    return ['Harry', 'Ron', 'Hermione']
print(good())


# Q9. Define a generator function called get_odds that returns the odd numbers from range(10). Use a
#     for loop to find and print the third value returned.

def get_odds():
    for i in range(1,10,2):
        yield i

num = 1
for i in get_odds():
    if num == 3:
        print("Third number",i)
        break
    num+=1


# Q10 Define an exception called OopsException. Raise this exception to see what happens. Then write
#     the code to catch this exception and print 'Caught an oops'.

class OopsException(Exception):
    pass

# raise OopsException ("Caught an oops")

try :
    a = 10
    b = 'sudh'
    if type(b) == str:
        raise OopsException ("Caught an oops")
    print("This will not print")
except OopsException as ops:
    print(ops)


# Q11. Use zip() to make a dictionary called movies that pairs these lists:
#      titles = ['Creature of Habit', 'Crewel Fate'] and
#      plots = ['A nun turns into a monster', 'A haunted yarn shop'].

titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
movies = dict(zip(titles,plots))
print(movies)

