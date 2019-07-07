import pandas as pd

scl = pd.read_csv("scl.csv",index_col=0)

# hacky way to select only rows of 2016
scl = scl.loc[pd.to_datetime(scl.index).year == 2016]

scl["sum"] = scl.sum(axis=1)
scl["cloud"] = scl[["cloud cirrus","cloud high prob", "cloud low prob", "cloud med prob"]].sum(axis=1)
scl["cloudpercent"] = scl["cloud"] / scl["sum"] *100
scl.reset_index().to_csv("scl2.csv")


#for cl in [.5,.25,.1,.01]:
#    cld = [el for el in scl.loc[scl["cloud%"]<=cl].index]
#    outstr= "('"+ "', '".join(cld) + "')"
#
#    filename="observations_2016_lesseual_"+str(int(cl*100))+"clouds.txt"
#    print("writing: "+filename)
#    with open(filename,'w') as f:
#        f.write(outstr)


