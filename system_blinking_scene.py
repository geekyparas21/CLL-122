from manim import *


class SystemBlinking(Scene):
    def construct(self):
        rect = Rectangle(width=4, height=2, color=WHITE)
        label = Text("System", font_size=36).move_to(rect.get_center())


        group = VGroup(rect, label)
        self.play(FadeIn(group))


        for _ in range(2):
            self.play(rect.animate.set_color(RED), run_time=0.3)
            self.play(rect.animate.set_color(WHITE), run_time=0.3)


        for _ in range(2):
            self.play(rect.animate.set_color(BLUE), run_time=0.3)
            self.play(rect.animate.set_color(WHITE), run_time=0.3)


        self.wait(0.5)


        eq = MathTex("G(T) = R(T)").next_to(rect, DOWN, buff=0.75)
        self.play(Write(eq))


        self.wait()



