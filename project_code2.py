import numpy as np
from scipy.io import loadmat
from matplotlib import pyplot as plt
from scipy.signal import find_peaks
from scipy import signal
import scipy.signal 
plt.ion()
data2=loadmat('ecg_1min.mat')

ECG2=data2['ecg'][0]


FS=data2['fs'][0,0]
TS=1/FS
N2=len(ECG2)
ecg2=ECG2[0:400]
n2=len(ecg2)
time2=np.arange(0,N2*TS,TS)
time4=np.arange(0,n2*TS,TS)



# STFT 
#window= signal.get_window('hann', seg_sec)
seg_sec=10*FS
freq, seg_time, stft= scipy.signal.stft(ECG2, FS, nperseg=seg_sec)#, nfft= 4*seg_sec)
#magnitude of the STFT 
mag=np.abs(stft)**2 

plt.figure(5)
plt.suptitle ('Original ECG Signal')
plt.plot(time2,ECG2)
plt.xlabel('time (seconds)')
plt.ylabel('Amplitude (V)')

plt.figure(1)
plt.suptitle ('Original ECG Signal')
plt.plot(time2,ECG2)
plt.xlim([5,15])
plt.xlabel('time (seconds)')
plt.ylabel('Amplitude (mV)')

plt.figure(2)
plt.suptitle ('Original signal(1)')
plt.plot(time4,ecg2)
plt.xlabel('time (seconds)')
plt.ylabel('Amplitude (mV)')

plt.figure(3)
plt.suptitle ('Short-time Fourier Transform')
plt.plot(freq,mag)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power (mV^2)')

plt.figure(4)
plt.suptitle ('Spectrogram')
plt.imshow(mag, vmin=0, vmax=0.1, aspect='auto', extent= [np.min(seg_time), np.max(seg_time),np.min(freq), np.max(freq)])
plt.colorbar()
plt.xlabel('Time (sec)')
plt.ylabel('Frequency (Hz)')




