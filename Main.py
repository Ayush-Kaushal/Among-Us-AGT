from os import system, name
import Task1
import Task2
import Task3


def clear_screen():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def main_menu():
    clear_screen()
    print()
    print("*"*80)
    print("WELCOME TO THE AMONG US")
    print("*"*80)
    print()
    print("Choices : ")
    print("1 : Possible Imposters")
    print("2 : Shortest Path between two Rooms")
    print("3 : Hamiltonian Path")
    print("4 : Exit")
    print()


def valid_input(choice_set):
    while True:
        choice_ = input("Enter Choice : ")
        if choice_ not in choice_set:
            print("INVALID CHOICE!")
        else:
            break
    return choice_


if __name__ == "__main__":

    choice = -1
    clear_screen()

    while True:
        if choice == -1:
            main_menu()
            choice = valid_input({"1", "2", "3", "4"})
        clear_screen()
        if choice == "1":
            Task1.run_task1()
        elif choice == "2":
            Task2.run_task2()
        elif choice == "3":
            Task3.run_task3()
        else:
            exit()

        print()
        print("Choices: ")
        print("1: Main Menu")
        print("2: Continue")
        print("0: Exit")

        choice_inner = valid_input({"0", "1", "2"})

        if choice_inner == "0":
            exit()
        elif choice_inner == "1":
            choice = -1
