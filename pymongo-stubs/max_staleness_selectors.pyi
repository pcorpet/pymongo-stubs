from pymongo.server_selectors import Selection

IDLE_WRITE_PERIOD: int
SMALLEST_MAX_STALENESS: int

def select(max_staleness: int, selection: Selection) -> Selection: ...
