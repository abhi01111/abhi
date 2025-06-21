# 1) Given a dictionary of students and their favourite colours:
# people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
# A. Find out how many students are in the list
# B. Change Lisa’s favourite colour
# C. Remove 'Jenny' and her favourite colour
# D. Sort and print students and their favourite colours alphabetically by name



def function():
    people = {
        "Arham" : "Blue",
        "Lisa" : "Yellow",
        "Vinod" : "Purple",
        "Jenny" : "Pink"
    }

    # for question A
    for key in people.keys():
        print(f"key = {key} , value = {people[key]}")

    print("-" * 100)

    #for question B
    people['Lisa'] = 'Red'
    print(people)

    print("-" * 100)

    #for question C
    key_B = people.pop("Jenny", None)
    print(f"key = {key}")

    print("-" * 100)

    for key in people.keys():
        print(f"key = {key} , value = {people[key]}")

    print("-" * 100)

    #for question D
    mykeys= list(people.keys())
    mykeys.sort()

    print(people)




    print("-" * 100)

function()