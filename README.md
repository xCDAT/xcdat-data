# xcdat-data

This repository exists to hold resource and example datasets for [xcdat](https://xcdat.readthedocs.io/en/latest/getting-started-guide/overview.html) (e.g., as used in the documentation)
that would bloat the [main repository](https://github.com/xCDAT/xcdat) if included there.

## Available Example Datasets

| Key                 | Filename                                                                            | Description                                                  | Subset                      | Approx. Filesize |
| ------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------ | --------------------------- | ---------------- |
| `pr_amon_access`    | `pr_Amon_ACCESS-ESM1-5_historical_r10i1p1f1_gn_185001-201412_subset.nc`             | Monthly precipitation data from the ACCESS-ESM1-5 model.     | `1870-01-01 to 1874-12-31`  | 7 MB             |
| `tas_amon_access`   | `tas_Amon_ACCESS-ESM1-5_historical_r10i1p1f1_gn_185001-201412_subset.nc`            | Monthly near-surface air temperature from ACCESS-ESM1-5.     | `1870-01-01 to 1874-12-31`  | 7 MB             |
| `tas_3hr_access`    | `tas_3hr_ACCESS-ESM1-5_historical_r10i1p1f1_gn_201001010300-201501010000_subset.nc` | 3-hourly near-surface air temperature from ACCESS-ESM1-5.    | Lat and lon points (15, 45) | 25 MB            |
| `tas_amon_canesm5`  | `tas_Amon_CanESM5_historical_r13i1p1f1_gn_185001-201412_subset.nc`                  | Monthly near-surface air temperature from the CanESM5 model. | `1870-01-01 to 1874-12-31`  | 2.0 MB           |
| `so_omon_cesm2`     | `so_Omon_CESM2_historical_r1i1p1f1_gn_185001-201412_subset.nc`                      | Monthly ocean salinity data from the CESM2 model.            | First three time points     | 29 MB            |
| `thetao_omon_cesm2` | `thetao_Omon_CESM2_historical_r1i1p1f1_gn_185001-201412_subset.nc`                  | Monthly ocean potential temperature from the CESM2 model.    | First three time points     | 37 MB            |
| `cl_amon_e3sm2`     | `cl_Amon_E3SM-2-0_historical_r1i1p1f1_gr_185001-189912_subset.nc`                   | Monthly cloud fraction data from the E3SM-2-0 model.         | `1870-01-01 to 1874-12-31`  | 54 MB            |
| `ta_amon_e3sm2`     | `ta_Amon_E3SM-2-0_historical_r1i1p1f1_gr_185001-189912_subset.nc`                   | Monthly air temperature data from the E3SM-2-0 model.        | `1870-01-01 to 1874-12-31`  | 14 MB            |

## Available Resource Datasets

| Key         | Filename                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                         | Subset | Approx. Filesize |
| ----------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ---------------- |
| `navy_land` | `resources/navy_land.nc` | Navy land mask dataset. The `navy_land.nc` file is used as the high-resolution land-sea mask. This file is sourced from the PCMDI (Program for Climate Model Diagnosis and Intercomparison) Metrics Package. It is a fixed asset (not expected to change) and is available at: [https://github.com/PCMDI/pcmdi_metrics/blob/main/share/data/navy_land.nc](https://github.com/PCMDI/pcmdi_metrics/blob/main/share/data/navy_land.nc) | Global | 8.97 MB          |
| `kerchunk_list` | `resources/kerchunk_list.json` | Kerchunk catalog of CMIP6 dataset references for remote-data demonstrations. | N/A | 50 MB |
| `ecsdata` | `resources/ecsdata.json` | Equilibrium climate sensitivity (ECS) metadata for CMIP6 models. | 53 models | 2 KB |

## CWSS 2026 Remote Kerchunk Demo

`resources/kerchunk_list.json` is a ~50 MB snapshot of Kerchunk metadata used by
xCDAT's [CWSS companion notebook](https://github.com/xCDAT/xcdat/blob/main/docs/demos/26-09-24-cwss-seminar/riotai_example_remote.ipynb).
It is stored in xcdat-data rather than xcdat to avoid bloating the xCDAT source
repository. The catalog identifies remote CMIP6 Kerchunk reference JSON files for
the demo's historical monthly `tas` analysis. See the [companion Google Slides
presentation](https://docs.google.com/presentation/d/1eDkwAIJC_peYnRnLnicplOPiR1eqiDZj2Sgwfrkvvrg/edit?slide=id.g3fa9c64b4de_0_73#slide=id.g3fa9c64b4de_0_73).

Consumers should access this file through a pinned xcdat-data release tag or
commit SHA, not an unpinned branch URL.

`resources/ecsdata.json` supplies the companion ECS metadata for the xCDAT CWSS
remote-Kerchunk demo. Its values are Gregory-regression ECS estimates from the
CMIP6 `abrupt-4xCO2` and `piControl` simulations, calculated using the [PCMDI
Metrics Package ECS implementation](https://github.com/PCMDI/pcmdi_metrics/blob/main/pcmdi_metrics/cloud_feedback/lib/compute_ECS_xr.py).
The JSON schema is `{model_name: ecs_value}`, where each model name is a string
and each ECS value is a numeric value in K.

## Usage

To access these datasets, simply import the tutorial `open_dataset()` function
and specify the key of the file to open.

```python
from xcdat.tutorial import open_dataset

# Specify the key
ds = open_dataset("pr_amon_access")
```
