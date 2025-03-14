# %%
from typing import List
import xarray as xr

dataset_paths = [
    "https://esgf-data1.llnl.gov/thredds/dodsC/css03_data/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r10i1p1f1/Amon/tas/gn/v20200605/tas_Amon_ACCESS-ESM1-5_historical_r10i1p1f1_gn_185001-201412.nc",
    "https://esgf-data1.llnl.gov/thredds/dodsC/css03_data/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r10i1p1f1/Amon/pr/gn/v20200605/pr_Amon_ACCESS-ESM1-5_historical_r10i1p1f1_gn_185001-201412.nc",
    # The below data is too big (~1.17 GB).
    # "https://esgf-data1.llnl.gov/thredds/dodsC/css03_data/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r10i1p1f1/3hr/tas/gn/v20200605/tas_3hr_ACCESS-ESM1-5_historical_r10i1p1f1_gn_201001010300-201501010000.nc",
    "http://aims3.llnl.gov/thredds/dodsC/css03_data/CMIP6/CMIP/CCCma/CanESM5/historical/r13i1p1f1/Amon/tas/gn/v20190429/tas_Amon_CanESM5_historical_r13i1p1f1_gn_185001-201412.nc",
    "http://aims3.llnl.gov/thredds/dodsC/css03_data/CMIP6/CMIP/NCAR/CESM2/historical/r1i1p1f1/Omon/so/gn/v20190308/so_Omon_CESM2_historical_r1i1p1f1_gn_185001-201412.nc",
    "http://aims3.llnl.gov/thredds/dodsC/css03_data/CMIP6/CMIP/NCAR/CESM2/historical/r1i1p1f1/Omon/thetao/gn/v20190308/thetao_Omon_CESM2_historical_r1i1p1f1_gn_185001-201412.nc",
]

grid_paths = [
    "https://esgf-data2.llnl.gov/thredds/dodsC/user_pub_work/E3SM/1_0/amip_1850_aeroF/1deg_atm_60-30km_ocean/atmos/180x360/time-series/mon/ens2/v3/TS_187001_189412.nc",
    "https://esgf-data2.llnl.gov/thredds/dodsC/user_pub_work/E3SM/1_0/amip_1850_aeroF/1deg_atm_60-30km_ocean/atmos/180x360/time-series/mon/ens2/v3/TS_189501_191912.nc",
    # The below dataset is too big (~362 MB)
    # "http://aims3.llnl.gov/thredds/dodsC/css03_data/CMIP6/CMIP/NOAA-GFDL/GFDL-CM4/abrupt-4xCO2/r1i1p1f1/day/tas/gr2/v20180701/tas_day_GFDL-CM4_abrupt-4xCO2_r1i1p1f1_gr2_00010101-00201231.nc",
]

# %%


def process_datasets(
    paths, subset=False, start_date="1870-01-01", end_date="1879-12-31"
) -> List[str]:
    failures = []

    for path in paths:
        try:
            print(f"Attempting to open dataset: {path}")

            # Open the dataset
            ds = xr.open_dataset(path, decode_cf=False)

            if subset:
                # Subset the dataset for the specified time range (assuming the time coordinate is named 'time')
                ds = ds.sel(time=slice(start_date, end_date))

            # Define the output file name
            output_file = path.split("/")[-1].replace(
                ".nc", "_subset.nc" if subset else "_subset.nc"
            )

            # Save the (subset) dataset to a netCDF file
            ds.to_netcdf(output_file)

            print(f"Saved {'subset ' if subset else ''}dataset to {output_file}")
        except ValueError as e:
            print(f"Failed to process {path}: {e}")
            failures.append(path)

    return failures


# Example usage
failed_datasets = process_datasets(dataset_paths, subset=True)
failed_grids = process_datasets(grid_paths, subset=False)

# %%
print("Failed datasets:")
for dataset in failed_datasets:
    print(dataset)

print("\nFailed grids:")
for grid in failed_grids:
    print(grid)
# %%
