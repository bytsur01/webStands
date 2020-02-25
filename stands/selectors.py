# lib for choices. Only input choices to this lib


def unit():
    battalion = [
        ('4-3 ADA', '4-3 ADA'),
        ('3-2 ADA', '3-2 ADA'),
    ]
    return battalion


def icc_t1():
    table_1 = [
        ('T1', 'Perform ICC PMCS/TWUD fault recognition'),
        ('T2', 'Perform AMG PMCS'),
        ('T3', 'Perform EPU PMCS'),
        ('T4', 'Perform LCU inialization/diagnostics'),
        ('T5', 'Perform Communication equipment PMCS'),
        ('T6', 'Initialize the MIDS'),
        ('T7', 'Perform MIDS Crypto-key loading'),
        ('T8', 'Emplace the ICC, AMG, and EPUs'),
        ('T9', 'Initialize the ICC'),
        ('T10', 'March Order the ICC, AMG, and EPUs'),
        ('T11', 'Perform initialization of the SMU and JTIDS terminal'),
        ('T12', 'Create a TBM and ABT Defense plan'),
        ('T13', 'Perform communications link planning'),
    ]
    return table_1


def icc_t2():
    table_2 = [
        ('T1', 'ICC crew members learn functions of tabs and tabular entries'),
        ('T2', 'ICC crew members learn the functions of all controls, switches, and indicators'),
        ('T3', 'ICC crew members recognize Patriot symbology'),
        ('T4', 'ICC crew members learn the situational displays'),
        ('T5', 'Crew members learn alert states, STO, and ACO'),
        ('T6', 'Crew members learn fix or fight criteria, including fire platoon faults'),
        ('T7', 'ICC crew members discuss evaluation decision and weapon assignment (EDWA)'),
        ('T8', 'ICC crew members learn Patriot weapon system capabilities and limitations'),
        ('T9', 'ICC crew members perform RFA drills, correctly configure configure for directed alert state'),
        ('T10', 'ICC crew members learn applicable TSOP and SOPs'),
        ('T11', 'ICC crew members learn to read and process USMTF messages ATOs/ACOs'),
        ('T12', 'Perform maintenance sustainment operations'),
    ]
    return table_2


def icc_t3():
    table_3 = [
        ('T1', 'ICC crew members create, update, and maintain the battalion site data book'),
        ('T2', 'Crew members apply the parameters stated in the TSOP and dictated by the STO'),
        ('T3', 'ICC crew members discuss defense design and events that result in the changing of tabular entries'),
        ('T4', 'Crew members identify the ICC and fire unit capabilities and limitations'),
        ('T5',
         'Crew members demonstrate how to use the Patriot tactical planner to develop a Battalion TBM/ABT defense '
         'design'),
        ('T6', 'Conduct air defense operations using ABMLs 1 through 4'),
        ('T7', 'Learn reporting requirements including mIRC procedures'),
    ]
    return table_3


def icc_t4():
    table_4 = [
        ('T1',
         'Crew members demonstrate proper performance of PMCS of the ICC, AMG, EPUs, and all communications equipment'),
        ('T2', 'ICC crew members will demonstrate knowledge of the Patriot system and unit tactical directives'),
        ('T3', 'ICC crew members demonstrate power up and initialize the ICC'),
        ('T4',
         'Crew members perform RFA drills and correctly configure the system for the directed alert state'),
        ('T5',
         'Crew members demonstrate how to use the Patriot tactical planner to develop battalion TBM/ABT DD'),
        ('T6', 'TDs/TDAs demonstrate knowledge of Patriot system capabilities and unit tactical directives'),
        ('T7',
         'ICC crew members conduct Patriot air defense operations using an ABML 5 scenario while controlling a '
         'minimum of two fire units'),
        ('T8', 'ICC crew members demonstrate reporting requirements'),
        ('T9', 'Establish and operate the battalion communications net per communications plan'),
        ('T10', 'ICC crew members demonstrate reporting requirements'),
        ('T11', 'Crew members perform maintenance sustainment operations'),
    ]
    return table_4


def icc_t5():
    table_5 = [
        ('T1',
         'Develop and implement a battalion level defense design based on threats/defended asset list and input into '
         'the ICC'),
        ('T2', 'TD/TDA process tactical information using the TCS Patriot tactical planner'),
        ('T3', 'TD/TDA create a site/system data book for Table V scenarios'),
        ('T4', 'TD/TDA conduct air defense operations using ABLMs 6 through 9'),
    ]
    return table_5


