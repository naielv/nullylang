"""NullOS Kernel"""
from programs import progs
import nullysdk as NullY
# TODO: Make the kernel
# NEEDS TO WORK WITH MICROPYTHON
# Needed funcs
# [x] Shell
# [ ] Console
# [ ] Input
# [ ] GUI


def shell():
    """Shell for the kernel"""
    flag_stop = 0
    while flag_stop == 0:

        args = input("$ ").split(" ")
        if args[0] in ["stop", "exit", "shutdown", "halt", "logout"]:
            flag_stop = 1
        elif args[0] == "":
            pass
        else:
            run(args)


def run(key: list):
    """Run a program in 'programs.json'"""
    colors = {
        "HEADER": '\033[95m',
        "OKBLUE": '\033[94m',
        "OKCYAN": '\033[96m',
        "OKGREEN": '\033[92m',
        "WARNING": '\033[93m',
        "FAIL": '\033[91m',
        "ENDC": '\033[0m',
        "DEFAULT": '\033[0m',
        "BOLD": '\033[1m',
        "UNDERLINE": '\033[4m'
    }
    if key[0] in progs:
        with open(progs[key[0]], "r") as file:
            exec(file.read(), {"y_args": key,
                 "y_program": key[0], "NullY": NullY})
    else:
        print(colors["FAIL"] + key[0] +
              " no está instalado, vinculado o escrito correctamente." + colors["ENDC"])


if __name__ == "__main__":
    shell()
