import project
from tabulate import tabulate
import disciples
import designs
import csv

valid_disciple_types = ["Outer", "Inner", "Core"]
valid_levels = [
    "Qi refinement",
    "Body refinement",
    "Foundation establishment",
    "Core formation",
    "Nascent soul",
    "Soul transformation",
    "Mahayana",
    "Tribulation",
]
valid_professions = [
    "Alchemist",
    "Weapon master",
    "Blacksmith",
    "Formation master",
    "Array master",
    "Tailsman master",
    "Pure combat",
    "Warrior",
]
valid_departments = [
    "Alchemy",
    "Weapons",
    "Array",
    "Tailsman",
    "Combat",
]

permission = ""


def options_available(acc_type) -> None:
    global permission
    if acc_type == None:
        print("Invalid username or password!")
        designs.delay(2)
        options_available(project.login())
    else:
        permission = acc_type
    options = [
        "Info on Cultivation Levels",
        "Info on Professions",
        "Add New Disciple",
        "Read Data of Disciples",
        "Update Data of Disciples",
        "Delete Data of Disciples",
        "Log out",
    ]
    designs.clr_screen()
    designs.get_header()
    print("Options Available:")
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")
    print(f"{i+2}. Exit")
    try:
        choice: int = get_choices()
    except ValueError:
        print("Please enter a number.")
        designs.delay(2)
        options_available(permission)
    else:
        match choice:
            case 1:
                designs.clr_screen()
                designs.get_header()
                get_cultivation_levels()
            case 2:
                designs.clr_screen()
                designs.get_header()
                get_professions()
            case 3:
                designs.clr_screen()
                designs.get_header()
                add_disciples()
            case 4:
                designs.clr_screen()
                designs.get_header()
                read_disciples()
            case 5:
                designs.clr_screen()
                designs.get_header()
                edit_disciples()
            case 6:
                designs.clr_screen()
                designs.get_header()
                delete_disciples()
            case 7:
                designs.clr_screen()
                designs.get_header()
                options_available(project.login())
            case 8:
                designs.clr_screen()
                print("Exiting...")
                designs.delay(2)
                designs.clr_screen()
                exit()
            case _:
                print("Please choose from 1-8")
                designs.delay(2)
                designs.clr_screen()
                options_available(permission)


def go_back_to_levels() -> None:
    global permission
    back: str = input("\nEnter (B)ack to go back: ").strip().upper()
    if back == "B":
        get_cultivation_levels()
    else:
        print("Invalid. Going back to Main menu.")
        designs.delay(2)
        options_available(permission)


def level_info(levels, choice) -> None:
    print(f"{levels[choice-1]['level']}:\n{levels[choice-1]['description']}")


