# Generated by Django 4.1.7 on 2023-04-25 05:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkerCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='login',
            old_name='is_user',
            new_name='is_customer',
        ),
        migrations.AddField(
            model_name='login',
            name='address',
            field=models.TextField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='login',
            name='gender',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='login',
            name='name',
            field=models.CharField(max_length=42, null=True),
        ),
        migrations.AddField(
            model_name='login',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='login',
            name='profile_pic',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='login',
            name='status',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.CreateModel(
            name='WorkSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('customer', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('message', models.CharField(max_length=150)),
                ('reply', models.CharField(blank=True, max_length=150, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.workschedule')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_done', models.CharField(max_length=100)),
                ('bill', models.FloatField(max_length=10)),
                ('date', models.DateField(blank=True, null=True)),
                ('appoint', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.bookappointment')),
            ],
        ),
        migrations.AddField(
            model_name='login',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.workercategory'),
        ),
    ]