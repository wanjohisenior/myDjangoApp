# Generated by Django 3.2.3 on 2022-02-25 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commissionrate', models.FloatField(max_length=4)),
                ('interestrate', models.FloatField(max_length=4)),
                ('waterrate', models.FloatField()),
                ('electricityrate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ElectricityMeter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('electricitymeternumber', models.CharField(max_length=50)),
                ('previousreading', models.CharField(max_length=50)),
                ('currentreading', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=50)),
                ('rent', models.IntegerField()),
                ('deposit', models.IntegerField()),
                ('garbagefee', models.IntegerField()),
                ('status', models.CharField(choices=[('VACCANT', 'Vaccant'), ('RENTED', 'Rented')], max_length=7)),
                ('rentduedate', models.DateField()),
                ('buildingid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.building')),
            ],
        ),
        migrations.CreateModel(
            name='Landlord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('nationalid', models.BigIntegerField()),
                ('birthday', models.DateField()),
                ('email', models.EmailField(blank=True, default='-', max_length=30, null=True)),
                ('primarycontact', models.BigIntegerField(blank=True, default='-', null=True)),
                ('othercontact', models.BigIntegerField(blank=True, default='-', null=True)),
                ('gender', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('nationalid', models.BigIntegerField()),
                ('birthday', models.DateField()),
                ('email', models.EmailField(blank=True, default='-', max_length=30, null=True)),
                ('primarycontact', models.IntegerField(blank=True, default='-', null=True)),
                ('othercontact', models.IntegerField(blank=True, default='-', null=True)),
                ('gender', models.CharField(max_length=7)),
                ('occupation', models.CharField(blank=True, default='-', max_length=30, null=True)),
                ('housenumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.house')),
            ],
        ),
        migrations.CreateModel(
            name='WaterMeter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meternumber', models.CharField(max_length=50)),
                ('previousreading', models.CharField(max_length=50)),
                ('currentreading', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transationtype', models.CharField(choices=[('CASH', 'Cash'), ('MPESA', 'Mpesa'), ('COOP-BANK', 'Cooperative Bank'), ('EQUITY-BANK', 'Equity Bank')], max_length=15)),
                ('datepaid', models.DateField()),
                ('amountpaid', models.IntegerField()),
                ('description', models.TextField(max_length=20)),
                ('tenantid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=20)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('groupid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.group')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='housesassigned',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.house'),
        ),
        migrations.AddField(
            model_name='building',
            name='landlordid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.landlord'),
        ),
    ]
