import wfdb
import matplotlib.pyplot as plt
import numpy as np


def functionname(Freq, EndTime, SigData):
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

    # print(SampleTimeRange)

    RevEndTime = stm0[stm_len - 1]

    # print(RevEndTime)
    return SampleTimeRange, RevEndTime
