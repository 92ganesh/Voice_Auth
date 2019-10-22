# Generated by Django 2.1.7 on 2019-10-21 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20191020_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('question_en', models.TextField(null=True)),
                ('question_hi', models.TextField(null=True)),
                ('answer', models.CharField(max_length=50, null=True)),
                ('answer_en', models.CharField(max_length=50, null=True)),
                ('answer_hi', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]