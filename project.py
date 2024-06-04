from designs import get_header, clr_screen, delay, greet
from getpass import getpass
from typing import Union
import hashlib
import csv
import menu


def start_page() -> bool:
    while True:
        clr_screen()
        get_header()
        exists: str = input("Do you have an account (yes/no)? ").strip().lower()
        if exists in ["yes", "y"]:
            choice = "y"
            break

        elif exists in ["no", "n"]:
            choice = "n"
            break
        else:
            print("Invalid!")
            delay(2)
            continue
    if choice == "y":
        return True
    else:
        return False


def sign_up() -> bool:
    clr_screen()
    get_header()
    while True:
        print("Sign up:")
        account_type: str = (
            input(
                "Enter account type [Sect (M)aster, (V)ice-Sect Master, Sect-(P)rotector, (D)isciple]: "
            )
            .strip()
            .upper()
        )

        if not account_type in ["M", "V", "P", "D"]:
            print("Invalid! Enter M, V, P or D")
            delay(2)
            clr_screen()
            get_header()
            continue
        if account_type == "M":
            permission = "M"
            break
        if account_type == "V":
            permission = "V"
            break
        if account_type == "P":
            permission = "P"
            break
        if account_type == "D":
            permission = "D"
            break
    user_name: str = input("Username: ").strip()
    password: str = hashlib.sha256(getpass().encode()).hexdigest()
    account = {"user_name": user_name, "password": password, "permission": permission}
    with open("accounts.csv", "a") as file:
        writer = csv.DictWriter(
            file, fieldnames=["user_name", "password", "permission"]
        )
        writer.writerow(account)
    print("Account created successfully!")
    delay(2)
    return True


def login() -> Union[str, None]:
    clr_screen()
    get_header()
    print("Login:")
    user_name: str = input("Username: ").strip()
    password: str = hashlib.sha256(getpass().encode()).hexdigest()
    with open("accounts.csv") as file:
        reader = csv.DictReader(file)
        accounts: list = []
        for row in reader:
            accounts.append(
                {
                    "user_name": row["user_name"],
                    "password": row["password"],
                    "permission": row["permission"],
                }
            )
    exists = False
    for dict in accounts:
        if dict.get("user_name") == user_name and dict.get("password") == password:
            print("Logged in!")
            delay(2)
            exists = True
            permission: str = dict.get("permission")
            break
        else:
            exists = False
    return permission if exists else None


def acc_exists() -> bool:
    with open("accounts.csv") as file:
        reader = csv.DictReader(file)
        try:
            next(reader)
        except StopIteration:
            return False
    return True


def main():
    clr_screen()
    greet()
    if not acc_exists():
        print("No account registered")
        delay(2)
        sign_up()

    if start_page():
        permission: Union[str, None] = login()
    else:
        sign_up()
        permission = login()
    menu.options_available(permission)


if __name__ == "__main__":
    main()

