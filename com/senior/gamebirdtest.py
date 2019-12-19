import pygame
import sys
import random

class Bird(object):
    """定义一个鸟类"""
    def __init__(self):
        """定义一个初始化方法"""
        self.birdRect=pygame.Rect(65,50,50,50)  # 鸟的矩形
        # 定义鸟的三种状态列表
        self.birdStatus=[pygame.image.load("..\\assets\\bird0_0.png"),pygame.image.load("..\\assets\\bird0_1.png"),pygame.image.load("..\\assets\\bird0_dead.png")]
        self.status=0   # 默认小鸟的飞行状态
        self.birdX=120  # 鸟所在的x轴坐标
        self.birdY=350  # 鸟所在的y轴坐标，即上下飞行的高度
        self.jump=False  # 默认情况小鸟自动降落
        self.jumpSpeed=10  # 跳跃高度
        self.gravity=5   # 重力
        self.dead=False  # 默认小鸟生命状态为活着

    def birdUpdate(self):
        if self.jump:
            # 小鸟跳跃
            self.jumpSpeed -=1  # 速度递减，上升越来越慢
            self.birdY -=self.jumpSpeed  # 鸟的Y轴坐标减小，小鸟上升
        else:
            # 小鸟坠落
            self.gravity+=0.2  # 重力递减，下降越来越快
            self.birdY+=self.gravity  # 鸟的Y轴坐标增加，小鸟下降

        self.birdRect[1]=self.birdY  # 更改y轴位置

class Pipeline(object):
    """定义一个管道类"""
    def __init__(self):
        """定义一个初始化方法"""
        self.wallx=400  # 管道所在x轴坐标
        self.pineUp=pygame.image.load("..\\assets\\pipe_down.png")  # 加载上管道图片
        self.pineDwon=pygame.image.load("..\\assets\\pipe_up.png")   # 加载下管道图片

    def updatePipelline(self):
        """水平移动"""
        self.wallx-=5  # 管道x轴坐标递减，即管道向左移动
        # 当管道运行到一定位置，即小鸟飞越管道，分数加1，并且重置管道
        if self.wallx<-80:
            global score
            score +=1
            self.wallx=400

def createMap():
    """定义一个创建地图的方法"""
    screen.fill((255,255,255))   # 填充颜色
    screen.blit(background,(0,0))   # 填入到背景

    # 显示管道
    screen.blit(Pipeline.pineUp,(Pipeline.wallx,-100))   # 上管道坐标位置
    screen.blit(Pipeline.pineDwon,(Pipeline.wallx,400))   # 下管道坐标位置
    Pipeline.updatePipelline()   # 管道移动

    # 显示小鸟
    if Bird.dead:   # 撞管道的状态
        Bird.status=2
    elif Bird.jump:   # 起飞状态
        Bird.status=1
    screen.blit(Bird.birdStatus[Bird.status],(Bird.birdX,Bird.birdY))  # 设置小鸟的坐标
    Bird.birdUpdate()   # 鸟移动

    #显示分数
    font = pygame.font.Font(None, 56)   # 创建字体对象
    screen.blit(font.render("Score:"+str(score),-1,(255,255,255)),(100,50))  # 设置颜色及坐标位置

    pygame.display.update()   # 更新显示

def checkDead():
    # 上方管子的矩形位置
    upRect=pygame.Rect(Pipeline.wallx,-100,Pipeline.pineUp.get_width() -10,Pipeline.pineUp.get_height())
    # 下方管子的矩形位置
    downRect=pygame.Rect(Pipeline.wallx,400,Pipeline.pineDwon.get_width()-10,Pipeline.pineDwon.get_height())
    # 检测小鸟与上下方管子是否碰撞
    if upRect.colliderect(Bird.birdRect) or downRect.colliderect(Bird.birdRect):
        Bird.dead=True
    # 检测小鸟是否废除上下边界
    if not 0<Bird.birdRect[1]<height:
        Bird.dead=True
        return True
    else:
        return False
def getResutl():
    final_text1="Game Over"
    final_text2="Your final score is:"+str(score)
    ft1_font=pygame.font.SysFont("Arial",70)    # 设置第一行文字字体
    ft1_surf=ft1_font.render(final_text1,1,(242,3,36))   # 设置第一行文字颜色
    ft2_font=pygame.font.SysFont("Arial",50)   # 设置第二行文字字体
    ft2_surf=ft2_font.render(final_text2,1,(253,177,6))   # 设置第二行文字颜色
    # 设置第一行文字显示位置
    screen.blit(ft1_surf,[screen.get_width()/2-ft1_surf.get_width()/2,100])
    # 设置第二行文字显示位置
    screen.blit(ft2_surf,[screen.get_width()/2-ft2_surf.get_width()/2,200])
    pygame.display.flip()   # 更新整个待显示的Surface对象到屏幕上

if __name__=='__main__':
    """主程序"""
    pygame.init()   # 初始化pygame
    size=width,height=365,650  # 设置窗口
    screen=pygame.display.set_mode(size)  # 显示窗口
    clock=pygame.time.Clock()  # 设置时钟
    Pipeline=Pipeline()  # 实例化管道类
    Bird=Bird()   # 实例化鸟类
    score=0   # 初始化分数
    while True:
        clock.tick(60)   # 每秒执行60次
        # 轮询事件
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if (event.type==pygame.KEYDOWN or event.type== pygame.MOUSEBUTTONDOWN) and not Bird.dead:
                Bird.jump=True  # 跳跃
                Bird.gravity=5  # 重力
                Bird.jumpSpeed=10   # 跳跃速度

        background=pygame.image.load("..\\assets\\background.png")  # 加载背景图片
        if checkDead():   # 检测小鸟生命状态
            getResutl()    # 如果小鸟死亡，显示游戏总分数
        else:
            createMap()  # 绘制地图

pygame.quit()  # 退出

