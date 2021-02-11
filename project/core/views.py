# coding: utf8
from flask import Flask,request,render_template,Blueprint,redirect
import pandas as pd
import os
from project.core.models import Crpage
from project.collection.mail import Emailmodule

core = Blueprint('core',__name__)

@core.route('/')          #首页
def index():
    emailDB = Emailmodule()
    receive = emailDB.receive_imap4()
    result_type = type(receive)
    result_count = receive.count('\n')
    result_sum = len(receive)
    return render_template('index.html',result_type=result_type,receive=receive,result_count=result_count,result_sum=result_sum)

@core.route('/croom',methods=['GET','POST'])  #IDC管理页面
def croom():
    d = Crpage('D:\\virtualenv\\ven-flask\\data\\idccr.xlsx')
    return render_template('croom.html',
                           xlsdb_columns=d.xlsdb_columns(),#读取表头
                           readxls=d.readxls(),#获取当前xlsx所有行内容
                           device_count=d.dev_count(),#读取当前所有设备数量
                           crsum=d.crsum()#获取当前所有机房
                          )
@core.route('/croompage')  #设备页面
def croompage():
    d = CRPAGE('D:\\virtualenv\\ven-flask\\data\\idccr.xlsx')
    xlsdb_columns = d.xlsdb_columns()
    readxls = d.readxls()
    if request.method == 'GET':
        mangeip = request.args.get('mangeip')
        crdev = request.args.get('crdev')
    return render_template('croompage.html',xlsdb_columns=xlsdb_columns,readxls=readxls,mangeip=mangeip,crdev=int(crdev))

@core.route('/nocpage',methods=['GET','POST'])
def noc():

    return render_template('noc.html')