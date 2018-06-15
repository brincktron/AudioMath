import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import scipy.signal

path1 = "DutSpkPinkWav_mic1.wav"
sig1, fs1 = sf.read(path1)

path2 = "DutSpkPinkWav_mic2.wav"
sig2, fs2 = sf.read(path2)

f, Cxy = scipy.signal.coherence(sig1, sig2, fs=16000, window='hann', nperseg=16000)
Cxy_pct = Cxy * 100
# figure1=plt.semilogy(f,Cxy_pct)
# plt.show()

Cxy_dB = -10 * np.log10(1 - (Cxy))
np.savetxt('Mic1Mic2_CBD.txt', np.transpose(np.array([f, Cxy_dB])), fmt='%1.3f')
figure2 = plt.semilogx(f, Cxy_dB)  # type: float
plt.xlim([100, 8000])
plt.show(figure2)
