from django.db import models
import uuid


# Create your models here.
class Classify(models.Model):
    """文章分类"""
    # 分类id
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False, verbose_name="分类ID")
    # 父级分类id
    parent_id = models.CharField(max_length=36, default=0, verbose_name="父级分类ID")
    # 分类名称
    name = models.CharField(max_length=20, verbose_name="分类名称")
    # 分类创建者
    creator = models.CharField(max_length=50, verbose_name="创建者")
    # 分类创建时间
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 分类状态
    status = models.BooleanField(default=False, verbose_name="状态")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "文章分类"


class Tag(models.Model):
    """文章标签"""
    # 标签名称
    title = models.CharField(max_length=100, verbose_name="标签名称")
    # 标签创建者
    creator = models.CharField(max_length=50, verbose_name="创建者")
    # 标签创建时间
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = "文章标签"


class Detail(models.Model):
    """文章详情"""
    # 文章名称
    title = models.CharField(max_length=100, verbose_name="文章名称")
    # 文章分类
    classify = models.ForeignKey(Classify, on_delete=models.CASCADE, verbose_name="文章分类")
    # 文章标签
    tags = models.ManyToManyField(Tag, verbose_name="文章标签")
    # 文章介绍
    desc = models.TextField(null=True, verbose_name="文章介绍")
    # 文章内容
    content = models.TextField(null=True, verbose_name="文章内容")
    # 文章创建者
    creator = models.CharField(max_length=50, verbose_name="创建者")
    # 文章创建时间
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 文章最后更新时间
    updateAt = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    # 文章状态
    status = models.BooleanField(default=False, verbose_name="状态")
    # 是否锁定
    isLocked = models.BooleanField(default=False, verbose_name="是否锁定")
    # 密码
    password = models.CharField(max_length=100, null=True, verbose_name="密码")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = "文章详情"
