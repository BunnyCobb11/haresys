from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'


app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@192.168.20.3:3306/mydb"
# 禁用sqlalchemy自动更跟踪数据库
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True
# 自动提交数据处理
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
Migrate(app,db)

#用户设置
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'


from project.core.views import core
from project.error_pages.handlers import error_pages
from project.users.views import users
from project.network.views import network
app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)
app.register_blueprint(network)

