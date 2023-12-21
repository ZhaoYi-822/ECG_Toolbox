import matplotlib.pyplot as plt
import numpy as np
from ECG_Tool.ECG_Process import stmgen

def functionname(sfq, ECG_Data, DispOptn):
    """
      Return the flipped signal and offset for flipping status

      Usage:
          ECG_sig = functionname(sfq, ECG_data, DispOptn)
      Output:
          Sig 	: Return the flipped (or original) ECG signals
      Input:
          sfq         : Given sampling frequency [Hz]
          ECG_data    : Original ECG data to be adjusted [mV]
          DisplayOpn  : Display Option [Off (0) or On (1)]

      Note:
          - Required Python file(s) : pyplot, numpy, stmgen
          - Simplified method for flipping signal
          - Display option is applied only if the signal is flipped
          - Ploting the comparison between Orignal and Flipped data
          - Revise for determine the baseline and flipping values

      Made by Zhao Yi [v0.3 || 12/21/2023]
    """

    d0 = ECG_Data
    f = sfq
    sig_len = len(d0)
    stm, stm_len = stmgen.functionname(f, 0, d0)

    st_idx = 0
    ed_idx = int(0.2 * np.floor(sig_len))
    d00 = d0[st_idx:ed_idx]
    dp = d00[d00 >= 0]
    dm = d00[d00 < 0]
    base = np.mean(d00)
    E0_max = abs(np.mean(dp) + base)
    E0_min = abs(np.mean(dm) + base)


    if abs(E0_max) <= abs(E0_min):
        offset = -1
        print('The ECG signal has been flipped ..................')
    else:
        offset = 1
        print('The ECG signal is NOT flipped ..................')

    d1 = offset * d0
    Sig = d1


    if (DispOptn == 1 and offset == -1):
        plt.subplot(2, 1, 1)
        plt.plot(stm, d0)
        plt.title('Original (Time)',fontsize=10)

        plt.subplot(2, 1, 2)
        plt.plot(stm, d1)
        plt.title('Flipped Signal (Time)',fontsize=10)
        plt.subplots_adjust(wspace=0.3, hspace=0.3)
        plt.show()

    return Sig