def icc_t6():
    table_6 = [
        ('T1', 'Crew members perform prepare for movement drills for the ICC, AMG, and EPUs'),
        ('T2', 'Crew members emplace the ICC, AMG, and EPUs'),
        ('T3', 'ICC crew members initialize the ICC'),
        ('T4',
         'ICC crew members perform ready for action drills, correctly configuring system for a directed alert state'),
        ('T5', 'Perform maintenance sustainment operations'),
    ]
    return table_6


def icc_t7():
    table_7 = [
        ('T1', 'Crew members prepare for movement drills for the ICC, AMG, and EPUs'),
        ('T2', 'Crew members emplace the ICC, AMG, and EPUs'),
        ('T3', 'ICC crew members initialize the ICC'),
        ('T4',
         'ICC crew members perform ready for action drills, correctly configuring system for directed alert state'),
        ('T5', 'The ICC conducts air defense operations while controlling two or more fire units using ABMLs 10 or 11'),
        ('T6', 'Perform maintenance sustainment operations'),
    ]
    return table_7


def icc_t8():
    table_8 = [
        ('T1', 'Crew members prepare for movement drills for the ICC, AMG, and EPUs'),
        ('T2', 'Crew members emplace the ICC, AMG, and EPUs'),
        ('T3', 'ICC crew members initialize the ICC'),
        ('T4',
         'ICC crew members perform ready for action drills, correctly configuring system for directed alert state'),
        ('T5', 'The ICC conducts air defense operations while controlling two or more fire units using ABML 11'),
        ('T6', 'Perform maintenance sustainment operations'),
    ]
    return table_8


def icc_t9():
    table_9 = [
        ('T1', 'Create site/system data book'),
        ('T2', 'Crew members conduct PMCS during on-going operations'),
        ('T3',
         'ICC crew members condition the system at an alert state 5-1, maintaining manning and communications '
         'requirements'),
        ('T4', 'ICC crew members conduct oversight of fire units, including fire unit control of an RL-3 site'),
        ('T5', 'ICC crews update status reports and demonstrate understanding of current equipment status'),
        ('T6', 'ICC crew members react to a STO directing at least two fire units to an alert state 1, 2, or 3'),
        ('T7', 'Process tactical information'),
        ('T8', 'Submit required tactical reports'),
        ('T9', 'Perform maintenance sustainment operations'),
    ]
    return table_9


def icc_t10():
    table_10 = [
        ('T1',
         'ICC crew members conduct Patriot AD operations using ABML 12-13 while controlling two or more fire units '
         'and managing the operations of one or more LCSs'),
        ('T2', 'Perform maintenance sustainment operations'),
    ]
    return table_10


def icc_11():
    table_11 = [
        ('T1', 'Crew members conduct PMCS during on-going operations'),
        ('T2',
         'ICC crew members condition the system at an alert state 5-1, maintaining manning and communications '
         'requirements'),
        ('T3', 'ICC crew members conduct oversight of the fire units, including fire units controlling RL-3 sites'),
        ('T4', 'ICC crews update status reports and demonstrate understanding of current equipment status'),
        ('T5', 'ICC crew members react to a STO directing at least two fire units to an alert state 1, 2, or 3'),
        ('T6', 'Submit required tactical reports'),
        ('T7',
         'ICC crew members conduct Patriot AD operations using ABML 14-15 while controlling two or more fire units '
         'and managing the operations of one or more LCSs'),
        ('T8', 'Perform maintenance sustainment operations'),
    ]
    return table_11


def icc_12():
    table_12 = [
        ('T1', 'Crew members conduct PMCS during on-going operations'),
        ('T2',
         'ICC crew members condition the system at an alert state 5-1, maintaining manning and communications '
         'requirements'),
        ('T3', 'ICC crew members conduct oversight of the fire units, including fire units controlling RL-3 sites'),
        ('T4', 'ICC crews update status reports and demonstrate understanding of current equipment status'),
        ('T5', 'ICC crew members react to a STO directing at least two fire units to an alert state 1, 2, or 3'),
        ('T6', 'Submit required tatical reports'),
        ('T7',
         'ICC crew members conduct Patriot AD operations using ABML 16 while controlling two or more fire units and '
         'managing the operations of one or more LCSs'),
        ('T8', 'Perform maintenance sustainment operations'),
    ]
    return table_12


