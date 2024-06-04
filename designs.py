from os import system
from time import sleep


def clr_screen():
    system("clear")


def delay(n):
    sleep(n)


def get_header():
    print("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\t\t~~~~~~~~~~         Cosmic Star Academy         ~~~~~~~~~~")
    print("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def greet():
    get_header()
    print("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\t\t~                                                       ~")
    print("\t\t~                                                       ~")
    print("\t\t~                                                       ~")
    print("\t\t~          Welcome to the Cosmic Star Academy           ~")
    print("\t\t~                  Management System                    ~")
    print("\t\t~                                                       ~")
    print("\t\t~                                                       ~")
    print("\t\t~                                                       ~")
    print("\t\t~                                                       ~")
    print("\t\t~                                                       ~")
    print("\t\t~                                                       ~")
    print("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    input("\t\tPress Enter key to continue...")


def main():
    greet()


if __name__ == "__main__":
    main()

