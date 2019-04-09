# Generated by Django 2.2 on 2019-04-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(blank=True, choices=[('blog', '日记'), ('doc', '文档')], default='blog', max_length=50, verbose_name='博客标签'),
        ),
    ]