from manim import *


class FirstOrderConversionScene(Scene):
    def construct(self):
        top_anchor = ORIGIN + UP * 3.2


        rate_law = MathTex(r"-r_A = k C_A").scale(0.8).move_to(top_anchor)
        self.play(Write(rate_law))
        self.wait(0.7)


        conc_eq = MathTex(r"C_A = C_{A0}(1 - X)").scale(0.8).next_to(rate_law, DOWN, buff=0.8)
        self.play(Write(conc_eq))
        self.wait(0.7)


        tau_def = MathTex(r"\tau = \frac{1}{k} \left( \frac{X}{1 - X} \right)").scale(0.8).next_to(conc_eq, DOWN, buff=0.8)
        self.play(Write(tau_def))
        self.wait(0.7)


        x_eq = MathTex(r"X = \frac{\tau k}{1 + \tau k}").scale(0.8).next_to(tau_def, DOWN, buff=0.8)
        self.play(Write(x_eq))
        self.wait(2)





