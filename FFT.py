# -*- coding: utf-8 -*-


instructions="""  
**************************************************************************
        FFT (Fast Fourier Transform) CALCULATION (v1.2)
**************************************************************************

Created by Maria Pedrosa Bustos (mpedrosab@gmail.com)
    on 16-03-2021 for the Department of Applised Physics (UGR)

Input: 
    Input file name. Raw text file with two columns: time (s) and data.
    (All headers before and in the same line as a label containing "T" are ignored)

Output: 
    Stored in the Output folder:
    1. File 'fft_out.txt' containing the FFT calculation of the input data.
    2. Images representing the output ('fft_out.png') and input ('fft_in.png') data.


REMARKS:   
    * Zero point is removed to avoid singularities.
    * Assumes that the time interval between samples is constant along the whole data.

*************************************************************************************
"""

import numpy as np
import sys
import matplotlib.pyplot as plt         #       

#datosIn.txt
print(instructions)
#Get name file
path=input("Enter the path of your data file: ")

#Read file
try:
    #Read txt
    try:
        f=open(path,"r", encoding='utf-8')
        dataStr=f.read()

    except:
        f=open(path,"r", encoding='latin-1')
        dataStr=f.read()

    f.close



    #Replace comma as decimal point (in case there is comma)
    dataStr=dataStr.replace(",", ".")

    try: #Data with header. Remove it
        dataFinal=dataStr.split("T",1)[-1].split("\n",1)[-1]
        
    except:     #No header
        dataFinal=dataStr
    data1=[]
    data2=[]

    #If there is a final breakline
    dataFinal=dataFinal.replace(" ","\t")    #in case separation is with spaces
    if dataFinal[-1]=="\n":
        dataFinal=dataFinal[:-1]

    for s in dataFinal.split('\n'):
        splitted=s.split('\t')

        if s=="\t":
            continue
        data1.append(float(splitted[0]))
        data2.append(float(splitted[1]))

    data=np.array([data1,data2])

    print("Computing FFT... Please wait\n")
    #Compute FFT
    dataFreq=int((data[0].shape[-1]+1)/(data[0,1]-data[0,0])) #To match units
    fq = np.fft.fftfreq(data[0].shape[-1],(data[0,1]-data[0,0]))     
    fdata= np.fft.fft(data[1])
    out=np.array([np.fft.fftshift(fq),np.fft.fftshift(np.abs(fdata.real))])
    #out=np.array([fq,np.abs(fdata.real)])
    out=np.transpose(out[:,out[0,:]>0])
    np.savetxt("Output/fft_out.txt",out, delimiter="\t", header="Freq (Hz)\tAmplitude",comments='')

    
    plt.figure()
    plt.plot(data[0],data[1],"-o")
    plt.xlabel("Time [s]")
    plt.grid()
    plt.title("Input data")
    plt.savefig("Output/fft_in.png")

    print("Plotting the data\n")
    plt.figure()
    plt.plot(out[:,0],out[:,1],"-o")
    plt.xlabel("Frequency [Hz]")
    plt.xscale("log")
    plt.grid()
    plt.title("FFT")
    plt.savefig("Output/fft_out.png")
    

    print("Finished! Check the Output folder :).")
    #input("Press any key to exit.")
    print("Close image window to exit.")

    plt.show()
except Exception as error:
    print(error)
    input("Press any key to exit.")
