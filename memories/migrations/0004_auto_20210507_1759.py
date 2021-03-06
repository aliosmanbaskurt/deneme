# Generated by Django 3.2 on 2021-05-07 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memories', '0003_alter_memory_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='memory',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='memories.Tag'),
        ),
    ]
