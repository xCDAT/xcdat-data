"""
conda create -n xcdat-data dask xarray netcdf4 ipykernel
"""

# %%
import xarray as xr

dataset_paths = [
    "https://esgf-data1.llnl.gov/thredds/dodsC/css03_data/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r10i1p1f1/Amon/tas/gn/v20200605/tas_Amon_ACCESS-ESM1-5_historical_r10i1p1f1_gn_185001-201412.nc",
    "https://esgf-data1.llnl.gov/thredds/dodsC/css03_data/CMIP6/CMIP/CSIRO/ACCESS-ESM1-5/historical/r10i1p1f1/Amon/pr/gn/v20200605/pr_Amon_ACCESS-ESM1-5_historical_r10i1p1f1_gn_185001-201412.nc",
    "http://aims3.llnl.gov/thredds/dodsC/css03_data/CMIP6/CMIP/CCCma/CanESM5/historical/r13i1p1f1/Amon/tas/gn/v20190429/tas_Amon_CanESM5_historical_r13i1p1f1_gn_185001-201412.nc",
]

start_date = "1870-01-01"
end_date = "1874-12-31"

successes = []
failures = []
for path in dataset_paths:
    try:
        print(f"Attempting to open dataset: {path}")

        # Open the dataset
        ds = xr.open_dataset(path)

        # Subset the dataset for the specified time range (assuming the time coordinate is named 'time')
        ds_sub = ds.sel(time=slice(start_date, end_date))

        # Define the output file name
        output_file = path.split("/")[-1].replace(".nc", "_subset.nc")

        # Save the (subset) dataset to a netCDF file
        ds_sub.to_netcdf(output_file)
        print(f"Saved dataset to {output_file}")

        # Print the size of the dataset
        dataset_size = ds_sub.nbytes / (1024**2)  # Convert bytes to megabytes
        print(f"Size of the dataset: {dataset_size:.2f} MB")

        successes.append(path)
    except ValueError as e:
        print(f"Failed to process {path}: {e}")
        failures.append(path)
# %%
print("Successful datasets:")
for dataset in successes:
    print(dataset)

# %%
print("Failed datasets:")
for dataset in failures:
    print(dataset)

# %%
# Big datasets
# ----------------
# The below file is 17.3 GB -- it is downloaded manually via http and subsetted locally: https://aims3.llnl.gov/thredds/fileServer/css03_data/CMIP6/CMIP/NCAR/CESM2/historical/r1i1p1f1/Omon/so/gn/v20190308/so_Omon_CESM2_historical_r1i1p1f1_gn_185001-201412.nc
# "http://aims3.llnl.gov/thredds/dodsC/css03_data/CMIP6/CMIP/NCAR/CESM2/historical/r1i1p1f1/Omon/so/gn/v20190308/so_Omon_CESM2_historical_r1i1p1f1_gn_185001-201412.nc"
# https://aims3.llnl.gov/thredds/fileServer/css03_data/CMIP6/CMIP/NCAR/CESM2/historical/r1i1p1f1/Omon/thetao/gn/v20190308/thetao_Omon_CESM2_historical_r1i1p1f1_gn_185001-201412.nc

local_dataset_paths = [
    "so_Omon_CESM2_historical_r1i1p1f1_gn_185001-201412.nc",
    "thetao_Omon_CESM2_historical_r1i1p1f1_gn_185001-201412.nc",
]
# %%
for path in local_dataset_paths:
    try:
        print(f"Attempting to open big dataset: {path}")

        # Open the big dataset with chunking
        ds_big = xr.open_dataset(path, chunks={"time": 20})

        # Subset the dataset for the first 3 time slices
        ds_sub = ds_big.isel(time=slice(0, 3))

        # Define the output file name
        output_file = path.split("/")[-1].replace(".nc", "_subset.nc")

        # Save the subset dataset to a netCDF file
        ds_sub.to_netcdf(output_file)
        print(f"Saved big dataset to {output_file}")

        # Print the size of the subset dataset
        dataset_size = ds_sub.nbytes / (1024**2)  # Convert bytes to megabytes
        print(f"Size of the subset dataset: {dataset_size:.2f} MB")

        successes.append(path)
    except ValueError as e:
        print(f"Failed to process {path}: {e}")
        failures.append(path)

# %%
