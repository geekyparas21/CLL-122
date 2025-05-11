from manim import *


class CSTRHeatBalanceContinuedScene(Scene):
    def construct(self):
         top_anchor = ORIGIN + UP * 3.3  
        rearranged = MathTex(
            r"C_{p0}\left(\frac{UA}{F_{A0}C_{p0}}\right)T_a + C_{p0}T_0 - "
            r"C_{p0}\left(\frac{UA}{F_{A0}C_{p0}} + 1\right)T - \Delta H_{R_x} X = 0"
        ).scale(0.6).move_to(top_anchor)
        self.play(Write(rearranged))
        self.wait(1)


       
        let_eqs = MathTex(
            r"\kappa = \frac{UA}{F_{A0}C_{p0}}, \quad T_c = \frac{\kappa T_a + T_0}{1 + \kappa}"
        ).scale(0.65).next_to(rearranged, DOWN, buff=0.6)
        self.play(Write(let_eqs))
        self.wait(1)


        eq_kappa = MathTex(
            r"-X \Delta H_{R_x} = C_{p0}(1 + \kappa)(T - T_c)"
        ).scale(0.7).next_to(let_eqs, DOWN, buff=0.6)
        self.play(Write(eq_kappa))
        self.wait(1)


        conv_eq = MathTex(
            r"X = \frac{C_{p0}(1 + \kappa)(T - T_c)}{-\Delta H_{R_x}}"
        ).scale(0.7).next_to(eq_kappa, DOWN, buff=0.6)
        self.play(Write(conv_eq))


        temp_eq = MathTex(
            r"T = T_c + \frac{-\Delta H_{R_x} X}{C_{p0}(1 + \kappa)}"
        ).scale(0.7).next_to(conv_eq, DOWN, buff=0.6)
        self.play(Write(temp_eq))
        self.wait(2)



