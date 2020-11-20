#解析器
def openFile():
    #打开Code.py
#    with open("Code.py") as target:
        #readline()
        #如果检测到import语句
        #读取import语句后面的内容
        #打开 当前路径根目录+语句后面的内容+.py文件
        #解析def ——读取文件内所有的def() 定义函数
    #    pass
    pass

#解析def #最小化解析单元模块
def parseDef():
    testcode="def a():\n print('a')\n pass"
    print(testcode)
    tmp1=testcode.split("\n")
    print(tmp1)
    pass
parseDef()
