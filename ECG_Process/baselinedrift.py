
import numpy as np
import matplotlib.pyplot as plt

from ECG_Tool.ECG_Process import stmgen


def functionname(sfq, ECG_Data, DispOptn):

    d0 = ECG_Data
    f = sfq

    stm, stm_len = stmgen.functionname(f, 0, d0)
    d0 = d0.flatten()
    stm = stm.flatten()
    stm_org = np.array(stm)

    cof = 35
    mu = np.array([np.mean(stm), np.std(stm, ddof=1)])
    for i in range(len(stm)):
        stm[i] = (stm[i] - mu[0]) / mu[1]
    p = np.polyfit(stm, d0, cof)
    f_y = np.polyval(p, stm)
    d1 = d0 - f_y
    Adjusted_ECG = d1

    if DispOptn == 1:
        plt.subplot(2, 1, 1)
        plt.plot(stm_org, d0)
        plt.plot(stm_org, f_y, 'r')
        plt.title('Original (Time)',fontsize=10)

        plt.subplot(2, 1, 2)
        plt.plot(stm_org, d1)
        plt.plot(stm_org, np.zeros((len(stm))), 'r')
        plt.title('Basline Drifted',fontsize=10)
        plt.subplots_adjust(wspace=0.15, hspace=0.3)
        plt.show()

    return Adjusted_ECG
