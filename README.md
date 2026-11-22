# unit-convert

Convert units from the terminal — length, weight, temperature, volume, and data size. Zero dependencies, standard library only.

## Usage

```bash
python3 unit_convert.py <value> <from-unit> <to-unit>
python3 unit_convert.py --list
```

## Examples

```bash
$ python3 unit_convert.py 5 km mi
5 km = 3.10686 mi

$ python3 unit_convert.py 100 C F
100 C = 212 F

$ python3 unit_convert.py 2 GiB MB
2 GiB = 2147.48 MB

$ python3 unit_convert.py 1 gal l
1 gal = 3.78541 l
```

## Supported units

- **length**: mm, cm, m, km, in, ft, yd, mi
- **weight**: mg, g, kg, t, oz, lb
- **volume**: ml, l, m3, tsp, tbsp, cup, pt, qt, gal
- **data**: B, KB, MB, GB, TB, KiB, MiB, GiB, TiB
- **temperature**: C, F, K

Mismatched categories (e.g. `km` to `kg`) are rejected with an error. Run with `--list` to see all supported units.
