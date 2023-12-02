import numpy as np
import pandas as pd


def function(rrif_ecg,ecg_seq,slice_ecg,file_rename,file):
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



