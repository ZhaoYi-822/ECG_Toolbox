from statistics import mean

import numpy as np


def functionname(n1_data):
    """
    Calculating the Mean of the gap between data

      Usage:
          meandelta, deltaset = functionname(n1_data)
      Output:
          meandelta     : Mean of data gap
          deltaset      : The set of collecting gap between data
      Input:
          n1_data   : Single lined data ([1xN] or [Nx1] data)

      Note:
          - Required Python file(s) : numpy, mean

      Made by Zhao Yi [v0.3 || 12/21/2023]
    """

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