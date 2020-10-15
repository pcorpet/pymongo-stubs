import datetime
from typing import Any, Dict, Mapping, Optional, Sequence, Tuple

from pymongo.ismaster import IsMaster
from pymongo.server_description import ServerDescription

class _EventListener: ...

class CommandListener(_EventListener):
    def started(self, event: CommandStartedEvent) -> None: ...
    def succeeded(self, event: CommandSucceededEvent) -> None: ...
    def failed(self, event: CommandFailedEvent) -> None: ...

class ConnectionPoolListener(_EventListener):
    def pool_created(self, event: Any) -> None: ...
    def pool_cleared(self, event: Any) -> None: ...
    def pool_closed(self, event: Any) -> None: ...
    def connection_created(self, event: Any) -> None: ...
    def connection_ready(self, event: Any) -> None: ...
    def connection_closed(self, event: Any) -> None: ...
    def connection_check_out_started(self, event: Any) -> None: ...
    def connection_check_out_failed(self, event: Any) -> None: ...
    def connection_checked_out(self, event: Any) -> None: ...
    def connection_checked_in(self, event: Any) -> None: ...

class ServerHeartbeatListener(_EventListener):
    def started(self, event: ServerHeartbeatStartedEvent) -> None: ...
    def succeeded(self, event: ServerHeartbeatSucceededEvent) -> None: ...
    def failed(self, event: ServerHeartbeatFailedEvent) -> None: ...

class TopologyListener(_EventListener):
    def opened(self, event: _ServerEvent) -> None: ...
    def description_changed(self, event: _ServerEvent) -> None: ...
    def closed(self, event: _ServerEvent) -> None: ...

class ServerListener(_EventListener):
    def opened(self, event: _ServerEvent) -> None: ...
    def description_changed(self, event: _ServerEvent) -> None: ...
    def closed(self, event: _ServerEvent) -> None: ...

def register(listener: _EventListener) -> None: ...

class _CommandEvent:
    def __init__(self, command_name: str, request_id: int, connection_id: Tuple[str, int], operation_id: int) -> None: ...
    @property
    def command_name(self) -> str: ...
    @property
    def request_id(self) -> int: ...
    @property
    def connection_id(self) -> Tuple[str, int]: ...
    @property
    def operation_id(self) -> int: ...

class CommandStartedEvent(_CommandEvent):
    def __init__(self, command: Mapping[str, Any], database_name: str, *args: Any) -> None: ...
    @property
    def command(self) -> Dict[str, Any]: ...
    @property
    def database_name(self) -> str: ...

class CommandSucceededEvent(_CommandEvent):
    def __init__(
        self,
        duration: datetime.timedelta,
        reply: Mapping[str, Any],
        command_name: str,
        request_id: int,
        connection_id: Tuple[str, int],
        operation_id: int,
    ) -> None: ...
    @property
    def duration_micros(self) -> int: ...
    @property
    def reply(self) -> Dict[str, Any]: ...

class CommandFailedEvent(_CommandEvent):
    def __init__(self, duration: datetime.timedelta, failure: Mapping[str, Any], *args: Any) -> None: ...
    @property
    def duration_micros(self) -> int: ...
    @property
    def failure(self) -> Dict[str, Any]: ...

class _PoolEvent:
    def __init__(self, address: Any) -> None: ...
    @property
    def address(self): ...

class PoolCreatedEvent(_PoolEvent):
    def __init__(self, address: Any, options: Any) -> None: ...
    @property
    def options(self): ...

class PoolClearedEvent(_PoolEvent): ...
class PoolClosedEvent(_PoolEvent): ...

class ConnectionClosedReason:
    STALE: str = ...
    IDLE: str = ...
    ERROR: str = ...
    POOL_CLOSED: str = ...

class ConnectionCheckOutFailedReason:
    TIMEOUT: str = ...
    POOL_CLOSED: str = ...
    CONN_ERROR: str = ...

class _ConnectionEvent:
    def __init__(self, address: Any, connection_id: Any) -> None: ...
    @property
    def address(self): ...
    @property
    def connection_id(self): ...

class ConnectionCreatedEvent(_ConnectionEvent): ...
class ConnectionReadyEvent(_ConnectionEvent): ...

class ConnectionClosedEvent(_ConnectionEvent):
    def __init__(self, address: Any, connection_id: Any, reason: Any) -> None: ...
    @property
    def reason(self): ...

class ConnectionCheckOutStartedEvent:
    def __init__(self, address: Any) -> None: ...
    @property
    def address(self): ...

class ConnectionCheckOutFailedEvent:
    def __init__(self, address: Any, reason: Any) -> None: ...
    @property
    def address(self): ...
    @property
    def reason(self): ...

class ConnectionCheckedOutEvent(_ConnectionEvent): ...
class ConnectionCheckedInEvent(_ConnectionEvent): ...

class _ServerEvent:
    def __init__(self, server_address: Tuple[str, int], topology_id: int) -> None: ...
    @property
    def server_address(self) -> Tuple[str, int]: ...
    @property
    def topology_id(self) -> int: ...

