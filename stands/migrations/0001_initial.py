# Generated by Django 3.0.3 on 2020-02-27 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrgTableFour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_1_tasks', models.CharField(blank=True, choices=[('T1', 'Perform maintenance/display procedures for using the DA 5988E worksheet'), ('T2', 'CRG crew members perform operator level PMCS on the vehicle'), ('T3', 'CRG crew members perform PMCS on the 30KW generator set'), ('T4', 'CRG crew members perform CRG system PMCS/fault recognition and associated equipment PMCS'), ('T5', 'Perform SINGARS PMCS'), ('T6', 'Perform DAGR PMCS per TM'), ('T7', 'Perform SKL (Simple Key Loader) PMCS and operations'), ('T8', 'Perform LCU diagnostics for Routing logic radio interface unit'), ('T9', 'Emplace the AMG and EPU'), ('T10', 'March Order the AMG and EPU'), ('T11', 'Perform initialization of SMU'), ('T12', 'Learn functions of all switches and indicators of the CRG system')], max_length=155)),
                ('task_complete', models.BooleanField(default=True)),
                ('date_completed', models.DateField(null=True)),
                ('trainer', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CrgTableOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_1_tasks', models.CharField(blank=True, choices=[('T1', 'Perform maintenance/display procedures for using the DA 5988E worksheet'), ('T2', 'CRG crew members perform operator level PMCS on the vehicle'), ('T3', 'CRG crew members perform PMCS on the 30KW generator set'), ('T4', 'CRG crew members perform CRG system PMCS/fault recognition and associated equipment PMCS'), ('T5', 'Perform SINGARS PMCS'), ('T6', 'Perform DAGR PMCS per TM'), ('T7', 'Perform SKL (Simple Key Loader) PMCS and operations'), ('T8', 'Perform LCU diagnostics for Routing logic radio interface unit'), ('T9', 'Emplace the AMG and EPU'), ('T10', 'March Order the AMG and EPU'), ('T11', 'Perform initialization of SMU'), ('T12', 'Learn functions of all switches and indicators of the CRG system')], max_length=155)),
                ('task_complete', models.BooleanField(default=True)),
                ('date_completed', models.DateField(null=True)),
                ('trainer', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CrgTableThree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_1_tasks', models.CharField(blank=True, choices=[('T1', 'Perform prepare for movement drills on CRG and EPU'), ('T2', 'Perform emplacement drill on CRG and EPU'), ('T3', 'Perform LCU initialization'), ('T4', 'Perform CRG initialization'), ('T5', 'Establish communications per communications plan'), ('T6', 'Perform maintenance sustainment operations')], max_length=155)),
                ('task_complete', models.BooleanField(default=True)),
                ('date_completed', models.DateField(null=True)),
                ('trainer', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CrgTableTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_1_tasks', models.CharField(blank=True, choices=[('T1', 'Establish communications per communications plan'), ('T2', 'Perform LCU initialization'), ('T3', 'Learn to identify fault indicators and indications'), ('T4', 'Select and interpret LCU tabular displays')], max_length=155)),
                ('task_complete', models.BooleanField(default=True)),
                ('date_completed', models.DateField(null=True)),
                ('trainer', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='IccTableFour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_4_tasks', models.CharField(blank=True, choices=[('T1', 'Crew members demonstrate proper performance of PMCS of the ICC, AMG, EPUs, and all communications equipment'), ('T2', 'ICC crew members will demonstrate knowledge of the Patriot system and unit tactical directives'), ('T3', 'ICC crew members demonstrate power up and initialize the ICC'), ('T4', 'Crew members perform RFA drills and correctly configure the system for the directed alert state'), ('T5', 'Crew members demonstrate how to use the Patriot tactical planner to develop battalion TBM/ABT DD'), ('T6', 'TDs/TDAs demonstrate knowledge of Patriot system capabilities and unit tactical directives'), ('T7', 'ICC crew members conduct Patriot air defense operations using an ABML 5 scenario while controlling a minimum of two fire units'), ('T8', 'ICC crew members demonstrate reporting requirements'), ('T9', 'Establish and operate the battalion communications net per communications plan'), ('T10', 'ICC crew members demonstrate reporting requirements'), ('T11', 'Crew members perform maintenance sustainment operations')], max_length=255)),
                ('task_complete', models.BooleanField(default=True)),
                ('trainer', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='IccTableOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_1_tasks', models.CharField(blank=True, choices=[('T1', 'Perform ICC PMCS/TWUD fault recognition'), ('T2', 'Perform AMG PMCS'), ('T3', 'Perform EPU PMCS'), ('T4', 'Perform LCU inialization/diagnostics'), ('T5', 'Perform Communication equipment PMCS'), ('T6', 'Initialize the MIDS'), ('T7', 'Perform MIDS Crypto-key loading'), ('T8', 'Emplace the ICC, AMG, and EPUs'), ('T9', 'Initialize the ICC'), ('T10', 'March Order the ICC, AMG, and EPUs'), ('T11', 'Perform initialization of the SMU and JTIDS terminal'), ('T12', 'Create a TBM and ABT Defense plan'), ('T13', 'Perform communications link planning')], max_length=155)),
                ('task_complete', models.BooleanField(null=True)),
                ('date_completed', models.DateField(null=True)),
                ('trainer', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='IccTableThree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_3_tasks', models.CharField(blank=True, choices=[('T1', 'ICC crew members create, update, and maintain the battalion site data book'), ('T2', 'Crew members apply the parameters stated in the TSOP and dictated by the STO'), ('T3', 'ICC crew members discuss defense design and events that result in the changing of tabular entries'), ('T4', 'Crew members identify the ICC and fire unit capabilities and limitations'), ('T5', 'Crew members demonstrate how to use the Patriot tactical planner to develop a Battalion TBM/ABT defense design'), ('T6', 'Conduct air defense operations using ABMLs 1 through 4'), ('T7', 'Learn reporting requirements including mIRC procedures')], max_length=155)),
                ('task_complete', models.BooleanField(default=True)),
                ('trainer', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='IccTableTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_2_tasks', models.CharField(blank=True, choices=[('T1', 'ICC crew members learn functions of tabs and tabular entries'), ('T2', 'ICC crew members learn the functions of all controls, switches, and indicators'), ('T3', 'ICC crew members recognize Patriot symbology'), ('T4', 'ICC crew members learn the situational displays'), ('T5', 'Crew members learn alert states, STO, and ACO'), ('T6', 'Crew members learn fix or fight criteria, including fire platoon faults'), ('T7', 'ICC crew members discuss evaluation decision and weapon assignment (EDWA)'), ('T8', 'ICC crew members learn Patriot weapon system capabilities and limitations'), ('T9', 'ICC crew members perform RFA drills, correctly configure configure for directed alert state'), ('T10', 'ICC crew members learn applicable TSOP and SOPs'), ('T11', 'ICC crew members learn to read and process USMTF messages ATOs/ACOs'), ('T12', 'Perform maintenance sustainment operations')], max_length=155)),
                ('task_complete', models.BooleanField(default=True)),
                ('date_completed', models.DateField(null=True)),
                ('trainer', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Soldierdata',
            fields=[
                ('DODID', models.IntegerField(primary_key=True, serialize=False)),
                ('Rank', models.CharField(blank=True, choices=[('PVT', 'PVT'), ('PV2', 'PV2'), ('PFC', 'PFC'), ('SPC', 'SPC'), ('SGT', 'SGT'), ('SSG', 'SSG'), ('SFC', 'SFC'), ('MSG', 'MSG'), ('2LT', '2LT'), ('1LT', '1LT'), ('CPT', 'CPT'), ('MAJ', 'MAJ'), ('WO1', 'WO1'), ('CW2', 'CW2'), ('CW3', 'CW3')], default='PVT', max_length=155)),
                ('last_name', models.CharField(max_length=155)),
                ('first_name', models.CharField(max_length=155)),
                ('MOS', models.CharField(choices=[('14E', '14E'), ('14T', '14T'), ('14H', '14H'), ('14A', '14A'), ('140K', '140K'), ('25N', '25N'), ('25U', '25U')], max_length=155)),
                ('Position', models.CharField(blank=True, choices=[('TD', 'Tactical Director'), ('TDA', 'Tactical Director Assistant'), ('TCO', 'Tactical Control Officer'), ('TCA', 'Tactical Control Assistant'), ('TPW', 'Early Warning Operator'), ('RO', 'Radio Operator/ Reports operator'), ('JWARN', 'JWARN Operator')], max_length=155)),
                ('Platoon', models.CharField(blank=True, choices=[('Fire Control', 'Fire Control'), ('Launcher', 'Launcher'), ('Fire Direction Control', 'Fire Direction Control')], max_length=155)),
                ('Battery', models.CharField(blank=True, choices=[('HHB', 'HHB'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=155)),
                ('Battalion', models.CharField(blank=True, choices=[('4-3 ADA', '4-3 ADA'), ('3-2 ADA', '3-2 ADA')], max_length=155)),
                ('Brigade', models.CharField(blank=True, choices=[('31st BDE', '31st BDE')], max_length=155)),
                ('AAMDC', models.CharField(blank=True, choices=[('32 AAMDC', '32 AAMDC'), ('10th AAMDC', '10th AAMDC'), ('94th AAMDC', '94th AAMDC')], max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crg_t1_complete', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stands.CrgTableOne')),
                ('crg_t2_complete', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stands.CrgTableTwo')),
                ('crg_t3_complete', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stands.CrgTableThree')),
                ('crg_t4_complete', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stands.CrgTableFour')),
                ('icc_t1_complete', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stands.IccTableOne')),
                ('icc_t2_complete', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stands.IccTableTwo')),
                ('icc_t3_complete', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stands.IccTableThree')),
                ('icc_t4_complete', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stands.IccTableFour')),
                ('soldier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stands.Soldierdata')),
            ],
        ),
        migrations.AddField(
            model_name='icctabletwo',
            name='soldier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stands.Soldierdata'),
        ),
        migrations.AddField(
            model_name='icctablethree',
            name='soldier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stands.Soldierdata'),
        ),
        migrations.AddField(
            model_name='icctableone',
            name='soldier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stands.Soldierdata'),
        ),
        migrations.AddField(
            model_name='icctablefour',
            name='soldier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stands.Soldierdata'),
        ),
        migrations.CreateModel(
            name='Cso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_1_tasks', models.CharField(blank=True, choices=[('T1', 'Perform maintenance/display procedures for using the DA 5988E worksheet'), ('T2', 'CRG crew members perform operator level PMCS on the vehicle'), ('T3', 'CRG crew members perform PMCS on the 30KW generator set'), ('T4', 'CRG crew members perform CRG system PMCS/fault recognition and associated equipment PMCS'), ('T5', 'Perform SINGARS PMCS'), ('T6', 'Perform DAGR PMCS per TM'), ('T7', 'Perform SKL (Simple Key Loader) PMCS and operations'), ('T8', 'Perform LCU diagnostics for Routing logic radio interface unit'), ('T9', 'Emplace the AMG and EPU'), ('T10', 'March Order the AMG and EPU'), ('T11', 'Perform initialization of SMU'), ('T12', 'Learn functions of all switches and indicators of the CRG system')], max_length=155)),
                ('t_2_tasks', models.CharField(blank=True, choices=[('T1', 'Establish communications per communications plan'), ('T2', 'Perform LCU initialization'), ('T3', 'Learn to identify fault indicators and indications'), ('T4', 'Select and interpret LCU tabular displays')], max_length=155)),
                ('t_3_tasks', models.CharField(blank=True, choices=[('T1', 'Perform prepare for movement drills on CRG and EPU'), ('T2', 'Perform emplacement drill on CRG and EPU'), ('T3', 'Perform LCU initialization'), ('T4', 'Perform CRG initialization'), ('T5', 'Establish communications per communications plan'), ('T6', 'Perform maintenance sustainment operations')], max_length=155)),
                ('t_4_tasks', models.CharField(blank=True, choices=[('T1', 'Perform prepare for movement drills on CRG and EPU'), ('T2', 'Perform emplacement drill on CRG and EPU'), ('T3', 'Perform LCU initialization'), ('T4', 'Perform CRG initialization'), ('T5', 'Establish communications per communications plan'), ('T6', 'Perform PMCS and fault recognition on CRG, EPU, and associated equipment')], max_length=155)),
                ('task_complete', models.BooleanField(null=True)),
                ('date_completed', models.DateField(null=True)),
                ('soldier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stands.Soldierdata')),
            ],
        ),
        migrations.AddField(
            model_name='crgtabletwo',
            name='soldier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stands.Soldierdata'),
        ),
        migrations.AddField(
            model_name='crgtablethree',
            name='soldier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stands.Soldierdata'),
        ),
        migrations.AddField(
            model_name='crgtableone',
            name='soldier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stands.Soldierdata'),
        ),
        migrations.AddField(
            model_name='crgtablefour',
            name='soldier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stands.Soldierdata'),
        ),
    ]
