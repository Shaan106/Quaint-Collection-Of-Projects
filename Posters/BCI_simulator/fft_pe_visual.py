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

# Increased linewidth for thicker stroke
linewidth = 3.0

# Plot the noisy sine wave
fig1, ax1 = plt.subplots(figsize=(10, 4), dpi=300)
ax1.plot(t, noisy_sine_wave, color=orange, linewidth=linewidth)
ax1.tick_params(axis='both', which='major', labelsize=10, colors=black)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_color(black)
ax1.spines['left'].set_color(black)
ax1.spines['bottom'].set_linewidth(linewidth)
ax1.spines['left'].set_linewidth(linewidth)
ax1.set_xticks([])
ax1.set_yticks([])

plt.tight_layout()
plt.savefig('noisy_sine_wave.png', dpi=300, bbox_inches='tight', transparent=True)
plt.close(fig1)

# Plot the FFT result (positive frequencies only)
fig2, ax2 = plt.subplots(figsize=(10, 4), dpi=300)
ax2.plot(positive_fft_freq, positive_fft_result, color=orange, linewidth=linewidth)
ax2.tick_params(axis='both', which='major', labelsize=10, colors=black)
ax2.set_xlim(0, 150)  # Limit x-axis to show relevant frequency range
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['bottom'].set_color(black)
ax2.spines['left'].set_color(black)
ax2.spines['bottom'].set_linewidth(linewidth)
ax2.spines['left'].set_linewidth(linewidth)
ax2.set_xticks([])
ax2.set_yticks([])

plt.tight_layout()
plt.savefig('fft_result.png', dpi=300, bbox_inches='tight', transparent=True)
plt.close(fig2)

import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create the sine waves (same as before)
sampling_rate = 1000
T = 1.0 / sampling_rate
t = np.linspace(0.0, 1.0, sampling_rate)

frequencies = [14, 50, 120]
amplitudes = [6/4, 1, 2]

sine_wave = np.zeros_like(t)
for frequency, amplitude in zip(frequencies, amplitudes):
    sine_wave += amplitude * np.sin(2 * np.pi * frequency * t)

noise = np.random.normal(0, 0.5, sine_wave.shape)
noisy_sine_wave = sine_wave + noise

# Step 2: Apply FFT (same as before)
fft_result = np.fft.fft(noisy_sine_wave)
fft_freq = np.fft.fftfreq(sampling_rate, T)

positive_freq_indices = np.where(fft_freq >= 0)
positive_fft_freq = fft_freq[positive_freq_indices]
positive_fft_result = np.abs(fft_result[positive_freq_indices])

# Step 3: Calculate power in Berger bands
berger_bands = [(0.1, 4), (4, 8), (8, 12), (12, 30), (30, 80), (80, 180)]
band_powers = []

for low, high in berger_bands:
    band_indices = np.where((positive_fft_freq >= low) & (positive_fft_freq < high))
    band_magnitudes = positive_fft_result[band_indices]
    band_power = np.sum(band_magnitudes**2)  # Using squared magnitude for power
    band_powers.append(band_power)

# Plotting settings
plt.style.use('default')
plt.rcParams['figure.facecolor'] = 'none'
plt.rcParams['axes.facecolor'] = 'none'
plt.rcParams['savefig.facecolor'] = 'none'

orange = '#FF8C00'
black = '#000000'
linewidth = 3.0

# Create bar plot of Berger band powers
fig, ax = plt.subplots(figsize=(10, 4), dpi=300)

band_names = ['Delta', 'Theta', 'Alpha', 'Beta', 'Gamma', 'High Gamma']
x_pos = np.arange(len(band_names))

ax.bar(x_pos, band_powers, color=orange, edgecolor='none')  # Removed black edge

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color(black)
ax.spines['left'].set_color(black)
ax.spines['bottom'].set_linewidth(linewidth)
ax.spines['left'].set_linewidth(linewidth)

ax.set_xticks([])
ax.set_yticks([])

plt.tight_layout()
plt.savefig('berger_band_powers.png', dpi=300, bbox_inches='tight', transparent=True)
plt.close()


# --------------------- power
import numpy as np
import matplotlib.pyplot as plt

# Generate data
x_points = [1024, 2048, 4096, 8192]
max_power = 100  # Maximum power value
rate = 0.0005  # Rate of approach to the asymptote

# Calculate y values (power) using an exponential approach to the asymptote
y_values = max_power * (1 - np.exp(-rate * np.array(x_points)))

# Plotting settings
plt.style.use('default')
plt.rcParams['figure.facecolor'] = 'none'
plt.rcParams['axes.facecolor'] = 'none'
plt.rcParams['savefig.facecolor'] = 'none'

orange = '#FF8C00'
black = '#000000'
linewidth = 3.0

# Create bar plot
fig, ax = plt.subplots(figsize=(10, 4), dpi=300)

ax.bar(range(len(x_points)), y_values, color=orange, edgecolor='none')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color(black)
ax.spines['left'].set_color(black)
ax.spines['bottom'].set_linewidth(linewidth)
ax.spines['left'].set_linewidth(linewidth)

ax.set_xticks([])
ax.set_yticks([])

plt.tight_layout()
plt.savefig('asymptotic_power_plot.png', dpi=300, bbox_inches='tight', transparent=True)
plt.close()