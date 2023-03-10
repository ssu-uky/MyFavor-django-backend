# Generated by Django 4.1.7 on 2023-03-10 07:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='', max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(3, '닉네임은 3자 이상이어야합니다.')]),
        ),
    ]
