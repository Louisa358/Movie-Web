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



