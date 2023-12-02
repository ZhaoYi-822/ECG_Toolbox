import tkinter as tk
from tkinter import filedialog

import numpy as np

import total_ecgprocess


from ECG_Tool.ECG_Process import preprocess
from ECG_Tool.TimeSlice import timeslice

if __name__ == "__main__":

    print('Input source ECG data address')

    origin_ecg_path = input('')

    print('Input save address')
    save_folder = input('')

    print('Input dataset type')
    ecg_file_suffix = input('')

    print('Input ECG use case:')
    ecg_case =input('')
    print('ECG slice interval:')
    slice_interval =input('')
    slice_interval = np.array(slice_interval.split()).astype(int)

    for ecg_num in ecg_case.split():

        revisedECG, sfq = preprocess.ecgprocess(origin_ecg_path,  ecg_num, slice_interval)
        print('Display for ECG_timeslice:')
        DispOptn = int(input())
        print('Input Slice time:')
        SliceTime = float(input())
        Data4ML = timeslice.function(sfq, revisedECG, SliceTime, DispOptn)

        filename=str(ecg_num)+'_'+ecg_file_suffix
        total_ecgprocess.function(Data4ML, filename, save_folder)