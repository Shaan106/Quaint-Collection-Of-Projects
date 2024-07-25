from manim import *

class NoisySineWave(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 30, 1], 
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
        self.play(Create(sine_wave), Write(sine_wave_label), run_time=4)
        self.wait(2)

class ConvolutionFormula(Scene):
    def construct(self):
        # Create the convolution formula using LaTeX
        convolution_formula = MathTex(
            r"(f * g)(t) = \int_{-\infty}^{\infty} f(\tau) \cdot g(t - \tau) \, d\tau"
        )

        # Set the size of the formula
        convolution_formula.scale(1.2)

        # Position the formula at the center
        # convolution_formula.move_to(ORIGIN)

        self.add(convolution_formula) # this adds a static formula

        # Display the formula
        # self.play(Write(convolution_formula))
        # self.wait(2)


class CustomPlot(Scene):
    def construct(self):
        # Set the background color
        self.camera.background_color = "#FED9BB"

        # Create axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": BLACK}
        )

        # Create curves
        curve_1 = axes.plot(lambda x: -x**3 + x, color=MAROON, x_range=[-2, 2])
        curve_2 = axes.plot(lambda x: np.sin(x), color=BLUE, x_range=[-3, 3])

        # Add points of interest
        point_1 = Dot(axes.coords_to_point(0, 0), color=ORANGE)
        point_2 = Dot(axes.coords_to_point(1, np.sin(1)), color=ORANGE)
        point_3 = Dot(axes.coords_to_point(-1, np.sin(-1)), color=ORANGE)

        # Add labels
        label_a = MathTex("a").next_to(axes.coords_to_point(1, np.sin(1)), UP, buff=0.1)
        label_b = MathTex("b").next_to(axes.coords_to_point(1, 0), RIGHT, buff=0.1)
        label_C = MathTex("C").next_to(axes.coords_to_point(2, np.sin(2)), RIGHT, buff=0.1)
        label_neg_C = MathTex("-C").next_to(axes.coords_to_point(-2, -2), LEFT, buff=0.1)
        label_x3_dot = MathTex(r"\dot{x}_3").next_to(axes.y_axis, UP, buff=0.1)
        label_x3 = MathTex("x_3").next_to(axes.x_axis, RIGHT, buff=0.1)

        # Add arrows
        arrow_a = Arrow(start=axes.coords_to_point(1, np.sin(1)), end=axes.coords_to_point(1, np.sin(1) + 1), buff=0, color=GREEN)
        arrow_b = Arrow(start=axes.coords_to_point(1, 0), end=axes.coords_to_point(2, 0), buff=0, color=GREEN)
        arrow_C = Arrow(start=axes.coords_to_point(2, np.sin(2)), end=axes.coords_to_point(2, np.sin(2) + 1), buff=0, color=BLUE)
        arrow_neg_C = Arrow(start=axes.coords_to_point(-2, -2), end=axes.coords_to_point(-2, -3), buff=0, color=MAROON)

        # Add elements to the scene
        self.add(axes)
        self.add(curve_1, curve_2)
        self.add(point_1, point_2, point_3)
        self.add(label_a, label_b, label_C, label_neg_C, label_x3_dot, label_x3)
        self.add(arrow_a, arrow_b, arrow_C, arrow_neg_C)


class CustomGraph(Scene):
    def construct(self):
        # Define the graph nodes and edges
        nodes = ["ADC", "FFT", "XCORR", "BBF", "SVM", "THR"]
        edges = [
            ("ADC", "FFT"), ("ADC", "XCORR"), ("ADC", "BBF"), 
            ("FFT", "SVM"), ("XCORR", "SVM"), ("BBF", "SVM"),
            ("SVM", "THR")
        ]

        # Create the graph
        graph = Graph(
            nodes,
            edges,
            layout="spectral",  # You can use different layouts
            vertex_config={"radius": 0.2, "color": WHITE, "fill_color": BLUE},
            edge_config={"color": GREY}
        )

        # Position the labels on the nodes
        for node in nodes:
            graph[node].scale(0.7)
            graph[node].set_color(WHITE)
        
        # Add the graph to the scene
        self.play(Create(graph))
        self.wait(2)

class SineCurveUnitCircle(Scene):
    # contributed by heejin_park, https://infograph.tistory.com/230
    def construct(self):
        self.show_axis()
        self.show_circle()
        self.move_dot_and_draw_curve()
        self.wait()

    def show_axis(self):
        x_start = np.array([-6,0,0])
        x_end = np.array([6,0,0])

        y_start = np.array([-4,-2,0])
        y_end = np.array([-4,2,0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)
        self.add_x_labels()

        self.origin_point = np.array([-4,0,0])
        self.curve_start = np.array([-3,0,0])

    def add_x_labels(self):
        x_labels = [
            MathTex("\pi"), MathTex("2 \pi"),
            MathTex("3 \pi"), MathTex("4 \pi"),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-1 + 2*i, 0, 0]), DOWN)
            self.add(x_labels[i])

    def show_circle(self):
        circle = Circle(radius=1)
        circle.move_to(self.origin_point)
        self.add(circle)
        self.circle = circle

    def move_dot_and_draw_curve(self):
        orbit = self.circle
        origin_point = self.origin_point

        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            # print(self.t_offset)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle():
            return Line(origin_point, dot.get_center(), color=BLUE)

        def get_line_to_curve():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )


        self.curve = VGroup()
        self.curve.add(Line(self.curve_start,self.curve_start))
        def get_curve():
            last_line = self.curve[-1]
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D)
            self.curve.add(new_line)

            return self.curve

        dot.add_updater(go_around_circle)

        origin_to_circle_line = always_redraw(get_line_to_circle)
        dot_to_curve_line = always_redraw(get_line_to_curve)
        sine_curve_line = always_redraw(get_curve)

        self.add(dot)
        self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line)
        self.wait(8.5)

        dot.remove_updater(go_around_circle)