from shapely.geometry import box
from shapely.ops import transform
import pyproj

bbox = box(79.521819, 5.917694, 81.880695, 9.835058)

projected_bbox = transform(pyproj.Transformer.from_crs("EPSG:4326", "EPSG:3857").transform, bbox)

area = projected_bbox.area / 10**6 

if area > 1000:
    n = int(area / 1000) + 1
    print(n)

    lon_step = (bbox.bounds[2] - bbox.bounds[0]) / n
    lat_step = (bbox.bounds[3] - bbox.bounds[1]) / n

    area_list = []
    for i in range(n):
        minx = bbox.bounds[0] + i * lon_step
        miny = bbox.bounds[1] + i * lat_step
        maxx = minx + lon_step
        maxy = miny + lat_step
        area_list.append(box(minx, miny, maxx, maxy))

else:
    area_list = [area]
