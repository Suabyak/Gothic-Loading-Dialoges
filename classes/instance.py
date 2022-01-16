class Instance:
    def __init__(self):
        self.__attributes = dict()

    def load(self, attribute: str, value: any) -> None:
        self.__attributes[attribute] = value

    def __str__(self) -> str:
        string = ""
        for attribute, value in self.__attributes.items():
            string += f"{attribute} = {value}\n"
        return string+"\n"

    def get_attribute(self, attribute: str) -> any:
        return self.__attributes[attribute]

    def get_attributes(self) -> dict:
        return self.__attributes
