import random
import freegames
import turtle

def func(x, y):
    global ans_x,ans_y,score,fail
    if score < 10:
        if -235 + ans_x < x < -135 + ans_x and -235 + ans_y < y < -135 + ans_y:
            turtle.clear()
            score += 1
            print('答對了!! 目前分數: ', score)
            if score == 10:
                main2()
            else:
                main1()
        else:
            fail += 1
            print('累積失敗次數',fail)
    else:
        if -240 + ans_x < x < -180 + ans_x and -240 + ans_y < y < -180 + ans_y:
            turtle.clear()
            score += 1
            print('答對了!! 目前分數: ',score)
            if score >= 20:
                turtle.goto(-80,0)
                turtle.write('恭喜破關!!!',font=100)
            else:
                main2()
        else:
            fail += 1
            print('累積失敗次數',fail)
    #失敗3次則遊戲結束
    if fail > 2:
        turtle.clear()
        turtle.penup()
        turtle.goto(-100, 0)
        turtle.pencolor('black')
        turtle.write(f'遊戲結束! 最終分數:{score}',font=100)
        turtle.exitonclick()
def main1():  # 第一階段
    global ans_x,ans_y
    # 隨機給予答案方塊顏色
    R_rd = random.randint(0, 255)
    G_rd = random.randint(0, 255)
    B_rd = random.randint(0, 255)
    colors = (R_rd,G_rd,B_rd)
    ans_x = random.randint(0, 3) * 125
    ans_y = random.randint(0, 3) * 125
    for j in range(4):
        for i in range(4):
            freegames.square(-235 + i * 125, -235 + j * 125, 100, colors)
    # 繪製答案方塊
    ans_color = (abs(R_rd - 20), abs(G_rd - 20), abs(B_rd - 20))
    freegames.square(-235 + ans_x, -235 + ans_y, 100, ans_color)
def main2():   # 第二階段
    global ans_x,ans_y
    # 隨機給予答案方塊顏色
    R_rd = random.randint(0, 255)
    G_rd = random.randint(0, 255)
    B_rd = random.randint(0, 255)
    colors = (R_rd,G_rd,B_rd)
    ans_x = random.randint(0, 5) * 80
    ans_y = random.randint(0, 5) * 80

    for j in range(6):
        for i in range(6):
            freegames.square(-240 + i * 80, -240 + j * 80, 60, colors)

    # 繪製答案方塊
    ans_color = (abs(R_rd - 20), abs(G_rd - 20), abs(B_rd - 20))
    freegames.square(-240 + ans_x, -240 + ans_y, 60, ans_color)

#給予起始參數
ans_x,ans_y = 0,0
score = 0
fail = 0

#建立背景設定
sc = turtle.Screen()
sc.listen()
sc.onclick(func)
sc.setup(600, 600, 300, 100)
sc.tracer(False)
turtle.colormode(255)

#繪製第一關
main1()

turtle.done()