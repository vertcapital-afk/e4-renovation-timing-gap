# e4-renovation-timing-gap

Data and analysis scripts supporting **"When is waiting worth it? Renovation
passports, real options, and the investor-regulator timing gap in residential
building stocks"** (S. F. Tadeu; companion deterministic study under review at
*Energy & Buildings*, ENB-D-26-05336).

## Contents

- `opcoes_categoria.json` - 1,078 measure-level Monte Carlo
  valuations (612 base grid + 432 technology-cost scenarios + 34
  discount-rate robustness runs). Each entry: option value (EUR/m2), Monte
  Carlo standard error, between-seed dispersion, exercise probabilities.
- `opcoes_pacote.json` - 72 package-level valuations (24 base:
  8 archetypes x 3 climates; + 48 discount-rate robustness at 1%/5%,
  suffixes `|r1pct` / `|r5pct`).
- `parametros_calibracao.json` - complete stochastic calibration (OU/GBM
  price processes, electricity-gas correlation, technology-cost poles with
  IRENA extraction anchors, carbon and grid-emission-factor scenarios,
  discount rates, grid design).
- `reproduzir_tabelas.py` - regenerates every table of the paper
  directly from the JSON files (stdlib only).

## What is *not* here

The building-physics and valuation engine (e4/ILLIANCe3, Python) is hosted
in a private repository and is available from the author on reasonable
request. The ICESD 2020 microdata used to calibrate empirical occupancy are
statistically confidential (INE/DGEEC); only aggregated outputs are used.

## Licence

Data: CC BY 4.0. Scripts: MIT.

## Funding

PRR - Recovery and Resilience Plan, European Union Next Generation EU;
"Agenda ILLIANCE" project [C644919832-00000035 | Project No. 46].
