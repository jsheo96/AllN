# Generated by Django 3.1.4 on 2021-01-24 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Issuedb',
            fields=[
                ('issue_id', models.AutoField(primary_key=True, serialize=False)),
                ('issue', models.TextField(blank=True, null=True)),
                ('data', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'IssueDB',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Newsdb',
            fields=[
                ('news_id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'NewsDB',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stockdb',
            fields=[
                ('stock_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('data', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'StockDB',
                'managed': False,
            },
        ),
    ]
