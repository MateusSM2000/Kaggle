from copy import deepcopy

import pandas as pd
ca_videos = pd.read_csv('../CAvideos.csv')
gb_videos = pd.read_csv('../GBvideos.csv')

print(ca_videos, '\n')
print(gb_videos, '\n' * 10)

ca_videos_2 = deepcopy(ca_videos)
ca_videos_2['country'] = 'Canada'
gb_videos_2 = deepcopy(gb_videos)
gb_videos_2['country'] = 'United Kingdom'
ca_gb_videos = pd.concat([ca_videos_2, gb_videos_2])
print(ca_gb_videos, '\n' * 10)


left = ca_videos.set_index(['title', 'trending_date'])
right = gb_videos.set_index(['title', 'trending_date'])
ca_gb_joined = left.join(right, lsuffix='_CA', rsuffix='_GB')
print(ca_gb_joined, '\n' * 10)