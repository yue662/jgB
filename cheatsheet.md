# cheat sheet

1、深拷贝：得到完全独立的两变量。

浅拷贝：将对象多用一个变量记录，两变量一起改变。

```
b=a.copy() # 浅拷贝 

import copy
c=a.deepcopy() # 深拷贝
```

当然，对一维数组可用切片 b=a[:]。

2、保留小数（对num保留n位小数）

```
nums="{:.nf}".format(num)
# 或
nums="%.nf" % num
```

3、记忆化

```
from functools import lru_cache
@lru_cache
def f(x):
```

在函数前加@lru_cache，当运行到重复的自变量时自动调用之前结果。但自变量中不可含可变类型参数，如 list。

4、临时函数 lambda

格式形如：lambda arguments: expression。

arguments为一个或多个参量，expression为计算表达式，如：

```
x = lambda a : a + 10
```

可直接储存给函数名f，应用时直接f(x)。或是在其他函数之中，如：

```
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # 输出: [1, 4, 9, 16, 25]
```

5、输出2进制：bin(x)   （x为整数int型）(结果有0b前缀)

绝对值: abs(x)

`math.ceil(number)`向上取整,`math.floor(number)` 或a//b向下取整

取模：a%b  求和 ：sum()

6、列表化:list(x)

- 字符串:`list('abc')==['a','b','c']`
- 迭代器/生成器:
  - `list(range(4))==[0,1,2,3]`
  - `list(map(int,input().split())==[2,5,1]`(假设输入'2 5 1')
  - `list(enumerate([2,5,1]))==[(0,2),(1,5),(2,1)]`（即前方赋一个位置变量）

7、集合：无重复数组

- 添加:`s.add(x)`
- 查询:`x (not) in s`,**O(1)**
- 删除:
  - `s.remove(x)`,**O(1)**
  - `s.discard(x)`,**O(1)**:删除x,如果没找到x就无事发生
- 集合运算:
  - 并:`a|b`
  - 交:`a&b`
  - 差:
    - `a-b`,注意这是表示∈a且∉b的元素的集合, 如`{1}-{1,2}==set(),{1,2}-{1}=={2}`
    - `a^b`,对称差,等于a|b-a&b
  - `a>=b,a>b,a<=b,a<b`,表示集合的包含关系,如果既不是子集也不是超集也返回False
- 构建集合:
  - 空集:`a=set()`
  - 集合化:set(x),x是列表\元组\字典(a是字典则会返回所有键组成的集合)

8、字典

- 删除:`del d[key]`
- 弹出:
  - `d.pop(key)`
- 获取:`d.get(key)`,返回键对应的值，如果key不在字典则返回None而不报错
  - `d.get(key,dft)`可以在key不在字典时返回默认值dft
- 键or值们:`d.keys()`,`d.values()`

9、欧拉筛：筛出1<=i<=n所有的素数

```
def ES(n):
  isprime=[True for _ in range(n+1)]
  prime=[]
  for i in range(2,n+1):
      if isprime[i]:
          prime.append(i)
      for j in range(len(prime)):
          if  i*prime[j]>n:break
          isprime[i*prime[j]]=False
          if i%prime[j]==0 :break
  return prime
```

求最大公约数：

```
def gcd(a, b):
  while b:
    a, b = b, a%b
  return a
```

10、ASCII码：`ord(x)` :输出对应ASCII码   `chr(x)` 输出对应字符

`s.lower()`： 将字符串全部转换为小写   `s.upper()`： 将字符串全部转换为大写

`s.capitalize()`:  将字符串化为仅有首字母大写

`s.lstrip()`： 删掉左侧空格    `s.rstrip()`： 删掉末尾空格     `s.title()`: 翻转大小写

11、index: 输出第一次检索到字符串所在位置（substring为字符串，另两个为开始与截止）

`str.index(substring, beg=0, end=len(string))`

end='' : print输出时以什么结尾，默认为换行符'\n',其余情况不会换行。

count:输出字符串中字母或子字符串个数

 `str.count(sub, start= 0,end=len(string))`

12、列表排序：

`list.sort( key=None, reverse=False)`

key为排序依据，结合临时函数 lambda运行，False为升序排列，True为降序排列

`list.reverse()`: 将列表反向

13、`global x` :定义全局变量（用于函数内）

try...except: 异常处理

```
try:
    代码
expect x:
    异常后的处理
```

x为错误类型，也可无x，对所有异常均判别。

`EOFError`：无输入，即输入为给定数量与结束标记，用于判断是否还有输入。

`KeyError`：字典里没有这个键。

14、decimal：高精度小数（y可为数字，也可用字符串导入）

```
import decimal  #导入模块
x=decimal.Decimal(y)
```
