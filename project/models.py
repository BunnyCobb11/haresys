from project import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    profile_image = db.Column(db.String(64),nullable=False,default='default_profile.png')
    email = db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))

    #posts = db.relationship('BlogPost',backref='author',lazy=True)

    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"Username {self.username}"

class Proxy(db.Model):

    __tablename__ = "proxys"

    id = db.Column(db.Integer,primary_key=True)
    remarks = db.Column(db.String(128),index=True)
    address = db.Column(db.String(128),unique=True,index=True)
    port = db.Column(db.String(32),index=True)
    username = db.Column(db.String(64),index=True)
    password = db.Column(db.String(128))

    def __init__(self,remarks,address,port,username,password):
        self.remarks = remarks
        self.address = address
        self.port = port 
        self.username = username
        self.password = password

    def __repr__(self):
        return f"{self.remarks} {self.address}"

class Crbj(db.Model):

    __tablename__ = 'crbj'

    id = db.Column(db.Integer,primary_key=True)
    region = db.Column(db.String(64))
    croom_name = db.Column(db.String(64))
    croom_att = db.Column(db.String(64))
    devidc_name = db.Column(db.String(64))
    running_time = db.Column(db.String(64))
    manage_ip = db.Column(db.String(64))
    line_att = db.Column(db.String(64))
    line_info = db.Column(db.String(64))
    state = db.Column(db.String(64))
    inter_port = db.Column(db.String(64))
    inter_vlan = db.Column(db.String(64))
    inter_ip = db.Column(db.String(64))
    resources_ip = db.Column(db.String(64))
    location = db.Column(db.String(128))

    def __init__(self,region,croom_name,croom_att,device_name,
                 running_time,mange_ip,line_att,line_info,state,inter_port,
                 inter_vlan,inter_ip,resources_ip,location):
        self.region = region
        self.croom_name = croom_name
        self.croom_att = croom_att
        self.devidc_name = device_name
        self.running_time = running_time
        self.manage_ip = mange_ip
        self.line_att = line_att
        self.line_info = line_info
        self.state = state
        self.inter_port = inter_port
        self.inter_vlan = inter_vlan
        self.inter_ip = inter_ip
        self.resources_ip = resources_ip
        self.location = location

    def __repr__(self):
        return  f"{self.manage_ip}"