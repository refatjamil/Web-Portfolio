# Generated by Django 4.0.1 on 2022-04-04 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='m_Email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='m_Message',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='m_Name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='m_Subject',
            field=models.CharField(max_length=100, null=True),
        ),
    ]