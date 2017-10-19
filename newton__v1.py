#newton.py
from sympy import*

x=Symbol('x')
y=x*exp(1)**x-1 #此处输入目标方程对应的函数
dy=diff(y,x)
z=x-y/dy

c=float(input('请输入初始值')) #此处输入初始值
c1=c
c=z.subs('x',c)
err=10**(-5) #此处输入精度
i=0
while abs(c1-c)>err:
    i=i+1
    print('x'+str(i)+'='+str(c))
    c1=c
    c=z.subs('x',c)
    print('end')
