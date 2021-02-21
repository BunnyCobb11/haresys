# coding: utf8
from flask import Flask,request,render_template,Blueprint,redirect,flash,url_for
from werkzeug.security import check_password_hash
import pandas as pd
import os
from project.core.models import Crpage
from project.collection.mail import Emailmodule
from project.library.forms import MailForm,MailFormd
from project.models import NocMail
from project import db

core = Blueprint('core',__name__)

@core.route('/')          #首页
def index():
    return render_template('index.html')

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
    d = Crpage('D:\\virtualenv\\ven-flask\\data\\idccr.xlsx')
    xlsdb_columns = d.xlsdb_columns()
    readxls = d.readxls()
    if request.method == 'GET':
        mangeip = request.args.get('mangeip')
        crdev = request.args.get('crdev')
    return render_template('croompage.html',xlsdb_columns=xlsdb_columns,readxls=readxls,
                            mangeip=mangeip,crdev=int(crdev))

@core.route('/nocsetting',methods=['GET','POST'])
def nocsetting():
    formd = MailFormd()
    result_type = None ;receive = '' ;result_count = 0 ;result_sum = 0
    formd.usermaild.choices = [(v.email) for v in NocMail.query.all()]
    print(len(formd.usermaild.choices))
    if formd.usermaild.choices:
        if request.method=='POST' and formd.validate_on_submit():
            maild = NocMail.query.filter_by(email=formd.usermaild.data).first()
            emailDB = Emailmodule()
            print(maild.email)
            receive = emailDB.server_imap4(maild.email,maild.password,maild.serveraddress,maild.port)
            result_type = type(receive)
            result_count = receive.count('\n')
            result_sum = len(receive)
            flash('选定账户:{:}'.format(maild.email))
        else:
            maild = NocMail.query.filter_by(email=formd.usermaild.choices[0]).first()
            emailDB = Emailmodule()
            print(maild.email)
            receive = emailDB.server_imap4(maild.email,maild.password,maild.serveraddress,maild.port)
            result_type = type(receive)
            result_count = receive.count('\n')
            result_sum = len(receive)
            flash('选定账户:{:}'.format(maild.email))
    else:
        return redirect(url_for('core.nocsetting_email'))
    return render_template('nocsetting.html',formd=formd,result_type=result_type,
                            receive=receive,result_count=result_count,result_sum=result_sum)

@core.route('/nocsetting_email',methods=['GET','POST'])
def nocsetting_email():
    form = MailForm()
    if form.validate_on_submit():
        user = form.usermail.data;passwd = form.password.data;server = form.serveraddr.data;port = form.port.data
        nocmail = NocMail(email=user,password=passwd,serveraddress=server,port=port)
        dbmail = NocMail.query.filter_by(email=user).count()
        if dbmail == 0:
            db.session.add(nocmail)
            db.session.commit()
            flash("提交成功")
        else:
            flash('账户已经存在！')
        return redirect(url_for('core.nocsetting_email'))
    return render_template('nocsetting_email.html',form=form,flash=flash)