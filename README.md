# xcdat-data

This repository exists to hold example datasets for [xcdat](https://xcdat.readthedocs.io/en/latest/getting-started-guide/overview.html) (e.g., as used in the documentation)
that would bloat the [main repository](https://github.com/xCDAT/xcdat) if included there.

## Available Datasets

Here's your updated table with the new entries:

| Key                 | Filename                                                                            | Description                                                  | Subset                      | Approx. Filesize |
| ------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------ | --------------------------- | ---------------- |
| `pr_amon_access`    | `pr_Amon_ACCESS-ESM1-5_historical_r10i1p1f1_gn_185001-201412_subset.nc`             | Monthly precipitation data from the ACCESS-ESM1-5 model.     | `1870-01-01 to 1874-12-31`  | 7 MB             |
| `tas_amon_access`   | `tas_Amon_ACCESS-ESM1-5_historical_r10i1p1f1_gn_185001-201412_subset.nc`            | Monthly near-surface air temperature from ACCESS-ESM1-5.     | `1870-01-01 to 1874-12-31`  | 7 MB             |
| `tas_3hr_access`    | `tas_3hr_ACCESS-ESM1-5_historical_r10i1p1f1_gn_201001010300-201501010000_subset.nc` | 3-hourly near-surface air temperature from ACCESS-ESM1-5.    | First 10 lat and lon points | 6 MB             |
| `tas_amon_canesm5`  | `tas_Amon_CanESM5_historical_r13i1p1f1_gn_185001-201412_subset.nc`                  | Monthly near-surface air temperature from the CanESM5 model. | `1870-01-01 to 1874-12-31`  | 2.0 MB           |
| `so_omon_cesm2`     | `so_Omon_CESM2_historical_r1i1p1f1_gn_185001-201412_subset.nc`                      | Monthly ocean salinity data from the CESM2 model.            | First three time points     | 29 MB            |
| `thetao_omon_cesm2` | `thetao_Omon_CESM2_historical_r1i1p1f1_gn_185001-201412_subset.nc`                  | Monthly ocean potential temperature from the CESM2 model.    | First three time points     | 37 MB            |
| `cl_amon_e3sm2`     | `cl_Amon_E3SM-2-0_historical_r1i1p1f1_gr_185001-189912_subset.nc`                   | Monthly cloud fraction data from the E3SM-2-0 model.         | `1870-01-01 to 1874-12-31`  | 54 MB            |
| `ta_amon_e3sm2`     | `ta_Amon_E3SM-2-0_historical_r1i1p1f1_gr_185001-189912_subset.nc`                   | Monthly air temperature data from the E3SM-2-0 model.        | `1870-01-01 to 1874-12-31`  | 14 MB            |

## Usage

To access these datasets, simply import the tutorial `open_dataset()` function
and specify the key of the file to open.

```python
from xcdat.tutorial import open_dataset

# Specify the key
ds = open_dataset("pr_amon_access")
```
