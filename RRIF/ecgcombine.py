import numpy as np
import pandas as pd


def functionname(rrif_ecg,ecg_seq,slice_ecg,file_rename,file):

    """
       Combine time slice data of the same R peak with RR interval framed slice data

        Input:
            rrif_ecg        : RR Interval Framed Sliced Data
            ecg_seq         : R peak data location
            slice_ecg       : Time-sliced data
            file_rename     : Save filename
            file            : Saved folder

        Note:
            - Required Python file(s) : numpy, pandas

          Made by Zhao Yi [v0.3 || 12/21/2023]
        """
    slice_ecg = np.array(slice_ecg)
    rrif_num = rrif_ecg.shape[1]
    slice_num = slice_ecg.shape[1]
    ecg_len = len(ecg_seq)
    cob_num = rrif_num + slice_num
    ecg_cob = np.empty((0, cob_num))
    cob_files = file + '/' + file_rename + '.csv'

    j = 0
    for i in ecg_seq[1:ecg_len]:
        sig_ecg = np.append(slice_ecg[i], rrif_ecg[j])
        ecg_cob = np.vstack((ecg_cob, sig_ecg))
        j = j + 1

    cob_data = pd.DataFrame(ecg_cob)
    cob_data.to_csv(cob_files)



