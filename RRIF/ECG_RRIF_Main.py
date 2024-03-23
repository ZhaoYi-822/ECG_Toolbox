

import numpy as np
import pandas as pd


from ECG_Tool.ECG_preprocess import preprocess
from ECG_Tool.RRIF import ecgrpeakframe, ecgcombine

if __name__ == "__main__":

    """
     Time slice main program

     Input:
        origin_ecg_path     :  Source ECG database location
        save_folder         :  Save ECG processed location
        slice_ecg_path      :  Storage location of ECG time slice
        ecg_file_suffix     :  ECG data
        ecg_case            :  Dataset type (train or test)
        slice_interval      :  Interval of ECG data to be process
        DispOptn            :  RR peak signal display Option [0 (Off), 1 (on)]
        TargetFrame         :  Target frame

     Note:
        - Original Python file: preprocess, ecgrpeakframe, ecgcombine, numpy, pandas

     Made by Zhao Yi [v0.3 || 12/21/2023]
    """

    print('Input source ECG data address')

    origin_ecg_path = input('')

    print('Input save address')
    save_folder = input('')

    print('Input TimeSlice ECG path')
    slice_ecg_path = input('')

    print('Input dataset type')
    ecg_file_suffix = input('')
    suffix=ecg_file_suffix

    print('Input ECG use case:')
    ecg_case = input('')
    print('ECG slice interval:')
    slice_interval = input('')
    slice_interval = np.array(slice_interval.split()).astype(int)

    for ecg_name in ecg_case.split():

        slice_ecg = pd.read_csv(slice_ecg_path+'/'+ecg_name+'_'+suffix+'.csv')
        revisedECG, sfq = preprocess.ecgprocess(origin_ecg_path,  ecg_name, slice_interval)
        print('Display for RR peak signal:')
        DispOptn = int(input())
        print('Input TargetFrame:')
        TargetFrame = input()
        TargetFrame=int(TargetFrame)
        rrif_ecg, ecg_seq = ecgrpeakframe.functionname(TargetFrame,sfq,revisedECG,DispOptn)
        file_rename=ecg_name+'_cob'+'_'+suffix
        ecgcombine.functionname(rrif_ecg, ecg_seq, slice_ecg, file_rename, save_folder)



