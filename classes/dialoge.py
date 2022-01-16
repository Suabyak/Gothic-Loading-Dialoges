from classes.instance import Instance


class Dialoge:

    def __init__(self):
        self.__instances = dict()
        self.__load = {"instance": self.__load_instance,
                       "func": self.__load_func}

    def load(self, key_line: str, content: str):
        keyword = key_line.split(" ")[0].strip()
        self.__load[keyword.lower()](key_line, content)

    def __load_instance(self, key_line: str, content: str) -> None:
        name = key_line.split(" ")[1][:key_line.split(" ")[1].find("(")]
        instance = Instance()
        for line in content.split("\n")[1:-1]:
            splited_line = line.strip().split(" ")
            attribute = splited_line[0]
            value = splited_line[2:]
            for i in range(len(value)-1):
                value[0] += f" {value[i+1]}"
            value = value[0]
            instance.load(attribute, value)
        self.__instances[name] = instance

    def __load_func(self, *args):
        pass

    def __str__(self) -> str:
        string = ""
        for name, instance in self.__instances.items():
            string += f"INSTANCE {name}:\n"
            for attrib, value in instance.get_attributes().items():
                string += f"\t{attrib} = {value[:-1]}\n"
        return string+"\n"
