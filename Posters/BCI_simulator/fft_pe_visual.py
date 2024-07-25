import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create the sine waves
sampling_rate = 1000 # samples per second
T = 1.0 / sampling_rate # sample interval
t = np.linspace(0.0, 1.0, sampling_rate) # time vector

# Frequencies and amplitudes of the sine waves
frequencies = [14, 50, 120] # Hz
amplitudes = [6/4, 1, 2] # Amplitudes

# Create the original signal with three sine waves
sine_wave = np.zeros_like(t)
for frequency, amplitude in zip(frequencies, amplitudes):
    sine_wave += amplitude * np.sin(2 * np.pi * frequency * t)

# Step 2: Add noise to the sine wave
noise = np.random.normal(0, 0.5, sine_wave.shape)
noisy_sine_wave = sine_wave + noise

# Step 3: Apply FFT to the noisy sine wave
fft_result = np.fft.fft(noisy_sine_wave)
fft_freq = np.fft.fftfreq(sampling_rate, T)

# Get the positive half of the frequencies
positive_freq_indices = np.where(fft_freq >= 0)
positive_fft_freq = fft_freq[positive_freq_indices]
positive_fft_result = np.abs(fft_result[positive_freq_indices])

# Set up the plot style
plt.style.use('default')
plt.rcParams['figure.facecolor'] = 'none'
plt.rcParams['axes.facecolor'] = 'none'
plt.rcParams['savefig.facecolor'] = 'none'

# Create a color palette
orange = '#FF8C00'
black = '#000000'

# Plot the noisy sine wave
fig1, ax1 = plt.subplots(figsize=(10, 4), dpi=300)
ax1.plot(t, noisy_sine_wave, color=orange, linewidth=1.5)
ax1.tick_params(axis='both', which='major', labelsize=10, colors=black)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_color(black)
ax1.spines['left'].set_color(black)
ax1.set_xticks([])
ax1.set_yticks([])

plt.tight_layout()
plt.savefig('noisy_sine_wave.png', dpi=300, bbox_inches='tight', transparent=True)
plt.close(fig1)

# Plot the FFT result (positive frequencies only)
fig2, ax2 = plt.subplots(figsize=(10, 4), dpi=300)
ax2.plot(positive_fft_freq, positive_fft_result, color=orange, linewidth=1.5)
ax2.tick_params(axis='both', which='major', labelsize=10, colors=black)
ax2.set_xlim(0, 150)  # Limit x-axis to show relevant frequency range
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['bottom'].set_color(black)
ax2.spines['left'].set_color(black)
ax2.set_xticks([])
ax2.set_yticks([])

plt.tight_layout()
plt.savefig('fft_result.png', dpi=300, bbox_inches='tight', transparent=True)
plt.close(fig2)