def amg_t1():
    table_1 = [
        ('T1', 'Perform maintenance/display procedures for using the DA 5988E worksheet'),
        ('T2', 'AMG crew members perform operator level PMCS on the vehicle'),
        ('T3', 'AMG crew members perform PMCS on the 30KW generator set'),
        ('T4', 'AMG crew members perform AMG system PMCS and associated equipment PMCS'),
        ('T5', 'Perform SINGARS PMCS'),
        ('T6', 'Perform DAGR PMCS per TM'),
        ('T7', 'Perform SKL (Simple Key Loader) PMCS and operations'),
        ('T8', 'Emplace the AMG and EPU'),
        ('T9', 'March Order the AMG and EPU'),
        ('T10', 'Perform initialization of SMU'),
        ('T11', 'Perform operator PMCS on any other applicable assigned equipment')
    ]
    return table_1


def amg_t2():
    table_2 = [
        ('T1', 'Establish communications per communications plan'),
        ('T2', 'Learn to identify fault indicators and indications'),
        ('T3', 'Perform maintenance sustainment operations'),
    ]
    return table_2


def amg_t3():
    table_3 = [
        ('T1', 'Perform prepare for movement drills on AMG and EPU'),
        ('T2', 'Perform emplacement drill on AMG and EPU'),
        ('T3', 'Establish communications per communications plan'),
        ('T4', 'Perform maintenance sustainment operations'),
    ]
    return table_3


def amg_t4():
    table_4 = [
        ('T1', 'Perform prepare for movement drills on CRG and EPU'),
        ('T2', 'Perform emplacement drill on CRG and EPU'),
        ('T3', 'Establish communications per communications plan'),
        ('T4', 'Perform PMCS and fault recognition on AMG, EPU, and associated equipment'),
    ]
    return table_4


def amg_t5():
    table_5 = [
        ('T1', 'Perform prepare for movement drills on AMG and EPU'),
        ('T2', 'Perform emplacement drill on AMG and EPU'),
        ('T3', 'Learn how the AMG functions with the ICC or CRG in an operational environment'),
    ]
    return table_5


def amg_t6():
    table_6 = [
        ('T1', 'Crew members demonstrate PMCS during on going operations'),
        ('T2', 'Crew members perform prepare for movement of the AMG, and EPUs collectively with the ICC or CRG'),
        ('T3', 'Crew members emplace of the AMG and EPUs collectively with the ICC or CRG'),
        ('T4', 'Establish and operate the Battalion coomunictions net'),
        ('T5', 'Perform maintenance sustainment operations'),
    ]
    return table_6


def amg_t7():
    table_7 = [
        ('T1', 'Crew members demonstrate PMCS during on going operations'),
        ('T2', 'Demonstrate prepare for movement of the AMG, and EPUs collectively with the ICC or CRG'),
        ('T3', 'Demonstrate emplacement of the AMG and EPUs collectively with the ICC or CRG'),
        ('T4', 'Peform maintenance sustainment operations on all assigned equipment'),
    ]
    return table_7


def amg_t8():
    table_8 = [
        ('T1', 'Demonstrate prepare for movement of the AMG, and EPUs collectively with the ICC or CRG'),
        ('T2', 'Demonstrate emplacement of the AMG and EPUs collectively with the ICC or CRG'),
        ('T3', 'Peform maintenance sustainment operations on all assigned equipment'),
    ]
    return table_8


