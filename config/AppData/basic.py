"""Program Group 001: 'Basic'"""


class HelpProgram(globals()["NullY"].Program):
    """HelpMan"""

    def main(self, args: list):
        """MAIN"""
        self.console.write_line("=== HelpMan ===", color="HEADER")
        if len(args) > 1:
            if args[1] in globals()["y_progs"]:
                if len(globals()["y_progs"].get(args[1])) == 2:
                    self.console.write_line(
                        "Program: " + args[1], color="OKBLUE")
                    self.console.write_line(
                        "= " + args[1] + " =", color="HEADER")
                    self.console.write_line(
                        globals()["y_progs"].get(args[1])[1])

                else:
                    self.console.write_line(
                        "¡El programa no tiene un mensaje de ayuda!", color="FAIL")
            else:
                self.console.write_line(
                    "¡El programa no existe!", color="FAIL")

        else:
            self.console.write_line(
                "¡No se ha especificado un programa!", color="FAIL")


class OSProgram(globals()["NullY"].Program):
    """OSMan"""

    def main(self, args: list):
        """MAIN"""
        self.console.write_line("=== OSMan ===", color="HEADER")
        self.console.write_line("Versión de NullOS: " + globals()["y_osver"], color="OKGREEN")

if globals()["y_program"] == "help":
    help = HelpProgram()
    help.main(globals()["y_args"])
if globals()["y_program"] == "os":
    os = OSProgram()
    os.main(globals()["y_args"])
