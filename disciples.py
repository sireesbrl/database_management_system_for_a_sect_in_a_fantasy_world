from os import path
import csv


class Disciples:
    def __init__(
        self,
        name: str,
        disciple_type: str,
        level: str,
        profession: str,
        department: str,
        cultivation_law: str,
    ) -> None:
        self._name = name
        self._disciple_type = disciple_type
        self._level = level
        self._profession = profession
        self._department = department
        self._cultivation_law = cultivation_law

    def add_data(self) -> None:
        row = {
            "Name": self._name,
            "Disciple_type": self._disciple_type,
            "Level": self._level,
            "Profession": self._profession,
            "Department": self._department,
            "Cultivation_law": self._cultivation_law,
        }
        if path.isfile("disciples.csv"):
            with open("disciples.csv", "a") as file:
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
                writer.writerow(row)
        else:
            with open("disciples.csv", "a") as file:
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
                writer.writerow(row)

