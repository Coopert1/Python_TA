def to_minutes(hours: int) -> int:
    return hours * 60


def to_hours(minutes: int) -> float:
    return round(minutes / 60, 4)


def is_whole_div(a: int, b: int) -> bool:
    return a % b == 0