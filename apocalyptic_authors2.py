#This is a global variable. All functions in this file have access to it, and functions in other files will too if this file gets imported into them.
authorinfo = {
    "Muir, Tamsyn": {
        "books": ["Gideon the Ninth",
                  "Harrohark the Ninth",
                  "Nona the Ninth"],
        "nationality": "New Zealand"
    },
    "Cixin, Liu": {
        "books": ["Three Body Problem"],
        "nationality": "China"
    },
    "Vandermeer, Jeff": {
        "books": ["Annihilation",
                  "Authority",
                  "Acceptance"],
        "nationality": "USA"
    },
}

#takes a list and makes it into a comma seperated string with the word "and" before the last element.
def listToEnglishString(listtostring):
    if len(listtostring) == 0:
        return ""
    if len(listtostring) == 1:
        return listtostring[0]
    concatstring = ", ".join(listtostring[0:-1]) + " and " + listtostring[-1]
    return concatstring

#takes an author, and prints the nationality and list of books written by that author.
def printInfoForAuthor(author):
    if author in authorinfo.keys():
        info = authorinfo[author]
        nationality = info.get("nationality", "nowhere")
        books = info["books"]
        bookstring = "nothing"
        if len(books) != 0:
            bookstring = listToEnglishString(books)
        print(f"{author} is from {nationality} and wrote {bookstring}")

#takes an author and prints out the name of the author and all the books written by them
def printBooksForAuthor(author):
    if author in authorinfo.keys():
        books = authorinfo[author]["books"]
        bookstring = "nothing"
        if len(books) != 0:
            bookstring = listToEnglishString(books)
        print(f"{author} wrote {bookstring}")
    else:
        print(f"Sorry, we have nothing for author {author}")


# Given an author and a nationality, it adds them to the dictionary. It returns true if the author gets added, returns false if the author is already in the dictionary.
def addAuthor(author, nationality="nowhere"):
    if not author in authorinfo.keys():
        authorinfo[author] = {
            "books": [],
            "nationality": nationality
        }
        return True
    return False

#Given an author and a book title, this function adds the book title for the list of books for the author.
def addBookForAuthor(author, booktitle):
    returnval = True
    if not author in authorinfo.keys():
        addAuthor(author)
    if not booktitle in authorinfo[author]["books"]:
        authorinfo[author]["books"].append(booktitle)
    else:
        returnval = False
    return returnval

#Given a nationality, this function creates and returns a list of authors of the nationality.
def getAuthorsOfNationality(nationality):
    authors = []
    for author, info in authorinfo.items():
        if info["nationality"] == nationality:
            authors.append(author)
    return authors

#Processes user input for the apocalyptic author program.
def processInput(userinput):
    if userinput == "q":
        return
    elif userinput == "s":
        for key in authorinfo.keys():
            printInfoForAuthor(key)
    elif userinput == "g":
        print("For which author do you want to get all the books?")
        author = input()
        printBooksForAuthor(author)
    elif userinput == "a":
        print("Please enter an author name in the format lastname, firstname.")
        author = input()
        print("Where is this person from?")
        nationality = input()
        if not addAuthor(author, nationality):
            print(f"Author {author} already exists in database.")
    elif userinput == "b":
        print("Who is the author of the book you wish to add? (lastname, firstname)")
        author = input()
        print("What is the title of the book you would like to add?")
        title = input()
        if not addBookForAuthor(author, title):
            print(
                f"Book {title} already exists in database for author {author}")
    elif userinput == "n":
        print("Which nationality would you like to search for?")
        nationality = input()
        authors = getAuthorsOfNationality(nationality)
        authorstring = listToEnglishString(authors)
        print(f"Authors from {nationality} are {authorstring}.")


# This code gets run when the user executes the program from the command line.
if __name__ == "__main__":
    userinput = ""
    print("Welcome to the Apocalyptic Author Dictionary!")
    while userinput != "q":

        options = ["s", "g", "a", "b", "n", "q"]
        # Note that \n is how you represent a carriage return
        print("\nWhat do you want to do? \n (s)ee all entries, \n (g)et all books by an author, \n(a)dd a new author, \n add a new (b)ook, \nget all authors of a (n)ationality, \n or (q)uit?")
        # I make the input lowercase so that the program behaves the same regardless of whether the user enters a capital or lowercase letter.
        userinput = input().lower()
        if userinput not in options:
            "Enter one of the specified options"
            continue
        processInput(userinput)
    print("Goodbye!")