def get_cultivation_levels() -> None:
    designs.clr_screen()
    designs.get_header()
    levels: list = []
    with open("levels.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            levels.append(row)
    print("Cultivation Levels:")
    for i in range(len(levels)):
        print(f"{i+1}. {levels[i]['level']}")
    print(f"{i+2}. Main Menu")
    print(f"{i+3}. Exit")
    try:
        choice: int = get_choices()
    except ValueError:
        print("Please enter a number.")
        designs.delay(2)
        get_cultivation_levels()
    else:
        match choice:
            case 1:
                designs.clr_screen()
                designs.get_header()
                level_info(levels, choice)
                go_back_to_levels()

            case 2:
                designs.clr_screen()
                designs.get_header()
                level_info(levels, choice)
                go_back_to_levels()

            case 3:
                designs.clr_screen()
                designs.get_header()
                level_info(levels, choice)
                go_back_to_levels()

            case 4:
                designs.clr_screen()
                designs.get_header()
                level_info(levels, choice)
                go_back_to_levels()

            case 5:
                designs.clr_screen()
                designs.get_header()
                level_info(levels, choice)
                go_back_to_levels()

            case 6:
                designs.clr_screen()
                designs.get_header()
                level_info(levels, choice)
                go_back_to_levels()

            case 7:
                designs.clr_screen()
                designs.get_header()
                level_info(levels, choice)
                go_back_to_levels()

            case 8:
                designs.clr_screen()
                designs.get_header()
                options_available(permission)
            case 9:
                designs.clr_screen()
                print("Exiting...")
                designs.delay(2)
                designs.clr_screen()
                exit()
            case _:
                print("Please choose from 1-9")
                designs.delay(2)
                designs.clr_screen()
                get_cultivation_levels()


def go_back_to_professions() -> None:
    global permission
    back: str = input("\nEnter (B)ack to go back: ").strip().upper()
    if back == "B":
        get_professions()
    else:
        print("Invalid. Going back to Main menu.")
        designs.delay(2)
        options_available(permission)


def profession_info(professions, choice) -> None:
    print(
        f"{professions[choice-1]['profession']}:\n{professions[choice-1]['description']}"
    )


def get_professions() -> None:
    designs.clr_screen()
    designs.get_header()
    global permission
    professions: list = []
    with open("professions.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            professions.append(row)
    print("Cultivation Professions:")
    for i in range(len(professions)):
        print(f"{i+1}. {professions[i]['profession']}")
    print(f"{i+2}. Main Menu")
    print(f"{i+3}. Exit")
    try:
        choice: int = get_choices()
    except ValueError:
        print("Please enter a number.")
        designs.delay(2)
        get_professions()
    else:
        match choice:
            case 1:
                designs.clr_screen()
                designs.get_header()
                profession_info(professions, choice)
                go_back_to_professions()

            case 2:
                designs.clr_screen()
                designs.get_header()
                profession_info(professions, choice)
                go_back_to_professions()

            case 3:
                designs.clr_screen()
                designs.get_header()
                profession_info(professions, choice)
                go_back_to_professions()

            case 4:
                designs.clr_screen()
                designs.get_header()
                profession_info(professions, choice)
                go_back_to_professions()

            case 5:
                designs.clr_screen()
                designs.get_header()
                profession_info(professions, choice)
                go_back_to_professions()
            case 6:
                designs.clr_screen()
                designs.get_header()
                options_available(permission)
            case 7:
                designs.clr_screen()
                print("Exiting...")
                designs.delay(2)
                designs.clr_screen()
                exit()
            case _:
                print("Please choose from 1-7")
                designs.delay(2)
                designs.clr_screen()
                get_professions()


def check_input(disciple_type, level, profession, department) -> bool:
    global valid_disciple_types, valid_levels, valid_professions, valid_departments
    if (
        not disciple_type in valid_disciple_types
        or not level in valid_levels
        or not profession in valid_professions
        or not department in valid_departments
    ):
        return False
    else:
        return True


def details_to_note() -> None:
    global valid_disciple_types, valid_levels, valid_professions, valid_departments
    print("DETAILS TO NOTE:")
    print("\nValid disciple types:")
    for types in valid_disciple_types:
        print(f"* {types} ", end="")
    print()
    print("\nValid cultivation levels:")
    for levels in valid_levels:
        print(f"* {levels}")
    print("\nValid professions:")
    for professions in valid_professions:
        print(f"* {professions}")
    print("\nValid departments:")
    for departments in valid_departments:
        print(f"* {departments} ", end="")
    print("\n")


def get_info() -> tuple:
    name: str = input("Name: ").strip().capitalize()
    disciple_type: str = (
        input("Type of Disciple (Outer/ Inner/ Core): ").strip().capitalize()
    )
    level: str = input("Cultivation Level: ").strip().capitalize()
    profession: str = input("Profession: ").strip().capitalize()
    department: str = input("Department: ").strip().capitalize()
    cultivation_law: str = (
        input("Cultivation Law (Five Elements, Special, etc): ").strip().capitalize()
    )
    return (name, disciple_type, level, profession, department, cultivation_law)


def add_disciples(tries=0) -> None:
    designs.clr_screen()
    designs.get_header()
    global permission
    if permission not in ["M", "V", "P"]:
        print("Access Denied!")
        designs.delay(2)
        options_available(permission)
    details_to_note()
    entry: tuple = get_info()
    valid: bool = check_input(entry[1], entry[2], entry[3], entry[4])
    if valid:
        while True:
            confirmation: str = input("Confirm (yes/no)? ").strip().lower()
            if confirmation in ["yes", "y"]:
                disciple = disciples.Disciples(*entry)
                disciple.add_data()
                break
            elif confirmation in ["no", "n"]:
                break
            else:
                print("Invalid")
                continue
        options_available(permission)
    else:
        while tries < 3:
            print("Invalid Data!")
            tries += 1
            designs.delay(1.5)
            if tries < 3:
                add_disciples(tries)
            else:
                print("Wrong entries too many times...")
                designs.delay(1)
                break
        options_available(permission)


def file_reader() -> list:
    with open("disciples.csv") as file:
        reader = csv.DictReader(file)
        table: list = []
        for row in reader:
            table.append(
                {
                    "Name": row["Name"],
                    "Disciple_type": row["Disciple_type"],
                    "Level": row["Level"],
                    "Profession": row["Profession"],
                    "Department": row["Department"],
                    "Cultivation_law": row["Cultivation_law"],
                }
            )
    return table


def read_disciples() -> None:
    designs.clr_screen()
    designs.get_header()
    global permission
    if permission not in ["M", "V", "P"]:
        print("Access Denied!")
        designs.delay(2)
        options_available(permission)
    try:
        table: list = file_reader()
    except FileNotFoundError:
        print(f"File not found: 'disciples.csv'")
        designs.delay(2)
        options_available(permission)

    else:
        if not table:
            print("There are no entries in the file!")
            designs.delay(2)
            options_available(permission)
        else:
            print(tabulate(table, headers="keys", tablefmt="grid"))
            input("Press Enter key to go back to Main menu...")
            options_available(permission)


def edit_disciples() -> None:
    designs.clr_screen()
    designs.get_header()
    global permission
    if permission not in ["M", "V"]:
        print("Access Denied!")
        designs.delay(2)
        options_available(permission)
    try:
        table: list = file_reader()
    except FileNotFoundError:
        print(f"File not found: 'disciples.csv'")
        designs.delay(2)
        options_available(permission)
    else:
        if is_empty():
            print("There are no entries in the file!")
            designs.delay(2)
            options_available(permission)
        else:
            print(tabulate(table, headers="keys", tablefmt="grid"))
            details_to_note()
            new_table: list = table
            while True:
                entry: tuple = get_info()
                valid: bool = check_input(entry[1], entry[2], entry[3], entry[4])
                if not valid:
                    print("Invalid!")
                    designs.delay(2)
                    options_available(permission)
                    break
                for dict in table:
                    if dict.get("Name") == entry[0] and valid:
                        dict["Name"] = entry[0]
                        dict["Disciple_type"] = entry[1]
                        dict["Level"] = entry[2]
                        dict["Profession"] = entry[3]
                        dict["Department"] = entry[4]
                        dict["Cultivation_law"] = entry[5]
                again = False
                while True:
                    more: str = input("Edit more entries (yes/no)? ").strip().lower()
                    if more not in ["yes", "y", "no", "n"]:
                        print("Invalid!")
                        continue
                    if more in ["yes", "y"]:
                        again = True
                        break
                    if more in ["no", "n"]:
                        again = False
                        break
                if again:
                    continue
                else:
                    break
        with open("disciples.csv", "w") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "Name",
                    "Disciple_type",
                    "Level",
                    "Profession",
                    "Department",
                    "Cultivation_law",
                ],
            )
            writer.writeheader()
            writer.writerows(new_table)
    print("Disciple data updated!")
    designs.delay(2)
    options_available(permission)


