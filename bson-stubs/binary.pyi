from typing import Any
from uuid import UUID

BINARY_SUBTYPE: int
FUNCTION_SUBTYPE: int
OLD_BINARY_SUBTYPE: int
OLD_UUID_SUBTYPE: int
UUID_SUBTYPE: int

class UuidRepresentation:
    UNSPECIFIED: int = ...
    STANDARD: Any = ...
    PYTHON_LEGACY: Any = ...
    JAVA_LEGACY: int = ...
    CSHARP_LEGACY: int = ...

STANDARD: Any
PYTHON_LEGACY: Any
JAVA_LEGACY: Any
CSHARP_LEGACY: Any
ALL_UUID_SUBTYPES: Any
ALL_UUID_REPRESENTATIONS: Any
UUID_REPRESENTATION_NAMES: Any
MD5_SUBTYPE: int
USER_DEFINED_SUBTYPE: int

class Binary(bytes):
    def __new__(cls: Any, data: bytes, subtype: int = ...) -> Binary: ...
    @classmethod
    def from_uuid(cls, uuid: Any, uuid_representation: Any = ...): ...
    def as_uuid(self, uuid_representation: Any = ...): ...
    @property
    def subtype(self) -> int: ...
    def __getnewargs__(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

class UUIDLegacy(Binary):
    def __new__(cls: Any, obj: UUID) -> UUIDLegacy: ...
    def __getnewargs__(self): ...
    @property
    def uuid(self) -> UUID: ...
