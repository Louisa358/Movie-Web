# Movie-Web



#### 网站组成：

1.前台：会员登录及注册，会员中心，电影播放，电影评论，收藏电影

2.后台：管理员登录，修改密码，标签管理，电影管理，上映预告管理，会员管理，评论管理，收藏管理，角色管理，权限管理，管理员管理，日志管理



#### 开发及生产环境：

生产环境：Centos7

开发环境：python3 （virtualenv）

数据库：mysql

前端：html5

框架：Flask

服务器：Nginx



python web框架对比：

1.flask：拓展丰富，冗余度小，性能优越，轻量级框架

2.Django：重量级全栈型web框架，功能强大，冗余度高，自带ORM和模板引擎，灵活自由度较差不适合小型项目

3.Tornado:  功能强大，支持协程、高效并发且可拓展，可利用异步协程机制开发高并发的服务器系统



为什么选择Flask？

1.轻量型框架 

2.WSGI工具箱采用werkzeug，封装了很多功能，eg.文件上传，生成及校验密码

3.模板引擎：Jinja2， 有丰富资料及标签

4.使用BSD授权



微内核框架：

microframework，用extension增加其他功能

没有默认的数据库、窗体验证工具

保留扩增的弹性，可用Flask-extension加入这些功能：ORM、窗体验证工具、文件上传、各种开放式身份验证技术



#### 前后台项目目录分析：

1.前台 home

数据模型： models.py

表单处理： home/forms.py

模板目录： templates/home

静态目录：static

2.后台 admin

数据模型： models.py

表单处理：admin/forms.py

模板目录：templates/admin

静态目录：static



```
manage.py    							入口启动脚本
app  									项目app
​	__init__.py 						初始化文件
	models.py							数据模型文件
	static								静态目录
	home/admin							前后台模块
		__init__.py						初始化脚本
		views.py						视图处理文件
		forms.py						表单处理文件
	templates							模板目录
		home/admin						前后台模板
```





### 蓝图

一个应用中或跨应用制作应用组件和支持通用的模式

蓝图作用：将不同功能模块化，构建大型应用，优化项目结构，增强可读性易于维护

```
1.定义蓝图（app/admin/___init__.py）

from flask import Blueprint
admin = Blueprint('admin',__name__)
import views

2.注册蓝图（app/__init__.py）
from admin import admin as admin_blueprint
app.register_blueprint(admin_blueprint,url_prefix='admin')

3.调用蓝图（app/admin/views.py)
from.import admin
@admin.route('/')
```



#### Flask的安装及virtualenv的使用

virtualenv使用：

```
1.创建虚拟环境： virtualenv venv
2.激活虚拟环境： source venv/bin/activate
3.退出虚拟环境： deactivate
```

flask的安装：

```
1.安装前检测：pip freeze
2.安装flask： pip install flask
3.安装后检测： pip freeze
```



#### 会员及会员登录日志数据模型设计

```
1.安装数据库连接依赖包

pip install flask-sqlalchemy

2.定义mysql数据库连接
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/movie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

定义会员数据模型：
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 昵称
    pwd = db.Column(db.String(100))  # 密码
    email = db.Column(db.String(100), unique=True)  # 邮箱
    phone = db.Column(db.String(11), unique=True)  # 手机号码
    info = db.Column(db.Text)  # 个性简介
    face = db.Column(db.String(255), unique=True)  # 头像
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间
    uuid = db.Column(db.String(255), unique=True)  # 唯一标志符
    userlogs = db.relationship('Userlog', backref='user')  # 会员日志外键关系关联
    comments = db.relationship('Comment', backref='user')  # 评论外键关系关联
    moviecols = db.relationship('Moviecol', backref='user')  # 收藏外键关系关联
    
会员登录日志：
class Userlog(db.Model):
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属会员
    ip = db.Column(db.String(100))  # 登录IP
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 登录时间
```

#### 标签、电影、上映预告数据模型设计

定义 *标签* 数据模型：

