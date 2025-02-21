import sys

sys.path.append(".")

from dataclasses import field, dataclass
from typing import Any, Optional
from jrequests import RequestBuilder, RequestMethod


@dataclass
class DeviceData:
    # Important to note that in order for the libary to instantiate, then set the values properly,
    # there needs to be a no argument constructor
    id: Optional[str] = field(init=False)
    name: Optional[str] = field(init=False)
    data: Optional[dict[Any, Any]] = field(init=False)


def main() -> None:
    response = (
        RequestBuilder(RequestMethod.GET, "https://api.restful-api.dev/objects")
        .withRetries(3)
        .withHeaders({"Content-Type": "application/json"})
        .execute()
        .getList(DeviceData)
    )
    for elem in response:
        print(f"Device ID: {elem.id}")
        print(f"Device Name: {elem.name}")
        print(f"Device Data: {elem.data}")
        print("=========")


if __name__ == "__main__":
    main()
