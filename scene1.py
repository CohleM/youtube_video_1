from cv2 import circle
from manim import *
import numpy as np
from tkinter import CENTER
from manim_ml.neural_network.layers import FeedForwardLayer
from manim_ml.neural_network.neural_network import NeuralNetwork

class OpeningManim(MovingCameraScene):
    def construct(self):

    #     m2 = MobjectMatrix(
    #         [ [MathTex("W_{0,0}"),MathTex("W_{0,1}"), " . .  " ,MathTex("W_{0,2}") ],
    #          [MathTex("W_{1,0}"),MathTex("W_{1,1}"), " . .  " ,MathTex("W_{1,2}") ],
    #         [MathTex("W_{2,0}"),MathTex("W_{2,1}"), " . .  ",MathTex("W_{2,2}") ] ]
    #    )


        # m3 = MobjectMatrix(
        #     [  [MathTex("W_{0,0}"), MathTex("W_{0,1}"), MathTex(". . ") , MathTex("W_{0,n}") ],
        #         [MathTex("W_{1,0}"), MathTex("W_{1,1}"), MathTex(". . ") , MathTex("W_{1,n}") ],
        #         [MathTex("."), MathTex("."), MathTex("."), MathTex(".")],
        #         [MathTex("."), MathTex("."), MathTex("."), MathTex(".")],
        #       [MathTex("W_{n,0}"), MathTex("W_{n,1}"), MathTex(". . ") , MathTex("W_{n,n}") ],
        #      ],
        # )           
        # self.play(Create(m3))

        neural_network = NeuralNetwork([
            FeedForwardLayer(28),
            FeedForwardLayer(8),
            FeedForwardLayer(4),

        ], layer_spacing=1.5)


        snake = VGroup()
        snake += Square(side_length=0.5, color=YELLOW).set_fill(RED, opacity=0.7)
        snake += Square(side_length=0.5, color=YELLOW).shift(0.5*DOWN)
        snake += Arrow(DOWN,UP).move_to(snake[0]).shift(0.5*UP).scale(0.5)
        snake.move_to(neural_network).shift(3*RIGHT)
        Direction = MathTex(" Direction = [1,0,0,0]").scale(0.5).move_to(snake).shift(2*DOWN)
        Frame1 = MathTex("Frame: 1").scale(0.5).move_to(neural_network).shift(5*LEFT + 3*UP)
        Frame2 = MathTex("Frame: 2").scale(0.5).move_to(neural_network).shift(5*LEFT + 3*UP)
        Frame3 = MathTex("Frame: 3").scale(0.5).move_to(neural_network).shift(5*LEFT + 3*UP)
        Frame4 = MathTex("Frame: 4").scale(0.5).move_to(neural_network).shift(5*LEFT + 3*UP)
        neural_network.scale(0.8)
        forward_propagation_animation = neural_network.make_forward_pass_animation(run_time=5, passing_flash=True)
        self.play(FadeIn(neural_network), FadeIn(snake),Create(Direction), Create(Frame1))
        self.play(forward_propagation_animation,ReplacementTransform(Frame1,Frame2), run_time = 2, lag_ratio = 0.5, )



        

        #self.play(forward_propagation_animation,run_time = 2, lag_ratio = 0.5) 
        #self.play(snake.animate.rotate(PI/2))
        Direction1 = MathTex(" Direction = [0,0,0,1]").scale(0.5).move_to(snake).shift(2*DOWN)
        self.play(ReplacementTransform(Direction,Direction1), snake.animate.rotate(PI/2))
        #self.play(snake.animate.rotate(PI/2))
        self.play(forward_propagation_animation,ReplacementTransform(Frame2,Frame3), run_time = 2, lag_ratio = 0.5, )
        Direction2 = MathTex(" Direction = [0,0,1,0]").scale(0.5).move_to(snake).shift(2*DOWN)
        self.play(ReplacementTransform(Direction1,Direction2), snake.animate.rotate(PI/2))
        #self.play(snake.animate.rotate(PI/2))
        Direction3 = MathTex(" Direction = [0,1,0,0]").scale(0.5).move_to(snake).shift(2*DOWN)
        self.play(forward_propagation_animation,ReplacementTransform(Frame3,Frame4), run_time = 2, lag_ratio = 0.5)
        self.play(ReplacementTransform(Direction2,Direction3),snake.animate.rotate(PI/2))

