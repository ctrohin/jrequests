import sys

sys.path.append(".")

from typing import Any, Optional
from jrequests import RequestBuilder, RequestMethod


class DeviceData:
    # Important to note that in order for the libary to instantiate, then set the values properly,
    # there needs to be a no argument constructor
    def __init__(self) -> None:
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.data: Optional[dict[Any, Any]] = None


def main() -> None:
    response = (
        RequestBuilder(RequestMethod.GET, "https://api.restful-api.dev/objects/1")
        .withRetries(3)
        .withHeaders({"Content-Type": "application/json"})
        .execute()
        .getObject(DeviceData)
    )
    print(f"Device ID: {response.id}")
    print(f"Device Name: {response.name}")
    print(f"Device Data: {response.data}")


if __name__ == "__main__":
    main()
