import math

import numpy as np
from matplotlib import pyplot as plt


def functionname(OrignalData,TargetFrame,DispOptn):

    ecg0=OrignalData
    ecg0=ecg0.flatten()
    DataLength=len(ecg0)
    UnitFrame=TargetFrame


    stidx = 0
    endidx = DataLength
    onelength = endidx - stidx
    sq0len = onelength-1

    len_b = np.lcm(UnitFrame, onelength)
    ecg_b = np.zeros([len_b, 1])

    sq0= np.linspace(0,sq0len,sq0len+1)
    sq1=np.linspace(0,sq0len,UnitFrame+1)
    sqb=np.linspace(0,sq0len,len_b+1)
    sq0=sq0.reshape(-1,1)
    # sqb=sqb.flatten()

    xx=np.array(sq0-sqb)
    x=np.abs(xx)
    idx_0,idx_b=np.array(np.where(x<0.005))
    idx_b=idx_b.astype(int)
    n=np.max(idx_b)
    ecgb_len=abs(n-len_b+1)
    for i in range(ecgb_len):
        ecg_b=np.append(ecg_b,0)
    ecg_b[idx_b] = ecg0[idx_0]

    base_ref=np.array([idx_b,ecg_b[idx_b]])
    base_ref=base_ref.T
    base_len=len(idx_b)

    for i in range(base_len-1):
        st_idx = idx_b[i]
        ed_idx = idx_b[i + 1]
        idx_num = ed_idx - st_idx-1
        for j in range(0,idx_num):
            ecg_b[st_idx + j+1] = ecg_b[st_idx] + (ecg_b[ed_idx] - ecg_b[st_idx]) * ((j+1) / (idx_num + 1))

    sq1=sq1.reshape(-1,1)
    y=np.abs(sq1-sqb)
    idx_1,idx_1b=np.array(np.where(y<0.005))

    ecg1=np.empty((UnitFrame+1))
    ecg1[idx_1] = ecg_b[idx_1b]

    RevisedData = ecg1.reshape(-1,1)
    NumofSlot = sq0len

    if DispOptn == 1:



        plt.subplot(2, 1, 1)
        plt.plot(sq0,ecg0)
        plt.title('Original Signal (Number of Slots =' +str(onelength-1) +')' )


        a=np.linspace(0,UnitFrame,UnitFrame+1)
        plt.subplot(2, 1, 2)
        plt.plot(a, ecg1,'r')
        plt.title('Revised Signal (Number of Slots =' +str(UnitFrame)+ ')')
        plt.show()


    return RevisedData