from statistics import mean

import numpy as np


def functionname(n1_data):

    n1_data=n1_data.flatten()
    d0=n1_data

    data_len = len(n1_data)

    delta = np.empty((0, 1))

    for i in range(data_len-1):
        dk = d0[i + 1]
        dk_1 = d0[i]
        delta0 = dk - (dk_1 - 1)
        delta = np.vstack((delta,delta0))

    delta=np.array(delta).flatten()
    meandelta = mean(delta)
    deltaset = np.array(delta)



    return meandelta,deltaset