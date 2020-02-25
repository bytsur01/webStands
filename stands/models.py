from django.db import models
from .selectors import *

# Create your models here.

platoon = [
    ('Fire Control', 'Fire Control'),
    ('Launcher', 'Launcher'),
    ('Fire Direction Control', 'Fire Direction Control'),

]
battery = [
    ('HHB', 'HHB'),
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
]
rank = [
    ('PVT', 'PVT'),
    ('PV2', 'PV2'),
    ('PFC', 'PFC'),
    ('SPC', 'SPC'),
    ('SGT', 'SGT'),
    ('SSG', 'SSG'),
    ('SFC', 'SFC'),
    ('MSG', 'MSG'),
    ('2LT', '2LT'),
    ('1LT', '1LT'),
    ('CPT', 'CPT'),
    ('MAJ', 'MAJ'),
    ('WO1', 'WO1'),
    ('CW2', 'CW2'),
    ('CW3', 'CW3'),
]

battalion = unit()

brigade = [
    ('31st BDE', '31st BDE'),
]

aamdc = [
    ('32 AAMDC', '32 AAMDC'),
    ('10th AAMDC', '10th AAMDC'),
    ('94th AAMDC', '94th AAMDC'),
]

mos = [
    ('14E', '14E'),
    ('14T', '14T'),
    ('14H', '14H'),
    ('14A', '14A'),
    ('140K', '140K'),
    ('25N', '25N'),
    ('25U', '25U'),
]

position = [
    ('TD', 'Tactical Director'),
    ('TDA', 'Tactical Director Assistant'),
    ('TCO', 'Tactical Control Officer'),
    ('TCA', 'Tactical Control Assistant'),
    ('TPW', 'Early Warning Operator'),
    ('RO', 'Radio Operator/ Reports operator'),
    ('JWARN', 'JWARN Operator'),
]


class Soldierdata(models.Model):
    DODID = models.IntegerField(primary_key=True)
    Rank = models.CharField(max_length=155, choices=rank, blank=True)
    last_name = models.CharField(max_length=155)
    first_name = models.CharField(max_length=155)
    MOS = models.CharField(max_length=155, choices=mos)
    Postion = models.CharField(max_length=155, choices=position, blank=True)
    Platoon = models.CharField(max_length=155, choices=platoon, blank=True)
    Battery = models.CharField(max_length=155, choices=battery, blank=True)
    Battalion = models.CharField(max_length=155, choices=unit(), blank=True)
    Brigade = models.CharField(max_length=155, choices=brigade, blank=True)
    AAMDC = models.CharField(max_length=155, choices=aamdc, blank=True)


class TdaTableOne(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_1_tasks = models.CharField(max_length=155, choices=icc_t1(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, null=False)


class TdaTableTwo(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_2_tasks = models.CharField(max_length=155, choices=icc_t2(), blank=True)
    task_complete = models.BooleanField(default=True)
    trainer = models.CharField(max_length=255, blank=False)


class TdaTableThree(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_3_tasks = models.CharField(max_length=155, choices=icc_t3(), blank=True)
    task_complete = models.BooleanField(default=True)
    trainer = models.CharField(max_length=255, blank=True)


class TdaTableFour(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_4_tasks = models.CharField(max_length=255, choices=icc_t4(), blank=True)
    task_complete = models.BooleanField(default=True)
    trainer = models.CharField(max_length=255, blank=True)


class Cso(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_1_tasks = models.CharField(max_length=155, choices=crg_t1(), blank=True)
    t_2_tasks = models.CharField(max_length=155, choices=crg_t2(), blank=True)
    t_3_tasks = models.CharField(max_length=155, choices=crg_t3(), blank=True)
    t_4_tasks = models.CharField(max_length=155, choices=crg_t4(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)




class Unit(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    icc_t1_complete = models.ForeignKey(TdaTableOne, on_delete=models.CASCADE)
    icc_t2_complete = models.ForeignKey(TdaTableTwo, on_delete=models.CASCADE)
    Cso = models.ForeignKey(Cso, on_delete=models.CASCADE)


if __name__ == "__main__":
    pass




