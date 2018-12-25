from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.shortcuts import reverse
# Create your models here.


@python_2_unicode_compatible
class Column(models.Model):
    name = models.CharField('栏目名称', max_length=256)
    slug = models.CharField('栏目网址', max_length=256, db_index=True)
    summary = models.TextField('栏目简介', default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('column', args=(self.slug,))

    class Meta:
        verbose_name = '栏目'
        verbose_name_plural = '栏目'  # 复数形式
        ordering = ['name']  # 按照哪个栏目排序


@python_2_unicode_compatible
class Article(models.Model):
    # 与Column模型为多对多关系，即一篇文章可以有多个栏目，一个栏目也有多个文章
    column = models.ManyToManyField('Column', verbose_name='归属栏目')
    title = models.CharField('标题', max_length=255)
    slug = models.CharField('网址', max_length=255, unique=True)
    # 用DjangoUeditor包里的编辑器编辑内容
    # 因为运行报错：TypeError: render() got an unexpected keyword argument 'renderer'
    # 所以将C:\Users\wangning\Anaconda3\lib\site-packages\django\forms\boundfield.py第93行renderer=self.form.renderer注释掉
    content = UEditorField('内容', height=300, width=1000, default=u'', blank=True, imagePath='uploads/images/',
                           toolbars='besttome', filePath='uploads/files/')
    # 作者可以为空
    author = models.ForeignKey(
        'auth.User',
        blank=True,
        null=True,
        verbose_name='作者',
        on_delete=models.CASCADE)
    published = models.BooleanField('正式发布', default=True)
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', args=(self.pk, self.slug,))

    class Meta:
        verbose_name = '教程'
        verbose_name_plural = '教程'
