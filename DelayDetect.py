import numpy as np
import matplotlib.pyplot as plt


print 'calculating cross correlation...'
crosscorr= np.correlate(sig2, sig1, 'full')
m = crosscorr.argmax() - (len(sig1) -1)
print 'delay based on cross correlation is: ' + str(m) + ' samples'
print len(sig1)
plt.plot(crosscorr)
plt.show()
plt.plot(sig1, 'r*')
plt.plot(sig2, 'b*')
plt.show()