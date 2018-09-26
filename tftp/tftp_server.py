'''
tftp 文件服务器程序
'''
from socket import * 
import os 
import signal 
import sys 
import time 

#文件库路径
FILE_PATH = "/home/tarena/"

#实现服务器功能模块
class TftpServer(object):
    def __init__(self,connfd):
        self.connfd = connfd
    def do_list(self):
        pass
    def do_get(self,filename):
        pass
    def do_put(self,filename):
        pass 

#流程控制,创建套接字连接,接收请求
def main():
    HOST = '0.0.0.0'
    PORT = 8888
    ADDR = (HOST,PORT)

    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(5)
    
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    print("Listen to port 8888....")

    while True:
        try: 
            connfd,addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue
        print("客户端登录:",addr)
        #创建父子进程
        pid = os.fork()
        if pid < 0:
            print("创建子进程失败")
            continue
        elif pid == 0:
            sockfd.close()
            tftp = TftpServer(connfd)
            #接收客户端请求
            while True:
                data = connfd.recv(1024).decode()
                if data[0] == 'L':
                    tftp.do_list()
                #data ==> G filename
                elif data[0] == 'G':
                    filename = data.split(' ')[-1]
                    tftp.do_get(filename)
                elif data[0] == 'P':
                    filename = data.split(' ')[-1]
                    tftp.do_put(filename)
                elif data[0] == 'Q':
                    print("客户端退出")
                    sys.exit(0)

        else:
            connfd.close()
            continue

if __name__ == "__main__":
    main()