def is_empty() -> bool:
    with open("disciples.csv") as file:
        reader = csv.DictReader(file)
        try:
            next(reader)
        except StopIteration:
            return True
    return False


def delete_disciples() -> None:
    designs.clr_screen()
    designs.get_header()
    global permission
    if permission != "M":
        print("Access Denied!")
        designs.delay(2)
        options_available(permission)
    try:
        table: list = file_reader()
    except FileNotFoundError:
        print(f"File not found: 'disciples.csv'")
        designs.delay(2)
        options_available(permission)
    else:
        if is_empty():
            print("There are no entries in the file!")
            designs.delay(2)
            options_available(permission)
        else:
            print(tabulate(table, headers="keys", tablefmt="grid"))
            while True:
                entry: str = input("Name: ").strip().capitalize()
                new_table: list = []
                exists: bool = False
                deleted: bool = False
                for dict in table:
                    if dict.get("Name") == entry:
                        exists = True
                        while True:
                            confirm: str = input("Confirm (yes/no)? ").strip().lower()
                            if confirm in ["yes", "y"]:
                                deleted = True
                                print("Disciple details deleted!")
                                break
                            elif confirm in ["no", "n"]:
                                print("Disciple details not deleted!")
                                break
                            else:
                                print("Invalid!")
                    if not deleted or dict.get("Name") != entry:
                        new_table.append(dict)
                if exists == False:
                    print("Name doesn't exist!")
                table = new_table
                more = False
                while True:
                    if not table:
                        print("There are no entries in the file!")
                        designs.delay(2)
                        break
                    else:
                        again = input("Delete more entries (yes/no)? ").strip().lower()
                        if again in ["yes", "y"]:
                            more = True
                            break
                        if again in ["no", "n"]:
                            break
                        elif again not in ["yes", "y", "no", "n"]:
                            print("Invalid!")
                            continue
                if more:
                    continue
                else:
                    break

        with open("disciples.csv", "w") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "Name",
                    "Disciple_type",
                    "Level",
                    "Profession",
                    "Department",
                    "Cultivation_law",
                ],
            )
            writer.writeheader()
            writer.writerows(table)
    options_available(permission)


def get_choices() -> int:
    while True:
        try:
            choice: int = int(input("Choose: ").strip())
        except ValueError:
            raise
        except KeyboardInterrupt:
            designs.clr_screen()
            print("Exiting...")
            designs.delay(2)
            designs.clr_screen()
            exit()
        except EOFError:
            designs.clr_screen()
            print("Exiting...")
            designs.delay(2)
            designs.clr_screen()
            exit()
        else:
            return choice


def main() -> None:
    designs.clr_screen()
    designs.get_header()
    options_available(permission)


if __name__ == "__main__":
    main()

