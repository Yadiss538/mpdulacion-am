import numpy as np
import matplotlib.pyplot as plt

# 1. Definición de la señal de entrada (Mensaje)
fs = 10000        # Frecuencia de muestreo
t = np.linspace(0, 1, fs) # 1 segundo de duración
f_m = 50          # Frecuencia del mensaje (50 Hz)
m = np.cos(2 * np.pi * f_m * t) # Señal de mensaje (cosenoidal)

# 2. Señal Portadora
f_c = 1000        # Frecuencia de la portadora (1000 Hz, mucho mayor que f_m)
c = np.cos(2 * np.pi * f_c * t)

# 3. Implementación de la Modulación AM
# Fórmula: s(t) = [1 + m_index * m(t)] * c(t)
m_index = 0.75    # Índice de modulación (0 < m_index <= 1)
s = (1 + m_index * m) * c

# 4. Introducir ruido y atenuación (Escenario con ruido)
ruido = np.random.normal(0, 0.2, len(t)) # Ruido gaussiano blanco
s_ruido = s + ruido                      # Señal afectada por ruido
s_atenuada = s * 0.5                     # Señal con atenuación

# --- Gráficos en el Dominio del Tiempo ---
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t[:500], m[:500], color='blue')
plt.title('1. Señal de Mensaje m(t)')
plt.ylabel('Amplitud')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t[:500], s[:500], color='red')
plt.title('2. Señal Modulada en Amplitud s(t)')
plt.ylabel('Amplitud')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t[:500], s_ruido[:500], color='green')
plt.title('3. Señal Modulada con Ruido y Distorsión')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)

plt.tight_layout()
plt.show()

# --- Análisis en el Dominio de la Frecuencia (FFT) ---
fft_s = np.fft.fft(s)
fft_freqs = np.fft.fftfreq(len(t), 1/fs)

plt.figure(figsize=(10, 4))
plt.plot(fft_freqs[:500], np.abs(fft_s)[:500] / len(t), color='purple')
plt.title('Espectro en Frecuencia de la Señal AM')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.grid(True)
plt.xlim(0, 1500)
plt.show()



