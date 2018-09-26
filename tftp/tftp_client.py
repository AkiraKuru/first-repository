from socket import * 
import sys 
import time 

#实现基本的请求功能
class TftpServer(object):
    def __init__(self,sockfd):
        self.sockfd = sockfd 
    def do_list(self):
        pass
    def do_get(self,filename):
        pass 
    def do_put(self,filename):
        pass
    def do_quit(self):
        self.sockfd.send(b'Q')


#套接字连接
def main():
    if len(sys.argv) < 3:
        print("argv is error")
        return 
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)

    sockfd = socket()
    sockfd.connect(ADDR)

    tftp = TftpServer(sockfd) #tftp对象调用请求方法

    while True:
        print("=======命令选项========")
        print("******* list *********")
        print("*******get file ******")
        print("*******put file ******")
        print("******* quit *********")
        print("======================")

        cmd = input("请输入命令>>")

        if cmd.strip() == 'list':
            tftp.do_list()
        elif cmd[:3] == "get":
            filename = cmd.split(' ')[-1]
            tftp.do_get(filename)
        elif cmd[:3] == "put":
            filename = cmd.split(' ')[-1]
            tftp.do_put(filename)
        elif cmd.strip() == "quit":
            tftp.do_quit()
            sockfd.close()
            sys.exit("欢迎使用") 
        else:
            print("请输入正确的命令!!!")
            continue
       
if __name__ == "__main__":
    main()
