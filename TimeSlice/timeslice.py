
import numpy as np
from matplotlib import pyplot as plt

from ECG_Tool.ECG_Process import stmgen
from ECG_Tool.TimeSlice import Rpeakfind


def functionname(fs, ECG_data, SliceTime, DisplayOption):
    """
         Slicing the ECG signal based on the slice time

        Usage:
            Data4ML = functionname(fs, ECG_data, SliceTime, DisplayOption)
        Output:
            Data4ML     : [MxN]-Matrix for N sliced samples
        Input:
            fs              : Sampling frequency
            ECG_data        : ECG data
            SliceTime       : Time for slicing the data [sec]
            DisplayOption   : [0 (Off), 1 (2D-plot), 3(3D-plot)]

        Note:
            - Required Python file(s) : stmgen, Rpeakfind, pyplot, numpy
            - Adding the plotting feature (Supporting 3D)

        Made by Zhao Yi [v0.3 || 12/21/2023]
      """


    ECG_data = ECG_data.flatten()
    Sig_data = ECG_data
    SampleFreq = fs
    SliceTime = SliceTime
    if SliceTime == 0:
        SliceTime=0.6



    d1 = Sig_data
    f = SampleFreq
    a,rpeak_num = Rpeakfind.functionname(0.6, f, d1)

    [stm, stm_ed] = stmgen.functionname(f, 0, d1)
    stm = stm.flatten()
    stm_len = len(stm)

    ans = 1 / f
    WindowTime = np.arange(0, SliceTime, ans)
    l = len(WindowTime) - 1
    if (WindowTime[l] + ans == SliceTime):
        WindowTime = np.append(WindowTime, SliceTime)
    win_slot = len(WindowTime)

    dat4train = []
    la = len(a[:, 1]) - 1
    slice_sq = []
    dat3D = []

    cut_end_idx = np.array(np.where(abs(stm - SliceTime) < 0.0001))
    if len(cut_end_idx) == 0:
        cut_end_idx = np.mean(np.array(np.where(abs(stm - SliceTime) < 0.001)))
    while a[la, 1] + cut_end_idx >= len(d1):
        la = la - 1

    Data4ML = np.empty((win_slot, 0))
    dat4train = np.empty((0, 2))
    z = np.empty((0, 2))

    for i2 in range(0, la + 1):
        st_idx = a[i2, 1]
        if st_idx < 0:
            st_idx = 0
        dataidx = np.linspace(st_idx, st_idx + win_slot - 1, win_slot).astype(int)

        slicetime = WindowTime.reshape(-1, 1)
        slicedata = d1[dataidx].reshape(-1, 1)
        slicedata_w = slicedata
        y = np.append(slicetime, slicedata, axis=1)
        dat4train = np.vstack((dat4train, y))
        Data4ML = np.column_stack((Data4ML, slicedata))
        slice_sq = np.append(slice_sq, i2)

    MeanPlot = np.mean(Data4ML, axis=1)
    slice_sq=slice_sq.reshape(-1,1)
    WindowTime=WindowTime.reshape(-1, 1)

    # x = Data4ML[:, 0:la + 1]
    Data4ML=Data4ML.T

    # csv_process.fun(y,filename,folder)


    if DisplayOption == 1:
        fig, ax = plt.subplots()
        plt.title('Regression Plot (2D)')
        plt.xlabel('Window Time (sec)')
        plt.ylabel('ECG Amplitude (mV or V)')
        plt.plot(slicetime, Data4ML[:, 0:la + 1])
        plt.legend(['Ref01', 'Ref02', 'Ref03', 'Ref04','Ref05','Ref06','Ref07','Ref08','Ref09'], loc='upper right')
        plt.show()


    if DisplayOption == 3:
        figure = plt.figure()
        ax = plt.axes(projection='3d')
        plt.title('Regression Plot (3D)')
        ax.set_xlabel('Sliced Samples')
        ax.set_zlabel('ECG Amplitude (mV or V)')
        ax.set_ylabel('Window Time (sec)')
        x, y = np.meshgrid(slice_sq, WindowTime)
        ax.plot_surface(x,y,Data4ML,cmap=plt.cm.brg)
        ax.view_init(20, 30)
        plt.show()

    return Data4ML


