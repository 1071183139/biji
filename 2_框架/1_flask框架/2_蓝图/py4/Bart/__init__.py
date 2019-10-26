from flask import Blueprint

#template_folder模板路径
# static_folder静态路径
# static_url_path修改静态的路径
bart_app=Blueprint('bart',import_name=__name__,template_folder='templates',static_folder='static',static_url_path='/lib')

from views import  bart_page