def tcs_t1():
    table_1 = [
        ('T1', 'Perform maintenance/display proper procedures for using the DA 5988E worksheet'),
        ('T2', 'Perform operator PMCS on the TCS truck'),
        ('T3', 'Perform operator PMCS on the TCS shelter'),
        ('T4', 'Perform opertor PMCS on the 30 kw tactical quiet generator'),
        ('T5', 'Perform SINCGARS PMCS'),
        ('T6', 'Perform DAGR PMCS'),
        ('T7', 'Perform SKL (Simple Key Loader) PMCS'),
        ('T8', 'Perform FOCA (FiberOptic Cable Assembly) PMCS'),
        ('T9', 'Perform emplacement on TCS and EPU'),
        ('T10', 'Perform prepare for movement on TCS'),
        ('T11', 'Understand the basic structure of the current PDB TCS/BCP course of instruction'),
        ('T12', 'Understand the TCS and ICC hardware setup'),
        ('T13', 'Understand the TCS communications setup'),
        ('T14', 'Verify software version of the TCS TPW'),
        ('T15', 'Understand the TPW main menu and toolbars'),
        ('T16', 'Understand how to use the workspace structure'),
        ('T17', 'How to open and save a file on the TPW'),
        ('T18', 'How to use the object select and delete functions on the TPW'),
        ('T19', 'Display bubble help for icons on the tool bar'),
        ('T20', 'Delete a map from the hard drive'),
        ('T21', 'Understand how to use the Master and Catalog functions'),
        ('T22', 'Insert an object on a 2525 symbol'),
        ('T23', 'Understand how to use the Geoset Manager'),
        ('T24', 'Demonstrate the ability to replay files using the camera'),
        ('T25', 'Demonstrate the ability to change user password'),
        ('T26',
         'Use print screen button on the Integrated Keyboard Monitor (IKM) to save a screen shoot to the hard drive'),
        ('T27', 'Backup user selected files (Screen Capture)'),
        ('T28', 'Backup, restore, and file transfer workspace files'),
        ('T29', 'Determine disk usage for all utilities'),
        ('T30', 'Communications theory and overview'),
        ('T31', 'Describe and understand the purpose of the ACMAF, SAMSTAT, STO, and JSIR reports'),
        ('T32', 'Understand and interpret the 3D air picture'),
        ('T33', 'Describe the TCS CIB setup'),
        ('T34', 'Describe the CIB data flow'),
        ('T35', 'Demonstrate TIPOFF shut down'),
        ('T36', 'Undertand geographic overlays and how to build them'),
        ('T37', 'Demonstrate and operate the alert system'),
        ('T38', 'Install TIPOFF hints'),
        ('T39', 'Review and understand Battalion netted configuration'),
        ('T40', 'Review and understand the TPW interface'),
        ('T41', 'Login as administrator within all applicable systems'),
        ('T42', 'Opem file management window with basic access and privileged access'),
        ('T43', 'Open terminal window and experiment with UNIX commands'),
        ('T44', 'Retrieve audit log files'),
        ('T45', 'Pre-Installation procedures'),
        ('T46', 'B2CP baseline software (Solaris Operation System) installation'),
        ('T47', 'Install Link 16 Common User Interface (CUI)'),
        ('T48', 'Update the etc/hosts file'),
        ('T49', 'Basic security module (auditing) configuration'),
        ('T50', 'Initializing Lennox Red Hat Management Console and adding user accounts'),
        ('T51', 'BSD/CDLI software installation'),
        ('T52', 'Demonstrate the ability to use the footprint installation'),
        ('T53', 'Patriot plug in software installation'),
        ('T54', 'Install Tactical Threat Database (TTDB)'),
        ('T55', 'Printer setup and print out host files'),
        ('T56', 'Set maximum replay file size'),
        ('T57', 'Link Manager (TIE) configuration'),
        ('T58', 'Add desktop program icons and menus for new accounts'),
        ('T59', 'Perform Sys-Unconfig'),
        ('T60', 'Configure and add new time zones to desktop'),
    ]
    return table_1


def tcs_t2():
    table_t2 = [
        ('T1', 'Perform ready for action drills'),
        ('T2', 'Discuss alert states, STOs, ACMAFs, SAMSTATs, and mIRC reporting procedures'),
        ('T3', 'Prepare and load the TCS for movement'),
        ('T4', 'Understand the TPW power-up procedures and link statuses'),
        ('T5', 'Understand and know how to confgure the ICC database'),
        ('T6', 'Know how to ground and power-up workstation'),
        ('T7', 'Know where to locate the ECU, SHCU, IKM, and how to operate them'),
        ('T8', 'Import and catelog DTED and ADRG maps from a CD-ROM'),
        ('T9', 'Insert, display, and delete a Map region or high area'),
        ('T10', 'Insert General Points, Preplanned Points, and Survery Sites'),
        ('T11', 'Demonstrate the ability to use replay'),
        ('T12', 'Restore replay files'),
        ('T13', 'Start the CUI software'),
        ('T14', 'Copying and Load files from a CD and the CUI directory'),
        ('T15', 'Operate the CUI software for JTIDS in the BCP netted mode'),
        ('T16', 'Power up the CIB'),
        ('T17', 'Load the JTT Crypto'),
        ('T18', 'Configure the JTT to TIPOFF to TCS links'),
        ('T19', 'Determine where to point the JTT Antenna'),
        ('T20', 'Set the JTT System Time'),
        ('T21', 'Sign on the CIB using sign on wizard, and connect to the workstation'),
        ('T22', 'Demonstrate the ability to use Geographic Filters'),
        ('T23', 'Power-up the JTT, TIPOFF laptop, and at least one TCS workstation'),
        ('T24', 'Check TIPOFF to JTT and TIPOFF to TCS configuration status'),
        ('T25', 'Activate the TIPOFF software'),
        ('T26', 'Use the alert system to alarm the site'),
        ('T27', 'Print tabs locally and send tabs to the ICC'),
        ('T28', 'Yser the pointer function and email'),
        ('T29', 'Display and print TCS netted status'),
        ('T30', 'Import mission into the TPW'),
        ('T31', 'Perform defense planning with the TPW'),
        ('T32', 'Create/Export defense design from the TPW'),
        ('T33', 'Import/modify imported mission and export defense plan'),
    ]
    return table_t2


