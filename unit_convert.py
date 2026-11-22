#!/usr/bin/env python3
"""unit-convert: convert values between units from the terminal.

Zero dependencies, standard library only.

Usage:
    python3 unit_convert.py <value> <from-unit> <to-unit>
    python3 unit_convert.py --list

Examples:
    python3 unit_convert.py 5 km mi
    python3 unit_convert.py 100 C F
    python3 unit_convert.py 2 GiB MB
    python3 unit_convert.py --list
"""

import sys

LENGTH = {
    "mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0,
    "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.344,
}
WEIGHT = {
    "mg": 0.001, "g": 1.0, "kg": 1000.0, "t": 1_000_000.0,
    "oz": 28.349523125, "lb": 453.59237,
}
VOLUME = {
    "ml": 0.001, "l": 1.0, "m3": 1000.0,
    "tsp": 0.00492892159375, "tbsp": 0.01478676478125,
    "cup": 0.2365882365, "pt": 0.473176473, "qt": 0.946352946,
    "gal": 3.785411784,
}
DATA = {
    "B": 1, "KB": 1000, "MB": 1000 ** 2, "GB": 1000 ** 3, "TB": 1000 ** 4,
    "KiB": 1024, "MiB": 1024 ** 2, "GiB": 1024 ** 3, "TiB": 1024 ** 4,
}
TEMPERATURE = {"C", "F", "K"}

CATEGORIES = {
    "length": LENGTH,
    "weight": WEIGHT,
    "volume": VOLUME,
    "data": DATA,
}


def convert_linear(value, src, dst, table):
    return value * table[src] / table[dst]


def convert_temperature(value, src, dst):
    if src == "C":
        celsius = value
    elif src == "F":
        celsius = (value - 32) * 5 / 9
    else:  # K
        celsius = value - 273.15
    if dst == "C":
        return celsius
    if dst == "F":
        return celsius * 9 / 5 + 32
    return celsius + 273.15


def find_category(src, dst):
    for name, table in CATEGORIES.items():
        if src in table and dst in table:
            return name, table
    return None, None


def list_units():
    for name, table in CATEGORIES.items():
        print(f"{name}: {', '.join(sorted(table))}")
    print(f"temperature: {', '.join(sorted(TEMPERATURE))}")


def main(argv):
    if len(argv) == 2 and argv[1] in ("--list", "-l"):
        list_units()
        return 0
    if len(argv) != 4:
        print(__doc__.strip().splitlines()[0])
        print("Usage: unit_convert.py <value> <from-unit> <to-unit>")
        print("       unit_convert.py --list")
        return 2
    try:
        value = float(argv[1])
    except ValueError:
        print(f"error: not a number: {argv[1]}")
        return 2
    src, dst = argv[2], argv[3]
    if src in TEMPERATURE or dst in TEMPERATURE:
        if src not in TEMPERATURE or dst not in TEMPERATURE:
            print(f"error: cannot convert {src} to {dst} (different categories)")
            return 2
        result = convert_temperature(value, src, dst)
    else:
        name, table = find_category(src, dst)
        if table is None:
            print(f"error: unknown or mismatched units: {src} -> {dst}")
            print("Run with --list to see supported units.")
            return 2
        result = convert_linear(value, src, dst, table)
    print(f"{value:g} {src} = {result:g} {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
