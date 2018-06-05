import os
# 上传文件存放的位置
BASE_DIR = os.path.dirname(os.path.abspath(__name__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR = os.path.join(STATIC_DIR, 'uploads')


class Config():
    DEBUG = True
    ENV = 'development'
    SECRET_KEY = 'akdikska8&&8&&$#%'
    # mysql数据库连接
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@10.35.163.128:3306/users'
    SQLALCHEMY_TRACK_MODIFICATIONS = False