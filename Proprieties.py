class Description:
    def __init__(self, desc: str) -> None:
        self.__setDescription__(desc)

    def __getDescription__(self) -> str:
        return self.__description
    
    def __setDescription__(self, desc: str) -> None:
        self.__description = desc

    def deleteDescription(self) -> None:
        self.__setDescription(None)

    def showDescription(self) -> None:
        print(self.__getDescription())


class Tag:
    def __init__(self, tag: str) -> None:
        self.__setTag__(tag)

    def __setTag__(self, tag: str) -> None:
        self.__tag = tag

    def __getTag__(self) -> str:
        return self.__tag

    def deleteTag(self) -> None:
        self.__setTag(None)

    def showTag(self) -> None:
        print(self.__getTag())


class History:
    def __init__(self, hist: list) -> None:
        self.__setHistory__(hist)

    def __getHistory__(self) -> list:
        return self.__hist
    
    def __setHistory__(self, value: list) -> None:
        self.__hist = value

    def __getFromHistory__(self, index: int) -> str:
        return self.__hist[index]

    def getLastAlteration(self) -> str:
        return self.__hist[-1]
    
    def addAlteration(self, value: str) -> None:
        aux = self.__getHistory__()
        aux.append(value)
        self.__setHistory__(aux)