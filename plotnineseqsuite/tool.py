from typing import List


def extract(data: List[str], start: int = None, end: int = None) -> List[str]:
    complete_len = len(data[0])
    if start is None:
        start = 0
    if end is None:
        end = complete_len
    return list(map(lambda x: x[start:end], data))