```
id：编号，name:标题，movies：电影外键关联，addtime：创建时间
```

定义 *电影* 数据模型：

```
id:编号，title：电影标题，url：电影地址，info：电影简介，logo：电影封面，star：星级，playnum：电影播放量，commentnum：电影评论量，tag_id:所属标签，area：地区，release_time:发布时间，length：电影长度，addtime：添加时间，comments: 电影评论外键关联，moviecols：电影收藏外键关联
```

定义*评论* 数据模型：

```
id：编号, content:评论内容，movie_id: 所属电影 ，user_id: 所属用户，addtime:最近登录时间
```

定义*收藏电影* 数据模型：

```
id：编号，movie_id：所属电影， user_id：所属用户，addtime：最近登录时间
```

定义*权限* 数据模型：

```
id：编号，name:名称，url：地址，addtime：创建时间
```

定义*角色* 数据模型：

```
id：编号，name:名称，auths：权限列表，addtime：创建时间，admins：管理员外键关联
```

定义*管理员* 数据模型：

```
id：编号，name：管理员名称，pwd：管理员密码，is_super:是否超级管理员，role_id:角色编号，addtime:创建时间，adminlogs:管理员登录日志外键管理，oplogs:操作日志外键关联
```

定义*管理员登录日志数据* 类型：

```
id：编号，admin_id:所属管理员编号，ip：最近登录ip地址，addtime：最近登陆时间
```

定义操作日志：

```
id：编号，admin_id:所属管理员编号，ip：操作ip地址，reason：操作原因，addtime：创建时间
```



# 前台布局搭建

```
1.静态文件引入：{{ url_for('static', filename = '文件路径') }}

2.定义路由： {{ url_for('模块名.视图名'，变量=参数)}}

3.定义数据库：{%block 数据库名称 %}...{% endblock %}

笔记：根据nav.html进行改写，写入home.html,index.html
```



#### 会员登录页面搭建

```
#登录
@home.route("/login/")
def login():
	return render_template("home/login.html")
#退出
@home.route("/logout/")
def logout():
	return redirect(url_for('home.login'))
```

#### 会员注册页面搭建

```
#注册
@home.route("/register/")
def register():
	return render_template("home/register.html")
```

#### 会员中心页面搭建

```
#会员中心
@home.route("/user/")
#修改密码
@home.route("/pwd/")
#评论记录
@home.route("/comments/")
#登陆日志
@home.route("/loginlog/")
#收藏电影
@home.route("/moviecol/")
```

#### 电影列表页面搭建

```
#列表
@home.route("/")
def index():
	return render_template("home/index.html")
#动画
@home.route("/animation/")
def animation():
	return render_template("home/animation.html")
```

#### 电影搜索页面搭建

```
#搜索
@home.route("/search/")
def search():
	return render_template("home/search.html")
```

#### 电影详情页面搭建

```
#详情
@home.route("/play/")
def play():
	return render_template("home/play.html")
```

#### 404页面搭建

```
#404
@app.errorhandler(404)
def page_not_found(error):
	return render_template("common/404.html"),404
```

# 后台页面搭建

#### 管理员登陆页面搭建

```
#登录
@admin.route("/login/")
def login():
	return render_template("admin/login.html")
#退出
@admin.route("/logout/")
def logout():
	return redirect(url_for("admin.login")) 
```

#### 后台布局搭建

```
#admin.html
{% block css%}...{% end %}
{% include "grid.html"%}
{% block content%}...{% end %}
{% block js%} ... {% end %}

#其他页面继承父模板
{% extends "admin/admin.html"%}
{% block css%} ... {% end %}
{% include "grid.html"%}
{% block content %}...{% end %}
{% block js %}...{% end %}
```

#### 修改密码

```
#修改密码
@admin.route("/pwd/")
def pwd():
	return render_template("admin/pwd.html")
```

#### 控制面板

```
@admin.route("/")
def index():
	return render_template("admin/index.html")
```

