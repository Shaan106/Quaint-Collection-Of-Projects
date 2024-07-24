from manim import *

class NoisySineWave(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 10, 1], 
            y_range=[-3, 3, 1], 
            axis_config={"color": BLUE}
        )
        
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        sine_wave = axes.plot(
            lambda x: np.sin(x) + np.random.uniform(-0.5, 0.5), 
            color=YELLOW
        )

        sine_wave_label = axes.get_graph_label(
            sine_wave, 
            label="f(x) = sin(x) + noise",
            direction=UP,
            color=RED
        )
        sine_wave_label.scale(0.7)  # Make the label smaller

        self.play(Create(axes), Write(axes_labels))
        self.play(Create(sine_wave), Write(sine_wave_label))
        self.wait(2)

if __name__ == "__main__":
    from manim import config
    config.quality = "production"  # Increase video resolution
    scene = NoisySineWave()
    scene.render()