def tcs_t3():
    table_t3 = [
        ('T1', 'Conduct air defense operationsusing Documents ABML 1 through 4'),
        ('T2', 'Learn reporting requirements including mIRC procedures per documents'),
        ('T3', 'Demonstrate the ability to toggle objects and maps'),
        ('T4', 'Use MEasure Distance feature'),
        ('T5', 'Use Object Locator feature'),
        ('T6', 'Use Site Editor feature'),
        ('T7', 'Use the 3D Camera and Tools'),
        ('T8', 'Demonstrate the ability to operate Battalion Exerciser'),
        ('T9', 'Use Message center'),
        ('T10', 'Retrieve a nd compare planning'),
        ('T11', 'Use BCP/TCS Auto Tabs'),
        ('T12', 'Air Picture Controls and Indicators'),
        ('T13', 'Describes the symbology used in the TCS/BCP'),
        ('T14', 'Operate and Filter an Air Picture'),
        ('T15', 'Statistics, Mission Report and Altitude vs. Time'),
        ('T16', 'Know and Understand how to Filter an Air Picture'),
        ('T17', 'Buffer Transfer data to the ICC'),
        ('T18', 'Receive and Print Tactical and Status Tabs from ICC'),
        ('T19', 'Buffer Transfer data to an ECS'),
        ('T20', 'Show differences between Tabs in the Active Plan and an ICC'),
        ('T21', 'Demonstrate the ability to input Automated Tab Inputs'),
        ('T22', 'Demonstratethe ability to Display Track Amp Tabs'),
    ]
    return table_t3


def tcs_t4():
    table_t4 = [
        ('T1', ' Perform opertor level PMCS on the 30-Kw generator'),
        ('T2',
         'Perform operator and organizational level maintenance on the TCS Shelter, Truck and all communications '
         'equipment'),
        ('T3', 'Demonstrate knowledge of Patriot communications capabilities and reporting procedures'),
        ('T4', 'Crewmembers conduct system initialization and ready-for-action drills'),
        ('T5', 'Conduct air defense operations using ABML 5'),
    ]
    return table_t4


def tcs_t5():
    table_5 = [
        ('T1', 'Discuss and create site data book'),
        ('T2', 'TCS crew members conduct air defense operations using ABMLs 6 through 9 with the ICC'),
        ('T3', 'Know and understand how to create a new defense plan and defense sub-folder'),
        ('T4',
         'Know and understand how to use the side panel to display, open, rename, copy, and delete a defense plan'),
        ('T5', 'Understand how to use the zoom and pan functions'),
        ('T6', 'Know and understand how to insert a single point object via mouse pick and/or key in'),
        ('T7', 'Understand the two ways to insert Range Rings'),
        ('T8', 'Understand how to insert the 2525 symbology'),
        ('T9', 'How to insert free text'),
        ('T10', 'Understand how to move an object'),
        ('T11', 'Know how to insert multiple point objects via mouse pick or key in'),
        ('T12', 'Know how to modify, delete, and insert a point from a multiple point object'),
        ('T13', 'Determine the version date of TBM footprints and Tactical Threat Data Base (TTDB)'),
        ('T14', 'Display the TBM defense tool bar'),
        ('T15', 'Know and understand the LACM tool bar'),
        ('T16', 'Understand missile fly out and missile aquisition test'),
        ('T17', ')Anaylze UHF communications links'),
        ('T18', 'Add a CRG and insert an LCS'),
        ('T19', 'Generate UHF communications links and remove bad communications links'),
        ('T20', 'Add communications link between two units'),
        ('T21', 'Toggle communications links on and off'),
        ('T22', 'Auto generate of Tab 62'),
        ('T23', 'Display and print communications net report'),
        ('T24', 'Use and generate bubble charts'),
        ('T25', 'Move a node and change a node type'),
        ('T26', 'Demenstrate the ability to conduct TBM defense planning'),
        ('T27', 'Demonstrate the ability to perform EMI analysis'),
        ('T28', 'Demonstrate the ability to perform TBM tailoring'),
        ('T29', 'Conduct planning for cruise missle/ABT low altitude keep out zone'),
        ('T30', 'Patriot cruise missile defense planning'),
        ('T31', 'Demonstrate the ability to conduct ABT defense planning'),
        ('T32', 'Demonstrate the anility to conduct passive emplacement'),
        ('T33', 'Know what radar sensor anyalysis consists of'),
        ('T34', 'Know and understand alternate search sectors'),
        ('T35', 'Conduct TCS planning and preperation for the ICC and fire units'),
        ('T36', 'Input a ACM database from an ACO'),
        ('T37', 'Delete ACM columes from a defense plan'),
        ('T38', 'Import an ACO into a defesne plan'),
        ('T39', 'Develop and activate a defense plan'),
    ]
    return table_5


