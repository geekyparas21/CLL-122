from manim import *


class HeatRemovedGraph(Scene):
    def construct(self):
        title = Title("Heat-Removed Term: R(T)")
        self.play(Write(title))
        self.wait(1)


        eq = MathTex(r"R(T) = C_{p0}(1 + \kappa)(T - T_c)")
        self.play(Write(eq))
        self.wait(1)


        self.play(eq.animate.to_edge(UP))


        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            x_length=7,
            y_length=5,
            axis_config={"include_tip": True},
            x_axis_config={"label_direction": DOWN},
            y_axis_config={"label_direction": LEFT},
        ).to_edge(DOWN)


        axes_labels = axes.get_axis_labels(x_label="T", y_label="R(T)")
        self.play(Create(axes), Write(axes_labels))


        slope = 1.0  
        colors = [BLUE, GREEN, ORANGE, RED]
        lines = VGroup()


        for i, shift in enumerate([1, 2, 3, 4]):
            line = axes.plot(lambda T: slope * (T - shift), x_range=[shift, 10], color=colors[i])
            lines.add(line)


        self.play(*[Create(line) for line in lines])
        self.wait(1)


        arrow = Arrow(start=axes.c2p(5, 7), end=axes.c2p(7, 7), buff=0.1, color=YELLOW)
        label = Text("Increase $T_0$", font_size=24).next_to(arrow, UP)


        self.play(GrowArrow(arrow), Write(label))
        self.wait(2)



