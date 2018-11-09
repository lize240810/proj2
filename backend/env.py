# -*- codeing:utf-8 -*-

'''
路径配置文件
'''

import os

# 后端目录
DIR_BACKEND = os.path.dirname(os.path.abspath(__file__))
# 项目目录
DIR_PROJ = os.path.dirname(DIR_BACKEND)
# 前端路径
DIR_FRONTEND = os.path.dirname(DIR_PROJ,'frontend')
# 静态文件
DIR_STATIC = os.path.dirname(DIR_FRONTEND, 'static')
# 模板目录
DIR_TEMPLATES = os.path.dirname(DIR_FRONTEND, 'templates')



