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
    elif userinput == "s":
        # See all entries
        for key, val in authorinfo.items():
            nationality = val.get("nationality", "nowhere")
            books = val["books"]
            bookstolist = "nothing"
            if len(books) > 1:
                # str.join is the opposite of list.split()
                bookstolist = ", ".join(books[0:-1]) + " and " + books[-1]
            elif len(books) == 1:
                bookstolist = books[0]
            print(f"{key} comes from {nationality} and has written {bookstolist}.")
    elif userinput == "g":
        print("For which author do you want to get all the books?")
        author = input()
        if not author in authorinfo.keys():
            print("Sorry, we have nothing for that author.")
        else:
            books = authorinfo[author]["books"]
            bookstolist = books[0]
            if len(books) > 1:
                # str.join is the opposite of list.split()
                bookstolist = ", ".join(books[0:-1]) + " and " + books[-1]
            print(f"{author} has written {bookstolist}.")
    elif userinput == "a":
        print("Please enter an author name in the format lastname, firstname.")
        author = input()
        print("Where is this person from?")
        nationality = input()
        if not author in authorinfo.keys():
            authorinfo[author] = {"books": [],
                                  "nationality": nationality}
        else:
            print(f"{author} is already in the dictionary.")
    elif userinput == "b":
        print("Who is the author of the book you wish to add? (lastname, firstname)")
        author = input()
        print("What is the title of the book you would like to add?")
        title = input()
        # if the author doesn't exist in the dictionary, add them.
        if author not in authorinfo.keys():
            authorinfo[author] = {"books": []}
        if title not in authorinfo[author]["books"]:
            authorinfo[author]["books"].append(title)
    elif userinput == "n":
        print("Which nationality would you like to search for?")
        nationality = input()
        authorsofnationality = []
        for key, val in authorinfo.items():
            nat = val.get("nationality", "nothing")
            if nat == nationality:
                authorsofnationality.append(key)
        authorstring = ", ".join(authorsofnationality)
        print(f"The authors from {nationality} are {authorstring}.")
print("Goodbye!")
