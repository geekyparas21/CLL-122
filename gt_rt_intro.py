from manim import *


class HeatBalanceDerivation(Scene):
    def construct(self):
        top = ORIGIN + UP * 3.3


        eq_854 = MathTex(r"-X \Delta H_{R_x} = C_{p0}(1 + \kappa)(T - T_c)").scale(0.7).move_to(top)
        self.play(Write(eq_854))
        self.wait(0.5)


        cp0_def = MathTex(r"C_{p0} = \sum \Theta_i C_{p,i}").scale(0.65).next_to(eq_854, DOWN, buff=0.8)
        self.play(Write(cp0_def))
        self.wait(0.5)


        kappa_def = MathTex(r"\kappa = \frac{UA}{C_{p0} F_{A0}}").scale(0.65).next_to(cp0_def, DOWN, buff=0.6)
        self.play(Write(kappa_def))
        self.wait(0.5)


        tc_eq = MathTex(
            r"T_c = \frac{T_0 F_{A0} C_{p0} + UA T_a}{UA + C_{p0} F_{A0}} = \frac{\kappa T_a + T_0}{1 + \kappa}"
        ).scale(0.65).next_to(kappa_def, DOWN, buff=0.8)
        self.play(Write(tc_eq))
        self.wait(0.7)


        eq_858 = MathTex(
            r"(-r_A V / F_{A0})(-\Delta H_{R_x}) = C_{p0}(1 + \kappa)(T - T_c)"
        ).scale(0.7).next_to(tc_eq, DOWN, buff=0.8)
        self.play(Write(eq_858))
        self.wait(0.8)


        g_of_t = MathTex(
            r"G(T) = (-\Delta H_{R_x})(-r_A V / F_{A0})"
        ).scale(0.7).next_to(eq_858, DOWN, buff=0.8)
        self.play(Write(g_of_t))
        self.wait(0.5)


        box = Rectangle(width=g_of_t.width + 0.4, height=g_of_t.height + 0.2, color=YELLOW, stroke_width=4)
        box.move_to(g_of_t)
        self.play(Create(box))


        r_of_t = MathTex(
            r"R(T) = C_{p0}(1 + \kappa)(T - T_c)"
        ).scale(0.7).next_to(g_of_t, DOWN, buff=0.6)
        self.play(Write(r_of_t))
        self.wait(2)





