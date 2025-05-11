from manim import *


from manim import *


class CSTRHeatBalanceScene(Scene):
    def construct(self):
        title = Tex("Energy Balance and Conversion in a CSTR").scale(0.8).to_edge(UP)


        eq1 = MathTex(
            r"\frac{UA}{F_{A0}}(T_a - T) - \sum \Theta_i C_{p,i}(T - T_0) - \Delta H_{R_x} X = 0"
        ).scale(0.7).next_to(title, DOWN, buff=0.5)


        solving_for_x = Tex("Solving for ", "$X$").scale(0.7).next_to(eq1, DOWN, aligned_edge=LEFT, buff=0.4)


        eq2 = MathTex(
            r"X = \frac{\frac{UA}{F_{A0}}(T - T_a) + \sum \Theta_i C_{p,i}(T - T_0)}{-\Delta H_{R_x}(T)}"
        ).scale(0.7).next_to(solving_for_x, DOWN, aligned_edge=LEFT)


        mole_balance = Tex("Equation is coupled with the mole balance:").scale(0.7).next_to(eq2, DOWN, aligned_edge=LEFT, buff=0.4)


        eq3 = MathTex(
            r"V = \frac{F_{A0}X}{-r_A(X, T)}"
        ).scale(0.7).next_to(mole_balance, DOWN, aligned_edge=LEFT)


        rearranging = Tex("Rewriting after letting ", r"$\sum \Theta_i C_{p,i} = C_{p0}$").scale(0.7).next_to(eq3, DOWN, aligned_edge=LEFT, buff=0.4)


        eq4 = MathTex(
            r"C_{p0} \left( \frac{UA}{F_{A0} C_{p0}} \right) T_a + C_{p0} T_0 - C_{p0} \left( \frac{UA}{F_{A0} C_{p0}} \right) T + T - \Delta H_{R_x} X = 0"
        ).scale(0.6).next_to(rearranging, DOWN, aligned_edge=LEFT)


        let_def = Tex("Let ", r"$\kappa = \frac{UA}{F_{A0}C_{p0}}$", " and ", r"$T_c = \frac{\kappa T_a + T_0}{1 + \kappa}$").scale(0.7).next_to(eq4, DOWN, aligned_edge=LEFT, buff=0.4)


        eq5 = MathTex(
            r"-X \Delta H_{R_x} = C_{p0}(1 + \kappa)(T - T_c)"
        ).scale(0.7).next_to(let_def, DOWN, aligned_edge=LEFT)


        x_eq = Tex("Solving for conversion ").scale(0.7).next_to(eq5, DOWN, aligned_edge=LEFT, buff=0.4)


        eq6 = MathTex(
            r"X = \frac{C_{p0}(1 + \kappa)(T - T_c)}{-\Delta H_{R_x}}"
        ).scale(0.7).next_to(x_eq, DOWN, aligned_edge=LEFT)


        t_eq = Tex("Solving for temperature ").scale(0.7).next_to(eq6, DOWN, aligned_edge=LEFT, buff=0.4)


        eq7 = MathTex(
            r"T = T_c + \frac{-\Delta H_{R_x} X}{C_{p0}(1 + \kappa)}"
        ).scale(0.7).next_to(t_eq, DOWN, aligned_edge=LEFT)


        self.play(Write(title))
        for mobj in [
            eq1, solving_for_x, eq2,
            mole_balance, eq3,
            rearranging, eq4,
            let_def, eq5,
            x_eq, eq6,
            t_eq, eq7
        ]:
            self.play(Write(mobj))
            self.wait(0.4)






class CSTRHeatBalanceContinuedScene(Scene):
    def construct(self):
        title = Tex("CSTR Energy Balance Continued").scale(0.8).to_edge(UP)


        rearranged = MathTex(
            r"C_{p0}\left(\frac{UA}{F_{A0}C_{p0}}\right)T_a + C_{p0}T_0 - "
            r"C_{p0}\left(\frac{UA}{F_{A0}C_{p0}} + 1\right)T - \Delta H_{R_x} X = 0"
        ).scale(0.6).next_to(title, DOWN, buff=0.7)
        self.play(Write(rearranged))
        self.wait(1)


        let_eqs = MathTex(
            r"\kappa = \frac{UA}{F_{A0}C_{p0}}, \quad T_c = \frac{\kappa T_a + T_0}{1 + \kappa}"
        ).scale(0.65).next_to(rearranged, DOWN, buff=1)
        self.play(Write(let_eqs))
        self.wait(1)


        eq_kappa = MathTex(
            r"-X \Delta H_{R_x} = C_{p0}(1 + \kappa)(T - T_c)"
        ).scale(0.7).next_to(let_eqs, DOWN, buff=0.8)
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



