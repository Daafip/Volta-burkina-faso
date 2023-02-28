import rasterio
import matplotlib
import os
import matplotlib.pyplot as plt
import contextily as cx
from rasterio.plot import show as rioshow


# setting up some variables for nice plots
cmap = matplotlib.cm.get_cmap("tab10")


def get_background_map(name, bounds):  
    """
    Given a name of area and bounds saves a local map file from Esri.WorldImagery using Contexitly
    """
    if os.path.exists(f'{name}_wgs84.tif'):
        pass 
    else:
        # only import if needed
        from rasterio.warp import calculate_default_transform, reproject, Resampling

        # unpack the bounds into the wanted corners
        xmin, ymin, xmax, ymax = bounds

        # get the needed background map of the northsea with the bounds we found above and saves to given path
        _ = cx.bounds2raster(xmin, ymin, xmax, ymax,
                            ll=True,
                            path=f"{name}.tif",
                            source=cx.providers.Esri.WorldImagery 
                            )

        # defines the wanted crs: we use WGS84                    
        dst_crs = 'EPSG:4326'
        
        # the map is in RD coordinates, so we transform it here
        # also see https://rasterio.readthedocs.io/en/latest/topics/reproject.html 
        with rasterio.open(f'{name}.tif') as src:
            transform, width, height = calculate_default_transform(src.crs, dst_crs, src.width, src.height, *src.bounds)
            kwargs = src.meta.copy()
            # change the dictionary to what we want
            kwargs.update({
                'crs': dst_crs,
                'transform': transform,
                'width': width,
                'height': height
            })

            # output a new .tif immage in the correct transformation        
            with rasterio.open(f'{name}_wgs84.tif', 'w', **kwargs) as dst:
                # update the image with the projection we want 
                for i in range(1, src.count + 1):
                    reproject(
                        source=rasterio.band(src, i),
                        destination=rasterio.band(dst, i),
                        src_transform=src.transform,
                        src_crs=src.crs,
                        dst_transform=transform,
                        dst_crs=dst_crs,
                        resampling=Resampling.nearest)
    return f'{name}_wgs84.tif'




