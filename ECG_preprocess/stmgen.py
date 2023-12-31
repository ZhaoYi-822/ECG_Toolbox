import numpy as np


def functionname(Freq, EndTime, SigData):
    """
     Generating Sampling Time Vector based on the frequency

     Usage:
        SampleTimeRange, RevEndTime = functionname(Freq, EndTime, SigData)
     Output:
        SampleTimeRange : Sampling time sequence aligned with signal data
        RevEndTime      : Revised time end
     Input:
        Freq        : Sampling frequency of the signal
        EndTime     : End time of the signal
        SigData     : ECG data

     Note:
        - Required Python file(s) : numpy
        - Generating the sampling time for signal data
        - SigData == 0 : Sampling Time generated by End Time and Frequency
        - EndTime == 0 : Sampling time generated by Signal Data

     Made by Zhao Yi [v0.3 || 12/21/2023]
    """

    f = Freq

    if np.any(SigData == 0):
        l0 = f * EndTime + 1
    else:
        l0 = len(SigData)

    if EndTime == 0:
        l0 = len(SigData)
    else:
        l0 = f * EndTime + 1

    x=(l0 - 1) / f
    y=1/f
    x=x+y/1000000000
    stm0=np.arange(0, x, y)
    lengeth = len(stm0)-1
    if stm0[lengeth]!=x and stm0[lengeth]+y <=x:
        stm0=np.append(stm0,x)

    stm_len = len(stm0)
    if stm_len > l0:
        stm0 = stm0[:l0]
        stm_len = l0

    SampleTimeRange = stm0.reshape(-1, 1)
    RevEndTime = stm0[stm_len - 1]


    return SampleTimeRange, RevEndTime
