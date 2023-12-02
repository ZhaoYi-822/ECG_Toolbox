import tkinter as tk
from tkinter import filedialog

import numpy as np
import pandas as pd

import csv_process
from ECG_Tool.ECG_Process import preprocess
from ECG_Tool.RRIF import ecgrpeakframe, ecgcombine

if __name__ == "__main__":

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

    for ecg_num in ecg_case.split():

        slice_ecg = pd.read_csv(slice_ecg_path+'/'+ecg_num+'_'+suffix+'.csv')
        revisedECG, sfq = preprocess.ecgprocess(origin_ecg_path,  ecg_num, slice_interval)
        print('Display for RR peak signal:')
        DispOptn = int(input())
        print('Input TargetFrame:')
        TargetFrame = input()
        TargetFrame=int(TargetFrame)
        rrif_ecg, ecg_seq = ecgrpeakframe.functionname(TargetFrame,sfq,revisedECG,DispOptn)
        file_rename=ecg_num+'_cob'+'_'+suffix
        ecgcombine.function(rrif_ecg, ecg_seq, slice_ecg, file_rename, save_folder)



