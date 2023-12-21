import matplotlib.pyplot as plt
import numpy as np

from ECG_Tool.ECG_Process import stmgen


def functionname(sfq, ECG_Data, DispOptn):
    """
      Deliver the adjusted signals after noise frequency removing automatically

      Usage:
          Adjusted_ECG = functionname(sfq, ECG_Data, DispOptn)
      Output:
          Ajusted_ECG : Adjusted ECG signals
      Input:
          sfq         : Given sampling frequency [Hz]
          ECG_data    : Original ECG data to be adjusted [mV]
          DisplayOpn  : Display Option [Off (0) or On (1)]

      Note:
          - Required Python file(s) : pyplot, numpy, stmgen
          - Ploting the comparison between Orignal and Adjusted data
          - Default cutoff ratio is 300 (times)
          - Adding PLI remover (50/60 Hz) and Low Frequency range

      Made by Zhao Yi [v0.3 || 12/21/2023]

    """

    d0 = ECG_Data
    f = sfq
    d0 = d0.flatten()
    CutoffRatio =300
    PLIFreq50 = 50
    PLIFreq60 = 60
    sig_len = len(d0)
    stm, stm_end = stmgen.functionname(f, 0, d0)
    d0_f = np.fft.fft(d0)

    d1_f = d0_f
    m0 = abs(d0_f)
    Cut_m = CutoffRatio * np.mean(m0)
    fq = np.linspace(0, (len(d1_f) - 1) * f, len(d1_f)) / len(d1_f)

    Lower0 = np.array(np.where(m0 > Cut_m)) + 1
    Lower1 = Lower0 - len(d1_f) / sfq
    Lower1 = Lower1.flatten()
    Upper0 = np.array(np.where(m0 > Cut_m)) + 1
    Upper1 = Upper0 + len(d1_f) / sfq
    Upper1 = Upper1.flatten()
    IdxSet = np.array([np.ceil(Lower1), np.floor(Upper1)])
    IdxSet = IdxSet.T
    n = np.size(IdxSet, axis=0)
    r = np.size(IdxSet, axis=1)

    for k in range(0, n - 1):
        if Lower1[k] > 0 and Upper1[k] <= sig_len:
            d1_f[int(IdxSet[k, 0]) - 1:int(IdxSet[k, 1]) + 1] = 0

    lowfq0 = np.array(np.where((fq > 0.1) & (fq < 0.9)))
    lowfq1 = np.array(np.where((fq > sfq - 0.9) & (fq < sfq - 0.1)))
    lowfq = np.append(lowfq0, lowfq1)

    pli1_50 = np.array(np.where((fq > (PLIFreq50 - 0.5)) & (fq < (PLIFreq50 + 0.5))))
    pli2_50 = np.array(np.where((fq > (sfq - PLIFreq50 - 0.5)) & (fq < (sfq - PLIFreq50 + 0.5))))

    pli1_60 = np.array(np.where((fq > (PLIFreq60 - 0.5)) & (fq < (PLIFreq60 + 0.5))))
    pli2_60 = np.array(np.where((fq > (sfq - PLIFreq60 - 0.5)) & (fq < (sfq - PLIFreq60 + 0.5))))

    d1_f[lowfq] = 0
    d1_f[pli1_50] = 0
    d1_f[pli2_50] = 0
    d1_f[pli1_60] = 0
    d1_f[pli2_60] = 0
    d1_f[m0 < 1e-6] = 0
    Z = np.array(np.where(m0 < 1e-6))
    Z = Z.flatten()
    for i in range(0, len(Z)):
        d1_f[Z[i]] = 0

    m1 = np.abs(d1_f)
    d1 = np.real(np.fft.ifft(d1_f))
    Adjusted_ECG = d1

    if (DispOptn == 1):

        plt.subplot(2, 2, 1)
        plt.plot(stm, d0)
        plt.title('Original (Time)',fontsize=10)

        plt.subplot(2, 2, 2)
        plt.plot(stm, d1)
        plt.title('Noise Removed (Time)',fontsize=10)

        plt.subplot(2, 2, 3)
        plt.plot(fq, m0)
        plt.title('Original (Freq)',fontsize=10)

        plt.subplot(2, 2, 4)
        plt.title('Noise Adjusted (Freq)',fontsize=10)
        plt.plot(fq, m1)
        plt.subplots_adjust( hspace=0.3)

        plt.show()

    return Adjusted_ECG
