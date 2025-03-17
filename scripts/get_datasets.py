"""
conda create -n xcdat-data dask xarray netcdf4 ipykernel
"""

# %%
import xarray as xr


def process_dataset(
    path, start_date=None, end_date=None, chunking=None, subset_slice=None
):
    try:
        print(f"Attempting to open dataset: {path}")

        # Open the dataset with optional chunking
        ds = xr.open_dataset(path, chunks=chunking)

        # Subset the dataset for the specified time range or slice
        if start_date and end_date:
            ds_sub = ds.sel(time=slice(start_date, end_date))
        elif subset_slice:
            ds_sub = ds.isel(time=subset_slice)
        else:
            ds_sub = ds

        # Define the output file name
        output_file = path.split("/")[-1].replace(".nc", "_subset.nc")

        # Save the (subset) dataset to a netCDF file
        ds_sub.to_netcdf(output_file)
        print(f"Saved dataset to {output_file}")

        # Print the size of the dataset
        dataset_size = ds_sub.nbytes / (1024**2)  # Convert bytes to megabytes
        print(f"Size of the dataset: {dataset_size:.2f} MB")

        return True
    except ValueError as e:
        print(f"Failed to process {path}: {e}")
        return False


def process_datasets(
    dataset_paths, start_date=None, end_date=None, chunking=None, subset_slice=None
):
    successes = []
    failures = []
    for path in dataset_paths:
        if process_dataset(path, start_date, end_date, chunking, subset_slice):
            successes.append(path)
        else:
            failures.append(path)
    return successes, failures


# %%
# Regular datasets
# ----------------
dataset_paths = [
    "https://esgf-data1.llnl.gov/thredds/dodsC/css03_data/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r10i1p1f1/Amon/tas/gn/v20200605/tas_Amon_ACCESS-ESM1-5_historical_r10i1p1f1_gn_185001-201412.nc",
    "https://esgf-data1.llnl.gov/thredds/dodsC/css03_data/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r10i1p1f1/Amon/pr/gn/v20200605/pr_Amon_ACCESS-ESM1-5_historical_r10i1p1f1_gn_185001-201412.nc",
    "http://aims3.llnl.gov/thredds/dodsC/css03_data/CMIP6/CMIP/CCCma/CanESM5/historical/r13i1p1f1/Amon/tas/gn/v20190429/tas_Amon_CanESM5_historical_r13i1p1f1_gn_185001-201412.nc",
]

start_date = "1870-01-01"
end_date = "1874-12-31"

successes, failures = process_datasets(dataset_paths, start_date, end_date)

print("Successful datasets:")
for dataset in successes:
    print(dataset)

print("Failed datasets:")
for dataset in failures:
    print(dataset)

# %%
# E3SM datasets
# ----------------

e3sm_dataset_paths = [
    "https://esgf-data2.llnl.gov/thredds/dodsC/user_pub_work/CMIP6/CMIP/E3SM-Project/E3SM-2-0/historical/r1i1p1f1/Amon/ta/gr/v20220830/ta_Amon_E3SM-2-0_historical_r1i1p1f1_gr_185001-189912.nc",
    "https://esgf-data2.llnl.gov/thredds/dodsC/user_pub_work/CMIP6/CMIP/E3SM-Project/E3SM-2-0/historical/r1i1p1f1/Amon/cl/gr/v20220830/cl_Amon_E3SM-2-0_historical_r1i1p1f1_gr_185001-189912.nc",
]

successes, failures = process_datasets(
    e3sm_dataset_paths, chunking={"time": 20}, subset_slice=slice(0, 3)
)

print("Successful datasets:")
for dataset in successes:
    print(dataset)

print("Failed datasets:")
for dataset in failures:
    print(dataset)

# Local datasets (too big to use OpenDAP)
# ----------------------------------------
local_dataset_paths = [
    "so_Omon_CESM2_historical_r1i1p1f1_gn_185001-201412.nc",
    "thetao_Omon_CESM2_historical_r1i1p1f1_gn_185001-201412.nc",
]

successes, failures = process_datasets(
    local_dataset_paths, chunking={"time": 20}, subset_slice=slice(0, 3)
)

print("Successful datasets:")
for dataset in successes:
    print(dataset)

print("Failed datasets:")
for dataset in failures:
    print(dataset)

# %%
tas_daily = xr.open_dataset(
    "tas_3hr_ACCESS-ESM1-5_historical_r10i1p1f1_gn_201001010300-201501010000.nc"
)
tas_daily_sub = tas_daily.sel(lat=slice(15, 45), lon=slice(15, 45))
tas_daily_sub.to_netcdf(
    "tas_3hr_ACCESS-ESM1-5_historical_r10i1p1f1_gn_201001010300-201501010000_subset.nc"
)

# %%
