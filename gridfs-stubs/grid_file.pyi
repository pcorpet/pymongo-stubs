from typing import Any, Optional

from pymongo.client_session import ClientSession
from pymongo.cursor import Cursor

EMPTY: bytes
NEWLN: bytes
DEFAULT_CHUNK_SIZE: Any

class GridIn:
    def __init__(
        self, root_collection: Any, session: Optional[ClientSession] = ..., disable_md5: bool = ..., **kwargs: Any
    ) -> None: ...
    def abort(self) -> None: ...
    @property
    def closed(self): ...
    filename: Any = ...
    name: Any = ...
    content_type: Any = ...
    length: Any = ...
    chunk_size: Any = ...
    upload_date: Any = ...
    md5: Any = ...
    def __getattr__(self, name: Any): ...
    def __setattr__(self, name: Any, value: Any) -> None: ...
    def close(self) -> None: ...
    def read(self, size: int = ...) -> None: ...
    def readable(self): ...
    def seekable(self): ...
    def write(self, data: Any) -> None: ...
    def writelines(self, sequence: Any) -> None: ...
    def writeable(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any): ...

class GridOut:
    def __init__(
        self,
        root_collection: Any,
        file_id: Optional[Any] = ...,
        file_document: Optional[Any] = ...,
        session: Optional[ClientSession] = ...,
    ) -> None: ...
    filename: Any = ...
    name: Any = ...
    content_type: Any = ...
    length: Any = ...
    chunk_size: Any = ...
    upload_date: Any = ...
    aliases: Any = ...
    metadata: Any = ...
    md5: Any = ...
    def __getattr__(self, name: Any): ...
    def readable(self): ...
    def readchunk(self): ...
    def read(self, size: int = ...): ...
    def readline(self, size: int = ...): ...
    def tell(self): ...
    def seek(self, pos: Any, whence: Any = ...) -> None: ...
    def seekable(self): ...
    def __iter__(self) -> Any: ...
    def close(self) -> None: ...
    def write(self, value: Any) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any): ...

class _GridOutChunkIterator:
    def __init__(self, grid_out: Any, chunks: Any, session: Optional[ClientSession], next_chunk: Any) -> None: ...
    def expected_chunk_length(self, chunk_n: Any): ...
    def __iter__(self) -> Any: ...
    def next(self): ...
    __next__: Any = ...
    def close(self) -> None: ...

class GridOutIterator:
    def __init__(self, grid_out: Any, chunks: Any, session: Optional[ClientSession]) -> None: ...
    def __iter__(self) -> Any: ...
    def next(self): ...
    __next__: Any = ...

class GridOutCursor(Cursor):
    def __init__(
        self,
        collection: Any,
        filter: Optional[Any] = ...,
        skip: int = ...,
        limit: int = ...,
        no_cursor_timeout: bool = ...,
        sort: Optional[Any] = ...,
        batch_size: int = ...,
        session: Optional[ClientSession] = ...,
    ) -> None: ...
    def next(self): ...
    __next__: Any = ...
    # TODO: error: Signature of "add_option" incompatible with supertype
    #  "Cursor"
    # Change pymongo to "mask: int"
    def add_option(self, *args: Any, **kwargs: Any) -> None: ...  # type: ignore
    def remove_option(self, *args: Any, **kwargs: Any) -> None: ...  # type: ignore