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