class OpeningManim1(MovingCameraScene):
    def construct(self):
        box = Square(side_length = 4, color = YELLOW).move_to(ORIGIN).shift(2*LEFT)
        self.play(Create(box))

        fitness_function = MathTex("Fitness Function").move_to(ORIGIN).shift(2*UP+ 3*RIGHT).scale(0.7)
        self.play(Create(fitness_function))

        fitness_formula = MathTex(r"= \frac{score - \frac{steps}{score + 1} }{score + \frac{steps}{score + 1}} ").scale(0.7).move_to(fitness_function).shift(DOWN)
        fitness_answer = MathTex(r"= \frac{17 - \frac{217}{17 + 1} }{17 + \frac{217}{17 + 1}} ").scale(0.7).move_to(fitness_formula).shift(1.5*DOWN) 
        final_ans = MathTex(" = 0.19778188539").move_to(fitness_answer).shift(1.5*DOWN).scale(0.7)
        
        self.play(Create(fitness_formula))
        self.play(Create(fitness_answer))
        self.play(FadeIn(final_ans))


        
class GeneticAlgorithm(MovingCameraScene):
    def construct(self):
        Evolution = Text('Evolution using Genetic Algorithm').scale(0.6).move_to(ORIGIN).shift( + 3.5*UP)
        self.play(Create(Evolution), run_time = 2, lag_ratio = 0.3)
        initPopulation = MathTex('Initial Population').move_to(ORIGIN).shift( 2.5*UP)
        self.play(Create(initPopulation))
        
        circleGrp = VGroup()
        for i in range(0,5):
            circleGrp += Circle(radius=0.25, color = BLUE, stroke_width =0).set_fill(BLUE,opacity = 0.7).shift(i*LEFT)

        circleGrp.move_to(ORIGIN).shift(UP)
        #circle = Circle(radius=0.5).set_fill(WHITE,opacity = 0.7)


        circleGrp1 = VGroup()
        for i in range(0,5):
            circleGrp1 += Circle(radius=0.25, color = BLUE, stroke_width =0).set_fill(BLUE,opacity = 0.7).shift(i*LEFT)

        circleGrp1.move_to(ORIGIN).shift(DOWN)
        #circle = Circle(radius=0.5).set_fill(WHITE,opacity = 0.7)

        self.play(FadeIn(circleGrp1), FadeIn(circleGrp))
        #self.play(Create(circleGrp))

        m5 = MobjectMatrix(
            [  [MathTex("0.123 "), MathTex(" 0.573 "), MathTex(" . . ") , MathTex(" 0.321 ") ],
                [MathTex(" 0.231 "), MathTex(" 0.342 "), MathTex(" . . ") , MathTex(" 0.522 ") ],
                [MathTex(" . "), MathTex(" . "), MathTex(" . "), MathTex(" . ")],
                [MathTex(" . "), MathTex(" . "), MathTex(" . "), MathTex(" . ")],
              [MathTex(" 0.211 "), MathTex(" 0.321 "), MathTex(" . . ") , MathTex(" 0.434 ") ],
             ],
        ).scale(0.5).move_to(ORIGIN).shift(5*RIGHT)    
       
        box = SurroundingRectangle(m5, color=WHITE).scale(1.2)

        self.play(Create(m5),Create(box), run_time = 2)


        fitness = VGroup()
        fitness += MathTex("Fitness Function").move_to(ORIGIN).shift(UP+ 4.5*LEFT).scale(0.7)
        

        fitness += MathTex(r" \frac{score - \frac{steps}{score + 1} }{score + \frac{steps}{score + 1}} ").scale(0.7).move_to(fitness[0]).shift(DOWN)
        box1 = SurroundingRectangle( fitness, color=WHITE).scale(1.2) 
        self.play(Create(box1),Create(fitness), run_time = 2 )





        fn1 = VGroup()
        fn1 += MathTex("0.03").move_to(circleGrp[0]).scale(0.4)
        fn1 += MathTex("0.93").move_to(circleGrp[1]).scale(0.4)
        fn1 += MathTex("0.01").move_to(circleGrp[2]).scale(0.4)
        fn1 += MathTex("0.43").move_to(circleGrp[3]).scale(0.4)
        fn1 += MathTex("0.87").move_to(circleGrp[4]).scale(0.4)
        fn1 += MathTex("0.20").move_to(circleGrp1[0]).scale(0.4)
        fn1 += MathTex("0.47").move_to(circleGrp1[1]).scale(0.4)
        fn1 += MathTex("0.65").move_to(circleGrp1[2]).scale(0.4)
        fn1 += MathTex("0.82").move_to(circleGrp1[3]).scale(0.4)
        fn1 += MathTex("0.91").move_to(circleGrp1[4]).scale(0.4)       
        self.play(Create(fn1))

        blob1 = VGroup()
        blob1 += circleGrp[1].copy()
        blob1 += fn1[1].copy()
        blob2 = VGroup()
        blob2 += circleGrp1[4].copy()
        blob2 += fn1[9].copy()


        self.wait()
        self.play(FadeOut(circleGrp), FadeOut(circleGrp1), FadeOut(m5),FadeOut(box),FadeOut(fitness), FadeOut(box1)  ,FadeOut(fn1), FadeIn(blob1), FadeIn(blob2) )
        
        self.play(blob1.animate.move_to(ORIGIN).shift(RIGHT), blob2.animate.move_to(ORIGIN).shift(LEFT))
        crossover = MathTex('Crossover').move_to(initPopulation)
        self.play(ReplacementTransform(initPopulation,crossover))

        cr1 = VGroup()
        cr2 = VGroup()

        cr1 += MobjectMatrix(
            [  [MathTex("0.123 "), MathTex(" 0.573 "), MathTex(" . . ") , MathTex(" 0.321 ") ],
                [MathTex(" 0.231 "), MathTex(" 0.342 "), MathTex(" . . ") , MathTex(" 0.522 ") ],
                [MathTex(" . "), MathTex(" . "), MathTex(" . "), MathTex(" . ")],
                [MathTex(" . "), MathTex(" . "), MathTex(" . "), MathTex(" . ")],
              [MathTex(" 0.211 "), MathTex(" 0.321 "), MathTex(" . . ") , MathTex(" 0.434 ") ],
             ],
        ).scale(0.5).move_to(ORIGIN).shift(3*LEFT)    
       
        cr1 += SurroundingRectangle(cr1[0], color=WHITE).scale(1.2)

        cr2 += MobjectMatrix(
            [  [MathTex("0.673 "), MathTex(" 0.324 "), MathTex(" . . ") , MathTex(" 0.781 ") ],
                [MathTex(" 0.431 "), MathTex(" 0.572 "), MathTex(" . . ") , MathTex(" 0.231 ") ],
                [MathTex(" . "), MathTex(" . "), MathTex(" . "), MathTex(" . ")],
                [MathTex(" . "), MathTex(" . "), MathTex(" . "), MathTex(" . ")],
              [MathTex(" 0.133 "), MathTex(" 0.231 "), MathTex(" . . ") , MathTex(" 0.234 ") ],
             ],
        ).scale(0.5).move_to(ORIGIN).shift(3*RIGHT)    
       
        cr2 += SurroundingRectangle(cr2[0], color=WHITE).scale(1.2)    

        #self.play(Create(cr1), Create(cr2))
        self.play(ReplacementTransform(blob2,cr1), ReplacementTransform(blob1,cr2))


