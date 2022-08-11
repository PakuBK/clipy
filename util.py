def convert_time(time: str) -> float:
    factors = (1, 60, 3600)
    time = [float(part) for part in time.split(":")]
    return sum(mult * part for mult, part in zip(factors, reversed(time)))