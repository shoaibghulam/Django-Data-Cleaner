# Generated by Django 4.0.4 on 2022-05-21 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('sheetId', models.AutoField(primary_key=True, serialize=False)),
                ('sheetName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SheetInfo',
            fields=[
                ('infoId', models.AutoField(primary_key=True, serialize=False)),
                ('infoName', models.TextField(max_length=900)),
                ('sheetId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.sheet')),
            ],
        ),
        migrations.CreateModel(
            name='SheetData',
            fields=[
                ('dataId', models.AutoField(primary_key=True, serialize=False)),
                ('dataTitle', models.CharField(max_length=200)),
                ('sheetId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.sheet')),
            ],
        ),
    ]