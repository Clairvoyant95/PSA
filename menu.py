# menu

def menu():

    while True:
        option = raw_input("Wybierz opcje: ")
        print "Wybrales opcje: " + option
        # START:
        if option == "1":
            print "funkcja jeden"
        # OPTIONS:
        elif option == "2":
            print "funkcja dwa"
        # END:
        elif option == "0":
            print "0"
            break
        else:
            print "Brak opcji!"
            print " "
    print "END"

    return 0
