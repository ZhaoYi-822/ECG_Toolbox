import os

import numpy as np
import pandas as pd
import wfdb

from ECG_RRIF import ecgrpeakframe, rrif_csv_process
from ECG_Tool.ECG_Process import baselinedrift, ecgflip, remove_noise


def ecgprocess(origin_ecg_path, ecg_num, slice_interval,TargetFrame):

    interval = slice_interval
    record = wfdb.rdrecord(origin_ecg_path + ecg_num, channels=[0])
    f = record.fs
    d0 = record.p_signal[interval[0]:interval[1]]
    sfq = f
    TargetFrame = TargetFrame

    slice_ecg = pd.read_csv('C:/Users/zhaoy/PycharmProjects/ECG_Python/new MIT-BIH Dataset/tl_test/220_test.csv')
    record = wfdb.rdrecord('C:/Users/zhaoy/PycharmProjects/ECG_Python/mitdb/220', channels=[0])





    DispOptn = 0
    d01 = baselinedrift.functionname(sfq, d0, DispOptn)
    d1 = d01

    DispOptn = 0
    d02 = ecgflip.functionname(sfq, d1, DispOptn)
    d1 = d02

    DispOptn = 0
    d03 = remove_noise.functionname(sfq, d1, DispOptn)
    d1 = d03

    rrif_ecg, ecg_seq = ecgrpeakframe.functionname(TargetFrame, sfq, d1, DispOptn)

    # file_rename="220_cob.csv"
    # files='C:/Users/zhaoy/PycharmProjects/ECG_Python/new MIT-BIH Dataset/cob_test'
    # rrif_csv_process.fun(rrif_ecg, ecg_seq, slice_ecg, file_rename, files)




if __name__=="__main__":

     ecgprocess()