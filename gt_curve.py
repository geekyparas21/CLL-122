from manim import *
import numpy as np


class GT(Scene):
    def construct(self):
        # Set up axes
        axes = Axes(
            x_range=[280, 480, 40],
            y_range=[0, 7500, 1000],
            x_length=10,
            y_length=6,
            tips=True,
            axis_config={"include_numbers": True, "font_size": 28}
        )


        # Custom axis labels
        x_label = Text("Inlet Temperature", font_size=24)
        y_label = Text("G(T)", font_size=28).rotate(PI/2)


        # Position labels
        x_label.next_to(axes.x_axis, DOWN)
        y_label.next_to(axes.y_axis, LEFT)


        # Group everything and shift upward to avoid clipping
        plot_group = VGroup(axes, x_label, y_label)
        plot_group.shift(UP * 0.05)


        self.play(Create(axes), Write(x_label), Write(y_label))


        # Define desmos-style exponential function
        def desmos_func(x):
            try:
                exp_term = np.exp((40000 / 1.987) * (1 / 350 - 1 / x))
                numerator = 7500 * 100 * 6.6e-3 * exp_term
                denominator = 1 + 100 * 6.6e-3 * exp_term
                return numerator / denominator
            except:
                return 0


        # Plot orange curve
        curve = axes.plot(
            desmos_func,
            color=RED,
            x_range=[310, 460]
        )
        self.play(Create(curve))


        self.wait(2)



