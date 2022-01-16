from classes.dialoge import Dialoge


class Read:
    def __init__(self, name: str):
        self.__name = name
        self.__dialoge = Dialoge()
        with open(f"Dialoge\\DIA_{name}.d", encoding="cp1250") as file:
            file_content = file.read().strip()
            pointer = 0
            while pointer != -1:
                key_line, pointer = self.read_key_line(file_content, pointer)
                content, pointer = self.read_content(file_content, pointer)
                if key_line == "":
                    break
                self.__dialoge.load(key_line, content)

    def read_key_line(self, string: str, start: int = 0) -> (str, int):
        index = string.find("{", start)
        key_line = string[start:index].strip()
        return (key_line, index)

    def read_content(self, string: str, start: int = 0) -> (str, int):
        content = string[start:start+1]
        start += 1
        if content == "":
            return ("", -1)
        while content.count("{") > content.count("};"):
            index = string.find("};", start)+2
            content += string[start:index]
            start = index
        return (content.strip(), index if index != 1 else -1)

    def __str__(self) -> str:
        string = f"dialoge of {self.__name}\n\n"
        string += str(self.__dialoge)
        return string


if __name__ == "__main__":
    print(Read("bau_903_bodo"))
