fart = True
name_list = []
while fart == True:
    name = input("Enter a name: ")
    if name == 'exit':
        fart = False
    elif name == 'done':
        answer = input("Are you ready to select a name? Type yes or no?")
        if answer == 'no':
            pass
        elif answer == 'yes':
            list = " or ".join(name_list)
            gifter = input(f"Who are you selecting a name for {list}?")
        else:
            pass
    else:
        print("Your have entered: ", name)
        name_list.append(name)
        print("Name List: ", ', '.join(name_list))
