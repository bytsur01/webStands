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
    Rank = models.CharField(max_length=155, choices=rank, blank=True, default='')
    last_name = models.CharField(max_length=155)
    first_name = models.CharField(max_length=155)
    MOS = models.CharField(max_length=155, choices=mos)
    Position = models.CharField(max_length=155, choices=position, blank=True)
    Platoon = models.CharField(max_length=155, choices=platoon, blank=True)
    Battery = models.CharField(max_length=155, choices=battery, default='')
    Battalion = models.CharField(max_length=155, choices=unit(), default='')
    #Brigade = models.CharField(max_length=155, choices=brigade, default='')
    #AAMDC = models.CharField(max_length=155, choices=aamdc, default='')

    def __str__(self):
        return self.last_name


class IccTableOne(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_1_tasks = models.CharField(max_length=155, choices=icc_t1(), blank=True)
    task_complete = models.BooleanField(null=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.soldier+' '+self.trainer


class IccTableTwo(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_2_tasks = models.CharField(max_length=155, choices=icc_t2(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.soldier+' '+self.trainer


class IccTableThree(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_3_tasks = models.CharField(max_length=155, choices=icc_t3(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.soldier+' '+self.trainer


class IccTableFour(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_4_tasks = models.CharField(max_length=255, choices=icc_t4(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.soldier+' '+self.trainer


class IccTableFive(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_5_tasks = models.CharField(max_length=255, choices=icc_t5(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.soldier+' '+self.trainer


class IccTableSix(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_6_tasks = models.CharField(max_length=255, choices=icc_t6(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.soldier+' '+self.trainer


class IccTableSeven(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_7_tasks = models.CharField(max_length=255, choices=icc_t7(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.soldier+' '+self.trainer


class IccTableEight(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_8_tasks = models.CharField(max_length=255, choices=icc_t8(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.soldier+' '+self.trainer


class IccTableNine(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_9_tasks = models.CharField(max_length=255, choices=icc_t9(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.soldier+' '+self.trainer


class IccTableTen(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_10_tasks = models.CharField(max_length=255, choices=icc_t10(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.soldier + ' ' + self.trainer


class IccTableEleven(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_11_tasks = models.CharField(max_length=255, choices=icc_t11(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.soldier + ' ' + self.trainer


class IccTableTwelve(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_12_tasks = models.CharField(max_length=255, choices=icc_t12(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.soldier + ' ' + self.trainer


class CrgTableOne(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_1_tasks = models.CharField(max_length=155, choices=crg_t1(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class CrgTableTwo(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_2_tasks = models.CharField(max_length=155, choices=crg_t2(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class CrgTableThree(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_3_tasks = models.CharField(max_length=155, choices=crg_t3(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class CrgTableFour(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_4_tasks = models.CharField(max_length=155, choices=crg_t4(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class CrgTableFive(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_5_tasks = models.CharField(max_length=155, choices=crg_t5(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class CrgTableSix(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_6_tasks = models.CharField(max_length=155, choices=crg_t6(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class CrgTableSeven(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_7_tasks = models.CharField(max_length=155, choices=crg_t7(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class CrgTableEight(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_8_tasks = models.CharField(max_length=155, choices=crg_t8(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class AmgTableOne(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_1_tasks = models.CharField(max_length=155, choices=amg_t1(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class AmgTableTwo(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_2_tasks = models.CharField(max_length=155, choices=amg_t2(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class AmgTableThree(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_3_tasks = models.CharField(max_length=155, choices=amg_t3(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class AmgTableFour(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_4_tasks = models.CharField(max_length=155, choices=amg_t4(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class AmgTableFive(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_5_tasks = models.CharField(max_length=155, choices=amg_t5(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class AmgTableSix(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_6_tasks = models.CharField(max_length=155, choices=amg_t6(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class AmgTableSeven(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_7_tasks = models.CharField(max_length=155, choices=amg_t7(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class AmgTableEight(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_8_tasks = models.CharField(max_length=155, choices=amg_t8(), blank=True)
    task_complete = models.BooleanField(default=True)
    date_completed = models.DateField(null=True)
    trainer = models.CharField(max_length=255, blank=False)


class Cso(models.Model):
    soldier = models.ForeignKey(Soldierdata, on_delete=models.CASCADE)
    t_1_tasks = models.CharField(max_length=155, choices=crg_t1(), blank=True)
    t_2_tasks = models.CharField(max_length=155, choices=crg_t2(), blank=True)
    t_3_tasks = models.CharField(max_length=155, choices=crg_t3(), blank=True)
    t_4_tasks = models.CharField(max_length=155, choices=crg_t4(), blank=True)
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
