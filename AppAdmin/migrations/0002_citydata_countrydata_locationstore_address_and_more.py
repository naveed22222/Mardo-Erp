# Generated by Django 5.1.2 on 2024-10-20 14:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAdmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('geom', models.TextField(max_length=200, null=True)),
                ('city_code', models.CharField(max_length=200, null=True, unique=True)),
                ('unique_code', models.CharField(max_length=200, null=True)),
                ('city_name', models.TextField(max_length=200, null=True)),
                ('image', models.ImageField(default='', upload_to='City')),
                ('description', models.TextField(max_length=300, null=True)),
                ('status', models.TextField(max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'tbl_city_data',
            },
        ),
        migrations.CreateModel(
            name='CountryData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('geom', models.TextField(max_length=200, null=True)),
                ('country_code', models.CharField(max_length=200, null=True, unique=True)),
                ('country_mobile_code', models.CharField(max_length=200, null=True)),
                ('country_name', models.TextField(max_length=200, null=True)),
                ('image', models.ImageField(default='', upload_to='Country')),
                ('description', models.TextField(max_length=300, null=True)),
                ('status', models.TextField(max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'tbl_country_data',
            },
        ),
        migrations.AddField(
            model_name='locationstore',
            name='address',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='locationstore',
            name='area',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='locationstore',
            name='image',
            field=models.ImageField(default='', upload_to='LocationStore'),
        ),
        migrations.AddField(
            model_name='locationstore',
            name='mobile',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='costcenter',
            name='status',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='BusinessAccount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('busi_acc_code', models.CharField(max_length=200, null=True, unique=True)),
                ('account_title', models.CharField(max_length=200, null=True)),
                ('account_no', models.TextField(max_length=200, null=True)),
                ('branch_code', models.IntegerField(null=True)),
                ('address', models.TextField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(max_length=200, null=True)),
                ('country', models.CharField(max_length=200, null=True)),
                ('activation_date', models.DateField(null=True)),
                ('block_date', models.DateField(null=True)),
                ('ibn_number', models.TextField(max_length=200, null=True)),
                ('description', models.TextField(max_length=300, null=True)),
                ('status', models.TextField(max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(max_length=200, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(max_length=200, null=True)),
                ('loc_store_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppAdmin.locationstore', to_field='loc_store_code')),
            ],
            options={
                'db_table': 'tbl_business_account',
            },
        ),
        migrations.CreateModel(
            name='AreaTownData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('geom', models.TextField(max_length=200, null=True)),
                ('area_code', models.CharField(max_length=200, null=True, unique=True)),
                ('unique_code', models.CharField(max_length=200, null=True)),
                ('area_name', models.TextField(max_length=200, null=True)),
                ('image', models.ImageField(default='', upload_to='Area')),
                ('description', models.TextField(max_length=300, null=True)),
                ('status', models.TextField(max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=200, null=True)),
                ('city_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppAdmin.citydata', to_field='city_code')),
            ],
            options={
                'db_table': 'tbl_area_town_data',
            },
        ),
        migrations.CreateModel(
            name='StateData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('geom', models.TextField(max_length=200, null=True)),
                ('state_code', models.CharField(max_length=200, null=True, unique=True)),
                ('unique_code', models.CharField(max_length=200, null=True)),
                ('state_name', models.TextField(max_length=200, null=True)),
                ('image', models.ImageField(default='', upload_to='State')),
                ('description', models.TextField(max_length=300, null=True)),
                ('status', models.TextField(max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=200, null=True)),
                ('country_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppAdmin.countrydata', to_field='country_code')),
            ],
            options={
                'db_table': 'tbl_state_data',
            },
        ),
        migrations.AddField(
            model_name='citydata',
            name='state_code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppAdmin.statedata', to_field='state_code'),
        ),
    ]
