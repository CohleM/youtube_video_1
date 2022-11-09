from manim import *


from tkinter import CENTER
from manim_ml.neural_network.layers import FeedForwardLayer
from manim_ml.neural_network.neural_network import NeuralNetwork
class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        # Pass number as the mobject of the animation
        super().__init__(number,  **kwargs)
        # Set start and end
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        # Set value of DecimalNumber according to alpha
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)


    
class OpeningManim(MovingCameraScene):
    def construct(self):

        number_plane = NumberPlane(
            x_range=(0, 10, 1),
            y_range=(0, 10, 1),
            x_length=5,
            y_length=5,
        ).move_to(LEFT*3)
        ax = number_plane.add_coordinates()
        sq = Square(side_length=0.5, color=YELLOW).move_to(ax.coords_to_point(4.5, 4.5))
        sq1 = Square(side_length=0.5, color=YELLOW).move_to(ax.coords_to_point(3.5, 4.5))
        sq2 = Square(side_length=0.5, color=YELLOW).move_to(ax.coords_to_point(3.5, 3.5))
        #sq = Rectangle(color=RED, width = 0.5 , height = 2).move_to(ax.coords_to_point(3.5, 4.5))
        sq.set_fill(RED, opacity=0.7)
        #print(ax)
        self.play(
            Create(number_plane, run_time=3, lag_ratio=0.1),
        )
        
        
        #self.add(number_plane,sq)
        self.wait()
        self.play(FadeIn(sq), FadeIn(sq1), FadeIn(sq2) )
        self.wait()

        arrows = VGroup()

        arrows += Arrow(start=ax.coords_to_point(4.5, 4.5), end=ax.coords_to_point(4.5, 10.5) )
        arrows += Arrow(start=ax.coords_to_point(4.5, 4.5), end=ax.coords_to_point(10.5, 10.5))
        arrows += Arrow(start=ax.coords_to_point(4.5, 4.5), end=ax.coords_to_point(10.5, 4.5))
        arrows += Arrow(start=ax.coords_to_point(4.5, 4.5), end=ax.coords_to_point(10.5, 0))
        arrows += Arrow(start=ax.coords_to_point(4.5, 4.5), end=ax.coords_to_point(4.5, 0))
        arrows += Arrow(start=ax.coords_to_point(4.5, 4.5), end=ax.coords_to_point(0, 0))
        arrows += Arrow(start=ax.coords_to_point(4.5, 4.5), end=ax.coords_to_point(0, 4.5))
        arrows += Arrow(start=ax.coords_to_point(4.5, 4.5), end=ax.coords_to_point(0, 10.5))
       


        allD = VGroup()

        allD += Text('D1').next_to(arrows[0].get_end(), UP).scale(0.5)
        allD += Text('D2').next_to(arrows[1].get_end(), RIGHT).scale(0.5)
        allD += Text('D3').next_to(arrows[2].get_end(), RIGHT).scale(0.5)
        allD += Text('D4').next_to(arrows[3].get_end(), DOWN).scale(0.5)
        allD += Text('D5').next_to(arrows[4].get_end(), DOWN).scale(0.5)
        allD += Text('D6').next_to(arrows[5].get_end(), LEFT).scale(0.5)
        allD +=Text('D7').next_to(arrows[6].get_end(), LEFT).scale(0.5)
        allD += Text('D8').next_to(arrows[7].get_end(), LEFT).scale(0.5)

        self.play(Create(arrows), runtime = 4)
        #self.play(Create(arrow_1), Create(arrow_2), Create(arrow_3) , Create(arrow_4),Create(arrow_5), Create(arrow_6), Create(arrow_7) , Create(arrow_8) )
        self.play(FadeIn(allD))

        # # # heading = Text("Snakes sees 3 Different things").move_to(RIGHT*4 + UP *2.5).scale(0.65)
        # # # self.play(Write(heading))
        Wall = Text("Wall").move_to(RIGHT*2 + UP *2.5).scale(0.4)
        Body = Text("Body").next_to(Wall, RIGHT, buff = 0.5).scale(0.4)
        Food= Text("Food").next_to(Body, RIGHT, buff = 0.5).scale(0.4)
        self.play(Write(Wall))
        self.play(Write(Body))
        self.play(Write(Food))

        

        #slider 
        
        line = Line([3, 0, 0], [6, 0, 0]).shift(DOWN)
        dot = Dot().move_to([3,0,0]).shift(DOWN)
        self.play(Create(dot), Create(line) )
        dot1 = dot.copy().set_color(BLACK) 
        zero = Text('0').move_to([3,-0.5,0]).scale(0.5)
        one = Text('1').move_to([6, -0.5, 0]).scale(0.5)
        good = Text('Bad').move_to([3,-1.5,0]).scale(0.5)
        bad = Text('Good').move_to([6, -1.5, 0]).scale(0.5) 
        # Create Decimal Number and add it to scene

        grp = VGroup(line,dot,zero,one,good,bad).move_to(ORIGIN).shift(3.5*RIGHT)
        self.play(Create(grp), run_time = 2.5)

        #self.play(Create(zero), Create(one), Create(good), Create(bad))
        #self.wait()
        self.play(MoveAlongPath(dot, line), run_time=2 )


        Wall1 = Wall.copy()
        self.play(FadeOut(grp), Wall1.animate.shift(2*DOWN).scale(1.3))

        wallFormula = MathTex(r"=\frac{number of blockes between Head and Wall}{total numberof blockes- 1} ")
        wallFormula.scale(0.4).next_to(Wall1, RIGHT)
        self.play(Create(wallFormula), run_time = 2)

        #find metrics in D1 direction 
        self.play(arrows[0].animate.set_color(GOLD))

        

        blocks = VGroup()
        for i in range(5,10):
            blocks += Square(side_length=0.5, color=WHITE).move_to(ax.coords_to_point(4.5, i + 0.5 ))

        self.play(Create(blocks))

        firstNum = Tex("= 5 ").move_to(Wall1).shift(0.8*RIGHT + DOWN).scale(0.5)
        secondNum = Tex("/ (10 - 1) ").move_to(firstNum).shift(0.7*RIGHT).scale(0.5)

        uponline = Line(LEFT, RIGHT).move_to(firstNum).shift(0.2*DOWN)

        self.play(
            ReplacementTransform(blocks, firstNum)
        ) 
        
        Totalblocks = VGroup()
        for i in range(0,10):
            Totalblocks += Square(side_length=0.5, color=BLUE).move_to(ax.coords_to_point(4.5, i + 0.5 ))
        self.play(Create(Totalblocks))
        # Play the Count Animation to count from 0 to 100 in 4 seconds
        #self.play(Count(number, 0, 1), run_time=2, rate_func=linear)
        self.play(
            ReplacementTransform(Totalblocks, secondNum)
        ) 

        answer = Tex(" = 0.55").move_to(firstNum).shift(DOWN + 0.2*RIGHT).scale(0.5)

        self.play(FadeIn(answer ))

        
        #self.wait()
        self.play(FadeOut(firstNum), FadeOut(secondNum))
        self.play(answer.animate.move_to(Wall).shift(0.5* DOWN) )
        


        #For body
        Body1 = Body.copy().scale(1.3).move_to(Wall1)
        bodyFormula = MathTex(r"=\frac{number of blockes between Head and Body}{total numberof blockes- 1} ").move_to(wallFormula).scale(0.4)
        self.play(ReplacementTransform(wallFormula, bodyFormula), ReplacementTransform(Wall1, Body1))

        firstNum = Tex("= 1 ").move_to(Wall1).shift(0.8*RIGHT + DOWN).scale(0.5)
        secondNum = Tex("/ (10 - 1) ").move_to(firstNum).shift(0.7*RIGHT).scale(0.5) 

        #sq1 = Square(side_length=0.5, color=YELLOW).move_to(ax.coords_to_point(3.5, 4.5))
        sq3 = Square(side_length=0.5, color=YELLOW).move_to(ax.coords_to_point(3.5, 4.5))

        self.play(Uncreate(sq2))
        sq4 = Square(side_length=0.5, color=YELLOW).move_to(ax.coords_to_point(3.5, 5.5))
        sq5 = Square(side_length=0.5, color=YELLOW).move_to(ax.coords_to_point(3.5, 6.5))
        sq6 = Square(side_length=0.5, color=YELLOW).move_to(ax.coords_to_point(4.5, 6.5))
        self.play(Create(sq4), Create(sq5),Create(sq6))
        Foodsq = Square(side_length=0.5, color = TEAL, fill_opacity = 1).move_to(ax.coords_to_point(4.5, 7.5))


        space = Square(side_length=0.5, color=WHITE).move_to(ax.coords_to_point(4.5, 5.5))
        self.play(Create(space))
        self.play(
            ReplacementTransform(space, firstNum)
        ) 
        Totalblocks1 = VGroup() 
        #self.play(FadeIn(Totalblocks))
        for i in range(0,10):
            Totalblocks1 += Square(side_length=0.5, color=BLUE).move_to(ax.coords_to_point(4.5, i + 0.5 ))
        self.play(Create(Totalblocks1))
        self.play(
            ReplacementTransform(Totalblocks1, secondNum)
        )  
        self.wait()


        answer1 = Tex(" = 0.11").move_to(firstNum).shift(DOWN + 0.2*RIGHT).scale(0.5)
        self.play(FadeIn(answer1))
        self.play(answer1.animate.move_to(Body).shift(0.5* DOWN), FadeOut(firstNum), FadeOut(secondNum)) 

        Food1 = Food.copy()
        self.play(
            Food1.animate.move_to(Body1), Uncreate(Body1)
        ) 

        
        foodFormula = MathTex(r"=\frac{a - b -1}{a- 1} ").move_to(Food1).scale(0.4).shift(RIGHT)
        a = MathTex("a = total numberof blockes").scale(0.4).move_to(foodFormula).shift(DOWN)
        b = MathTex("b = number of blockes between Head and Food").scale(0.4).move_to(a).shift(0.4*DOWN)
        self.play(ReplacementTransform(bodyFormula, foodFormula) )
        self.play(FadeIn(a), FadeIn(b))
        self.play(FadeOut(firstNum))

        self.play(Create(Foodsq))
        answer2 = Tex(" = 0.77").move_to(foodFormula).scale(0.5)
        self.play(ReplacementTransform(foodFormula, answer2) ) 
        self.play(FadeOut(a), FadeOut(b))
        self.play(answer2.animate.move_to(Food).shift(0.5* DOWN), FadeOut(Food1) ) 
        self.play(arrows.animate.set_color(GOLD))

        #all FadingOut clearing

        self.play(FadeOut(number_plane),FadeOut(arrows), FadeOut(allD), FadeOut(sq),FadeOut(sq4),FadeOut(sq5),FadeOut(sq6),FadeOut(Foodsq), FadeOut(answer),FadeOut(answer1),FadeOut(answer2),FadeOut(sq2),FadeOut(space),FadeOut(sq1)  )


        metrics = VGroup()
        metrics += Food
        metrics += Wall
        metrics += Body 




