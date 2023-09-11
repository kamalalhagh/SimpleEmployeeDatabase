from modules import read_database, header, add_person
from modules import edit_person, delete_person, show_all, save, sleep, create_db


def main():
    database = read_database()
    while True:
        options = ("Add person", "Edit person", "Delete person", "Show all(tmp)", "Save to db", "Exit(tmp will "
                                                                                                "delete)",
                   "Delete database and create new one")
        header(options)
        menu = input("menu: ")
        if menu == "1":
            add_person(database)
        elif menu == "2":
            edit_person(database)
        elif menu == "3":
            delete_person(database)
        elif menu == "4":
            show_all(database)
        elif menu == "5":
            save(database)
        elif menu == "6":
            break
        elif menu == "7":
            ans = input("Are you sure you want to delete every things?(YES): ")
            if ans == "YES":
                create_db()
        else:
            print("Invalid input!")
            print("this option is disable in menu!")
            print(f"Please enter valid range between 1 and {len(options)}")
            print("You will redirect to main menu in 3 seconds ...")
            sleep(3)
            continue


if __name__ == '__main__':
    main()
