import datetime
from typing import Any, Optional, Union

class ObjectId:
    def __init__(self, oid: Optional[Union[str, ObjectId, bytes]] = ...) -> None: ...
    @classmethod
    def from_datetime(cls: Any, generation_time: datetime.datetime) -> ObjectId: ...
    @classmethod
    def is_valid(cls: Any, oid: Any) -> bool: ...
    @property
    def binary(self) -> bytes: ...
    @property
    def generation_time(self) -> datetime.datetime: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...
