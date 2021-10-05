# Aqui, me baseei no artigo apresentado na atividade solicitada da aula 10, onde os autores leram sinais de Eletrogastrografia (egg) e plotaram gráficos de egg em função do tempo,e aplicaram transformada de fourier"

# Fazendo os imports

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

n = 1000     # número de pontos no gráfico
tx = 250     # unidade de tempo arbritária     
w = 2.0 * np.pi/tx       # frequência angular 

t = np.linspace(0, tx, n)

# criando sinais com amplitudes e frequências arbritárias
s1 = 2.0*np.cos(0.03*w*t)
s2 = 5.0*np.cos(0.05*w*t)
s3 = 3.0*np.cos(0.07*w*t)

s = s1+s2+s3


freq = np.fft.fftfreq(n)
mascara = freq > 0

fft_calc = np.fft.fft(s)

plt.figure(1)
plt.title("Sinal original")
plt.plot(t,s)

plt.figure(2)
plt.title("sinal da fft")
plt.plot(freq[mascara],fft_calc[mascara])

plt.show()