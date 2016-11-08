#main function calls menu

#create empty dictionary

#keys are names of lists and values are lists
'''
menu function



functions:
    display keys
    disply values of specifc key
    add key to dictionary
    add value to specifc key
    remove value from, specific key
    remove entire key/values from dictionary
    type exit to exit
''' 
dictionary_of_lists = {}

def main():
    print"Welcome! This program allows you to create various lists. Please choose from the following options: "
    menu()

def menu():
    while(True):
        print"To show the main menu, press 0."
        print"To show all lists, press 1."
        print"To show a specific list, press 2."
        print"To add a new shopping list, press 3."
        print"To add an item to a shopping list, press 4."
        print"To remove an item from a shopping list, press 5." 
        print"To remove a list by nickname, press 6."
        print"To exit, press 7."
        user_choice = int(raw_input("choose an option: "))
       
        if user_choice ==7:
            break
        elif user_choice == 0:
            pass
        elif user_choice == 1:
            print dictionary_of_lists
        elif user_choice == 2:
            list_key = raw_input("what list would you like to see? ")
            print dictionary_of_lists[list_key]
        elif user_choice == 3:
            new_list=raw_input("what is the name of the shopping lists you want to make?")
            dictionary_of_lists[new_list] = []
        elif user_choice == 4:
            which_list = raw_input("what list would you like to add items to?")
            which_item = raw_input("what items would you like to add?")
            if "," in which_item:
                str_parser(which_item)
            add_to_list(which_list, which_item)

        elif user_choice == 5:
            pass
        elif user_choice == 6:
            pass
        else:
            print "You did not select one of the provided options. Please select a number from 1-7. "

def add_to_list(list_key, item):
    this_list = dictionary_of_lists[list_key]
    this_list.append(item)
    return this_list

def str_parser(item):
    item.split(", ")
    return item


if __name__ == '__main__':
    main()