from manim import *


class IgnitionExtinctionCurve2(Scene):
    def construct(self):
        # Set up the axes
        axes = Axes(
            x_range=[0, 6.5, 1],
            y_range=[0, 6.5, 1],
            x_length=7,
            y_length=6,
            axis_config={"include_numbers": False}
        )

        x_axis_label = Tex("Inlet Temperature ($T_0$)").scale(0.75)
        y_axis_label = Tex("Reactor Temperature ($T$)").rotate(PI / 2).scale(0.75)

        x_axis_label.next_to(axes.coords_to_point(3.25, 0), DOWN * 3.0)
        y_axis_label.next_to(axes.coords_to_point(0, 3.25), LEFT * 3.2)

        points = [
            axes.coords_to_point(1, 1),        
            axes.coords_to_point(2, 5/4),      
            axes.coords_to_point(2, 3),        
            axes.coords_to_point(3, 1.5),      
            axes.coords_to_point(3, 2.4),      
            axes.coords_to_point(3, 13/4),     
            axes.coords_to_point(4, 7/4),      
            axes.coords_to_point(4, 15/7),     
            axes.coords_to_point(4, 3.5),      
            axes.coords_to_point(5, 2),        
            axes.coords_to_point(5, 15/4),     
            axes.coords_to_point(6, 4),        
        ]
        stable_upper = VMobject(color=RED).set_points_as_corners([points[i] for i in [2, 5, 8, 10, 11]])
        stable_lower = VMobject(color=BLUE).set_points_as_corners([points[i] for i in [0, 1, 3, 6, 9]])
        unstable = DashedVMobject(VMobject().set_points_as_corners([points[i] for i in [2, 4, 7, 9]]))

        arrows = [
            Arrow(points[2], points[1], buff=0.1, max_tip_length_to_length_ratio=0.1),
            Arrow(points[9], points[10], buff=0.1, max_tip_length_to_length_ratio=0.1),
        ]
        dots = [Dot(points[i - 1], radius=0.06) for i in range(1, 13)]

        labels = [
            Tex(r"$T_{s6}$").next_to(axes.coords_to_point(0, 6), LEFT).scale(0.65),
            Tex(r"$T_{s1}$").next_to(axes.coords_to_point(0, 1), LEFT).scale(0.65),
            Tex(r"$T_{o1}$").next_to(axes.coords_to_point(1, 0), DOWN).scale(0.65),
            Tex(r"$T_{o2}$").next_to(axes.coords_to_point(2, 0), DOWN).scale(0.65),
            Tex(r"$T_{o3}$").next_to(axes.coords_to_point(3, 0), DOWN).scale(0.65),
            Tex(r"$T_{o4}$").next_to(axes.coords_to_point(4, 0), DOWN).scale(0.65),
            Tex(r"$T_{o5}$").next_to(axes.coords_to_point(5, 0), DOWN).scale(0.65),
            Tex(r"$T_{o6}$").next_to(axes.coords_to_point(6, 0), DOWN).scale(0.65),
        ]

        lower_steady_numbers = [
            Tex("10").next_to(points[9], DOWN).scale(0.5),
            Tex("7").next_to(points[6], DOWN).scale(0.5),
            Tex("4").next_to(points[3], DOWN).scale(0.5),
            Tex("2").next_to(points[1], DOWN).scale(0.5),
            Tex("1").next_to(points[0], DOWN).scale(0.5),
        ]
        unstable_numbers = [
            Tex("5").next_to(points[4], 0.01*DOWN).scale(0.5),
            Tex("8").next_to(points[7], 0.01*DOWN).scale(0.5),
        ]
        upper_steady_numbers = [
            Tex("3").next_to(points[2], UP).scale(0.5),
            Tex("6").next_to(points[5], UP).scale(0.5),
            Tex("9").next_to(points[8], UP).scale(0.5),
            Tex("11").next_to(points[10], UP).scale(0.5),
            Tex("12").next_to(points[11], UP).scale(0.5),
        ]

        plot_group = VGroup(
            axes, x_axis_label, y_axis_label,
            stable_upper, stable_lower, unstable,
            *dots, *arrows, *labels,
            *lower_steady_numbers, *unstable_numbers, *upper_steady_numbers
        )
        plot_group.shift(UP * 0.6)

        self.play(Create(axes))
        self.play(Write(x_axis_label), Write(y_axis_label))
        self.play(Create(stable_lower), run_time=2)
        self.wait(0.5)
        self.play(Create(unstable), run_time=1)
        self.wait(0.5)
        self.play(Create(stable_upper), run_time=2)
        self.wait(0.5)
        self.play(*[FadeIn(dot) for dot in dots])
        self.play(*[GrowArrow(arrow) for arrow in arrows])
        self.play(*[Write(label) for label in labels])
        self.play(*[Write(num) for num in lower_steady_numbers])
        self.play(*[Write(num) for num in upper_steady_numbers])
        self.play(*[Write(num) for num in unstable_numbers])

        legend_dot_upper = Line(LEFT * 0.3, RIGHT * 0.3, color=RED)
        legend_dot_lower = Line(LEFT * 0.3, RIGHT * 0.3, color=BLUE)
        legend_dot_unstable = DashedVMobject(Line(LEFT * 0.3, RIGHT * 0.3), color=WHITE)

        legend_label_upper = Tex("Upper steady states").scale(0.5).next_to(legend_dot_upper, RIGHT, buff=0.2)
        legend_label_lower = Tex("Lower steady states").scale(0.5).next_to(legend_dot_lower, RIGHT, buff=0.2)
        legend_label_unstable = Tex("Unstable steady states").scale(0.5).next_to(legend_dot_unstable, RIGHT, buff=0.2)

        legend = VGroup(
            VGroup(legend_dot_upper, legend_label_upper),
            VGroup(legend_dot_lower, legend_label_lower),
            VGroup(legend_dot_unstable, legend_label_unstable)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_corner(UR)

        self.play(FadeIn(legend))
        self.wait(2)
