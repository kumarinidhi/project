def start_chat(name, age, rating):
    show_menu = True
    while show_menu:
        menu_choices = "Wat do u want to do . \n 1. Add status. \n 2.Close Application  "
        result = int (raw_input(menu_choices))
        if(result == 1):
            pass
        elif(result == 2):
            show_menu = False
        else:
            print "wrong choice try again"

