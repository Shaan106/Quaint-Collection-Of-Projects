import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create the sine waves
sampling_rate = 1000 # samples per second
T = 1.0 / sampling_rate # sample interval
t = np.linspace(0.0, 1.0, sampling_rate) # time vector

berger_bands = [(0.1, 4), (4, 8), (8, 12), (12, 30), (30, 80), (80, 180)]

# Frequencies and amplitudes of the sine waves
frequencies = [2,  7,  15, 61,  120]
amplitudes = [0.8, 0.4, 1, 1.4, 0.9] # Amplitudes

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

# ---- latency vs power
import numpy as np
import matplotlib.pyplot as plt

# Generate data
x_points = [1024, 2048, 4096, 8192]
min_latency = 100   # Minimum latency value
max_latency = 20  # Maximum latency value

# Calculate y values (latency) decreasing linearly
y_values = np.linspace(max_latency, min_latency, len(x_points))

# Invert y_values so that bars grow upwards as points increase
y_values = max_latency - y_values + min_latency

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

# Remove tick marks
ax.set_xticks([])
ax.set_yticks([])

# Add axis labels
# ax.set_xlabel("", fontsize=12, color=black, labelpad=10)
# ax.set_ylabel("", fontsize=12, color=black, labelpad=10)

plt.tight_layout()
plt.savefig('latency_vs_points.png', dpi=300, bbox_inches='tight', transparent=True)
plt.close()


# -- 3d ---
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate data
x = np.linspace(0, 10, 50)
z = np.linspace(0, 10, 50)
X, Z = np.meshgrid(x, z)

# Calculate performance (example function)
# simple
# Y = np.sin(X) * np.cos(Z) + 0.2 * (X - 5)**2 + 0.2 * (Z - 5)**2

# complex
# Y = (np.sin(X*-2.5) * np.cos(Z*1.5) + 
#      30 * np.exp(-((X-3)**2 + (Z-3)**2)/3) + 
#      20 * np.exp(-((X-7)**2 + (Z-7)**2)/3) +
#      15 * np.exp(-((X-5)**2 + (Z-8)**2)/3))

def three_peak_function(x, z):
    peak1 = 3 * np.exp(-((x-4)**2 + (z-2)**2)/2)
    peak2 = 4 * np.exp(-((x-1)**2 + (z-7)**2)/3)
    peak3 = 3.5 * np.exp(-((x-8)**2 + (z-4)**2)/2.5)
    peak3 = 0
    noise = 0.1 *(np.sin(X*2.5) * np.cos(Z*1.5))
    return peak1 + peak2 + peak3 + noise

# Y = three_peak_function(X, Z)

Y = np.sin(X) * np.cos(Z) + 0.2 * (X - 5)**2 + 0.2 * (Z - 5)**2

# Plotting settings
plt.style.use('default')
plt.rcParams['figure.facecolor'] = 'none'
plt.rcParams['axes.facecolor'] = 'none'
plt.rcParams['savefig.facecolor'] = 'none'

orange = '#FF8C00'
black = '#000000'
linewidth = 2.0

# Create 3D surface plot
fig = plt.figure(figsize=(10, 8), dpi=300)
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(X, Z, Y, cmap='YlOrRd', edgecolor='none', alpha=0.8)

# Customize the plot
# ax.set_xlabel('Parameter 1', fontsize=12, color=black, labelpad=10)
# ax.set_ylabel('Parameter 2', fontsize=12, color=black, labelpad=10)
# ax.set_zlabel('Performance', fontsize=12, color=black, labelpad=10)

# Remove tick labels
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])

# Set edge color
ax.xaxis.line.set_color(black)
ax.yaxis.line.set_color(black)
ax.zaxis.line.set_color(black)

# Set edge linewidth
ax.xaxis.line.set_linewidth(linewidth)
ax.yaxis.line.set_linewidth(linewidth)
ax.zaxis.line.set_linewidth(linewidth)

# Remove background panes
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

# Remove grid lines
ax.grid(False)

# Adjust the view angle
ax.view_init(elev=30, azim=45)

plt.tight_layout()
plt.savefig('parameter_optimization_3d.png', dpi=300, bbox_inches='tight', transparent=True)
plt.close()