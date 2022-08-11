import os


def convert_time(time: str) -> float:
    factors = (1, 60, 3600)
    time = [float(part) for part in time.split(":")]
    return sum(mult * part for mult, part in zip(factors, reversed(time)))


def check_and_create_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)