from dbHelper import DBHelper


def main():
    db = DBHelper()
    while True:
        print("***********WELCOME********")
        print()
        print("PRESS 1 to insert new user")
        print("PRESS 2 to display all users")
        print("PRESS 3 to display a single user")
        print("PRESS 4 to delete user")
        print("PRESS 5 to update user")
        print("PRESS 6 to exit program")
        print()
        try:
            choice = int(input())
            if (choice == 1):
                #insert user
                uid = int(input("Enter user id: "))
                username = input("Enter user name :")
                userphone = input("Enter user phone: ")
                db.insertDataToTable(uid, username, userphone)
            elif choice == 2:
                #display  user
                db.fetchAlldata()
            elif choice == 3:
                #fetch single user
                userid = int(
                    input("enter user id to which you want to display"))
                db.fetchUser(userid)
            elif choice == 4:
                #delete user
                userid = int(
                    input("enter user id to which you want to delete"))
                db.deleteUser(userid)
            elif choice == 5:
                #update user
                uid = int(input("enter id of user : "))
                username = input("new name :")
                userphone = input("new phone: ")
                db.updateUser(uid, username, userphone)
            elif choice == 6:
                break
            else:
                print("Invalid input ! Try again")
        except Exception as e:
            print(e)
            print("Invalid Details ! Try again")


if __name__ == "__main__":
    main()
