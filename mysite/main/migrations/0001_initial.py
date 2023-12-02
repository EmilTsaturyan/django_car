# Generated by Django 4.2.7 on 2023-12-02 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Category name')),
                ('image', models.ImageField(upload_to='logo', verbose_name='Category image')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Car name')),
                ('year', models.PositiveIntegerField(verbose_name='Year')),
                ('color', models.CharField(choices=[('White', 'white'), ('Black', 'Black'), ('Red', 'red'), ('Blue', 'Blue'), ('Purple', 'purple')], max_length=10, verbose_name='Color')),
                ('price', models.PositiveIntegerField(verbose_name='Car price')),
                ('description', models.TextField(verbose_name='Car description')),
                ('caetgory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat_prod', to='main.category')),
            ],
        ),
    ]