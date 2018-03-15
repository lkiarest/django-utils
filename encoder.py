# 编码辅助工具
# 转换 Model 对象到 Json 格式
import json
from datetime import date
from datetime import datetime
from django.db.models import Model
from datetime import datetime, date
import decimal

# 提取对象指定的属性值（list）生成 dict 对象
def make_obj_json(obj, attrs):
    json_obj = {}
    for attr in attrs:
        val = getattr(obj, attr)
        if isinstance(val, Model):
            val = str(val)
        elif isinstance(val, datetime):
            val = val.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(val, date):
            val = val.strftime('%Y-%m-%d')
        elif isinstance(val, decimal.Decimal):
            val = str(val)

        json_obj[attr] = val

    return json_obj

# 类装饰器，方便定义对象的 get_json 方法
# eg. @json_encoder('id', 'name') # decorate a model class
#     model.to_json()
def json_encoder(*attrs):
    def wrapper(cls):
        def _get_json(self):
            # print(self.__dict__.items())
            return make_obj_json(self, attrs)

        setattr(cls, 'to_json', _get_json)

        return cls

    return wrapper
