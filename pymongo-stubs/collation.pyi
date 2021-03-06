from typing import Any, Dict, Optional, Union

class CollationStrength:
    PRIMARY: int = ...
    SECONDARY: int = ...
    TERTIARY: int = ...
    QUATERNARY: int = ...
    IDENTICAL: int = ...

class CollationAlternate:
    NON_IGNORABLE: str = ...
    SHIFTED: str = ...

class CollationMaxVariable:
    PUNCT: str = ...
    SPACE: str = ...

class CollationCaseFirst:
    UPPER: str = ...
    LOWER: str = ...
    OFF: str = ...

class Collation:
    def __init__(
        self,
        locale: str,
        caseLevel: Optional[bool] = ...,
        caseFirst: Optional[str] = ...,
        strength: Optional[int] = ...,
        numericOrdering: Optional[bool] = ...,
        alternate: Optional[str] = ...,
        maxVariable: Optional[str] = ...,
        normalization: Optional[bool] = ...,
        backwards: Optional[bool] = ...,
        **kwargs: Any,
    ) -> None: ...
    @property
    def document(self) -> Dict[str, Any]: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

def validate_collation_or_none(value: Optional[Union[Dict[str, Any], Collation]]) -> Optional[Dict[str, Any]]: ...
