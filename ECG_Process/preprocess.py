
import wfdb

from ECG_Tool.ECG_Process import baselinedrift, ecgflip, remove_noise


def ecgprocess(origin_ecg_path, ecg_num, slice_interval):



    interval = slice_interval
    record = wfdb.rdrecord(origin_ecg_path+'/'+ecg_num, channels=[0])
    f = record.fs
    d0 = record.p_signal[interval[0]:interval[1]]
    sfq = f

    print('Display option for baselinedrift:')
    DispOptn = int(input())
    d01 = baselinedrift.functionname(sfq, d0, DispOptn)
    d1 = d01

    print('Display option for ecgflip:')
    DispOptn = int(input())
    d02 = ecgflip.functionname(sfq, d1, DispOptn)
    d1 = d02

    print('Display option for remove noise:')
    DispOptn = int(input())
    d03 = remove_noise.functionname(sfq, d1, DispOptn)
    d1 = d03

    RevisedECG = d1

    return RevisedECG, sfq