def tcs_t6():
    table_6 = [
        ('T1', 'Perform prepare for movement on TCS and EPU'),
        ('T2', 'Perform emplacement on TCS and EPU'),
        ('T3', 'Establish and operate a TCS with a provided communications plan'),
        ('T4', 'Establish and operate a Battalion communications net'),
        ('T5', 'Perform maintenance sustainment operations'),
    ]
    return table_6


def tcs_t7():
    table_7 = [
        ('T1', 'Perform prepare for movement on TCS and EPU'),
        ('T2', 'Perform emplacement on TCS and EPU'),
        ('T3', 'Establish and operate a TCS with provided communications plan'),
        ('T4', 'Coordinate/Conduct air defense operations using ABML 9-10'),
        ('T5', 'Perform maintenance sustainment operations'),
    ]
    return table_7


def tcs_t8():
    table_8 = [
        ('T1', 'Perform prepare for movement on TCS and EPU'),
        ('T2', 'Perform emplacement on TCS and EPU'),
        ('T3', 'Establish and operate a TCS with provided communications plan'),
        ('T4', 'Coordinate/Conduct air defense operations using ABML 11'),
        ('T5', 'Perform maintenance sustainment operations'),
    ]
    return table_8


def tcs_t9():
    table_9 = [
        ('T1', 'Create site/system data book'),
        ('T2', 'Process tactical information in the TSOP and unit SOPs'),
        ('T3', 'Perform ready for action drills'),
        ('T4', 'Submit required tactical reports including mIRC procedures'),
        ('T5', 'Perform maintenance sustainment operations in a steady state environment'),
    ]
    return table_9


def tcs_t10():
    table_10 = [
        ('T1', 'Crew members conduct PMCS on TCS and all associated equipment during on going operations'),
        ('T2', 'Perform ready for action drills'),
        ('T3',
         'Conduct Patriot AD operations using ABML 12-13 while controlling two or more fire units and managing the '
         'operations of one or more LCSs'),
    ]
    return table_10


def tcs_t11():
    table_11 = [
        ('T1', 'Crew members conduct PMCS during on-going operations'),
        ('T2',
         'TCS crew members manage system at an alert state 5-1, maintaining manning and communications requirements'),
        ('T3', 'TCS crew members conduct oversight of the fire units, including fire units controlling RL-3 sites'),
        ('T4', 'TCS crews update status reports and demonstrate understanding of current equipment status'),
        ('T5', 'TCS crew members react to a STO directing at least two fire units to an alert state 1, 2, or 3'),
        ('T6', 'Submit required tatical reports'),
        ('T7',
         'ICC crew members conduct Patriot AD operations using ABMLs 14-15 while controlling two or more fire units '
         'and managing the operations of one or more LCSs'),
        ('T8', 'Perform maintenance sustainment operations'),
    ]
    return table_11


