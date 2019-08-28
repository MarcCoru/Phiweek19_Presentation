import pandas as pd
import sys
f=sys.argv[1]

data = pd.read_csv(f)

# normalize
norm=1e-4
data["B1"] *= norm
data["B2"] *= norm
data["B3"] *= norm
data["B4"] *= norm
data["B5"] *= norm
data["B6"] *= norm
data["B7"] *= norm
data["B8"] *= norm
data["B9"] *= norm
data["B10"] *= norm
data["B11"] *= norm
data["B12"] *= norm
data["B8A"] *= norm

data["doa"] = pd.to_datetime(data['doa'], format='%Y-%m-%d')
data["t"] = data.doa.dt.dayofyear/365
data.to_csv("prep_"+f)

