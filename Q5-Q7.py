import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

Ns = 2**14
time = np.arange(Ns)
x = np.zeros(Ns)
for i in time:
    x[i] = np.sin(440*i)
t = np.linspace(0, (6*np.pi)/440)
l = len(t)
xc = x[0:l]

alfa = 0.5
def saturation(a):
        return a if np.abs(a)<= alfa else alfa

def saturation1(a):
    if np.abs(a)<= alfa:  
        return a 
    elif a<0: 
        return -alfa
    else: 
        return alfa

y = np.zeros(Ns)
for i in time:
    y[i] = saturation(x[i])

yc = y[0:l]

ext = np.concatenate((x, y))
#sd.play(ext)

#################################
#ATTENTION EAR PIERCING SOUND
###################################

yf = np.fft.fft(y)
xf = np.fft.fft(x)

#Plotting section

plt.plot(t,xc)
plt.plot(t,yc)

#plt.plot(np.abs(xf))
#plt.plot(np.abs(yf))

#fig1, axs1 = plt.subplots(2)
#fig1.suptitle('The sine signal and its Fourier transform')
#axs1[0].plot(t,xc)
#axs1[1].plot(xf)