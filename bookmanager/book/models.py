from django.db import models

# Create your models here.
class BookInfo(models.Model):
    """
    1. 我们模型类需要继承自 models.Model
    2. 系统会自动为我们添加一个主键 --id
    3. 字段
            字段名=model.类型 (选项)
            字段数据其实就是数据数据表的字段名

            char (M)
            varchar(M)
            M 就是选项
    """
    # id
    name = models.CharField(max_length=10)

# 人物
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束 : 人物属于哪本书
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
