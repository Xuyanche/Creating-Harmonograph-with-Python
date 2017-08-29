# Creating-Harmonograph-with-Python
利用python及其中的pygame组件绘制harmonograph。同时可以通过serail组件利用串口控制相关硬件，在纸上绘制出曲线。


## Harmonograph介绍
harmonograph是一类利用单摆的机械结构画出的图形。他们遵循同一类公式：  
x(t)=A_{1}\sin(tf_{1}+p_{1})e^{-d_{1}t}+A_{2}\sin(tf_{2}+p_{2})e^{-d_{2}t}  
y(t)=A_{3}\sin(tf_{3}+p_{3})e^{-d_{3}t}+A_{4}\sin(tf_{4}+p_{4})e^{-d_{4}t}  
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

这样如果可以看到下面打出了pygame的版本号，就可以认为你的Python已经装好了pygame的库。比如我的Python就会回复我：

    1.9.3
    
然而serial并不支持这个方法。所以在我的程序里还有一个专门用来检测你的serial是不是在运作。这个程序其实也很简陋，不过只是“检测serial是不是在运作”这种小事还是可以做到的。

## 所用硬件说明
其实可以替代的有很多，这里只是列出我们使用的硬件罢了。   具体参考instructable的这个项目：http://www.instructables.com/id/Polargraph-Drawing-Machine/  
其中，我们是使用了一套自动窗帘的齿轮和链子作为拉动笔的组件。步进电机则是在淘宝上卖的，一步是1.8°，如果电机和这里使用的不同，那么pygame界面上的位置和实际画出的位置换算时的公式就会受电影像。当然不只是这个，两个电机之间的距离也会对这个公式有影响。而至于后面的垫住纸的板子，我们用的是一张废弃的桌子的桌板。
