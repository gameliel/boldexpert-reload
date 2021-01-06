# Generated by Django 3.1.2 on 2020-12-28 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_auto_20201228_1201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='publicat',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='store.Tag'),
        ),
        migrations.DeleteModel(
            name='Publication',
        ),
    ]