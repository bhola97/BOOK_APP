# Generated by Django 3.2.2 on 2021-05-10 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('cart_list', models.CharField(max_length=500)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_app.sell')),
            ],
        ),
    ]
