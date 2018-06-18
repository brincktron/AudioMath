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


soundcheck_info=np.zeros(len(f), dtype='|S8')
soundcheck_info[0:5]=['Mic1Mic2_CBD', 'x data lin', 'y data lin', 'x axis log', 'y axis lin']

out=np.column_stack([soundcheck_info,f,Cxy_dB])
np.savetxt('Mic1Mic2_CBD.txt', out, delimiter='\t', fmt='%s')

figure2 = plt.semilogx(f, Cxy_dB)  # type: float
plt.xlim([100, 8000])
plt.show(figure2)
