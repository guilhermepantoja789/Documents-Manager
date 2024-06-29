from Document import Document

class Group:
    def __init__(self, groupName: str, groupColor: str, dataName: list, dataPriority: list) -> None:
        self.__setGroupName__(groupName)
        self.__setGroupColor__(groupColor)
        self.__setDataName__(dataName)
        self.__setDataPriority__(dataPriority)
    
    def __setGroupName__(self, name: str) -> None:
        self.__groupName = name
    
    def __getGroupName__(self) -> str:
        return self.__groupName
    
    def __setGroupColor__(self, color: str) -> None:
        self.__groupColor = color

    def __getGroupColor__(self) -> str:
        return self.__groupColor
    
    def __setDataName__(self, data: list) -> None:
        self.__dataName = data
    
    def __getDataName__(self) -> list:
        return self.__dataName
    
    def __setDataPriority__(self, data: list) -> None:
        self.__dataPriority = data

    def __getDataPriority__(self) -> list:
        return self.__dataPriority
    
    def getGroupLen(self) -> int:
        return len(self.__getDataName__())
    
    def addNameToList(self, doc: Document) -> None:
        self.__setNameInData__(doc.getName(), self.getGroupLen() + 1)
    
    def addPriorityToList(self, doc: Document) -> None:
        self.__setPriorityInData__(doc.getPriority(), self.getGroupLen() + 1)

    def orderByAlpha(self) -> None:
        aux = []
        for x in self.__getDataName__():
            aux.append(x.lower())
        print(sorted(aux))

    def orderByPriority(self) -> None:
        print(sorted(self.__getDataPriority__()))

    

