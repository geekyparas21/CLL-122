from manim import *


class StableEquilibrium(Scene):
    def construct(self):
        parabola = FunctionGraph(
            lambda x: 0.25 * x**2 - 1,
            x_range=[-4, 4],
            color=BLUE
        )
        self.play(Create(parabola))


        ball = Dot(point=[0, -1, 0], radius=0.12, color=YELLOW)
        self.play(FadeIn(ball))


        right_path = VMobject()
        right_path.set_points_as_corners([
            np.array([0, -1, 0]),
            np.array([0.5, 0.25 * 0.5**2 - 1, 0]),
            np.array([1, 0.25 * 1**2 - 1, 0]),
            np.array([1.5, 0.25 * 1.5**2 - 1, 0]),
            np.array([2, 0.25 * 2**2 - 1, 0]),
        ])


        self.play(MoveAlongPath(ball, right_path), run_time=2.5)
        self.play(MoveAlongPath(ball, right_path.copy().reverse_direction()), run_time=2.5)


        left_path = VMobject()
        left_path.set_points_as_corners([
            np.array([0, -1, 0]),
            np.array([-0.5, 0.25 * 0.5**2 - 1, 0]),
            np.array([-1, 0.25 * 1**2 - 1, 0]),
            np.array([-1.5, 0.25 * 1.5**2 - 1, 0]),
            np.array([-2, 0.25 * 2**2 - 1, 0]),
        ])


        self.play(MoveAlongPath(ball, left_path), run_time=2.5)
        self.play(MoveAlongPath(ball, left_path.copy().reverse_direction()), run_time=2.5)


        self.wait()



