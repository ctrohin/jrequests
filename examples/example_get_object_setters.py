import sys

sys.path.append(".")

from typing import Any, Optional
from jrequests import RequestBuilder, RequestMethod


class DeviceData:
    # Important to note that in order for the libary to instantiate, then set the values properly,
    # there needs to be a no argument constructor
    def __init__(self) -> None:
        self.__id: Optional[str] = None
        self.__name: Optional[str] = None
        self.__data: Optional[dict[Any, Any]] = None

    def setId(self, id: str) -> None:
        self.__id = id

    def getId(self) -> Optional[str]:
        return self.__id

    def setName(self, name: str) -> None:
        self.__name = name

    def getName(self) -> Optional[str]:
        return self.__name

    def setData(self, data: dict[Any, Any]) -> None:
        self.__data = data

    def getData(self) -> Optional[dict[Any, Any]]:
        return self.__data


def main() -> None:
    response = (
        RequestBuilder(RequestMethod.GET, "https://api.restful-api.dev/objects/1")
        .withRetries(3)
        .withHeaders({"Content-Type": "application/json"})
        .execute()
        .getObject(DeviceData)
    )
    print(f"Device ID: {response.getId()}")
    print(f"Device Name: {response.getName()}")
    print(f"Device Data: {response.getData()}")


if __name__ == "__main__":
    main()
