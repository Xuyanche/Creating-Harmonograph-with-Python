# Creating-Homonograph-with-Python
利用python及其中的pygame组件绘制homonograph。同时可以通过serail组件利用串口控制相关硬件，在纸上绘制出曲线。


## Homonograph介绍
homonograph是一类利用单摆的机械结构画出的图形。他们遵循同一类公式：  
x(t)=A_{1}\sin(tf_{1}+p_{1})e^{-d_{1}t}+A_{2}\sin(tf_{2}+p_{2})e^{-d_{2}t}  
y(t)=A_{3}\sin(tf_{3}+p_{3})e^{-d_{3}t}+A_{4}\sin(tf_{4}+p_{4})e^{-d_{4}t}  
通过调整其中A,p,d,p等参数就可以得到许多形态各异的Homonograph了。  
具体定义及相关信息参见维基百科。  
Homograph维基：https://en.wikipedia.org/wiki/Homograph

## pygame与serial安装方法  
两个组件的具体函数及用法请参考他们的官网。  
pygame官网：http://www.pygame.org/  
serial官网：https://pythonhosted.org/pyserial/index.html  
官网上有标准的
注意：我使用的是Python3，并自己添加了pygame和serail组件。在Python2上能否成功我也不知道。

## 所用硬件说明
其实可以替代的有很多，这里只是列出我们使用的硬件罢了。 具体参考instructable的这个项目：http://www.instructables.com/id/Polargraph-Drawing-Machine/ 
### 电子器件
+ arduino
主要是使用arduino的串口功能，所以说在可以在电脑上安装arduino的编程软件，这是最快速的为你的电脑装上arduino的串口驱动的方法
+ 步进电机 * 2
我们使用的是淘宝上卖的步进电机，一步1.8°。所使用的步进电机会影响到程序中pygame的显示与实际的换算公式。