def tcs_t12():
    table_12 = [
        ('T1', 'Crew members conduct PMCS during on-going operations'),
        ('T2',
         'TCS crew members manage system at an alert state 5-1, maintaining manning and communications requirements'),
        ('T3', 'TCS crew members conduct oversight of the fire units, including fire units controlling RL-3 sites'),
        ('T4', 'TCS crews update status reports and demonstrate understanding of current equipment status'),
        ('T5', 'TCS crew members react to a STO directing at least two fire units to an alert state 1, 2, or 3'),
        ('T6', 'Submit required tatical reports'),
        ('T7',
         'ICC crew members conduct Patriot AD operations using ABML 16 while controlling two or more fire units and '
         'managing the operations of one or more LCSs'),
        ('T8', 'Perform maintenance sustainment operations'),
    ]
    return table_12


def crg_t1():
    table_1 = [
        ('T1', 'Perform maintenance/display procedures for using the DA 5988E worksheet'),
        ('T2', 'CRG crew members perform operator level PMCS on the vehicle'),
        ('T3', 'CRG crew members perform PMCS on the 30KW generator set'),
        ('T4', 'CRG crew members perform CRG system PMCS/fault recognition and associated equipment PMCS'),
        ('T5', 'Perform SINGARS PMCS'),
        ('T6', 'Perform DAGR PMCS per TM'),
        ('T7', 'Perform SKL (Simple Key Loader) PMCS and operations'),
        ('T8', 'Perform LCU diagnostics for Routing logic radio interface unit'),
        ('T9', 'Emplace the AMG and EPU'),
        ('T10', 'March Order the AMG and EPU'),
        ('T11', 'Perform initialization of SMU'),
        ('T12', 'Learn functions of all switches and indicators of the CRG system'),
    ]
    return table_1


def crg_t2():
    table_2 = [
        ('T1', 'Establish communications per communications plan'),
        ('T2', 'Perform LCU initialization'),
        ('T3', 'Learn to identify fault indicators and indications'),
        ('T4', 'Select and interpret LCU tabular displays'),
    ]
    return table_2


def crg_t3():
    table_3 = [
        ('T1', 'Perform prepare for movement drills on CRG and EPU'),
        ('T2', 'Perform emplacement drill on CRG and EPU'),
        ('T3', 'Perform LCU initialization'),
        ('T4', 'Perform CRG initialization'),
        ('T5', 'Establish communications per communications plan'),
        ('T6', 'Perform maintenance sustainment operations'),
    ]
    return table_3


def crg_t4():
    table_4 = [
        ('T1', 'Perform prepare for movement drills on CRG and EPU'),
        ('T2', 'Perform emplacement drill on CRG and EPU'),
        ('T3', 'Perform LCU initialization'),
        ('T4', 'Perform CRG initialization'),
        ('T5', 'Establish communications per communications plan'),
        ('T6', 'Perform PMCS and fault recognition on CRG, EPU, and associated equipment'),
    ]
    return table_4


def crg_t5():
    table_5 = [
        ('T1', 'Perform prepare for movement drills on CRG and EPU'),
        ('T2', 'Perform emplacement drill on CRG and EPU'),
        ('T3', 'Learn functions of all switches and indicators of the CRG'),
        ('T4', 'Learn to operate and initialize CRG as an LCS'),
    ]
    return table_5


def crg_t6():
    table_6 = [
        ('T1', 'Perform prepare for movement of the CRG, AMG, and EPUs collectively'),
        ('T2', 'Peform emplacement of the CRG, AMG, and EPUs collectively'),
        ('T3', 'Receive and manage tactical information'),
        ('T4', 'Initialize and perform LCS functions'),
    ]
    return table_6


def crg_t7():
    table_7 = [
        ('T1', 'Demonstrate prepare for movement of the CRG, AMG, and EPUs collectively'),
        ('T2', 'Demonstrate emplacement of the CRG, AMG, and EPUs collectively'),
        ('T3', 'Receive and manage tactical information'),
        ('T4', 'Initialize and perform LCS functions'),
        ('T5', 'Peform maintenance sustainment operations on all assigned equipment'),
    ]
    return table_7


def crg_t8():
    table_8 = [
        ('T1', 'Demonstrate prepare for movement of the CRG, AMG, and EPUs collectively'),
        ('T2', 'Demonstrate emplacement of the CRG, AMG, and EPUs collectively'),
        ('T3', 'Receive and manage tactical information'),
        ('T4', 'Initialize and perform LCS functions'),
        ('T5', 'Peform maintenance sustainment operations on all assigned equipment'),
    ]
    return table_8


