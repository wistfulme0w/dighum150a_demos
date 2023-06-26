
# This code simulates a long car ride with an 8 year old child. It also demonstrates flow of control in code
# with a while loop and multiple if-statements.

def FlowDemo():
    print("Would you like to hear a joke? y/n")

    # Get the user's input, make it lower case, and store it in the variable "telljoke".
    # Make it  lowercase so that we don't have to account for all the weird cases of capitalization.
    telljoke = input().lower()
    if telljoke == "yes" or telljoke == "y":
        print("Ok. Here's my favorite.")
        whowasleft = "repete"
        while whowasleft == "repete":
            print("Pete and Repete were in a boat. Pete fell out. Who was left?")
            whowasleft = input().lower()
            if whowasleft == "repete":
                print("*giggle* Ok.")
            else:
                print(":(")
    elif telljoke == "no" or telljoke == "n":
        print("Fine. Be that way.")
    else:
        print("I don't understand that. Sorry.")


if __name__ == "__main__":
    FlowDemo()
