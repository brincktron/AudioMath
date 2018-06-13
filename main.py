import numpy as np
import matplotlib.pyplot as plt
import wave
x2=np.linspace(100,1000,10)
y=[99.2, 99.4, 98.1, 98.2, 97.0, 98.0, 99.1, 99.99, 99.999, 99.8]
plt.plot(x2,y)
plt.ylabel('[%]')
plt.title('Coherence')
# plt.show()

DutSpkPinkWav_mic1 = wave.open("DutSpkPinkWav_mic1.wav")
test