def crg_t9():
    table_9 = [
        ('T1', 'Perform functions of all switches and indicators'),
        ('T2', 'Operate and initialize CRG as an LCS'),
        ('T3', 'Configure the CRG to conduct remote launch operations'),
        ('T4', 'Receive and manage tactical information'),
    ]
    return table_9


def crg_t10():
    table_10 = [
        ('T1', 'CRG crew members perform CRG system PMCS/fault recognition and associated equipment PMCS'),
        ('T2', 'Perform LCU diagnostics for Routing Logic Radio Interface Unit (RLRIU)'),
        ('T3', 'Perform communications PMCS'),
        ('T4', 'Perform maintenance sustainment and reporting operations'),
    ]
    return table_10


def crg_t11():
    table_11 = [
        ('T1', 'Demenstrate functions of all switches and indicators'),
        ('T2', 'Demonstrate how to operate and initialize CRG as an LCS'),
        ('T3', 'Demonstrate how to Configure CRG to conduct remote launch operations'),
        ('T4', 'Receive and manage tactical information and reports from an ICC or fire unit'),
        ('T5', 'Perform maintenance sustainment and reporting operations'),
    ]
    return table_11


def crg_t12():
    table_12 = [
        ('T1', 'Demenstrate functions of all switches and indicators'),
        ('T2', 'Demonstrate how to operate and initialize CRG as an LCS'),
        ('T3', 'Demonstrate how to Configure CRG to conduct remote launch operations'),
        ('T4', 'Receive and manage tactical information and reports from an ICC or fire unit'),
        ('T5', 'Perform maintenance sustainment and reporting operations'),
    ]
    return table_12


def epp_t1():
    table_1 = [
        ('T1', 'Perform maintenance/display procedures for using the DA 5988E worksheet'),
        ('T2', 'EPP crew members perform operator level PMCS on the vehicle'),
        ('T3', 'EPP crew members perform PMCS on the 150KW generator set'),
        ('T4', 'EPP crew members perform PDU system PMCS and associated equipment PMCS'),
        ('T5', 'Emplace the EPP'),
        ('T6', 'March Order the EPP'),
        ('T7', 'Perform operator PMCS on any other applicable assigned equipment')
    ]
    return table_1


def epp_t2():
    table_2 = [
        ('T1', 'Learn to identify fault indicators and indications'),
        ('T2', 'Perform maintenance sustainment operations'),
    ]
    return table_2


def epp_t3():
    table_3 = [
        ('T1', 'Perform prepare for movement drills on EPP'),
        ('T2', 'Perform emplacement drill on EPP'),
        ('T3', 'Perform maintenance sustainment operations'),
    ]
    return table_3


def epp_t4():
    table_4 = [
        ('T1', 'Perform prepare for movement drills on EPP'),
        ('T2', 'Perform emplacement drill on EPP'),
        ('T3', 'Perform PMCS and fault recognition on EPP and associated equipment'),
    ]
    return table_4


def epp_t5():
    table_5 = [
        ('T1', 'Perform prepare for movement drills on EPP'),
        ('T2', 'Perform emplacement drill on EPP'),
        ('T3', 'Learn EPP service interval and provide operator level support for service'),
    ]
    return table_5


def epp_t6():
    table_6 = [
        ('T1', 'Crew members demonstrate PMCS during on going operations'),
        ('T2', 'Crew members perform prepare for movement of the EPP collectively with the ECS, Radar, BCP, and AMG'),
        ('T3', 'Crew members emplace of the EPP EPP collectively with the ECS, Radar, BCP, and AMG'),
        ('T4', 'Perform maintenance sustainment operations'),
    ]
    return table_6


def epp_t7():
    table_7 = [
        ('T1', 'Crew members demonstrate PMCS during on going operations'),
        ('T2', 'Demonstrate prepare for movement of the EPP collectively with the ECS, Radar, BCP, and AMG'),
        ('T3', 'Demonstrate emplacement of the EPP collectively with the ECS, Radar, BCP, and AMG'),
        ('T4', 'Peform maintenance sustainment operations and reporting on all assigned equipment'),
    ]
    return table_7


def epp_t8():
    table_8 = [
        ('T1', 'Demonstrate prepare for movement of the EPP collectively with the ECS, Radar, BCP, and AMG'),
        ('T2', 'Demonstrate emplacement of the EPP collectively with the ECS, Radar, BCP, and AMG'),
        ('T3', 'Peform maintenance sustainment operations and reporting on all assigned equipment'),
    ]
    return table_8


if __name__ == "__main__":
    pass
