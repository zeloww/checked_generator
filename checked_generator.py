import string
from os import system
from requests import get
from random import choice, SystemRandom

checked_generator = """
                             ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
                            ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
                            ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██║  ██║
                            ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██║  ██║
                            ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██████╔╝
                             ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝\n
                    ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
                   ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
                   ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
                   ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
                   ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
                    ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                    1 > unchecked generator                 by Zelow#9999
                                                     2 > checked generator
"""

yes = ["y", "yes"]
no = ["n", "no"]
infinity = ["infinity", "inf", "i"]


def gencode():
    return letters_add.join(
        SystemRandom().choice(letters) for i in range(int(number_of_characters))
    )

def unchecked():
    letters = ""
    letters_add = ""
    base_code = ""

    lower_case = input("Do you want lowercase letters? [y/n]: ")

    if lower_case.lower() in yes:
        letters += string.ascii_lowercase

    else:
        if not lower_case.lower() in no:
            print("Error, Lowers Letters is now off!")

    upper_case = input("Do you want uppercase letters? [y/n]: ")

    if upper_case.lower() in yes:
        letters += string.ascii_uppercase

    else:
        if not upper_case.lower() in no:
            print("Error, Uppers Letters is now off!")

    digits = input("Do you want numbers? [y/n]: ")

    if digits.lower() in yes:
        letters += string.digits

    else:
        if not digits.lower() in no:
            print("Error, Numeros is now off!")

    punctuation = input("Do you want punctuation numbers? [y/n]: ")

    if punctuation.lower() in yes:
        letters += string.punctuation

    else:
        if not punctuation.lower() in no:
            print("Error, Specials Symboles is now off!")

    whitespace = input("Do you want whitespaces? [y/n]: ")

    if whitespace.lower() in yes:
        letters += string.whitespace

    else:
        if not whitespace.lower() in no:
            print("Error, Whitespace is now off!")

    if letters == "":
        print("Please enter a positive answer!\nLowers and Uppers letters are now on!")
        letters += string.ascii_lowercase + string.ascii.uppercase

    base = input("Do you want a base of character? [y/n]: ")

    if base.lower() in yes:
        base_code = input("enter the base of characters for your codes >>> ")

    elif base.lower() not in no:
        print("Error, base code is now off!")

    number_of_characters_error = True

    while number_of_characters_error:
        number_of_characters = input("How much character do you want?: ")
        try:
            number_of_characters = int(number_of_characters)
            number_of_characters_error = False
        except:
            number_of_characters_error = True

    code_number = input("How much unchecked code do you want?: ")

    if code_number in infinity:
        code_number = float("inf")

    elif code_number.isnumeric():
        code_number = int(code_number)

    else:
        print("Error, enter a valid number!")
        exit()

    with open("uncheckedcodes.txt", "a+") as UncheckedCodes:

        print("\nUnchecked Code Generation... Check your file uncheckedcodes.txt ;)")

        i = 1
        while i <= code_number:
            i = i + 1
            UncheckedCodes.write(base_code + gencode() + "\n")
            
        print(f"Ended. {i-1} unchecked codes generated!")

    input()

def checked():
    file_directory = input("enter the file directory >>> ")
    base = input("enter base url >>> ").lower()
    proxy = input("do you have proxies? >>> ").lower()

    with open(file_directory, "r") as file:
        unchecked_codes = file.readlines()

    if proxy in yes:
        with open("proxies_list", "r") as file:
            proxy_file = file.readlines()

    headers = {
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }

    for url in unchecked_codes:
        if proxy in yes:
            proxy = choice(proxies_file)

            proxies = {
            "http": "http://" + proxy,
            "https": "http://" + proxy
            }

            response = get(base + url, headers=headers, proxies=proxies)

        else:
            response = get(base + url, headers=headers)

        if response.ok:
            print("\033[32m[+] {} | {}\033[0m".format(response.status_code, url), end="")

        else:
            print("\033[31m[-] {} | {}\033[0m".format(response.status_code, url), end="")

    input("\033[34m\n[+] Finish {} checked codes !\033[0m".format(len(unchecked_codes)))

def main():

    while True:
        system("cls")
        system("color 3")
        print(checked_generator)

        choice = int(input(">>> "))

        if choice == 1:
            unchecked()

        elif choice == 2:
            checked()

        else:
            exit("bye :D")

if __name__ == "__main__":
    main()
