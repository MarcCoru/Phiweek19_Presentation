import os
import pandas as pd

ROLLING_MEAN_WINDOW=10
metric="oa"

files=[["/home/russwurm/projects/MTLCC/data/bavaria/models/2017_IJGI/multiyear/train/convlstm128_2016_2017_f0/train.csv",
"/home/russwurm/projects/MTLCC/data/bavaria/models/2017_IJGI/multiyear/train/convlstm128_2016_2017_f1/train.csv",
"/home/russwurm/projects/MTLCC/data/bavaria/models/2017_IJGI/multiyear/train/convlstm128_2016_2017_f2/train.csv"],
["/home/russwurm/projects/MTLCC/data/bavaria/models/2017_IJGI/multiyear/train/convlstm128_2016_f0/train.csv",
"/home/russwurm/projects/MTLCC/data/bavaria/models/2017_IJGI/multiyear/train/convlstm128_2016_f1/train.csv",
"/home/russwurm/projects/MTLCC/data/bavaria/models/2017_IJGI/multiyear/train/convlstm128_2016_f2/train.csv"],
["/home/russwurm/projects/MTLCC/data/bavaria/models/2017_IJGI/multiyear/train/convlstm128_2017_f0/train.csv",
"/home/russwurm/projects/MTLCC/data/bavaria/models/2017_IJGI/multiyear/train/convlstm128_2017_f1/train.csv",
"/home/russwurm/projects/MTLCC/data/bavaria/models/2017_IJGI/multiyear/train/convlstm128_2017_f2/train.csv"],
["/home/russwurm/projects/MTLCC/data/bavaria/models/2017_IJGI/multiyear/train/convlstm128_9x2016_1x2017_f0/train.csv",
"/home/russwurm/projects/MTLCC/data/bavaria/models/2017_IJGI/multiyear/train/convlstm128_9x2016_1x2017_f1/train.csv",
None],
["/home/russwurm/projects/MTLCC/data/bavaria/models/2017_IJGI/multiyear/train/convlstm128_first2016_later20162017_f0/train.csv",None, None],
["/home/russwurm/projects/MTLCC/data/bavaria/models/2017_IJGI/multiyear/train/convlstm128_first2016_later2017_f0/train.csv",None,None]]
#"/home/russwurm/projects/MTLCC/data/bavaria/models/dgx1/multiyear/train/convlstm128_9x2016_1x2017_f2/train.csv"]

for f1_csv,f2_csv,f3_csv in files:
    basename = f1_csv.split("/")[-2].replace("_f0","")
    print basename

    outfilename="{basename}_{year}_{partition}_{metric}.csv"

    f1 = pd.read_csv(f1_csv, header=[0, 1, 2],index_col=0)

    # 1 fold available
    if f2_csv is None:
        train = f1    
    # 2 folds available
    elif f3_csv is None:
        f2 = pd.read_csv(f2_csv, header=[0, 1, 2],index_col=0)
        tr_ = pd.concat((f1, f2))
        gr = tr_.groupby(tr_.index)
        train = gr.mean() 
    # 3 fold available
    else: 
        f2 = pd.read_csv(f2_csv, header=[0, 1, 2],index_col=0)
        f3 = pd.read_csv(f3_csv, header=[0, 1, 2],index_col=0)
        tr_ = pd.concat((f1, f2, f3))
        gr = tr_.groupby(tr_.index)
        train = gr.mean() 
    

 

    # apply smoothing
    train = train.rolling(window=ROLLING_MEAN_WINDOW,center=True).mean()
    
    for year in ["2016","2017"]:
        for partition in ["train","test"]:
            for metric in ["oa","xe"]:
                series = train[year,partition,metric].dropna()
                series.to_csv(path=outfilename.format(basename=basename,year=year,partition=partition,metric=metric), index=True)
                #break

    #break
