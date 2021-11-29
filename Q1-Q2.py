import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd

#Using the sf.read command I take the information from the sound, 
#and take the 2-D array and the frequency. 
#The array has 2 dimensions because we have a stereo sound here, 
#if I use the headphones I'll be able to hear the sound with two ears, 
#with a slight difference
short, fsp1 = sf.read('NeckCleanExt.ogg')
Ar = len(short)
short = short[:,0] #I take one of the channels
shortcrunch, fsp2 = sf.read('NeckCrunchExt.ogg')
shortcrunch = shortcrunch[:,0]

shortdirt, fsp3 = sf.read('NeckDirtyExt.ogg')
shortdirt = shortdirt[:,0]
Ard = len(shortdirt)
#Here I am defining the time array,
#as the length of the array (the length of the file)
#is the same for all 3 audios, I'll take one of them.
timep1 = np.arange(Ar)/fsp1
timep2 = np.arange(Ar)/fsp2
timep3 = np.arange(Ard)/fsp3

fig, axs = plt.subplots(3)
fig.suptitle('Clean, Crunchy and Dirty Sounds')
axs[0].plot(timep1,short)
axs[1].plot(timep2, shortcrunch)
axs[2].plot(timep3, shortdirt)

ext = np.concatenate((short, shortcrunch, shortdirt))
sd.play(ext)

Fc = np.fft.fft(short)
Fcr = np.fft.fft(shortcrunch)
Fd = np.fft.fft(shortdirt)

fig1, axs1 = plt.subplots(3)
fig1.suptitle('Fourier Transforms of clean, crunchy and dirty signals')
axs1[0].plot(Fc)
axs1[1].plot(Fcr)
axs1[2].plot(Fd)

plt.show(fig, fig1)