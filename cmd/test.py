"""Test NullY Program, run with:
    from test import TestProgram
    test = TestProgram()
    test.main()"""

class TestProgram(globals()["NullY"].Program):
    """Test App"""
    def main(self, args: list):
        """MAIN"""
        self.console.write_line("=== Test ===", color="HEADER")
        self.console.write_line("Args: " + str(args), color="OKBLUE")
        self.console.write_line(
            self.console.read_line("Entra texto y se devolvera"))


if globals()["y_program"] == "test":
    test = TestProgram()
    test.main(globals()["y_args"])
