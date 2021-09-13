# 2021-Computer-Graphics-Homework
Computer Graphics Homework 2021
计算机图形学作业-图元绘制

要求:
任务1：
利用你熟悉的绘图环境，实现Bresenham直线光栅化算法，并用你实现的绘制直线的算法替代系统中提供的直线绘制函数，绘制如图1中的各种线段。
任务2
(1).利用你熟悉的绘图环境，实现基于Bresenham算法思想的中点圆光栅化算法。
(2).利用(1)中实现的算法绘制图2中的各种圆，底图中的栅格线也需要绘制，绘制点为你自己定义的栅格点（即底图栅格点），而不是屏幕上的栅格点。
要求栅格的大小可以调整，并且当栅格的大小调整后，圆的逼近点要调整到新的自定义光栅点上。


draw_line.py:
1.函数draw(x,y,n)搭配colorlist，用指定颜色在画布上显示指定的点(x,y)
2.函数XYarea(x,y)，将指定的点(x,y)划分到八个区域之一
3.函数BresenhamLine(x,y)，调用draw(x,y,n)，用Bresenham算法绘制过点(0,0)和点(x,y)的直线
4.用while语句循环求出每条直线的终点并调用BresenhamLine(x,y)绘图

draw_circle.py:
1.键盘输入grid_step定义可调节的栅格大小
2.函数draw(x,y,n)搭配colorlist，用指定颜色在画布上显示指定的点(x,y)
3.基于Bresenham算法思想的中点圆光栅化算法，八等分画5个圆
4.圆的逼近点与光栅点的位置关系有待调节
