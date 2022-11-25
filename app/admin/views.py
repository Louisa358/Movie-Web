# coding:utf8
from . import admin
from flask import render_template, redirect, url_for


@admin.route('/')
def index():
    return render_template("admin/index.html")

#登录
@admin.route("/login/")
def login():
    return render_template("admin/login.html")

#退出
@admin.route("/logout/")
def logout():
    return redirect(url_for("admin.login"))

#修改密码
@admin.route("/pwd/")
def pwd():
    return render_template("admin/pwd.html")

#编辑标签
@admin.route("/tag/add/")
def tag_add():
    return render_template("admin/tag_add.html")
#标签列表
@admin.route("/tag/list/")
def tag_list():
    return render_template("admin/tag_list.html")

#编辑电影
@admin.route("/movie/add/")
def movie_add():
    return render_template("admin/movie_add.html")
#电影列表
@admin.route("/movie/list/")
def movie_list():
    return render_template("admin/movie_list.html")