class ServerDescriptionChangedEvent(_ServerEvent):
    def __init__(self, previous_description: ServerDescription, new_description: ServerDescription, *args: Any) -> None: ...
    @property
    def previous_description(self) -> ServerDescription: ...
    @property
    def new_description(self) -> ServerDescription: ...

class ServerOpeningEvent(_ServerEvent): ...
class ServerClosedEvent(_ServerEvent): ...

class TopologyEvent:
    def __init__(self, topology_id: int) -> None: ...
    @property
    def topology_id(self) -> int: ...

class TopologyDescriptionChangedEvent(TopologyEvent):
    def __init__(self, previous_description: ServerDescription, new_description: ServerDescription, *args: Any) -> None: ...
    @property
    def previous_description(self) -> ServerDescription: ...
    @property
    def new_description(self) -> ServerDescription: ...

class TopologyOpenedEvent(TopologyEvent): ...
class TopologyClosedEvent(TopologyEvent): ...

class _ServerHeartbeatEvent:
    def __init__(self, connection_id: Tuple[str, int]) -> None: ...
    @property
    def connection_id(self) -> Tuple[str, int]: ...

class ServerHeartbeatStartedEvent(_ServerHeartbeatEvent): ...

class ServerHeartbeatSucceededEvent(_ServerHeartbeatEvent):
    def __init__(self, duration: Any, reply: Any, connection_id: Any, awaited: bool = ...) -> None: ...
    @property
    def duration(self) -> int: ...
    @property
    def reply(self) -> IsMaster: ...
    @property
    def awaited(self): ...

class ServerHeartbeatFailedEvent(_ServerHeartbeatEvent):
    def __init__(self, duration: Any, reply: Any, connection_id: Any, awaited: bool = ...) -> None: ...
    @property
    def duration(self) -> int: ...
    @property
    def reply(self) -> Exception: ...
    @property
    def awaited(self): ...

class _EventListeners:
    def __init__(self, listeners: Sequence[_EventListener]) -> None: ...
    @property
    def enabled_for_commands(self) -> bool: ...
    @property
    def enabled_for_server(self) -> bool: ...
    @property
    def enabled_for_server_heartbeat(self) -> bool: ...
    @property
    def enabled_for_topology(self) -> bool: ...
    @property
    def enabled_for_cmap(self): ...
    def event_listeners(self) -> Tuple[Sequence[_EventListener]]: ...
    def publish_command_start(
        self,
        command: Mapping[str, Any],
        database_name: str,
        request_id: int,
        connection_id: Tuple[str, int],
        op_id: Optional[int] = ...,
    ) -> None: ...
    def publish_command_success(
        self,
        duration: datetime.timedelta,
        reply: Mapping[str, Any],
        command_name: str,
        request_id: int,
        connection_id: Tuple[str, int],
        op_id: Optional[int] = ...,
    ) -> None: ...
    def publish_command_failure(
        self,
        duration: datetime.timedelta,
        failure: Mapping[str, Any],
        command_name: str,
        request_id: int,
        connection_id: Tuple[str, int],
        op_id: Optional[int] = ...,
    ) -> None: ...
    def publish_server_heartbeat_started(self, connection_id: Tuple[str, int]) -> None: ...
    def publish_server_heartbeat_succeeded(self, connection_id: Any, duration: Any, reply: Any, awaited: Any) -> None: ...
    def publish_server_heartbeat_failed(self, connection_id: Any, duration: Any, reply: Any, awaited: Any) -> None: ...
    def publish_server_opened(self, server_address: Tuple[str, int], topology_id: int) -> None: ...
    def publish_server_closed(self, server_address: Tuple[str, int], topology_id: int) -> None: ...
    def publish_server_description_changed(
        self,
        previous_description: ServerDescription,
        new_description: ServerDescription,
        server_address: Tuple[str, int],
        topology_id: int,
    ) -> None: ...
    def publish_topology_opened(self, topology_id: int) -> None: ...
    def publish_topology_closed(self, topology_id: int) -> None: ...
    def publish_topology_description_changed(
        self, previous_description: ServerDescription, new_description: ServerDescription, topology_id: int
    ) -> None: ...
    def publish_pool_created(self, address: Any, options: Any) -> None: ...
    def publish_pool_cleared(self, address: Any) -> None: ...
    def publish_pool_closed(self, address: Any) -> None: ...
    def publish_connection_created(self, address: Any, connection_id: Any) -> None: ...
    def publish_connection_ready(self, address: Any, connection_id: Any) -> None: ...
    def publish_connection_closed(self, address: Any, connection_id: Any, reason: Any) -> None: ...
    def publish_connection_check_out_started(self, address: Any) -> None: ...
    def publish_connection_check_out_failed(self, address: Any, reason: Any) -> None: ...
    def publish_connection_checked_out(self, address: Any, connection_id: Any) -> None: ...
    def publish_connection_checked_in(self, address: Any, connection_id: Any) -> None: ...