class GeneticAlgorithm1(MovingCameraScene):
    def construct(self):


        Evolution = Text('Evolution using Genetic Algorithm').scale(0.6).move_to(ORIGIN).shift( + 3.5*UP)
        self.play(Create(Evolution), run_time = 2, lag_ratio = 0.3)
        initPopulation = MathTex('Initial Population').move_to(ORIGIN).shift( 2.5*UP)
        self.play(Create(initPopulation))
        
        circleGrp = VGroup()
        for i in range(0,5):
            circleGrp += Circle(radius=0.25, color = BLUE, stroke_width =0).set_fill(BLUE,opacity = 0.7).shift(i*LEFT)

        circleGrp.move_to(ORIGIN).shift(UP)
        #circle = Circle(radius=0.5).set_fill(WHITE,opacity = 0.7)


        circleGrp1 = VGroup()
        for i in range(0,5):
            circleGrp1 += Circle(radius=0.25, color = BLUE, stroke_width =0).set_fill(BLUE,opacity = 0.7).shift(i*LEFT)

        circleGrp1.move_to(ORIGIN).shift(DOWN)
        #circle = Circle(radius=0.5).set_fill(WHITE,opacity = 0.7)

        self.play(FadeIn(circleGrp1), FadeIn(circleGrp))
        #self.play(Create(circleGrp))

        m5 = MobjectMatrix(
            [  [MathTex("0.123 "), MathTex(" 0.573 "), MathTex(" . . ") , MathTex(" 0.321 ") ],
                [MathTex(" 0.231 "), MathTex(" 0.342 "), MathTex(" . . ") , MathTex(" 0.522 ") ],
                [MathTex(" . "), MathTex(" . "), MathTex(" . "), MathTex(" . ")],
                [MathTex(" . "), MathTex(" . "), MathTex(" . "), MathTex(" . ")],
              [MathTex(" 0.211 "), MathTex(" 0.321 "), MathTex(" . . ") , MathTex(" 0.434 ") ],
             ],
        ).scale(0.5).move_to(ORIGIN).shift(5*RIGHT)    
       
        box = SurroundingRectangle(m5, color=WHITE).scale(1.2)

        self.play(Create(m5),Create(box), run_time = 2)


        fitness = VGroup()
        fitness += MathTex("Fitness Function").move_to(ORIGIN).shift(UP+ 4.5*LEFT).scale(0.7)
        

        fitness += MathTex(r" \frac{score - \frac{steps}{score + 1} }{score + \frac{steps}{score + 1}} ").scale(0.7).move_to(fitness[0]).shift(DOWN)
        box1 = SurroundingRectangle( fitness, color=WHITE).scale(1.2) 
        self.play(Create(box1),Create(fitness), run_time = 2 )





        fn1 = VGroup()
        fn1 += MathTex("0.03").move_to(circleGrp[0]).scale(0.4)
        fn1 += MathTex("0.93").move_to(circleGrp[1]).scale(0.4)
        fn1 += MathTex("0.01").move_to(circleGrp[2]).scale(0.4)
        fn1 += MathTex("0.43").move_to(circleGrp[3]).scale(0.4)
        fn1 += MathTex("0.87").move_to(circleGrp[4]).scale(0.4)
        fn1 += MathTex("0.20").move_to(circleGrp1[0]).scale(0.4)
        fn1 += MathTex("0.47").move_to(circleGrp1[1]).scale(0.4)
        fn1 += MathTex("0.65").move_to(circleGrp1[2]).scale(0.4)
        fn1 += MathTex("0.82").move_to(circleGrp1[3]).scale(0.4)
        fn1 += MathTex("0.91").move_to(circleGrp1[4]).scale(0.4)       
        self.play(Create(fn1))

        blob1 = VGroup()
        blob1 += circleGrp[1].copy()
        blob1 += fn1[1].copy()
        blob2 = VGroup()
        blob2 += circleGrp1[4].copy()
        blob2 += fn1[9].copy()


        self.wait()
        self.play(FadeOut(circleGrp), FadeOut(circleGrp1), FadeOut(m5),FadeOut(box),FadeOut(fitness), FadeOut(box1)  ,FadeOut(fn1), FadeIn(blob1), FadeIn(blob2) )
        
        self.play(blob1.animate.move_to(ORIGIN).shift(RIGHT), blob2.animate.move_to(ORIGIN).shift(LEFT))
        crossover = MathTex('Crossover').move_to(initPopulation)
        self.wait()
        self.play(ReplacementTransform(initPopulation,crossover))

        cr1 = VGroup()
        cr2 = VGroup()

        cr1 += MobjectMatrix(
            [  [MathTex("0.123 "), MathTex(" 0.573 "), MathTex(" . . ") , MathTex(" 0.321 ") ],
                [MathTex(" 0.231 "), MathTex(" 0.342 "), MathTex(" . . ") , MathTex(" 0.522 ") ],
                [MathTex(" . "), MathTex(" . "), MathTex(" . "), MathTex(" . ")],
                [MathTex(" . "), MathTex(" . "), MathTex(" . "), MathTex(" . ")],
              [MathTex(" 0.211 "), MathTex(" 0.321 "), MathTex(" . . ") , MathTex(" 0.434 ") ],
             ],
        ).scale(0.5).move_to(ORIGIN).shift(3*LEFT)    
       
        cr1 += SurroundingRectangle(cr1[0], color=WHITE).scale(1.2)

        cr2 += MobjectMatrix(
            [  [MathTex("0.673 "), MathTex(" 0.324 "), MathTex(" . . ") , MathTex(" 0.781 ") ],
                [MathTex(" 0.431 "), MathTex(" 0.572 "), MathTex(" . . ") , MathTex(" 0.231 ") ],
                [MathTex(" . "), MathTex(" . "), MathTex(" . "), MathTex(" . ")],
                [MathTex(" . "), MathTex(" . "), MathTex(" . "), MathTex(" . ")],
              [MathTex(" 0.133 "), MathTex(" 0.231 "), MathTex(" . . ") , MathTex(" 0.234 ") ],
             ],
        ).scale(0.5).move_to(ORIGIN).shift(3*RIGHT)    
       
        cr2 += SurroundingRectangle(cr2[0], color=WHITE).scale(1.2)    

        #self.play(Create(cr1), Create(cr2))
        self.play(ReplacementTransform(blob2,cr1), ReplacementTransform(blob1,cr2))
        self.wait()


        flattenedMatrix = MobjectMatrix(
            [  MathTex("0.123 "), MathTex(" 0.573 "), MathTex("0.231") , MathTex("0.342 ") , MathTex(".."), MathTex(" .. ") ,MathTex("0.522"), MathTex("0.434"),MathTex("0.341"),MathTex("0.324")
             ],
        ).scale(0.5).move_to(ORIGIN).shift(2*LEFT)
        flattenedMatrix1 = MobjectMatrix(
            [  MathTex("0.456 "), MathTex(" 0.345 "), MathTex("0.465") , MathTex("0.654 ") , MathTex(".."), MathTex(" .. ") ,MathTex("0.453"), MathTex("0.325"),MathTex("0.765"),MathTex("0.654")
             ],
        ).scale(0.5).move_to(ORIGIN).shift(2*RIGHT)

        sbox1 = SurroundingRectangle(flattenedMatrix[0][:5],color=BLUE)
        sbox3 = SurroundingRectangle(flattenedMatrix[0][-5:],color=BLUE)
        sbox2 = SurroundingRectangle(flattenedMatrix1[0][-5:])
        sbox4 = SurroundingRectangle(flattenedMatrix1[0][:5]) 


        # background= Rectangle().scale(5)
        # background.set_fill(opacity=.5)
        # background.set_color([TEAL, YELLOW])
        # self.add(background)







        ma1 = MobjectMatrix(
            [  MathTex("0.123 "), MathTex(" 0.573 "), MathTex("0.231") , MathTex("0.342 ") , MathTex(".."), MathTex(" .. ") ,MathTex("0.456 "), MathTex(" 0.345 "), MathTex("0.465") , MathTex("0.654 ")
             ],
        ).scale(0.5).move_to(ORIGIN).shift(2*LEFT) 

        ma2 = MobjectMatrix(
            [ MathTex("0.522"), MathTex("0.434"),MathTex("0.341"),MathTex("0.324") , MathTex(" .. "), MathTex(" .. ") ,MathTex("0.453"), MathTex("0.325"),MathTex("0.765"),MathTex("0.654")
             ],
        ).scale(0.5).move_to(ORIGIN).shift(2*RIGHT) 


        self.play(ReplacementTransform(cr1,flattenedMatrix),ReplacementTransform(cr2,flattenedMatrix1),run_time = 1.5)
        self.play(Create(sbox1),Create(sbox2), Create(sbox3),Create(sbox4), run_time = 2)

        self.play(sbox4.animate.move_to(sbox3),sbox3.animate.move_to(sbox4), run_time = 2 )
        self.play(ReplacementTransform(flattenedMatrix,ma1), ReplacementTransform(flattenedMatrix1,ma2))
        self.wait()
        self.play(FadeOut(sbox1), FadeOut(sbox2), FadeOut(sbox3), FadeOut(sbox4))

        mutation = MathTex('Mutation').move_to(ORIGIN).shift( 3*UP)
        self.play(Create(mutation))


        #self.play(ReplacementTransform(ma1[0][0], MathTex('0.111').move_to( ma1[0][0].scale(0.2)) ))

        r1 =  MobjectMatrix(
            [ MathTex("0.011"), MathTex("0.434"),MathTex("0.341"),MathTex("0.324") , MathTex(" .. "), MathTex(" .. ") ,MathTex("0.453"), MathTex("0.325"),MathTex("0.765"),MathTex("0.654")
             ],
        ).scale(0.5).move_to(ma2).shift(RIGHT)
        r2 =  MobjectMatrix(
            [ MathTex("0.522"), MathTex("0.434"),MathTex("0.341"),MathTex("0.577") , MathTex(" .. "), MathTex(" .. ") ,MathTex("0.453"), MathTex("0.325"),MathTex("0.765"),MathTex("0.654")
             ],
        ).scale(0.5).move_to(r1).shift(RIGHT)
        r3 =  MobjectMatrix(
            [ MathTex("0.522"), MathTex("0.434"),MathTex("0.341"),MathTex("0.324") , MathTex(" .. "), MathTex(" .. ") ,MathTex("0.453"), MathTex("0.677"),MathTex("0.765"),MathTex("0.654")
             ],
        ).scale(0.5).move_to(r2).shift(RIGHT)
        br1 = SurroundingRectangle(r1[0][0])
        br2 = SurroundingRectangle(r2[0][3])
        br3 = SurroundingRectangle(r3[0][7])
        self.play(FadeIn(r1), Create(br1), FadeIn(r2), Create(br2), FadeIn(r3), Create(br3), run_time = 2)



        l1 = MobjectMatrix(
            [  MathTex("0.123 "), MathTex(" 0.765 "), MathTex("0.231") , MathTex("0.342 ") , MathTex(".."), MathTex(" .. ") ,MathTex("0.456 "), MathTex(" 0.345 "), MathTex("0.465") , MathTex("0.654 ")
             ],
        ).scale(0.5).move_to(ma1).shift(LEFT) 

        l2 = MobjectMatrix(
            [  MathTex("0.123 "), MathTex(" 0.765 "), MathTex("0.231") , MathTex("0.433 ") , MathTex(".."), MathTex(" .. ") ,MathTex("0.456 "), MathTex(" 0.345 "), MathTex("0.465") , MathTex("0.654 ")
             ],
        ).scale(0.5).move_to(l1).shift(LEFT) 
        
        l3 = MobjectMatrix(
            [  MathTex("0.123 "), MathTex(" 0.765 "), MathTex("0.231") , MathTex("0.342 ") , MathTex(".."), MathTex(" .. ") ,MathTex("0.456 "), MathTex(" 0.345 "), MathTex("0.221") , MathTex("0.654 ")
             ],
        ).scale(0.5).move_to(l2).shift(LEFT) 

        bl1 = SurroundingRectangle(l1[0][1])
        bl2 = SurroundingRectangle(l2[0][3])
        bl3 = SurroundingRectangle(l3[0][8])
        self.play(FadeIn(l1), Create(bl1), FadeIn(l2), Create(bl2), FadeIn(l3), Create(bl3), run_time = 2)


        self.play(FadeOut(br1), FadeOut(br2), FadeOut(br3), FadeOut(bl1), FadeOut(bl2), FadeOut(bl3))

        circleGrp = VGroup()
        circleGrp += Circle(radius=0.25, color = BLUE, stroke_width =0).set_fill(BLUE,opacity = 0.7).move_to(ma2)
        circleGrp += circleGrp[0].copy().move_to(r1) 
        circleGrp += circleGrp[1].copy().move_to(r2) 
        circleGrp += circleGrp[2].copy().move_to(r3) 

        circleGrp1 = VGroup()
        circleGrp1 += Circle(radius=0.25, color = BLUE, stroke_width =0).set_fill(BLUE,opacity = 0.7).move_to(ma1)
        circleGrp1 += circleGrp1[0].copy().move_to(l1) 
        circleGrp1 += circleGrp1[1].copy().move_to(l2) 
        circleGrp1 += circleGrp1[2].copy().move_to(l3) 

        #self.play(Create(circleGrp), Create(circleGrp1))


        self.play(ReplacementTransform(ma2,circleGrp[0]) , ReplacementTransform(r1, circleGrp[1]), ReplacementTransform(r2, circleGrp[2]), ReplacementTransform(r3, circleGrp[3]) )
        self.play(ReplacementTransform(ma1,circleGrp1[0]) , ReplacementTransform(l1, circleGrp1[1]), ReplacementTransform(l2, circleGrp1[2]), ReplacementTransform(l3, circleGrp1[3]) )

        circleGrp += circleGrp[3].copy().move_to(circleGrp[0]).shift(LEFT)

        fn1 = MathTex("0.91").move_to(circleGrp[4]).scale(0.4)

        circleGrp1 += circleGrp1[3].copy().move_to(circleGrp1[0]).shift(RIGHT)
        fn2 = MathTex("0.93").move_to(circleGrp1[4]).scale(0.4) 

        self.play(FadeIn(circleGrp[4]),FadeIn(fn1),FadeIn(circleGrp1[4]),FadeIn(fn2)  )

        self.play(FadeOut(fn1), FadeOut(fn2))
        self.play(circleGrp.animate.move_to(ORIGIN).shift(UP) , circleGrp1.animate.move_to(ORIGIN).shift(DOWN))



