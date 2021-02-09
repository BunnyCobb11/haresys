#coding: -*- utf-8 -*-
import paramiko,time
'''
1.密钥文件在根目录。
2.TXT文本6行包含主机远程信息，密钥文件名保持一致。
'''

times = time.strftime("%Y%m%d %H %M %S",time.localtime())

def main():
    Instance()

class Startd:
    def ip(self): return self.host['ip']
    def ports(self): return self.host['ports']
    def user(self): return self.host['user']
    def passwd(self): return self.host['passwd']
    def key(self): return self.host['key']
    def command(self): return self.host['command']

class Host(Startd):
    host = dict(ip = '',
                ports = '',
                user = '',
                passwd = '',
                key = '',
                command = ''
                )

class Dev(Startd):
    with open('host.txt','rt',encoding='utf-8') as h:
        hs = h.read()
        dev = Host()
        dev.host['ip'] = hs.splitlines()[0]
        dev.host['ports'] = hs.splitlines()[1]
        dev.host['user'] = hs.splitlines()[2]
        dev.host['passwd'] = hs.splitlines()[3]
        dev.host['key'] = hs.splitlines()[4]
        dev.host['command'] = hs.splitlines()[5]

def Instance():
    try:
        dev2 = Host()
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        key = paramiko.RSAKey.from_private_key_file(dev2.key(), password=dev2.passwd())
        ssh.load_system_host_keys()  
        ssh.connect(hostname=dev2.ip(), port=dev2.ports(), username=dev2.user(), pkey=key)
        stdin, stdout, stderr = ssh.exec_command(dev2.command())
        result = str(stdout.read(),'utf8')
        with open('host-key-result.txt','wt') as f:
            f.write(result) 
    except Exception as err:
        print('Error:',err.__class__,err)
    finally:
        ssh.close()
        print('END:',times)

if __name__ == "__main__":   main()