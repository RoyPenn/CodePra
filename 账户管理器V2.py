#---------------------------------------------------------#程序信息
#账户管理器 V2版本 文件存储版本
#maoge 2017.6.29
import os,sys
#---------------------------------------------------------#变量定义
accounts={}
fileName="D:\CodePra\accounttest.txt"; #D:\CodePra
#---------------------------------------------------------#函数定义
#界面显示
def show():
    print("====================")
    print("请选择操作")
    print("1:查看账户列表")
    print("2:新增账户")
    print("3:删除账户")
    print("4:保存到文件")
    print("5:退出程序")
    print("====================")
    return input()
#读取文件
def readFile(fileName):
    if os.path.isfile(fileName)==True:#文件存在
        file=open(fileName,"r")
        global accounts
        accounts=eval(file.read())
        for temp in accounts.keys():
            print(temp)
        file.close();
#写入文件
def writeFile(fileName):
    file=open(fileName,"w")#w表示写 a表示追加模式
    global accounts
    file.write(str(accounts));
    file.close()#读写完毕一定要关闭文件对象
#显示已有账户信息
def showAccounts():
    if len(accounts)==0:
        print("暂无账户")
    else:
        print("========账户列表如下")
        for temp in accounts.keys():
            print(temp)
        print("可以输入@+账户名称，查询账户密码")
        print("========")
#处理无效指令及@指令
def dealAt(user):
    if user.startswith("@"):
        str=user.lstrip("@")
        if str not in accounts.keys():
            print("查无此账户！")
        else:
            print(str+"账户的密码为："+accounts[str])
    elif user.startswith("$"):
        str=user.lstrip("$")
        if str not in accounts.keys():
            print("查无此账户！")
        else:
            accounts.pop(str)
            print("删除账户成功！")
    elif user.startswith("#"):
        str=user.lstrip("#")
        username=str.split("#")[0]
        userpass=str.split("#")[1]
        accounts[username]=userpass
        print("添加账户成功！")
    else:
        print("无效指令！")


#---------------------------------------------------------#主程序
print("欢迎使用稍微有一点完善的账户管理器V2版本")
readFile(fileName)
while(True):
    user=show()
    if user=="5":
        print("欢迎您下次使用")
        sys.exit()
    elif user=="1":
        showAccounts()
    elif user=="2":
        print("可以输入#账户名#密码新增账户")
    elif user=="3":
        print("可以输入$账户名删除账户")
    elif user=="4":
        writeFile(fileName)
        print("已保存到文件")
    else:
        dealAt(user)
