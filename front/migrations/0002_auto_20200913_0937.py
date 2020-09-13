# Generated by Django 3.1.1 on 2020-09-13 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=700)),
                ('image', models.ImageField(upload_to='slider/')),
            ],
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='description',
            field=models.TextField(max_length=700),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]