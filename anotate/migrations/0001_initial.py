# Generated by Django 3.2.9 on 2021-11-29 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('password', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('project_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anotate.users')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.FileField(blank=True, null=True, upload_to='static/uploads/images')),
                ('image_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anotate.project')),
            ],
        ),
    ]