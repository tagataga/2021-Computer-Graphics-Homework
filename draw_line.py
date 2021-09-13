import numpy as np
import matplotlib.pyplot as plt

plt.axis([-201,201,-201,201])#设置坐标范围
ax = plt.gca()
ax.set_facecolor('black')#设置plot背景颜色

#颜色列表
col1 = 'blue'
col2 = 'grey'
col3 = 'white'
col4 = 'yellow'
col5 = 'pink'
col6 = 'red'
col7 = 'aqua'
col8 = 'green'
colorlist = [col1,col2,col3,col4,col5,col6,col7,col8]

#画点
def draw(x,y,n):
    plt.plot(x,y, '.', color=colorlist[n-1], markersize=0.8, alpha=1.0)

#按颜色分区，从第一象限开始，将八个区域称为abcdefgh
def XYarea(x,y):
    if(x>0):    #区域abcd
        if(y>0):    #区域ab
            if(x<y):    #区域a
                area = 1
            else:    #区域b
                area = 2
        else:   #区域cd
            if(x>(-y)): #区域c
                area = 3
            else:   #区域d
                area = 4
    else:   #区域efgh
        if(y<0):    #区域ef
            if((-x)<(-y)):  #区域e
                area = 5
            else:   #区域f
                area = 6
        else:   #区域gh
            if(y<(-x)): #区域g
                area = 7
            else:   #区域h
                area = 8
    return area
pass

#过(0,0)和(x,y)的360°Bresenham直线
def BresenhamLine(x,y):
    area = XYarea(x,y)
    delta_x = x
    delta_y = y
    i = 0
    x1 = 0
    y1 = 0
    if(area==1):   #区域a，xy交换
        temp = delta_x
        delta_x = delta_y
        delta_y = temp
        NError = 2*delta_y-delta_x
        while(i<=delta_x):
            draw(x1,y1,area)
            if(NError >= 0):
                x1 = x1 + 1
                NError = NError - 2*delta_x
            y1 = y1 + 1
            NError = NError + 2*delta_y
            i = i + 1
    elif(area==2):  #区域b
        NError = 2*delta_y-delta_x
        while(i<=delta_x):
            draw(x1,y1,area)
            if(NError >= 0):
                y1 = y1 + 1
                NError = NError - 2*delta_x
            x1 = x1 + 1
            NError = NError + 2*delta_y
            i = i + 1
    elif(area==3):  #区域c，y取负值
        delta_y = -delta_y
        NError = 2*delta_y-delta_x
        while(i<=delta_x):
            draw(x1,y1,area)
            if(NError >= 0):
                y1 = y1 - 1
                NError = NError - 2*delta_x
            x1 = x1 + 1
            NError = NError + 2*delta_y
            i = i + 1
    elif(area==4):  #区域d，y取负值，且xy交换
        delta_y = -delta_y
        temp = delta_x
        delta_x = delta_y
        delta_y = temp
        NError = 2*delta_y-delta_x
        while(i<=delta_x):
            draw(x1,y1,area)
            if(NError >= 0):
                x1 = x1 + 1
                NError = NError - 2*delta_x
            y1 = y1 - 1
            NError = NError + 2*delta_y
            i = i + 1
    elif(area==5):  #区域e,xy都取负值，且交换
        delta_x = -delta_x
        delta_y = -delta_y
        temp = delta_x
        delta_x = delta_y
        delta_y = temp
        NError = 2*delta_y-delta_x
        while(i<=delta_x):
            draw(x1,y1,area)
            if(NError >= 0):
                x1 = x1 - 1
                NError = NError - 2*delta_x
            y1 = y1 - 1
            NError = NError + 2*delta_y
            i = i + 1
    elif(area==6):  #区域f,xy都取负值
        delta_x = -delta_x
        delta_y = -delta_y
        NError = 2*delta_y-delta_x
        while(i<=delta_x):
            draw(x1,y1,area)
            if(NError >= 0):
                y1 = y1 - 1
                NError = NError - 2*delta_x
            x1 = x1 - 1
            NError = NError + 2*delta_y
            i = i + 1
    elif(area==7):  #区域g,x取负值
        delta_x = -delta_x
        NError = 2*delta_y-delta_x
        while(i<=delta_x):
            draw(x1,y1,area)
            if(NError >= 0):
                y1 = y1 + 1
                NError = NError - 2*delta_x
            x1 = x1 - 1
            NError = NError + 2*delta_y
            i = i + 1
    elif(area==8):  #区域h,x取负值,且xy交换
        delta_x = -delta_x
        temp = delta_x
        delta_x = delta_y
        delta_y = temp
        NError = 2*delta_y-delta_x
        while(i<=delta_x):
            draw(x1,y1,area)
            if(NError >= 0):
                x1 = x1 - 1
                NError = NError - 2*delta_x
            y1 = y1 + 1
            NError = NError + 2*delta_y
            i = i + 1
pass

#每5°画一条直线
i = 1
while(i<=72):
    x = round(np.sin((5*i)*np.pi/180)*200)
    y = round(np.cos((5*i)*np.pi/180)*200)
    BresenhamLine(x,y)
    i = i+1

plt.show()
