"""Test NullY Program, run with:
    test = TestProg()
    test.main()"""
import nullysdk as NullY


class TestProg(NullY.Program):
    """Test App"""
    def main(self, cliargs: list = None):
        """MAIN"""
        self.console.write_line("TEST TEST TEST")
        self.console.write_line(
            self.console.read_line("Entra texto y se devolvera"))


if __name__ == "__main__":
    test = TestProg()
    test.main()
