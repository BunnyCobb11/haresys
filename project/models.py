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

    __tablename__ = 'idccr'

    id = db.Column(db.Integer,primary_key=True)
    Area = db.Column(db.String(64))
    CrName = db.Column(db.String(64))
    CrAttributes = db.Column(db.String(64))
    DevName = db.Column(db.String(64))
    RuningTime = db.Column(db.String(64))
    ManagementIP = db.Column(db.String(64),unique=True)
    ISPAttributes = db.Column(db.String(64))
    Status = db.Column(db.String(64))
    LinkAttributes = db.Column(db.String(64))
    LinkPort = db.Column(db.String(64))
    LinkVLAN = db.Column(db.String(64))
    LinkIP = db.Column(db.String(64))
    BroadcastAddress = db.Column(db.String(512))
    Address = db.Column(db.String(128))

    def __init__(self,Area,CrName,CrAttributes,DevName,RuningTime,ManagementIP,ISPAttributes,Status,LinkAttributes,LinkPort,LinkVLAN,LinkIP,BroadcastAddress,Address):
        self.Area = Area
        self.CrName = CrName
        self.CrAttributes = CrAttributes
        self.DevName = DevName
        self.RuningTime = RuningTime
        self.ManagementIP = ManagementIP
        self.ISPAttributes = ISPAttributes
        self.Status = Status
        self.LinkAttributes = LinkAttributes
        self.LinkPort = LinkPort
        self.LinkVLAN = LinkVLAN
        self.LinkIP = LinkIP
        self.BroadcastAddress = BroadcastAddress
        self.Address = Address

    def __repr__(self):
        return  f"{self.ManagementIP}"

class NocMail(db.Model):

    __tablename__ = 'NocMail'

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(64),unique=True,index=True)
    password = db.Column(db.String(128))
    serveraddress = db.Column(db.String(128))
    port = db.Column(db.String(32))

    def __init__(self,email,password,serveraddress,port):
        self.email = email
        self.password = password
        self.serveraddress = serveraddress
        self.port = port

    def __repr__(self):
        return f'{self.email}'