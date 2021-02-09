import paramiko,time
class Ssh:
    def __init__(self,ip,port,username,password,command):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.command = command

    def result(self):
        con = paramiko.SSHClient()
        con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        con.connect(hostname=self.ip,port=self.port,username=self.username,password=self.password,allow_agent=False,look_for_keys=False)
        stdin, stdout, stderr = con.exec_command(self.command,get_pty=True)
        time.sleep(float(1))
        result = str(stdout.read(),'utf8')
        con.close()
        return result
class Ssh_rs:
    def __init__(self,ip,port,username,password,command):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.command = command

    def result(self):
        con = paramiko.SSHClient()
        con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        con.connect(hostname=self.ip,port=self.port,username=self.username,password=self.password,allow_agent=False,look_for_keys=False)
        con_shell = con.invoke_shell()
        result = con_shell.send(self.command+'\n'*50)
        time.sleep(float(1))
        result = con_shell.recv(99999)
        con_shell.close()
        return result

