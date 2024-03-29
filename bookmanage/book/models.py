from django.db import models

# Create your models here.
# ORM kuang jia
"""
1.need extend models.Model
2.already exist id
3.ziduan
  
  ziduan=model.leixing(option)
  
  char(M)
  varchar(M)
  M is option
  
4.must be zhuche subapp else can not find 
"""


# 准备书籍列表信息的模型类
class BookInfo(models.Model):
    # 创建字段，字段类型...
    name = models.CharField(max_length=10)


# 准备人物列表信息的模型类
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束：人物属于哪本书 ForeignKey
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