class OpeningScene(MovingCameraScene):
    def construct(self):

        r1 = Rectangle(height = 2.5, width= 4).move_to(ORIGIN).shift(3*LEFT + 2*DOWN)
        r2 = Rectangle(height = 2.5, width= 4).move_to(ORIGIN).shift(3*RIGHT + 2*DOWN)
        AIlearns = Text("AI learns to ...").scale(0.8).move_to(ORIGIN).shift(3*UP) 
        self.play(FadeIn(r1), FadeIn(r2), r1.animate.shift(2*UP) , r2.animate.shift(2*UP), Create(AIlearns), run_time = 2)
        codeBullet = MathTex("Code Bullet").scale(0.5).move_to(r1).shift(1.5*DOWN)
        techwithtim = MathTex("Tech with tim").scale(0.5).move_to(r2).shift(1.5*DOWN) 

        self.play(Create(codeBullet), Create(techwithtim))
        self.wait()
        self.play(r1.animate.shift(3*RIGHT), FadeOut(r2), codeBullet.animate.shift(3*RIGHT), FadeOut(techwithtim))

        self.play(FadeOut(r1), FadeOut(codeBullet),FadeOut(AIlearns))




        number_plane = NumberPlane(
            x_range=(0, 10, 1),
            y_range=(0, 10, 1),
            x_length=5,
            y_length=5,
        ).move_to(ORIGIN).shift(UP + 0.7*RIGHT)
        ax = number_plane.add_coordinates()
        sq = VGroup()
        sq += Square(side_length=0.5, color=YELLOW).move_to(ax.coords_to_point(4.5, 4.5))
        sq += Square(side_length=0.5, color=YELLOW).move_to(ax.coords_to_point(3.5, 4.5))
        sq += Square(side_length=0.5, color=YELLOW).move_to(ax.coords_to_point(3.5, 3.5))
        #sq = Rectangle(color=RED, width = 0.5 , height = 2).move_to(ax.coords_to_point(3.5, 4.5))
        sq[0].set_fill(RED, opacity=0.7)
        #print(ax)
        # self.play(
        #     Create(number_plane, run_time=3, lag_ratio=0.1),
        # )
        
        
        #self.add(number_plane,sq)
        self.wait()
        self.play(FadeIn(sq))

        self.play(sq.animate.shift(3*LEFT))

       # Make the Layer object
        neural_network = NeuralNetwork([
            
            FeedForwardLayer(24),
            FeedForwardLayer(8),
            FeedForwardLayer(4),

        ], layer_spacing=1)

        neural_network.scale(1)
        # Make Animation
        #self.play(Create(nn))
        #forward_propagation_animation = nn.make_forward_pass_animation(run_time=5, passing_flash=True)

        #self.play(forward_propagation_animation)

        self.play(Create(neural_network, lag_ratio=1))
        #self.add(neural_network)
        
        r = Rectangle(color=BLUE, width = 0.6 , height = 3.5)
        HL = Text('Hidden Layer').move_to(neural_network).scale(0.4).shift(2.5*UP+ RIGHT*0.2 )

        r1 = Rectangle(color=BLUE, width = 0.6 , height = 8).shift(1.30*LEFT)
        input = Text('Input Layer').next_to(r1, LEFT).scale(0.5)
        eye = Text("Snake's eye ").next_to(r1, LEFT).scale(0.5) 

        r2 = Rectangle(color=BLUE, width = 0.6 , height = 2).shift(1.30*RIGHT)
        
        Output = Text('Output Layer').next_to(r2, RIGHT).scale(0.5) 
        self.play(Create(r1, run_time= 2),FadeOut(sq))
        self.play(Write(input))
        self.play(
            ReplacementTransform(r1, r)
        ) 
        self.play(Write(HL))

        self.play(
            ReplacementTransform(r, r2)
        ) 
        self.play(Write(Output))
        self.play(FadeOut(r2))
        self.play(
            ReplacementTransform(input, eye)
        ) 