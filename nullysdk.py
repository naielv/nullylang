"""SDK providing 'NullY' functions"""


class Console:
    """Class for controlling the Console"""

    def __init__(self):
        self.colors = {"HEADER": '\033[95m',
                       "OKBLUE": '\033[94m',
                       "OKCYAN": '\033[96m',
                       "OKGREEN": '\033[92m',
                       "WARNING": '\033[93m',
                       "FAIL": '\033[91m',
                       "ENDC": '\033[0m',
                       "DEFAULT": '\033[0m',
                       "BOLD": '\033[1m',
                       "UNDERLINE": '\033[4m'}
        return

    def write_line(self, text: str, start: str = "", end: str = "\n", color: str = "DEFAULT"):
        """Writes a line to the console"""
        print(self.colors[color] + start + text +
              end + self.colors["ENDC"], end="")

    def read_line(self, prompt: str, start: str = "", end: str = "\n> ", color: str = "DEFAULT"):
        """Reads a line from the console"""
        return input(self.colors[color] + start + prompt + self.colors["ENDC"] + end)


class Program:
    """Class for making a CLI Program"""

    def __init__(self):
        """Program Init"""
        self.console = Console()

    def main(self, args: list):
        """-- PLEASE CHANGE THE MAIN SECTION ON YOUR CODE OR ADD A DOCSTRING --"""
        self.console.write_line(
            "This program does not have a 'main' function.")
        self.console.write_line("Args: " + str(args), color="OKBLUE")
