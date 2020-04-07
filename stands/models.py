from django.db import models
from .selectors import *
from datetime import datetime

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

BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))


class Soldierdata(models.Model):
    DODID = models.IntegerField(primary_key=True)
    Rank = models.CharField(max_length=155, choices=rank, blank=True, default='')
    last_name = models.CharField(max_length=155)
    first_name = models.CharField(max_length=155)
    MOS = models.CharField(max_length=155, choices=mos)
    Position = models.CharField(max_length=155, choices=position, blank=True)
    Platoon = models.CharField(max_length=155, choices=platoon, blank=True)
    Battery = models.CharField(max_length=155, choices=battery, blank=True)
    Battalion = models.CharField(max_length=155, choices=unit(), blank=True)

    # Brigade = models.CharField(max_length=155, choices=brigade, default='')
    # AAMDC = models.CharField(max_length=155, choices=aamdc, default='')

    def __str__(self):
        return self.Rank+' '+self.last_name+', '+self.first_name


class IccTableOne(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_1_tasks = models.CharField(max_length=155, choices=icc_t1(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class IccTableTwo(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_2_tasks = models.CharField(max_length=155, choices=icc_t2(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class IccTableThree(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_3_tasks = models.CharField(max_length=155, choices=icc_t3(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class IccTableFour(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_4_tasks = models.CharField(max_length=255, choices=icc_t4(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class IccTableFive(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_5_tasks = models.CharField(max_length=255, choices=icc_t5(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class IccTableSix(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_6_tasks = models.CharField(max_length=255, choices=icc_t6(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class IccTableSeven(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_7_tasks = models.CharField(max_length=255, choices=icc_t7(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class IccTableEight(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_8_tasks = models.CharField(max_length=255, choices=icc_t8(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class IccTableNine(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_9_tasks = models.CharField(max_length=255, choices=icc_t9(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class IccTableTen(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_10_tasks = models.CharField(max_length=255, choices=icc_t10(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class IccTableEleven(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_11_tasks = models.CharField(max_length=255, choices=icc_t11(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class IccTableTwelve(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_12_tasks = models.CharField(max_length=255, choices=icc_t12(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class TcsTableOne(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_1_tasks = models.CharField(max_length=255, choices=tcs_t1(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class TcsTableTwo(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_2_tasks = models.CharField(max_length=255, choices=tcs_t2(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class TcsTableThree(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_3_tasks = models.CharField(max_length=255, choices=tcs_t3(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class TcsTableFour(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_4_tasks = models.CharField(max_length=255, choices=tcs_t4(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class TcsTableFive(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_5_tasks = models.CharField(max_length=255, choices=tcs_t5(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class TcsTableSix(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_6_tasks = models.CharField(max_length=255, choices=tcs_t6(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class TcsTableSeven(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_7_tasks = models.CharField(max_length=255, choices=tcs_t7(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class TcsTableEight(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_8_tasks = models.CharField(max_length=255, choices=tcs_t8(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class TcsTableNine(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_9_tasks = models.CharField(max_length=255, choices=tcs_t9(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class TcsTableTen(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_10_tasks = models.CharField(max_length=255, choices=tcs_t10(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class TcsTableEleven(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_11_tasks = models.CharField(max_length=255, choices=tcs_t11(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class TcsTableTwelve(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_12_tasks = models.CharField(max_length=255, choices=tcs_t12(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class CrgTableOne(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_1_tasks = models.CharField(max_length=255, choices=crg_t1(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return f'{self.soldier} {self.t_1_tasks}, {self.date_completed}'


class CrgTableTwo(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_2_tasks = models.CharField(max_length=255, choices=crg_t2(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class CrgTableThree(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_3_tasks = models.CharField(max_length=255, choices=crg_t3(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class CrgTableFour(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_4_tasks = models.CharField(max_length=255, choices=crg_t4(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class CrgTableFive(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_5_tasks = models.CharField(max_length=255, choices=crg_t5(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class CrgTableSix(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_6_tasks = models.CharField(max_length=255, choices=crg_t6(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class CrgTableSeven(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_7_tasks = models.CharField(max_length=255, choices=crg_t7(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class CrgTableEight(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_8_tasks = models.CharField(max_length=255, choices=crg_t8(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class CrgTableNine(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_9_tasks = models.CharField(max_length=255, choices=crg_t9(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class CrgTableTen(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_10_tasks = models.CharField(max_length=255, choices=crg_t10(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class CrgTableEleven(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_11_tasks = models.CharField(max_length=255, choices=crg_t11(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class CrgTableTwelve(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_12_tasks = models.CharField(max_length=255, choices=crg_t12(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class AmgTableOne(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_1_tasks = models.CharField(max_length=255, choices=amg_t1(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class AmgTableTwo(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_2_tasks = models.CharField(max_length=255, choices=amg_t2(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class AmgTableThree(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_3_tasks = models.CharField(max_length=255, choices=amg_t3(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class AmgTableFour(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_4_tasks = models.CharField(max_length=255, choices=amg_t4(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class AmgTableFive(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_5_tasks = models.CharField(max_length=255, choices=amg_t5(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class AmgTableSix(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_6_tasks = models.CharField(max_length=255, choices=amg_t6(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class AmgTableSeven(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_7_tasks = models.CharField(max_length=255, choices=amg_t7(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class AmgTableEight(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_8_tasks = models.CharField(max_length=255, choices=amg_t8(), blank=True)
    task_complete = models.BooleanField(choices=BOOL_CHOICES, null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class Icc(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_1_tasks = models.CharField(max_length=155, choices=icc_t1(), null=True)
    t_2_tasks = models.CharField(max_length=155, choices=icc_t2(), null=True)
    t_3_tasks = models.CharField(max_length=155, choices=icc_t3(), null=True)
    t_4_tasks = models.CharField(max_length=155, choices=icc_t4(), null=True)
    t_5_tasks = models.CharField(max_length=155, choices=icc_t5(), null=True)
    t_6_tasks = models.CharField(max_length=155, choices=icc_t6(), null=True)
    t_7_tasks = models.CharField(max_length=155, choices=icc_t7(), null=True)
    t_8_tasks = models.CharField(max_length=155, choices=icc_t8(), null=True)
    t_9_tasks = models.CharField(max_length=155, choices=icc_t9(), null=True)
    t_10_tasks = models.CharField(max_length=155, choices=icc_t10(), null=True)
    t_11_tasks = models.CharField(max_length=155, choices=icc_t11(), null=True)
    t_12_tasks = models.CharField(max_length=155, choices=icc_t12(), null=True)
    task_complete = models.BooleanField(null=True)
    date_completed = models.DateField(null=True)


class Unit(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    icc_t1_complete = models.ForeignKey(IccTableOne, on_delete=models.CASCADE, null=True)
    icc_t2_complete = models.ForeignKey(IccTableTwo, on_delete=models.CASCADE, null=True)
    icc_t3_complete = models.ForeignKey(IccTableThree, on_delete=models.CASCADE, null=True)
    icc_t4_complete = models.ForeignKey(IccTableFour, on_delete=models.CASCADE, null=True)
    crg_t1_complete = models.ForeignKey(CrgTableOne, on_delete=models.CASCADE, null=True)
    crg_t2_complete = models.ForeignKey(CrgTableTwo, on_delete=models.CASCADE, null=True)
    crg_t3_complete = models.ForeignKey(CrgTableThree, on_delete=models.CASCADE, null=True)
    crg_t4_complete = models.ForeignKey(CrgTableFour, on_delete=models.CASCADE, null=True)


if __name__ == "__main__":
    pass
