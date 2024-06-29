from Proprieties import Tag
from Proprieties import Description
from Proprieties import History
import json

class Document(History):
    def __init__(self, name: str, priority: int, tag: Tag, description: Description, history: list) -> None:
        self.setName(name)
        self.setPriority(priority)
        self.setTag(tag.__getTag__())
        self.setDescription(description.__getDescription__())
        super().__init__(history)

    def __init__(self, path: str) -> None:
        with open(path) as file:
            dataDict = json.load(file)
        name = dataDict["name"]
        priority = dataDict["priority"]
        tag = Tag(dataDict["tag"])
        description = Description(dataDict["description"])
        history = dataDict["history"]
        self.setName(name)
        self.setPriority(priority)
        self.setTag(tag.__getTag__())
        self.setDescription(description.__getDescription__())
        super().__init__(history)

    def getName(self) -> str:
        return self.__name
    
    def setName(self, name: str) -> None:
        self.__name = name
    
    def getPriority(self) -> int:
        return self.__priority
    
    def setPriority(self, priority: int) -> None:
        self.__priority = priority

    def getTag(self) -> Tag:
        return self.__tag
    
    def setTag(self, tag: Tag) -> None:
        self.__tag = tag

    def getDescription(self) -> str:
        return self.__description
    
    def setDescription(self, description: str) -> None:
        self.__description = description

    def getHistory(self) -> list:
        return self.__history
    
    def setHistory(self, history: list):
        self.__history = history
    
    def delete() -> None:
        pass
    def create() -> None:
        pass
    def update() -> None:
        pass

    def view(self) -> None:
        print("Nome do Documento: " + self.getName())
        print("Prioridade do Documento: " + str(self.getPriority()))
        print("Tag do Documento: " + self.getTag())
        print("Detalhes do Documento: " + self.getDescription())
        print("Ultima Alteracao do Documento: " + self.getLastAlteration())



    def send() -> None:
        pass
    def recieve() -> None:
        pass
    def scan() -> None:
        pass