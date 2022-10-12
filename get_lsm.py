import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels-monthly-means',
    {
        'product_type': 'monthly_averaged_reanalysis',
        'variable': 'land_sea_mask',
        'year': '1979',
        'month': '01',
        'time': '00:00',
        'area': [
            65, -180, -65,
            180,
        ],
        'format': 'netcdf',
    },
    'lsm.nc')