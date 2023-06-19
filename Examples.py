# ------------------------
# ----Show_Skills---------
# ------------------------
# [1]
myskills_withoutrank = ("Excel", "Tableau", "R")

myskills_withrank = {"python": "80%", "M/L": "50%", "D/L": "90%"}


def show_skills(name, *skills_withoutrank, **skills_withrank):
    print(f" Hello {name.strip().capitalize()} to show your skills :   ")

    for skl in skills_withoutrank:
        print(f" {skl.capitalize()}  ")
    print("=" * 30)
    for skll, sklll in skills_withrank.items():
        print(f" {skll.capitalize()} => {sklll}")


# call fun

# show_skills("gamal", *myskills_withoutrank, **myskills_withrank)

# -----------------------------------------------------------------------------

# ------------------------
# ----Check Password------
# ------------------------
# [2]


def check_pass(password):
    tries = 3

    while tries > 0:
        correctpass = "gamal"

        if password != correctpass:
            tries -= 1
            print(f" you enter uncorrect pass and left {tries} chance ")

        else:
            print(f" you enter correct pass ,  Welcome ")

            break

        inputpass = input(" please write pass : ")

        password = inputpass

    else:
        print(" connect to support team to solve Problem ")


# inputpass = input(" please write pass : ")


# call fun

# check_pass(inputpass)

# ------------------------------------------------------------------

# ------------------------
# ----clean word----------
# ------------------------
# [3]
# word => "wwwoooooorlldddd"


def clean_word(word):
    if len(word) == 1:
        return word

    if word[0] == word[1]:
        return clean_word(word[1:])

    return word[0] + clean_word(word[1:])


# call fun

# print(clean_word("wwwoooooorlldddd"))

# print(clean_word("ggaaaammmmmaalll"))


# -----------------------------------------------------------------

# ------------------------
# ----lambda fun----------
# ------------------------
# [4]
info = (
    lambda fname, mname, lname, age: f" My name is {fname.strip().capitalize()} {mname.capitalize():.1s} {lname.capitalize()} and your age is {age} "
)

# print(info("gamal","hisham","saad",26))

# -------------------------------------------------------------------

# ------------------------
# --find duplicate value--
# ------------------------
# [5]


def find_duplicate(elements):
    duplicate_value = []
    unduplicate_value = []

    for element in elements:
        if element in unduplicate_value:
            duplicate_value.append(element)

        else:
            unduplicate_value.append(element)

    return unduplicate_value, duplicate_value


# call fun
data = [1, 3, 5, 5, 6, 8, 7, 5, 8, 9, 3, 1, 1]

# print(find_duplicate(data))

# ------------------------------------------------------------------------------
# find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False
# [6]

# def check(data):
#     return data.count(19) == 2 and data.count(5) >= 3


# mydata = [19, 1, 19, 5, 6, 7]
# mydata = [5, 1, 19, 5, 6, 5, 7]
# mydata = [19, 1, 19, 5, 6, 7, 5, 5]

# print(check(mydata))

# -------------------------------------------------------------------------------
# program that accepts a list of integers and calculates the length and the fifth element
# and Return true if the length of the list is 8 and the fifth element occurs thrice in the said list
# [7]

# def check(data):
#     return len(data) == 8 and data.count(mydata[4]) == 3


# # mydata = [5, 1, 19, 5, 6, 5, 7, 6]
# mydata = [5, 1, 19, 5, 5, 8, 7, 6]

# print(check(mydata))

# --------------------------------------------------------------------------------------------
# Write a Python program to get a string made of the first 2 and last 2 characters of a given string and
# If the string length is less than 2, return the empty string instead.
# [8]

# mystring = "gamal hisham"
# mystring = "f"


# def checkstring(string):
#     if len(string) < 2:
#         return " "

#     return string[0:2] + string[-2:]


# print(checkstring(mystring))
# ----------------------------------------------------------------------------------------

# Write a Python program to get a string from a given string
# where all occurrences of its first char have been changed to '$', except the first char itself.
# [9]

# mystr = "pepsi"
# mystr = "remaaremarg"


# def replace(mystring):
#     char = mystring[0]

#     mystring = mystring.replace(char, "$")

#     mystring = char + mystring[1:]

#     return mystring


# print(replace(mystr))
# -----------------------------------------------------------------------
# Write a Python program to count the number of strings from a given list of strings and
# The string length is 2 or more and the first and last characters are the same.
# [10]

# mydata = ["abc", "xyz", "aba", "1221", "saas"]


# def check(data):
#     count = 0

#     for x in data:
#         if len(data) > 1 and x[0] == x[-1]:
#             count += 1

#     return count


# print(check(mydata))
# ------------------------------------------------------------------------------------------------------
# check empty list
# [11]

# x = []      # empty list return false
# if not x :
#     print("list is empty")

# -----------------------------------------------------------------------------------------------------
# Write a Python program to find the list of words that are longer than n from a given list of words
# [12]

n = 4
mylist = ["gamal", "saad", "amr", "ahmed", "adel", "alaa"]

# def check (list,N):
#     longer_than_list = []

#     for word in list :
#         if len(list[list.index(word)]) > N :

#             longer_than_list.append(list[list.index(word)])

#     return longer_than_list

# print(check(mylist,n))

# another sol
# def longwords (data,x):
#     longerlist = []

#     for element in data :
#         if len(element) > x :

#             longerlist.append(element)

#     return longerlist

# print(longwords(mylist,n))
# ------------------------------------------------------------------------------------------------
# Write a Python script to concatenate the following dictionaries to create a new one.
# [13]

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4 = {}

# for d in (dic1,dic2,dic3) :

#     dic4.update(d)

# print(dic4)
# --------------------------------------------------------------------------------------------------------
# Write a Python script to check whether a given key already exists in a dictionary
# [14]

# mykey = 9

# mydict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# def check_key (dic , key):

#     if key in dic :
#         print(" key is present in dictionary")

#     else:
#         print(" key isn\'t present in dictionary")

# check_key(mydict,mykey)

# ----------------------------------------------------------------------------------------------------