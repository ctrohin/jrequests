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

    def set_id(self, id: str) -> None:
        self.__id = id

    def get_id(self) -> Optional[str]:
        return self.__id

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> Optional[str]:
        return self.__name

    def set_data(self, data: dict[Any, Any]) -> None:
        self.__data = data

    def get_data(self) -> Optional[dict[Any, Any]]:
        return self.__data


def main() -> None:
    response = (
        RequestBuilder(RequestMethod.GET, "https://api.restful-api.dev/objects")
        .withRetries(3)
        .withHeaders({"Content-Type": "application/json"})
        .execute()
        .getList(DeviceData)
    )
    for elem in response:
        print(f"Device ID: {elem.get_id()}")
        print(f"Device Name: {elem.get_name()}")
        print(f"Device Data: {elem.get_data()}")
        print("=========")


if __name__ == "__main__":
    main()
