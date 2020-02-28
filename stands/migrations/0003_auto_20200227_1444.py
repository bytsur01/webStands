# Generated by Django 3.0.3 on 2020-02-27 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stands', '0002_auto_20200227_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldierdata',
            name='AAMDC',
            field=models.CharField(choices=[('32 AAMDC', '32 AAMDC'), ('10th AAMDC', '10th AAMDC'), ('94th AAMDC', '94th AAMDC')], default='', max_length=155),
        ),
        migrations.AlterField(
            model_name='soldierdata',
            name='Battalion',
            field=models.CharField(choices=[('4-3 ADA', '4-3 ADA'), ('3-2 ADA', '3-2 ADA')], default='', max_length=155),
        ),
        migrations.AlterField(
            model_name='soldierdata',
            name='Battery',
            field=models.CharField(choices=[('HHB', 'HHB'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='', max_length=155),
        ),
        migrations.AlterField(
            model_name='soldierdata',
            name='Brigade',
            field=models.CharField(choices=[('31st BDE', '31st BDE')], default='', max_length=155),
        ),
        migrations.AlterField(
            model_name='soldierdata',
            name='Platoon',
            field=models.CharField(choices=[('Fire Control', 'Fire Control'), ('Launcher', 'Launcher'), ('Fire Direction Control', 'Fire Direction Control')], default='', max_length=155),
        ),
        migrations.AlterField(
            model_name='soldierdata',
            name='Rank',
            field=models.CharField(blank=True, choices=[('PVT', 'PVT'), ('PV2', 'PV2'), ('PFC', 'PFC'), ('SPC', 'SPC'), ('SGT', 'SGT'), ('SSG', 'SSG'), ('SFC', 'SFC'), ('MSG', 'MSG'), ('2LT', '2LT'), ('1LT', '1LT'), ('CPT', 'CPT'), ('MAJ', 'MAJ'), ('WO1', 'WO1'), ('CW2', 'CW2'), ('CW3', 'CW3')], default='', max_length=155),
        ),
    ]
