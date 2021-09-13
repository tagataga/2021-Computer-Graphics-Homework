import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((205,205))

grid_step = int(input("请输入网格边长："))

plt.xticks(np.arange(2.5,207.5,grid_step))
plt.yticks(np.arange(2.5,207.5,grid_step))
plt.grid()  # 生成网格

#颜色列表
col1 = 'red'
col2 = 'lime'
col3 = 'blue'
col4 = 'aqua'
col5 = 'yellow'
colorlist = [col1,col2,col3,col4,col5]

def draw(x,y,n): #画点(x,y)，颜色为colorlist中的第(n-1)个
    x += int(img.shape[0]/2)
    y += int(img.shape[1]/2)
    img[-y,x] = grid_step
    plt.plot(x,y, 'o', color=colorlist[n-1], markersize=1, alpha=0.5)
pass

for n in range(1,6,1):  #n为圆的编号，20*n为圆的半径
    (x,y) = (20*n-(20*n%grid_step),0)   #水平最右边的第一个点，取在栅格上
    P_k = -2*20*n + 3
    while x>=y:
        if P_k>=0: #外侧候选点离圆弧更远
            P_k_next = P_k - 4*x + 4*y + 10
            (x_next,y_next) = (x-grid_step,y+grid_step)
        else:   #内侧候选点离圆弧更远
            P_k_next = P_k +4*y +6
            (x_next,y_next) = (x,y+grid_step)
    #对称法画其他地方
        draw(x,y,n)
        draw(-x,y,n)
        draw(x,-y,n)
        draw(-x,-y,n)
        draw(y,x,n)
        draw(y,-x,n)
        draw(-y,x,n)
        draw(-y,-x,n)
    #更新坐标和P_k
        (x,y) = (int(x_next),int(y_next))
        P_k = P_k_next
pass

plt.imshow(img)
plt.show()
