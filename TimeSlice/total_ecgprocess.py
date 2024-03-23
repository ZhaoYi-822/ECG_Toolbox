
import pandas as pd



def function(Data4ML,filename,folder):
    """
    ECG time slice data is stored in .csv format

    Input:
        Data4ML     :  ECG Time Sliced Data
        filename    :  Save filename
        folder      :  Saved folder

    Note:
        - Original Python file: pandas

    Made by Zhao Yi [v0.3 || 12/21/2023]
    """
    data1 = pd.DataFrame(Data4ML)
    data1.to_csv(folder+filename+'.csv')








