from flask import render_template,url_for,flash,redirect,request,Blueprint
from project import db
from .sshp import Ssh,Ssh_rs
from .forms import SshxForm,ProxyForm,TestForm
from project.models import Proxy

network = Blueprint("network",__name__)

@network.route("/sshx",methods=['GET','POST'])
def sshx():
    form = SshxForm()
    echo = ''
    n = 0
    if form.validate_on_submit():
        ip = form.address.data
        port = form.port.data
        username = form.username.data
        password = form.password.data
        command = form.command.data
        ssh = Ssh(ip,port,username,password,command)
        echo = ssh.result()
        n = echo.count('\n')
    return render_template('remote_server.html',form=form,echo=echo,n=n)

@network.route("/sshx_rs",methods=['GET','POST'])
def sshx_rs():
    form = SshxForm()
    echo = ''
    n = 0
    if form.validate_on_submit():
        ip = form.address.data
        port = form.port.data
        username = form.username.data
        password = form.password.data
        command = form.command.data
        ssh = Ssh_rs(ip,port,username,password,command)
        echo = ssh.result()
        echo = echo.decode('utf8')
        n = echo.count('\n')
    return render_template('remote_rssw.html',form=form,echo=echo,n=n)

@network.route("/proxy",methods=['GET','POST'])
def proxy():
    form = ProxyForm()
    if form.validate_on_submit():
        data_count = Proxy.query.filter_by(address=form.address.data).count()
        if data_count == 0:
            proxys = Proxy(remarks=form.remarks.data,
                           address=form.address.data,
                           port=form.port.data,
                           username = form.username.data,
                           password = form.password.data)
            db.session.add(proxys)
            db.session.commit()
            flash("success!")
        else:
            pass
    resultall = Proxy.query.all()
    n = len(resultall)
    return render_template('add_proxy.html',form=form,resultall=resultall,n=n)

@network.route('/tracert',methods=['GET','POST'])
def tracert():
    form = TestForm()
    form.address.choices = [(v.address,v.remarks) for v in Proxy.query.all()]
    proxy = []
    echo = ''
    n = 0
    if request.method=='POST' and form.validate_on_submit():
        commands = 'mtr -n -r ' + form.proxyid.data
        proxy = Proxy.query.filter_by(address=form.address.data).first()
        ssh = Ssh(proxy.address,proxy.port,proxy.username,proxy.password,commands)
        echo = ssh.result()
        n = echo.count('\n')
    return render_template('route_tracert.html',form=form,echo=echo,n=n)