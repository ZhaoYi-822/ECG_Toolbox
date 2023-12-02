
import pandas as pd



def function(Data4ML,filename,folder):
    data1 = pd.DataFrame(Data4ML)
    data1.to_csv(folder+filename+'.csv')








