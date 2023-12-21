import numpy as np
from matplotlib import pyplot as plt
from ECG_Tool.RRIF import ecgframechanger, deltamean, rpeakdetect


def functionname(TargetFrame, sfq, ECG_data, DispOptn):
    """
       ECG baseline drift correction

       Usage:
           ecg1set, seq_num = functionname(TargetFrame,sfq, ECG_data, DispOptn)
       Output:
           ecg1set  : ECG RR interval framed slice data
           seq_num  : Value of ECG RR interval framed data
       Input:
           TargetFrame  : Target number of grids between one RR-peaks
           sfq          : Sampling frequency of ECG data
           ECG_data     : ECG data
           DispOpn      : Display option [0 (Off), 1 (2D-plot), 3(3D-plot)]

       Note:
           - Required Python file(s): pyplot, numpy, ecgframechanger, deltamean, rpeakdetect
           - Adding the plotting feature (Supporting 3D)

       Made by Zhao Yi [v0.3 || 12/21/2023]

     """



    seq_num = np.empty([], dtype=int)
    d1=ECG_data
    a= rpeakdetect.functionname(0.6, sfq, d1)
    a_m=a.shape[0]
    a=np.array(a)
    NumSlice = a_m



    UnitFrame = TargetFrame
    OneGrid = (UnitFrame /22)
    ad = a[:,1]
    delt,s= deltamean.functionname(ad)

    ave_RR_sec = delt/sfq
    stm=np.linspace(0,ave_RR_sec,UnitFrame+1)
    RR_sec = s/sfq
    OneGrid_sec = (ave_RR_sec/UnitFrame)*OneGrid

    ecg1set=np.empty((0,UnitFrame+1))

    for i in range(1,NumSlice):

        stidx = a[i - 1, 1]
        if stidx == 0:
            i = i + 1
        seq=int(i-1)
        stidx = int(a[i - 1, 1])
        endidx = int(a[i, 1])
        onelength = endidx - (stidx - 1)


        ecg0 = d1[stidx:endidx+1]
        # ecg1 = sqframechanger.functionname(sfq,ecg0,UnitFrame,1,i)
        ecg1=ecgframechanger.functionname(ecg0,UnitFrame,0)
        ecg1=ecg1.flatten()


        xx=np.diff(ecg1)

        ddecg=np.diff(xx)
        ddl=np.array(np.where(ddecg))==0
        ddl=len(ddl.reshape(-1,1))
        qualidx = ddl / len(ddecg)

        if qualidx >= 0.8:
            ecg1set=np.vstack((ecg1set,ecg1))
            seq_num=np.append(seq_num,seq)


    MeanPlot = np.mean(ecg1set, 1)
    # ModePlot = np.mod(ecg1set, 0)
    ecg1set1=ecg1set.T
    n =ecg1set1.shape[1]


    if DispOptn==1:
        plt.title('R-R Peak Cycle ECG Signal (Unit Frame = '+ str(UnitFrame)+ ')')
        plt.xlabel('Time [sec]')
        plt.ylabel('Amplitute [mV]')
        plt.plot(stm, ecg1set1[:,0:UnitFrame+1])
        plt.legend(['Ref01', 'Ref02', 'Ref03', 'Ref04', 'Ref05', 'Ref06', 'Ref07', 'Ref08', 'Ref09'], loc='upper right', bbox_to_anchor=(0.9, 1))
        # plt.savefig('C:\\Users\\zhaoy\\Desktop\\img_ecg\\2D_rrif.eps', dpi=600)
        plt.show()


    if DispOptn==3:

        figure = plt.figure()
        ax = plt.axes(projection='3d')
        plt.title('R-R Peak Cycle ECG Signal (Unit Frame = '+ str(UnitFrame)+ ')')
        ax.set_xlabel('Sliced Samples (' +str(n) +')')
        ax.set_ylabel('Time [sec]')
        ax.set_zlabel('Amplitute [mV]')

        x_value = np.linspace(0, n-1, n)
        x, y = np.meshgrid(x_value, stm)
        ax.plot_surface(x,y,ecg1set1,cmap=plt.cm.brg)
        ax.view_init(20, 30)
        # plt.savefig('C:\\Users\\zhaoy\\Desktop\\img_ecg\\3D_rrif.eps', dpi=600)
        plt.show()

    return ecg1set, seq_num













