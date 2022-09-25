#!/usr/bin/env python
# coding: utf-8

# In[1]:


import geopandas as gpd
import rioxarray as rxr
from rasterstats import zonal_stats


# In[2]:


gdf = gpd.read_file("BRA_RF_Municipal/BRA_RF_Municipal.shp")


# In[3]:


zs_list = zonal_stats("BRA_RF_Municipal/BRA_RF_Municipal.shp", "ECMWF_001.nc", stats=['mean'])
meanList = []
for value in zs_list:
    meanList.append(value['mean'])


# In[4]:


gdf['ecmfw_mean'] = meanList
gdf.to_csv('ECMWF_001_mean_BRA_RF_Municipal.csv')

