import os
value=""
def main():
    autoComplete="Write()"
    print("欢迎使用代码自动补全系统,请输入1开始使用，输入0退出，输入cls清屏")
    while True:
        value=input()
        if(value=="1"):
            print("欢迎使用,请尝试开始输入英文代码，如果导入的py文件中存在你输入的方法，将会自动进行补充")
        elif(value=="0"):
            print("感谢使用，此程序开发者128hh，学历：职高，但不要瞧不起职高生")
            break
        #如果输入的代码存在已经存在的API的关键字，则进行自动补充
        elif(value in autoComplete):
            print("你输入的代码中存在关键字->\n自动填充代码为->Write()")
            print(autoComplete)
        elif(value=="cls"):
            #只做了linux的东西
            os.system("clear")
        else:
            print("错误，不存在你输入的指令！")
    pass
main()
