#目录的遍历

#导入os模块
import os

#获取目录信息
print("请输入目录信息")
dir=input()
while os.path.exists(dir)==False:
    print("目录不存在，请重新输入")
    dir=input()

#对一个目录的处理函数
def ShowPathInfo(path):
    print("*****")
    for folder,subFolders,files in os.walk(path):
        print("\n==当前遍历目录:"+folder)
        for file in files:
            print("[文件]："+file)
        for subFolder in subFolders:
            print("[文件夹]："+subFolder)
            ShowPathInfo(subFolder)

#主程序
print("==========遍历开始")
ShowPathInfo(dir)
print("==========遍历结束")