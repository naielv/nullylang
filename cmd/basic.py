"""Program Group 001: 'Basic'"""

class HelpProgram(globals()["NullY"].Program):
    """Test App"""
    def main(self, args: list):
        """MAIN"""
        self.console.write_line("=== HelpMan ===", color="HEADER")
        if len(args) > 1:
            self.console.write_line("Program: " + args[1], color="OKBLUE")
        else:
            self.console.write_line("¡No se ha especificado un programa!", color="FAIL")

if globals()["y_program"] == "help":
    test = HelpProgram()
    test.main(globals()["y_args"])
