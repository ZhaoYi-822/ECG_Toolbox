from statistics import mode

import numpy as np
from matplotlib import pyplot as plt

from ECG_Tool.ECG_Process import stmgen
from ECG_Tool.RRIF import rpeakdetect


def functionname(Level, sfq, sig_dat):

    """
    Gives the R-peak index and values from ECG data

    Usage:
          Rpeak_Mat = functionname(Level, sfq, sig_dat)
    Output:
          Rpeak_Mat (2xN Array) = [Value of Peak, Index of Peak]
    Input:
        Level       :  Peak ratio
        sfq         :  Sampling frequency
        sig_dat     :  ECG data

    Note:
        - Original Matlab file: rpeakdetect, stmgen, pyplot, numpy, mode
        - Adding for ploting the signal (with grid on)

    Made by Zhao Yi [v0.3 || 12/21/2023]
    """

    sig_dat=sig_dat.flatten()
    d0=sig_dat
    DispOptn=0
    [stm, stm_ed] = stmgen.functionname(sfq, 0, d0)
    sig_len=len(stm)


    PeakLevel = Level
    NoiseRatio = 0.2
    ConfidentLevel = 1 - NoiseRatio
    MinofPeak = np.floor(stm_ed * ConfidentLevel)
    MaxofPeak = (5 / 3) * stm_ed
    Rpeak_Mat = np.empty((0, 2))
    ECG_len = len(d0)

    x = max(d0)
    a_idx = np.array(np.where(d0 >= PeakLevel * x))
    a_d = d0[a_idx].flatten()
    Threshold = mode(a_d)

    RR_peak = np.floor(sfq / 2)
    Loop_len = int(np.floor(ECG_len / RR_peak))

    for i in range(Loop_len):
        sig_data = sig_dat[int((i) * RR_peak):int((i + 1) * RR_peak)]
        R_peak = max(sig_data)
        ECG_Idx = np.argwhere(sig_data == R_peak)
        if (len(ECG_Idx) == 1):
            ECG_Idx = ECG_Idx.astype(int)
        else:
            ECG_Idx = ECG_Idx[0].astype(int)

        if (ECG_Idx >= 0):
            if (R_peak >= Threshold):
                Adj_Idx = int(ECG_Idx + (i) * RR_peak - 1)
                Rpeak = [[R_peak, Adj_Idx]]
                Rpeak_Mat = np.vstack((Rpeak_Mat, Rpeak))

    a_m = Rpeak_Mat.shape[0]
    a_n = Rpeak_Mat.shape[1]
    a_mn = str(a_m)

    if (a_m < MinofPeak):
        print('The number of R-peaks ', a_m, 'which is smaller than the threshold', a_n)
        Peak_Rev = PeakLevel * 0.9
        Rpeak_Mat=rpeakdetect.functionname(Peak_Rev, sfq, sig_dat)
    print('Finding total ', a_m, ' R-peaks on the signal........')


    if DispOptn == 1:
        plt.title('Ploting ECG with R-R Peaks')

        plt.xlabel("sampling time (s)")
        plt.ylabel("ECG amplitude (mV or V)")

        plt.plot(stm, d0)
        x = np.array(Rpeak_Mat[:, 1]).astype(int) + 1
        stm = stm[x]
        d0 = d0[x]
        plt.plot(stm, d0, 'm*')
        plt.show()

    return Rpeak_Mat