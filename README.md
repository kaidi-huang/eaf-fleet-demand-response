# Cast-Break-Free Demand Response of Electric Arc Furnace Fleets: Supplementary Material

This repository accompanies the paper

> "Cast-Break-Free Demand Response of Electric Arc Furnace Fleets: Exact
> Counting Polytopes and Certified Rolling Dispatch"

It holds the Supplementary Material of the paper, with the proofs of its
theorems, and a script that checks the example of the Supplementary
Material.

## Layout

```
supplementary.pdf        Supplementary Material of the paper
scripts/
    gpoly_example.py     check of the example in Section III
LICENSE                  CC BY 4.0
```

## Supplementary Material

`supplementary.pdf` gives

- the rows of the counting polytope for the live state and the end of the
  horizon,
- the proofs of Theorems 1 to 4 of the paper, and
- an example showing that the block loads of a plant need not form a
  generalized polymatroid (Theorem 1(ii)).

## Example check

`scripts/gpoly_example.py` enumerates the schedules of the example plant in
Section III, prints the load vectors of the first three blocks, and lists the
vertices and edges of their convex hull. Its output contains the edge from
(2, 2, 1) to (3, 1, 2), of direction (1, -1, 1). It requires NumPy and SciPy:

```
python scripts/gpoly_example.py
```

## Citation

K. Huang, "Cast-break-free demand response of electric arc furnace fleets:
Supplementary material," 2026. [Online]. Available:
https://github.com/kaidi-huang/eaf-fleet-demand-response

## License

The contents of this repository are licensed under the Creative Commons
Attribution 4.0 International License (CC BY 4.0). See `LICENSE`.
