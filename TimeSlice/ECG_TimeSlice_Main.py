

import numpy as np

import total_ecgprocess


from ECG_Tool.ECG_preprocess import preprocess
from ECG_Tool.TimeSlice import timeslice

if __name__ == "__main__":

    """
        Time slice main program

        Input:
            origin_ecg_path     :  Source ECG database location
            save_folder         :  Save ECG processed location
            ecg_file_suffix     :  ECG data
            ecg_case            :  Dataset type (train or test)
            slice_interval      :  Interval of ECG data to be process
            DispOptn            :  Timeslice display Option [0 (Off), 1 (2D-plot), 3(3D-plot)]
            SliceTime           :  Sliced ECG data interval

        Note:
            - Original Python file: preprocess, timeslice, total_ecgprocess, numpy

        Made by Zhao Yi [v0.3 || 12/21/2023]
        """

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

    for ecg_name in ecg_case.split():

        revisedECG, sfq = preprocess.ecgprocess(origin_ecg_path,  ecg_name, slice_interval)
        print('Display for ECG_timeslice:')
        DispOptn = int(input())
        print('Input Slice time:')
        SliceTime = float(input())
        Data4ML = timeslice.functionname(sfq, revisedECG, SliceTime, DispOptn)

        filename=str(ecg_name)+'_'+ecg_file_suffix
        total_ecgprocess.function(Data4ML, filename, save_folder)
