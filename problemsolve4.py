
def determine_gender(username):

    if len(username) == 1:

        return "boy"

    else:

        return "girl"


username = input("Enter the username: ")

gender = determine_gender(username)

print("The user is", gender)