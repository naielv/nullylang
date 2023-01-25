"""NullOS Kernel, not needed for SDK"""
from programs import progs
# TODO: Make the kernel
# NEEDS TO WORK WITH MICROPYTHON
# Needed funcs
# [x] Shell
# [ ] Console
# [ ] Input
# [ ] GUI


def shell():
    "Shell for the kernel"
    FLAG_STOP = 0
    while FLAG_STOP == 0:

        args = input("$ ").split(" ")
        if args[0] in ["stop", "exit", "shutdown", "halt", "logout"]:
            FLAG_STOP = 1
        elif args[0] == "":
            pass
        else:
            run(" ".join(args))


def run(key: str):
    """run a program in 'programs.json'"""
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
    if key in progs:
        with open(progs[key], "r") as file:
            exec(file.read())
    else:
        print(colors["FAIL"] + key +
              " is not installed or linked!" + colors["ENDC"])


if __name__ == "__main__":
    shell()
