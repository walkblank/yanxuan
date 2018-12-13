from crazybee import userInterfaceShell

def userInterfaceShellLoop():
    userInterfaceShell()
    while True:
        print('______________')
        print('搜索完成，是否继续搜索:')
        print("0 继续")
        print("1 退出")
        print('______________')
        select = input("请输入==>")
        if select == '0':
            userInterfaceShell()
        if select == '1':
            break

if __name__ == '__main__':
    userInterfaceShellLoop()
