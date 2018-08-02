import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import scipy.signal
import json

wav1 = "DutSpkPinkWav_mic1.wav"
wav2 = "DutSpkPinkWav_mic2.wav"

sig1, fs1 = sf.read(wav1)
sig2, fs2 = sf.read(wav2)

sig1 = np.append(np.zeros(10000),sig1)

def coherence(sig1,sig2,resolution,fs=0):
    ''' This function returns the coherence between two wav signals
    file1 (string): path to file 1 or data
    file2 (string): path to file 2 or data
    resolution (integer) : for instance 20 meaning 20 Hz Resolution
    and 1 meaning 1 Hz resolution'''
    if isinstance(sig1,str):
        if sig1[-3:] == 'wav' and sig2[-3:] == 'wav':
            sig1, fs1 = sf.read(wav1)
            sig2, fs2 = sf.read(wav2)
            print 'reading wav files...'
    elif isinstance(sig1,list) and isinstance(sig2,list):
        print 'reading data files...'
    elif type(sig1).__module__ == np.__name__ and type(sig2).__module__ == np.__name__:
        print 'reading numpy data...'
    else:
        print 'data not recognized, please input either wav-file paths or python lists as the two firs arguments'

#    if fs1 > 0 and fs1 == fs2:
#        fs = fs1
#        print 'sampling rate is ' + str(fs) + ' Hz'
#    elif fs1 > 0 and fs1 != fs2:
#       fs = 0
#        print 'sampling rates do not match'

    if resolution < 1:
        print 'resolution must be 1 Hz resolution or lower'
        print 'resolution set to default (20 Hz Resolution)'
        resolution = 20

    res = fs * 1./resolution
    # coherence calculation using scipy
    f, Cxy = scipy.signal.coherence(sig1, sig2, fs, window='hann', nperseg = round(res))

    # conversion of coherence pct to dB
    Cxy_dB = -10 * np.log10(1 - Cxy)

    return Cxy * 100, Cxy_dB, f, fs

Cxy_pct, Cxy_dB, f, fs = coherence(sig1 ,sig2 ,100 ,fs=16000)


data_out={}
# 0 is log, 1 is linear
data_out['soundcheck info']={'filename': 'Mic1Mic2_CBD',
                  'curve name': 'Coherence',
                  'x unit': 'Hz',
                  'y unit': 'dB',
                  'z unit': 'deg'}

z=np.zeros(len(Cxy_dB)).tolist()
data_out['frequency info'] = {'x-data': f.tolist(), 'y-data': Cxy_dB.tolist(), 'z-data':z}


def delaydetect(ref_signal, snippet):
    crosscorr = np.correlate(ref_signal, snippet, 'full')
    delay = crosscorr.argmax() - (len(snippet) - 1)
    print 'delay based on cross correlation is: ' + str(delay) + ' samples'
    if delay < 0:
        crosscorr = crosscorr[np.round(len(crosscorr)/2)+delay:]
        x = np.linspace(delay,len(crosscorr)+delay,len(crosscorr))
    else:
        crosscorr = crosscorr[np.round(len(crosscorr)/2):]
        x = np.linspace(0,len(crosscorr)-1,len(crosscorr))
    return delay, x, crosscorr

delay, x, crosscorr = delaydetect(sig1,sig2)

plt.plot(crosscorr)
plt.show()

#write to file
with open('Mic1Mic2_CBD.json', 'w') as outfile:
    json.dump(data_out, outfile)

