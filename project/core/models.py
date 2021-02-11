import pandas as pd

class Crpage:
    def __init__(self,path):
        '''获取文件url'''
        self.path = path
        self.xlsdb = pd.read_excel(self.path,engine='openpyxl',nrows=200)
    def xlsdb_columns(self):
        '''读取表头'''
        self.xlsdb_columns = self.xlsdb.columns.values
        return self.xlsdb_columns
    def readxls(self):
        '''读取当前xlsx所有内容'''
        self.readxls = self.xlsdb.loc[0:].values
        return self.readxls
    def dev_count(self):
        '''读取当前所有设备数量'''
        self.dev_count = len(self.readxls)
        return self.dev_count
    def crsum(self):
        '''读取当前所有机房'''
        self.crsum = set([vk for vk in set([i[1] for i in self.readxls])])
        return self.crsum