# Creating-Harmonograph-with-Python
利用python及其中的pygame组件绘制harmonograph。同时可以通过serail组件利用串口控制相关硬件，在纸上绘制出曲线。


## Harmonograph介绍
harmonograph是一类利用单摆的机械结构画出的图形。他们遵循同一类公式：  
x(t)=A<sub>1</sub> * sin(tf<sub>1</sub> + p<sub>1</sub>) * e<sup>-d<sub>1</sub>t</sup> + A<sub>2</sub> * sin(tf<sub>2</sub> + p<sub>2</sub>) * e<sup>-d<sub>2</sub>t</sup>    
y(t)=A<sub>3</sub> * sin(tf<sub>3</sub> + p<sub>3</sub>) * e<sup>-d<sub>3</sub>t</sup> + A<sub>4</sub> * sin(tf<sub>4</sub> + p<sub>4</sub>) * e<sup>-d<sub>4</sub>t</sup>    
通过调整其中A,p,d,p等参数就可以得到许多形态各异的Homonograph了。  
具体定义及相关信息参见维基百科。  
Homograph维基：https://en.wikipedia.org/wiki/Harmonograph

## pygame与serial安装方法
两个组件的安装方法和具体函数及用法请参考他们的官网。  
pygame官网：http://www.pygame.org/  
serial官网：https://pythonhosted.org/pyserial/index.html  
官网上有各种平台上的安装步骤。我是在win10的平台上运行的，其他平台上的方法也可以在这个网站上找到。  
注意：我使用的是Python3，并自己添加了pygame和serail组件。如果是Python2，你的Python可能自带pygame的库。这时候可以在Python shell里输入：  

    >>> import pygame
    >>> print('pygame.ver')

这样如果可以看到下面打出了pygame的版本号，就可以认为你的Python已经装好了pygame的库。比如我的Python就会回复我：`1.9.3`
    
然而serial并不支持这个方法。所以在还有一个简单的程序专门用来检测你的serial是不是在运作

## 所用硬件说明
具体请参照instructable的这个项目：http://www.instructables.com/id/Polargraph-Drawing-Machine/  
很多部件是可以替换的，仅仅供大家参考。

## 程序列表
- test_serial.py  
用于检测你的serial库是不是在运作
- Harmonograph_drawing.py  
在屏幕上用pygame画出harmonograph并保存其图片于工作目录中，文件名就是参数。
- harmonograph_drawing_random.py  
同上，但是所有参数都是随机设定的。
- harmonograph_drawing_full.py  
在harmonograph_drawing.py的基础上调用serial库，可以让你在纸上画出Harmonograph。
