import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import scipy.signal
import math
#x2=np.linspace(100,1000,10)
#y=[99.2, 99.4, 98.1, 98.2, 97.0, 98.0, 99.1, 99.99, 99.999, 99.8]
#plt.plot(x2,y)
#plt.ylabel('[%]')
#plt.title('Coherence')
#plt.show()

path1 = "DutSpkPinkWav_mic1.wav"
sig1, fs1 = sf.read(path1)

path2 = "DutSpkPinkWav_mic2.wav"
sig2, fs2 = sf.read(path2)

f, Cxy = scipy.signal.coherence(sig1,sig2,fs=16000,window='hann',nperseg=1024)
plt.semilogy(f,Cxy)
#plt.show()

Cxy_decim=Cxy/100;
Cxy_dB = 10*math.log(1-(Cxy/100));

plt.semilogy(f,Cxy_dB)
plt.show()

test=2