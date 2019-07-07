import pandas as pd
from os.path import join
import sys

path="raw"
tag="oa"
run="L1C"
partition="test2016"

def load(path,run,partition,tag):
    csv_file = join(path,"run_{run}_{partition}-tag-{tag}.csv".format(run=run, partition=partition, tag=tag))
    return pd.read_csv(csv_file)

rolling_window = int(sys.argv[1])
outfile = "train_rw{}.csv".format(sys.argv[1])

collection = list()
for tag in ["oa", "xe"]:
    for run, partition in [
        ("clouds01","test2016clouds01"),
        ("clouds10","test2016clouds10"),
        ("clouds25","test2016clouds25"),
        ("clouds50","test2016clouds50"),
        ("clouds80","test2016"),
        ("cloudsall","test2016clouds01"),
        ("cloudsall","test2016clouds10"),
        ("cloudsall","test2016clouds25"),
        ("cloudsall","test2016clouds50"),
        ("cloudsall","test2016"),
        ]:
        #for partition in ["test2016","test2016L2A"]:
        #print run + partition
        df = load(path,run,partition,tag)
        df = df.set_index("Step")
        df = df[~df.index.duplicated(keep='last')] # drop duplicated indices https://stackoverflow.com/questions/13035764/remove-rows-with-duplicate-indices-pandas-dataframe-and-timeseries/34297689#34297689
        df = df["Value"]
        df.name = run + "_" + partition + "_" + tag
        collection.append(df)

table = pd.concat(collection,axis=1)

# average first and second folds
#table["L1C_test2016_mean"] = table[["L1C_test2016_oa","L1Cf2_test2016"]].sum(axis=1,skipna=False).divide(2)
#table["L1C_test2016L2A_mean"] = table[["L1C_test2016L2A","L1Cf2_test2016L2A"]].sum(axis=1,skipna=False).divide(2)

#table["L2A_test2016_mean"] = table[["L2A_test2016","L2Af2_test2016"]].sum(axis=1,skipna=False).divide(2)
#table["L2A_test2016L2A_mean"] = table[["L2A_test2016L2A","L2Af2_test2016L2A"]].sum(axis=1,skipna=False).divide(2)

table = table.rolling(rolling_window).mean()
table.to_csv(outfile)

print("columns: " + str(table.columns))
