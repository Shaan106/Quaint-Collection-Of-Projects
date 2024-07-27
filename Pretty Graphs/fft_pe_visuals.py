from manim import *
import numpy as np

class SineWaveAndFFT(Scene):
    def construct(self):
        # Step 1: Create the sine waves
        sampling_rate = 1000  # samples per second
        T = 1.0 / sampling_rate  # sample interval
        t = np.linspace(0.0, 1.0, sampling_rate)  # time vector

        # Frequencies and amplitudes of the sine waves
        frequencies = [14, 50, 120]  # Hz
        amplitudes = [6/4, 1, 2]  # Amplitudes

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

        # Create the axes for the noisy sine wave plot
        axes1 = Axes(
            x_range=[0, 1, 0.2],
            y_range=[-10, 10, 5],
            axis_config={"color": BLUE},
            x_axis_config={"label_direction": DOWN},
            y_axis_config={"label_direction": LEFT},
        )

        # Create the graph for the noisy sine wave
        graph1 = axes1.plot_line_graph(
            x_values=t,
            y_values=noisy_sine_wave,
            line_color=RED,
            add_vertex_dots=False
        )

        # Create labels for the first plot
        labels1 = axes1.get_axis_labels(x_label="Time [s]", y_label="Amplitude")
        title1 = Text("Noisy Sine Wave").next_to(axes1, UP)

        # Create the axes for the FFT plot
        axes2 = Axes(
            x_range=[0, 150, 50],
            y_range=[0, 1000, 250],
            axis_config={"color": BLUE},
            x_axis_config={"label_direction": DOWN},
            y_axis_config={"label_direction": LEFT},
        )

        # Create the graph for the FFT
        graph2 = axes2.plot_line_graph(
            x_values=positive_fft_freq,
            y_values=positive_fft_result,
            line_color=GREEN,
            add_vertex_dots=False
        )

        # Create labels for the second plot
        labels2 = axes2.get_axis_labels(x_label="Frequency [Hz]", y_label="Amplitude")
        title2 = Text("FFT of Noisy Sine Wave (Positive Frequencies)").next_to(axes2, UP)

        # Group the elements for each plot
        plot1 = VGroup(axes1, graph1, labels1, title1)
        plot2 = VGroup(axes2, graph2, labels2, title2)

        # Arrange the plots vertically
        plots = VGroup(plot1, plot2).arrange(DOWN, buff=1)

        # Scale down the entire group to fit the scene
        plots.scale(0.3)

        # Add the plots to the scene
        self.play(Create(plots))
        self.wait(2)