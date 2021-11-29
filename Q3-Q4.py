import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

long, fsp = sf.read('NeckClean.ogg')
longcr, fspcr = sf.read('NeckCrunch.ogg')
longd, fspd = sf.read('NeckDirty.ogg')

N = len(long)
N2 = len(longd)
N3 = len(longcr)

long = long[:,0]
longcr = longcr[:,0]
longd = longd[:,0]

ts = 1/fsp
tscr = 1/fspcr
tsd = 1/fspd

T_s = 2 #seconds (the starting point)
N_start = int(np.floor(N*T_s/53)) #the length of the audio files is 53 seconds
N_start_d = int(np.floor(N2*T_s/50)) #the length of the audio file is 50 seconds

Np = int(2**14) #number of points in a window
Ns = int(np.floor(N/Np))

longwincl = long[N_start:N_start+Np]
longwincr = longcr[N_start:N_start+Np]
longwind = longd[N_start_d:N_start_d+Np]
Nd = len(longwind)

long1 = np.fft.fft(longwincl)
long2 = np.fft.fft(longwincr)
long3 = np.fft.fft(longwind)

freqsp = np.arange(Np)/(ts*Np)
freqspc = np.arange(Np)/(tscr*Np)
freqspd = np.arange(Np)/(tsd*Np)

n = 5500 #to zoom in I used n=5500 or 500
long1 = long1[0:n]
long2 = long2[0:n]
long3 = long3[0:n]

freqsp = freqsp[0:n]
freqspc = freqspc[0:n]
freqspd = freqspd[0:n]

plt.plot(freqspd, np.log10(np.abs(long3)))
plt.plot(freqspc, np.log10(np.abs(long2)))
plt.plot(freqspc, np.log10(np.abs(long1)))





















