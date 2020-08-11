DOT = "."
COLON = ":"
DOUBLE_COLON = "::"
OCTET = 8


class ValidationTools:

    def decimal_to_binary(self, value):
        """
        """
        if type(value) == str:
            try:
                value = int(value)
            except ValueError:
                return None

        binary_value = bin(value).replace("0b", "")

        n = len(binary_value)
        padding = ""

        if n < OCTET:
            while n < OCTET:
                padding += "0"
                n += 1

        binary_value = padding + binary_value

        return binary_value

    def is_unicast(self, address):
        """
        """
        count = 0
        groupings = self.split_address(address)

        for group in groupings:
            if count == 0:
                if int(group) <= 0 or int(group) >= 224:
                    return False
            else:
                if int(group) < 0 or int(group) > 255:
                    return False
            count += 1

        return True

    def split_address(self, address):
        """
        """
        groupings = []

        if DOT in address:
            groupings = address.split(".")

            return groupings
