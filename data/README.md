# The data aspect of this project can be split into different sections
- `Climate data`
   - a small amount of climate projections
- `Combining data`
    - takes all the other data into account and combines it into one model
- `discharge data volta`
    - reads the given discharge data provided by the client and combines it into one model
- `Evaporation`
    - Uses Thornwait form [pyeto](https://github.com/woodcrafty/PyETo) data to calculate the evaporation using mean temperature 
- `rainfall data volta`
    - analyses ichrip initially and then the precipitation data provided by the client.
- `Volta_ERA5_lat_lon` & `Volta_precip_latest` contain the data mentioned above respectively

#### all the spatial data is handled in hte Qgis files 

#### python:
`volta_enviroment.yml` contains all the packages needed and can be installed using [conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html), don't forget to follow the steps to get `pyeto` to work. 