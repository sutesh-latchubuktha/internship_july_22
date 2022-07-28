class Solution:
    def defangIPaddr(self, address: str) -> str:
        numbers = address.split(".")
        result = "[.]".join(numbers)
        return result