#GGGG

        m0 = DecimalMatrix([
            [0.55555556],
            [0.11111111],
            [0.77777778],
            [0.55555556],
            [1.        ],
            [0.        ],
            [0.55555556],
            [1.        ],
            [0.        ],
            [0.44444444],
            [1.        ],
            [0.        ],
            [0.44444444],
            [1.        ],
            [0.        ],
            [0.44444444],
            [1.        ],
            [0.        ],
            [0.44444444],
            [0.        ],
            [0.        ],
            [0.44444444],
            [0.        ],
            [0.        ],
            # [0.        ],
            # [1.        ],
            # [0.        ],
            # [0.        ]
        ], element_to_mobject_config={"num_decimal_places": 3}).scale(0.3).shift(4*LEFT)

        self.play(ReplacementTransform(metrics,m0))
       # self.play(Create(m0))
        vision = MathTex("Vision").scale(0.5).move_to(m0).shift(LEFT)
        self.play(Create(vision))

        number_plane = NumberPlane(
            x_range=(0, 10, 1),
            y_range=(0, 10, 1),
            x_length=5,
            y_length=5,
        ).move_to(RIGHT)
        ax = number_plane.add_coordinates()

        self.play(Create(number_plane) ,run_time=3, lag_ratio=0.1)

        snake = VGroup()
        snake += Square(side_length=0.5, color=YELLOW).set_fill(RED, opacity=0.7)
        snake += Square(side_length=0.5, color=YELLOW).shift(0.5*DOWN)
        snake += Arrow(DOWN,UP).move_to(snake[0]).shift(0.5*UP).scale(0.5)
        snake.move_to(ax.coords_to_point(4.5, 4.5))
        self.play(FadeIn(snake))
        Direction = MathTex(" Direction = [1,0,0,0]").scale(0.5).move_to(number_plane).shift(3*DOWN)
        self.play(Create(Direction))
        #self.play(snake.animate.rotate(PI/2))
        Direction1 = MathTex(" Direction = [0,0,0,1]").scale(0.5).move_to(number_plane).shift(3*DOWN)
        self.play(ReplacementTransform(Direction,Direction1), snake.animate.rotate(PI/2))
        #self.play(snake.animate.rotate(PI/2))
        Direction2 = MathTex(" Direction = [0,0,1,0]").scale(0.5).move_to(number_plane).shift(3*DOWN)
        self.play(ReplacementTransform(Direction1,Direction2), snake.animate.rotate(PI/2))
        #self.play(snake.animate.rotate(PI/2))
        Direction3 = MathTex(" Direction = [0,1,0,0]").scale(0.5).move_to(number_plane).shift(3*DOWN)
        self.play(ReplacementTransform(Direction2,Direction3),snake.animate.rotate(PI/2))
        #self.play(snake.animate.rotate(PI/2))

        m2 = DecimalMatrix([
            [0.55555556],
            [0.11111111],
            [0.77777778],
            [0.55555556],
            [1.        ],
            [0.        ],
            [0.55555556],
            [1.        ],
            [0.        ],
            [0.44444444],
            [1.        ],
            [0.        ],
            [0.44444444],
            [1.        ],
            [0.        ],
            [0.44444444],
            [1.        ],
            [0.        ],
            [0.44444444],
            [0.        ],
            [0.        ],
            [0.44444444],
            [0.        ],
            [0.        ],
            [0.        ],
            [1.        ],
            [0.        ],
            [0.        ]
        ], element_to_mobject_config={"num_decimal_places": 3}).scale(0.3).shift(4*LEFT)

        m1 = DecimalMatrix([
            [0.        ],
            [1.        ],
            [0.        ],
            [0.        ]
        ], element_to_mobject_config={"num_decimal_places": 3}).scale(0.3).shift(4*LEFT+ 2.5*DOWN)

        self.play(m0.animate.shift(UP), ReplacementTransform(Direction3, m1))
        directionText = MathTex("Direction").scale(0.5).move_to(m1).shift(LEFT)
        self.play(Create(directionText))    
        self.play(FadeOut(m1),ReplacementTransform(m0,m2) )
        #self.play(ReplacementTransform(m0, m1))

        self.play(FadeOut(snake), FadeOut(number_plane))
        neural_network = NeuralNetwork([
            FeedForwardLayer(28),
            FeedForwardLayer(8),
            FeedForwardLayer(4),

        ], layer_spacing=1.5)

        neural_network.scale(0.8)


        self.play(Create(neural_network, lag_ratio = 1))
        self.play(m2.animate.shift(2*RIGHT))

        input1 = MathTex("Input").scale(0.5).move_to(m2).shift(LEFT)
        self.play(ReplacementTransform(vision,input1), FadeOut(directionText))
        
        #self.camera.frame.save_state()
        inputSize = VGroup()
        inputSize += MathTex("28").move_to(neural_network).shift(1.4*LEFT+3.7*DOWN).scale(0.5)
        inputSize += MathTex("8").move_to(neural_network).shift(1.3*DOWN).scale(0.5)
        inputSize += MathTex("4").move_to(neural_network).shift(1.4*RIGHT + 0.9*DOWN).scale(0.5)
        self.play(Create(inputSize[0]), Create(inputSize[1]), Create(inputSize[2]) )

        m3 = MobjectMatrix(
            [  [MathTex("W_{0,0}"), MathTex("W_{0,1}"), MathTex(". . ") , MathTex("W_{0,n}") ],
                [MathTex("W_{1,0}"), MathTex("W_{1,1}"), MathTex(". . ") , MathTex("W_{1,n}") ],
                [MathTex("."), MathTex("."), MathTex("."), MathTex(".")],
                [MathTex("."), MathTex("."), MathTex("."), MathTex(".")],
              [MathTex("W_{n,0}"), MathTex("W_{n,1}"), MathTex(". . ") , MathTex("W_{n,n}") ],
             ],
        ).scale(0.5)       
        weights = MathTex("Weights of size (8,28)").move_to(m3).shift(UP*1.4).scale(0.5) 
        hidden_layer = MathTex("Hidden Layer").move_to(m3).shift(DOWN*1.4).scale(0.5)   
        self.play(ReplacementTransform(neural_network,m3))
        dimSize = VGroup()
        dimSize += MathTex("(8,28)").move_to(m3).shift(1.9*RIGHT + DOWN).scale(0.5) 
        self.play(ReplacementTransform(inputSize,dimSize[0]), Create(weights), Create(hidden_layer))

        m4 = MobjectMatrix(
            [  [MathTex("0.587 "), MathTex(" 0.124 "), MathTex(" . . ") , MathTex(" 0.374 ") ],
                [MathTex(" 0.267 "), MathTex(" 0.189 "), MathTex(" . . ") , MathTex(" 0.435 ") ],
                [MathTex(" . "), MathTex(" . "), MathTex(" . "), MathTex(" . ")],
                [MathTex(" . "), MathTex(" . "), MathTex(" . "), MathTex(" . ")],
              [MathTex(" 0.435 "), MathTex(" 0.123 "), MathTex(" . . ") , MathTex(" 0.388 ") ],
             ],
        ).scale(0.5)   
        self.play(ReplacementTransform(m3,m4))
        
        inputMatrix = MobjectMatrix(
            [  [MathTex( "0.55")] ,
                [MathTex("0.11")],
               [MathTex(".")],
                [MathTex(".")],
              [MathTex("0.00")],
             ],
        ).scale(0.5).move_to(m2)  

        self.play(ReplacementTransform(m2,inputMatrix),input1.animate.move_to(inputMatrix).shift(1.4*DOWN))
        self.play(inputMatrix.animate.move_to(m4), m4.animate.move_to(inputMatrix) ,hidden_layer.animate.move_to(input1),input1.animate.move_to(hidden_layer),FadeOut(dimSize), weights.animate.move_to(inputMatrix).shift(1.4*UP) )
        equals = MathTex(" = ").move_to(inputMatrix).shift(RIGHT)
        
        outputMatrix = MobjectMatrix(
            [  [MathTex( "0.01")] ,
                [MathTex("0.22")],
               [MathTex(".")],
                [MathTex(".")],
              [MathTex("0.65")],
             ],
        ).scale(0.5).move_to(equals).shift(RIGHT) 
        self.play(Create(equals), Create(outputMatrix), run_time = 2) 
        inputToOL = MathTex("Input to Output Layer").move_to(outputMatrix).shift(DOWN*1.4).scale(0.5) 
        self.play(Create(inputToOL), run_time = 2)



        ##for Output layer


        m5 = MobjectMatrix(
            [  [MathTex("0.123 "), MathTex(" 0.573 "), MathTex(" . . ") , MathTex(" 0.321 ") ],
                [MathTex(" 0.231 "), MathTex(" 0.342 "), MathTex(" . . ") , MathTex(" 0.522 ") ],
                [MathTex(" . "), MathTex(" . "), MathTex(" . "), MathTex(" . ")],
                [MathTex(" . "), MathTex(" . "), MathTex(" . "), MathTex(" . ")],
              [MathTex(" 0.211 "), MathTex(" 0.321 "), MathTex(" . . ") , MathTex(" 0.434 ") ],
             ],
        ).scale(0.5).move_to(m4)           

        weights1 = MathTex("Weights of size (4,8)").move_to(weights).scale(0.5)   
        outputLayer = MathTex("Output Layer").move_to(hidden_layer).scale(0.5)
        self.play(FadeOut(inputMatrix), outputMatrix.animate.move_to(inputMatrix), ReplacementTransform(hidden_layer,outputLayer), ReplacementTransform(m4,m5), ReplacementTransform(weights,weights1), inputToOL.animate.move_to(input1).scale(0.8),FadeOut(input1))

        finalOutput = MobjectMatrix(
            [  [MathTex( "0.98")] ,
                [MathTex("0.22")],
                [MathTex("0.43")],
              [MathTex("0.65")],
             ],
        ).scale(0.5).move_to(equals).shift(RIGHT)
        self.play(Create(finalOutput), run_time = 2) 
        box = SurroundingRectangle(finalOutput[0][0], color=YELLOW,)
        self.play(Create(box))
        directionVec = MobjectMatrix(
            [  [MathTex( "1")] ,
                [MathTex("0")],
                [MathTex("0")],
              [MathTex("0")],
             ],
        ).scale(0.5).move_to(finalOutput).shift(RIGHT)
        up = MathTex("UP").move_to(directionVec).scale(0.5).shift(RIGHT)
        self.play(Create(directionVec),Create(up) )
        #self.play(self.camera.frame.animate.scale(0.3).move_to(ORIGIN))
