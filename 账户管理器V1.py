#欢迎界面
print("欢迎使用异常不完善的账户管理器")

#数据存储
accounts={"qq":"qq123456","微信":"weixin123456","邮箱":"mail12334"};

#交互函数
def show():
    print("已有账户列表：")
    for temp in accounts.keys():
        print(temp)
    print("请输入账户名称查询密码，或者输入exit退出程序:")
    return input();

#主程序
while(True):
    str=show()
    if(str=="exit"):
        break
    if str not in accounts.keys():
        print("无此账户，请重新输入:")
    else:
        print(str+"账户的密码为："+accounts[str])
print("Game Over")