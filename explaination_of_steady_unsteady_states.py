from manim import *
import numpy as np

class DesmosStyledPlotWithLabels(MovingCameraScene):
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
        x_label = Text("Reactor Temperature", font_size=24)
        y_label = Text("R(T), G(T)", font_size=28).rotate(PI/2)

        x_label.next_to(axes.x_axis, DOWN)
        y_label.next_to(axes.y_axis, LEFT)

        plot_group = VGroup(axes, x_label, y_label)
        plot_group.shift(UP * 0.05)
        
        self.play(Create(axes), Write(x_label), Write(y_label))

        def desmos_func(x):
            try:
                exp_term = np.exp((40000 / 1.987) * (1 / 350 - 1 / x))
                numerator = 7500 * 100 * 6.6e-3 * exp_term
                denominator = 1 + 100 * 6.6e-3 * exp_term
                return numerator / denominator
            except:
                return 0
        curve = axes.plot(
            desmos_func,
            color=RED,
            x_range=[280, 460]
        )
        self.play(Create(curve))

        a_values = [400]
        line_colors = [BLUE]

        for a, color in zip(a_values, line_colors):
            def line_func(x, a=a):
                return 150 * (x - ((a + 600) / 3))
            line = axes.plot(
                line_func,
                color=color,
                x_range=[(a+600)/3, 60+((a+600)/3)]  
            )
            self.play(Create(line), run_time=0.3)
        points = [
            (382.79, 7418.52),
            (336.33, 449.0),
            (345.99, 1898.88),
        ]
        for x, y in points:
            dot = Dot(axes.c2p(x, y), radius=0.05, color=WHITE)
            self.play(FadeIn(dot), run_time=0.1)
       
        namesforpoints = [
            Tex(r"$5$").next_to(axes.coords_to_point(*points[1]), UP*(0.05)+(0.05)*LEFT).scale(0.75),
            Tex(r"$6$").next_to(axes.coords_to_point(*points[2]), UP*(0.05)+(0.05)*LEFT).scale(0.75),
            Tex(r"$7$").next_to(axes.coords_to_point(*points[0]), UP*(0.05)+(0.05)*LEFT).scale(0.75),
        ]
        self.play(*[Write(num) for num in namesforpoints])

        dotted_lines = []
        x_labels = [r"$T_{s5}$", r"$T_{s6}$", r"$T_{s7}$"]
        x_coords = [points[1][0], points[2][0], points[0][0]]  


        for x, label in zip(x_coords, x_labels):
            top_y = line_func(x,400)
            line = DashedLine(
                start=axes.c2p(x, top_y),
                end=axes.c2p(x, 0),
                color=WHITE,
                stroke_width=1.5,
                dash_length=0.15
            )
            dotted_lines.append(line)

            x_label = Tex(label).scale(0.55)
            x_label.next_to(axes.c2p(x, 0), DOWN, buff=0.2)
            self.add(x_label)


        self.play(*[Create(line) for line in dotted_lines], run_time=1)

        rect_data = [
            (280, 336.33, RED),
            (336.33, 345.99, BLUE),
            (345.99, 382.79, RED),
            (382.79, 480, BLUE)
        ]
        rectangles = []
        for x_start, x_end, color in rect_data:
            width = axes.c2p(x_end, 0)[0] - axes.c2p(x_start, 0)[0]
            height = axes.c2p(0, 7500)[1] - axes.c2p(0, 0)[1] + 100
            rect = Rectangle(
                width=width,
                height=height,
                fill_color=color,
                fill_opacity=0.3,
                stroke_width=0
            )
            rect.move_to(axes.c2p((x_start + x_end) / 2, 7500 / 2))
            rectangles.append(rect)

        self.play(*[FadeIn(r) for r in rectangles], run_time=1)
       
        legend_blue = Rectangle(width=0.4, height=0.4, fill_color=BLUE, fill_opacity=0.6, stroke_width=0)
        legend_red = Rectangle(width=0.4, height=0.4, fill_color=RED, fill_opacity=0.6, stroke_width=0)

        label_blue = Text("R > G", font_size=24)
        label_red = Text("G > R", font_size=24)
        legend_item_blue = VGroup(legend_blue, label_blue).arrange(RIGHT*(1.05), buff=0.2)
        legend_item_red = VGroup(legend_red, label_red).arrange(RIGHT*(1.05), buff=0.2)
        legend = VGroup(legend_item_blue, legend_item_red).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        legend.to_corner(UR).shift(LEFT * 0.5 + DOWN * 0.5)  # top-right corner

        self.play(FadeIn(legend))

        point7_pos = axes.c2p(*points[0])
        self.play(
            self.camera.frame.animate.move_to(point7_pos+RIGHT*(1)).set(width=4),
            run_time=1.5
        )
        self.wait(10)

        self.play(
            self.camera.frame.animate.move_to(ORIGIN).set(width=14),
            run_time=1.5
        )

        point6_pos = axes.c2p(*points[2])
        self.play(
            self.camera.frame.animate.move_to(point6_pos+RIGHT*(1)).set(width=4),
            run_time=1.5
        )
        self.wait(10)
        
        self.play(
            self.camera.frame.animate.move_to(ORIGIN).set(width=14),
            run_time=1.5
        )

        self.play(*[FadeOut(r) for r in rectangles], run_time=1)

        self.wait(2)
