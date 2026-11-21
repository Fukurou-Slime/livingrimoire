import re

from LivinGrimoirePacket.RailPunk import PopulatorFunc, RailPunk


class IfXThenY(PopulatorFunc):
    # "if x then y" -> key x, value y
    example = "if hi then hello"

    def __init__(self):
        super().__init__()
        self.pattern = re.compile(r"^if (?P<x>.+?) then (?P<y>.+)$", re.IGNORECASE)

    def populate(self, railbot: RailPunk, str1: str) -> bool:
        match = self.pattern.match(str1.strip())
        if match is None:
            return False
        railbot.learn_key_value(match.group("x"), match.group("y"))
        return True


class IfISayXThenSayYSosu(PopulatorFunc):
    # "if i say x then say y" -> key x, value "y sosu"
    example = "if i say hi then say hello"

    def __init__(self):
        super().__init__()
        self.pattern = re.compile(r"^if i say (?P<x>.+?) then say (?P<y>.+)$", re.IGNORECASE)

    def populate(self, railbot: RailPunk, str1: str) -> bool:
        match = self.pattern.match(str1.strip())
        if match is None:
            return False
        railbot.learn_key_value(match.group("x"), f"{match.group('y')} sosu")
        return True