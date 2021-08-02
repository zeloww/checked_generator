import random, string, os

os.system("cls")
os.system("color 3")
print(
    """
                    ██╗   ██╗███╗   ██╗ ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
                    ██║   ██║████╗  ██║██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
                    ██║   ██║██╔██╗ ██║██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██║  ██║
                    ██║   ██║██║╚██╗██║██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██║  ██║
                    ╚██████╔╝██║ ╚████║╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██████╔╝
                     ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝\n
                    ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
                   ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
                   ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
                   ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
                   ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
                    ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                        by Zelow#9999
"""
)

yes = ["y", "yes", "Y", "YES", "Yes"]
no = ["n", "no", "N", "NO", "No"]
infinity = ["infinity", "inf", "i"]

restart = True


def gencode():
    return letters_add.join(
        random.SystemRandom().choice(letters) for i in range(int(number_of_characters))
    )


while restart:
    restart = False

    letters = ""
    letters_add = ""

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
        print("Please enter a positive answer!")

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

    with open("uncheckedcodes.txt", "w") as UncheckedCodes:

        print("\nUnchecked Code Generation... Check your file uncheckedcodes.txt ;)")

        i = 1
        while i <= code_number:
            i = i + 1
            UncheckedCodes.write(gencode() + "\n")

        UncheckedCodes.close()
        print(f"Ended. {i-1} unchecked codes generated!")

    while restart is False:
        do_you_restart = input("Do you want restart? [y/n]")

        if do_you_restart in yes:
            print("Restart...\n")
            restart = True

        elif do_you_restart in no:
            print("Ok, bye :p")
            exit()

        else:
            print("Error, I don't understand!")
