from manim import *


class ReactorAssumptions(Scene):
    def construct(self):
        title = MathTex(r"\text{Reactor Assumptions}", font_size=48)
        title.to_corner(UR)
        self.play(Write(title))
        self.wait(0.5)


        assumptions = [
            r"\bullet~\text{Non-isothermal}",
            r"\bullet~\text{Jacketed CSTR}",
            r"\bullet~\text{First-order reaction}",
            r"\bullet~\text{Irreversible}",
            r"\bullet~\text{Exothermic}",
            r"\bullet~\text{Liquid-phase reaction}"
        ]


        for i, item in enumerate(assumptions):
            assumption_tex = MathTex(item, font_size=32)
            assumption_tex.to_corner(UR)
            assumption_tex.shift(DOWN * ((i + 1) * 0.7)) 
            self.play(Write(assumption_tex))
            self.wait(0.4)




