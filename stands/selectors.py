# lib for choices. Only input choices to this lib


def unit():
    battalion = [
        ('4-3 ADA', '4-3 ADA'),
        ('3-2 ADA', '3-2 ADA'),
    ]
    return battalion


def icc_t1():
    table_1 = [
        ('T1', 'Perform maintenance/display procedures for using the DA 5988E worksheet'),
        ('T2', 'Perform operator level PMCS on the ICC vehicle'),
        ('T3', 'Perform operator level PMCS/TWUD on the Information Coordination Central (ICC) system'),
        ('T4', 'Perform operator level PMCS on the Electronic Power Unit (EPU) 30kw'),
        ('T5', 'Perform operator level PMCS on the Single Channel Ground and Airborne Radio System (SINGARS)'),
        ('T6', 'Perform operator level PMCS on the Defense Advanced GPS Receiver (DAGR)'),
        ('T7', 'Perform operator level PMCS on the Simple Key Loader (SKL)'),
        ('T8', 'Perform LCU initialization/diagnostics using the Patriot communications operator handbook'),
        ('T9', 'Initialize the Multifunctional Information Distribution System MIDS'),
        ('T10', 'Perform MIDS Crypto-key loading'),
        ('T11', 'Perform initialization of the MIDS terminal'),
        ('T12', 'Perform initialization of the Switch Multiplexer Unit (SMU)'),
        ('T13', 'Install and remove the corner reflector on the ICC'),
        ('T14', 'Perform prepare for movement of the ICC and EPUs'),
        ('T15', 'Emplace the ICC and EPUs'),
        ('T16', 'Perform parallel operations between the 30kW generator sets'),
        ('T17', 'Initialize the ICC'),
        ('T18', 'Create a basic TBM and ABT Defense plan on the TPW'),
        ('T19', 'Perform communications link planning on the Tactical Planner Workstation (TPW)'),
    ]
    return table_1


def icc_t2():
    table_2 = [
        ('T1', 'Learn functions of tabs and tabular entries'),
        ('T2', 'Learn the functions of all controls, switches, and indicators'),
        ('T3', 'Recognize Patriot symbology'),
        ('T4', 'Learn the situational displays'),
        ('T5', 'Learn alert states, STO, and ACMAF'),
        ('T6', 'Learn fix or fight criteria, including common fire platoon faults'),
        ('T7', 'Troubleshoot common faults that occur on the ICC system'),
        ('T8', 'Discuss evaluation decision and weapon assignment (EDWA)'),
        ('T9', 'Discuss the implementation of Special Instructions (SPINS)'),
        ('T10', 'Learn Patriot weapon system capabilities and limitations'),
        ('T11', 'Perform RFA drills, correctly configuring system for directed alert state'),
        ('T12', 'Learn applicable Tactical Standard Operating Procedures (TSOP) and Theater/Unit SOPs'),
        ('T13', 'Learn to read and process USMTF messages ATOs/ACOs'),
        ('T14', 'Perform maintenance sustainment operations'),
    ]
    return table_2


def icc_t3():
    table_3 = [
        ('T1', 'Create, update, and maintain the Battalion site data book'),
        ('T2', 'Apply parameters in the ICC stated in the TSOP and dictated by the STO'),
        ('T3', 'Discuss defense design and events that result in the changing of tabular entries'),
        ('T4', 'Identify the ICC and fire unit capabilities and limitations'),
        ('T5', 'Demonstrate how to use the TPW to develop a Battalion TBM/ABT defense design'),
        ('T6', 'Coordinate air battle management using levels 1 through 5'),
        ('T7', 'Learn to script ABMLs and demonstrate the ability to send to fire units'),
        ('T8', 'Learn reporting requirements including mIRC procedures'),
    ]
    return table_3


def icc_t4():
    table_4 = [
        ('T1', 'Demonstrate operator level PMCS on the vehicle'),
        ('T2', 'Demonstrate operator level PMCS/TWUD on the ICC system'),
        ('T3', 'Demonstrate operator level PMCS on the 30kw generator (EPU)'),
        ('T4', 'Demonstrate prepare for movement drill on the ICC and EPU'),
        ('T5', 'Demonstrate emplacement drill on the ICC and EPU'),
        ('T6', 'Demonstrate parallel operations between the 30kW generator sets'),
        ('T7', 'Demonstrate knowledge of the Patriot system and unit tactical directives'),
        ('T8', 'Demonstrate power up and initialize the ICC'),
        ('T9', 'Demonstrate parallel operations between the 30kW generator sets'),
        ('T10', 'Demonstrate RFA drills and correctly configure the system for the directed alert state'),
        ('T11', 'Demonstrate how to use the TPW to develop Battalion TBM/ABT Defense Design'),
        ('T12', 'Demonstrate knowledge of Patriot system capabilities and unit tactical directives'),
        ('T13', 'Conduct air battle management using level 5 scenario while controlling a minimum of two fire units'),
        ('T14', 'Demonstrate reporting requirements including mIRC procedures'),
        ('T15', 'Establish and operate the battalion communications net per communications plan'),
        ('T16', 'Perform maintenance sustainment operations'),
    ]
    return table_4


def icc_t5():
    table_5 = [
        ('T1', 'Learn to interpret a basic defense design and discuss'),
        ('T2', 'Develop and implement a BN level DD based on threats/defended asset list and input into the ICC'),
        ('T3', 'Understand and process tactical information using the TCS Patriot TPW'),
        ('T4', 'Create a site/system data book for Table V scenarios'),
        ('T5', 'Create a Master Event List (MEL) and script ABMLs 6 through 9 with applicable STOs and ACMAFs'),
        ('T6', 'Conduct air battle management using levels 6 through 9'),
    ]
    return table_5


def icc_t6():
    table_6 = [
        ('T1', 'Collectively perform prepare for movement drills for the ICC, AMG, TCS, and EPUs'),
        ('T2', 'Collectively Emplace the ICC, AMG, TCS, and EPUs'),
        ('T3', 'Initialize the ICC using at least 2 Fire Units'),
        ('T4', 'Perform ready for action drills, correctly configuring system for a directed alert state'),
        ('T5', 'Perform maintenance sustainment operations'),
    ]
    return table_6


def icc_t7():
    table_7 = [
        ('T1', 'Demonstrate operator level PMCS on the ICC vehicle'),
        ('T2', 'Demonstrate operator level PMCS/TWUD on the Information Coordination Central (ICC) system'),
        ('T3', 'Demonstrate operator level PMCS on the Electronic Power Unit (EPU) 30kw'),
        ('T4', 'Demonstrate operator level PMCS on the Single Channel Ground and Airborne Radio System (SINGARS)'),
        ('T5', 'Demonstrate operator level PMCS on the Defense Advanced GPS Receiver (DAGR)'),
        ('T6', 'Demonstrate operator level PMCS on the Simple Key Loader (SKL)'),
        ('T7', 'Collectively perform prepare for movement drills for the ICC, AMG, and EPUs'),
        ('T8', 'Collectively emplace the ICC, AMG, and EPUs'),
        ('T9', 'Initialize the ICC using at least 2 Fire Units'),
        ('T10', 'Demonstrate ready for action drills, correctly configuring system for directed alert state'),
        ('T11', 'Conduct air battle management using levels 10 or 11 while controlling at least 2 Fire Units'),
        ('T12', 'Submit required tactical reports to Higher Echelon Unit (HEU)'),
        ('T13', 'Demonstrate maintenance sustainment operations'),
    ]
    return table_7


def icc_t8():
    table_8 = [
        ('T1', 'Demonstrate operator level PMCS on the ICC vehicle'),
        ('T2', 'Demonstrate operator level PMCS/TWUD on the Information Coordination Central (ICC) system'),
        ('T3', 'Demonstrate operator level PMCS on the Electronic Power Unit (EPU) 30kw'),
        ('T4', 'Demonstrate operator level PMCS on the Single Channel Ground and Airborne Radio System (SINGARS)'),
        ('T5', 'Demonstrate operator level PMCS on the Defense Advanced GPS Receiver (DAGR)'),
        ('T6', 'Demonstrate operator level PMCS on the Simple Key Loader (SKL)'),
        ('T7', 'Collectively demonstrate preparing for movement drills for the ICC, AMG, and EPUs'),
        ('T8', 'Collectively demonstrate emplacement of the ICC, AMG, and EPUs'),
        ('T9', 'Collectively demonstrate initializing the ICC using at least 2 Fire Units'),
        ('T10', 'Perform ready for action drills, correctly configuring system for directed alert state'),
        ('T11', 'Conduct air battle management using level 11 while controlling at least 2 Fire Units'),
        ('T12', 'Submit required tactical reports to Higher Echelon Unit (HEU)'),
        ('T13', 'Demonstrate maintenance sustainment operations'),
    ]
    return table_8


def icc_t9():
    table_9 = [
        ('T1', 'Create site battle books/system data book'),
        ('T2', 'Conduct PMCS during on-going operations'),
        ('T3', 'Condition the system at an alert state 5-1, maintaining manning and communications requirements'),
        ('T4', 'Conduct oversight of fire units, including fire unit control of an Remote Launch RL-3 site'),
        ('T5', 'Update status reports and demonstrate understanding of current equipment status'),
        ('T6', 'React to a STO directing at least two fire units to an alert state 1, 2, or 3'),
        ('T7', 'Process tactical information'),
        ('T8', 'Submit required tactical reports'),
        ('T9', 'Perform maintenance sustainment operations'),
    ]
    return table_9


def icc_t10():
    table_10 = [
        ('T1', 'Conduct PMCS during on-going operations'),
        ('T2', 'Develop a threat brief on a current countries capabilities'),
        ('T3', 'Develop and implement a BN level DD based on threats/defended asset list and input into the ICC'),
        ('T4', 'Understand and process tactical information using the TCS Patriot TPW'),
        ('T5', 'Create a site/system data book for Table X scenarios'),
        ('T6', 'Conduct Patriot AD operations using ABMLs 12-13 while managing two Fire Units and an LCS'),
    ]
    return table_10


def icc_t11():
    table_11 = [
        ('T1', 'Demonstrate PMCS during on-going operations'),
        ('T2', 'Demonstrate the ability to interpret Patriot Defense Design'),
        ('T3', 'Condition the system at an alert state 5-1, maintaining manning and communications requirements'),
        ('T4', 'Conduct oversight of the fire units, including fire units controlling RL-3 sites'),
        ('T5', 'Update status reports and demonstrate understanding of current equipment status'),
        ('T6', 'React to a STO directing at least two fire units to an alert state 1, 2, or 3'),
        ('T7', 'Submit required tactical reports'),
        ('T8', 'Conduct Patriot AD operations using ABMLs 14-16 while managing two Fire Units and an LCS'),
        ('T9', 'Demonstrate maintenance sustainment operations'),
    ]
    return table_11


def icc_t12():
    table_12 = [
        ('T1', 'Demonstrate PMCS during on-going operations'),
        ('T2', 'Demonstrate the ability to interpret Patriot Defense Design'),
        ('T3', 'Condition the system at an alert state 5-1, maintaining manning and communications requirements'),
        ('T4', 'Conduct oversight of the fire units, including fire units controlling RL-3 sites'),
        ('T5', 'Update status reports and demonstrate understanding of current equipment status'),
        ('T6', 'React to a STO directing at least two fire units to an alert state 1, 2, or 3'),
        ('T7', 'Submit required tactical reports'),
        ('T8', 'Conduct Patriot AD operations using ABML 16 while managing 2 Fire Units and an LCS'),
        ('T9', 'Demonstrate maintenance sustainment operations'),
    ]
    return table_12


def amg_t1():
    table_1 = [
        ('T1', 'Perform maintenance/display procedures for using the DA 5988E worksheet'),
        ('T2', 'Perform operator level PMCS on the vehicle'),
        ('T3', 'Perform operator level PMCS on the 30kW generator set'),
        ('T4', 'Perform operator level PMCS on the Antenna Mast Group (AMG) system'),
        ('T5', 'Perform operator level PMCS on the Single Channel Ground and Airborne Radio System (SINGARS)'),
        ('T6', 'Perform operator level PMCS on the Defense Advanced GPS Receiver (DAGR)'),
        ('T7', 'Perform operator level PMCS on the Simple Key Loader (SKL)'),
        ('T8', 'Perform prepare for movement drills on the AMG and EPU'),
        ('T9', 'Perform emplacement on the AMG and EPU'),
        ('T10', 'Perform parallel procedures on the EPUs'),
        ('T11', 'Perform operator PMCS on any other applicable assigned equipment'),
    ]
    return table_1


def amg_t2():
    table_2 = [
        ('T1', 'Establish communications per communications plan'),
        ('T2', 'Learn and understand the hydraulic and pneumatic pallet pressure gauges'),
        ('T3', 'Learn to identify fault indicators and warnings'),
    ]
    return table_2


def amg_t3():
    table_3 = [
        ('T1', 'Learn and understand what components run off of AC and which work off of DC power'),
        ('T2', 'Perform maintenance sustainment operations'),
    ]
    return table_3


def amg_t4():
    table_4 = [
        ('T1', 'Demonstrate operator level PMCS on the vehicle'),
        ('T2', 'Demonstrate operator level PMCS on the 30kw generator set'),
        ('T3', 'Demonstrate operator level PMCS on the Antenna Mast Group (AMG) system'),
        ('T4', 'Demonstrate operator level PMCS on the Single Channel Ground and Airborne Radio System (SINGARS)'),
        ('T5', 'Demonstrate operator level PMCS on the Defense Advanced GPS Receiver (DAGR)'),
        ('T6', 'Demonstrate operator level PMCS on the Simple Key Loader (SKL)'),
        ('T7', 'Demonstrate prepare for movement drills on AMG and EPU'),
        ('T8', 'Demonstrate emplacement drills on AMG and EPU'),
        ('T9', 'Establish communications per communications plan'),
    ]
    return table_4


def amg_t5():
    table_5 = [
        ('T1', 'Perform organizational maintenance mast lubrication order '),
        ('T2', 'Perform organizational maintenance mast seal replacement'),
        ('T3', 'Learn how the AMG functions with the ICC or CRG in an operational environment'),
    ]
    return table_5


def amg_t6():
    table_6 = [
        ('T1', 'Perform PMCS during on going operations'),
        ('T2', 'Perform prepare for movement of the AMG, and EPUs collectively with the ICC or CRG'),
        ('T3', 'Emplace of the AMG and EPUs collectively with the ICC or CRG'),
        ('T4', 'Establish and operate the battalion communications net'),
        ('T5', 'Perform maintenance sustainment operations'),
    ]
    return table_6


def amg_t7():
    table_7 = [
        ('T1', 'Demonstrate operator level PMCS on the vehicle'),
        ('T2', 'Demonstrate operator level PMCS on the 30kW generator set'),
        ('T3', 'Demonstrate operator level PMCS on the Antenna Mast Group (AMG) system'),
        ('T4', 'Demonstrate operator level PMCS on the Single Channel Ground and Airborne Radio System (SINGARS)'),
        ('T5', 'Demonstrate operator level PMCS on the Defense Advanced GPS Receiver (DAGR)'),
        ('T6', 'Demonstrate operator level PMCS on the Simple Key Loader (SKL)'),
        ('T7', 'Demonstrate prepare for movement of the AMG, and EPUs collectively with the ICC or CRG'),
        ('T8', 'Demonstrate emplacement of the AMG and EPUs collectively with the ICC or CRG'),
        ('T9', 'Demonstrate maintenance sustainment operations'),
    ]
    return table_7


def amg_t8():
    table_8 = [
        ('T1', 'Demonstrate operator level PMCS on the vehicle'),
        ('T2', 'Demonstrate operator level PMCS on the 30kW generator set'),
        ('T3', 'Demonstrate operator level PMCS on the Antenna Mast Group (AMG) system'),
        ('T4', 'Demonstrate operator level PMCS on the Single Channel Ground and Airborne Radio System (SINGARS)'),
        ('T5', 'Demonstrate operator level PMCS on the Defense Advanced GPS Receiver (DAGR)'),
        ('T6', 'Demonstrate operator level PMCS on the Simple Key Loader (SKL)'),
        ('T7', 'Demonstrate prepare for movement of the AMG, and EPUs collectively with the ICC or CRG'),
        ('T8', 'Demonstrate emplacement of the AMG and EPUs collectively with the ICC or CRG'),
        ('T9', 'Demonstrate maintenance sustainment operations'),
    ]
    return table_8


def tcs_t1():
    table_1 = [
        ('T1', 'Perform maintenance/display proper procedures for using the DA 5988E worksheet'),
        ('T2', 'Perform operator level PMCS on the Tactical Control System (TCS) vehicle'),
        ('T3', 'Perform operator level PMCS on the TCS'),
        ('T4', 'Perform operator level PMCS on the 30 kw tactical quiet generator'),
        ('T5', 'Perform PMCS on SINCGARS, DAGR, Simple Key Loader (SKL), and Fiber Optic Cable Assembly (FOCA) PMCS'),
        ('T6', 'Perform prepare for movement on the expandable van TCS and EPU'),
        ('T7', 'Emplace the expandable van Tactical Command System on TCS and EPU'),
        ('T8', 'Learn how to ground and power-up workstation'),
        ('T9', 'Learn power and power down procedures for TCS'),
        ('T10', 'Initialize the Patriot Tactical Planner Workstation (TPW)'),
        ('T11', 'Understand basic TPW functions including opening, saving, and deleting a Defense Design'),
        ('T12', 'Learn Link Manager (TIE) configuration'),
        ('T13', 'Install Link 16 Common User Interface (CUI)'),
        ('T14', 'Learn how to remote the system into a Tactical Operations Center (TOC)'),
        ('T15', 'Learn software installation including Lennox, BSD, TTDB, DTEDs, Maps, and TBM footprints'),
    ]
    return table_1


def tcs_t2():
    table_t2 = [
        ('T1', 'Recognize Patriot symbols'),
        ('T2', 'Learn the applicable TSOP and SOPs'),
        ('T3', 'Read and process USMTF messages/NATO ATOs/ ACOs'),
        ('T4', 'Learn to process and input USMTF messages and ACO information into the Patriot TPW'),
        ('T5', 'Learn to load map data on the Patriot TPW'),
        ('T6', 'Perform ready for action drills, configuring the system for a directed alert state'),
        ('T7', 'Perform control and display unit power up'),
        ('T8', 'Use the alert system to alarm the site'),
        ('T9', 'Discuss and understand alert states, STOs, ACMAFs, SAMSTATs, and mIRC reporting procedures'),
        ('T10', 'Prepare and load the TCS for movement'),
        ('T11', 'Start the CUI software'),
        ('T12', 'Power up the CIB'),
        ('T13', 'Operate the CUI software for MIDS in the TCS netted mode'),
        ('T14', 'Load the JTT Crypto and set the JTT system time'),
        ('T15', 'Power-up the JTT, TIPOFF laptop, and at least one TCS workstation'),
        ('T16', 'Configure the JTT to TIPOFF to TCS links'),
        ('T17', 'Understand and know how to configure the ICC database'),
        ('T18', 'Copying and Load files from a CD and the CUI directory'),
        ('T19', 'Perform defense design planning with the TPW'),
        ('T20', 'Create/Export defense design from the TPW'),
        ('T21', 'Import/modify imported mission and export defense plan'),
    ]
    return table_t2


def tcs_t3():
    table_t3 = [
        ('T1', 'Using the Patriot TPW, develop a Battalion level defense design'),
        ('T2', 'Conduct air battle management using levels 1 through 5'),
        ('T3', 'Learn reporting requirements including mIRC procedures'),
        ('T4', 'Demonstrate the ability to toggle objects and maps'),
        ('T5', 'Use measure distance feature'),
        ('T6', 'Demonstrate the ability to operate Battalion Exerciser'),
        ('T7', 'Demonstrate how to use air picture controls and indicators'),
        ('T8', 'Describes the symbols used in the TCS/BCP'),
        ('T9', 'Operate and filter an air picture'),
        ('T10', 'Understand system statistics, mission report, and Time vs Altitude'),
        ('T11', 'Know and understand how to filter an air picture'),
        ('T12', 'Buffer transfer data to the ICC'),
        ('T13', 'Receive and print tactical and status tabs from ICC'),
        ('T14', 'Buffer Transfer data to an ECS'),
        ('T15', 'Show differences between tabs in the active plan and an ICC'),
        ('T16', 'Demonstrate the ability to display track amp tabs'),
    ]
    return table_t3


def tcs_t4():
    table_t4 = [
        ('T1', 'Demonstrate operator level PMCS on the Tactical Control System (TCS) vehicle'),
        ('T2', 'Demonstrate operator level PMCS on the TCS'),
        ('T3', 'Demonstrate operator level PMCS on the 30 kw tactical quiet generator'),
        ('T4', 'Demonstrate operator level PMCS on SINCGARS'),
        ('T5', 'Demonstrate operator level PMCS on the DAGR'),
        ('T6', 'Demonstrate operator level PMCS on the SKL'),
        ('T7', 'Demonstrate operator level PMCS on the FOCA'),
        ('T8', 'Demonstrate prepare for movement on the expandable van TCS and EPU'),
        ('T9', 'Demonstrate emplacement of the expandable van TCS and EPU'),
        ('T10', 'Conduct power up and initialization of the TCS systems'),
        ('T11', 'Demonstrate knowledge of Patriot communications capabilities and reporting procedures'),
        ('T12', 'Demonstrate how to input a Battalion level defense design'),
        ('T13', 'Demonstrate ready-for-action drills, configuring the system for a directed alert state'),
        ('T14', 'Conduct air defense operations using ABML 5, while controlling at least 2 fire units'),
    ]
    return table_t4


def tcs_t5():
    table_5 = [
        ('T1', 'Discuss and create site data book'),
        ('T2', 'Conduct air defense operations using ABMLs 6 through 9 with the ICC'),
        ('T3', 'Understand how to use the side panel to display, open, rename, copy, and delete a defense plan'),
        ('T4', 'Understand how to use the zoom and pan functions'),
        ('T5', 'Know and understand how to insert a single point object via mouse pick and/or key in'),
        ('T6', 'Know how to modify, delete, and insert a point from a multiple point object'),
        ('T7', 'Determine the version date of TBM footprints and Tactical Threat Data Base (TTDB)'),
        ('T8', 'Know and understand the LACM tool bar'),
        ('T9', 'Understand missile fly out and missile acquisition test'),
        ('T10', 'Analyze UHF communications links'),
        ('T11', 'Add a CRG and insert an Launcher Control Station (LCS)'),
        ('T12', 'Generate UHF communications links and remove bad communications links'),
        ('T13', 'Add and toggle communications links between two units'),
        ('T14', 'Use and generate communication bubble charts'),
        ('T15', 'Demonstrate the ability to conduct TBM defense planning'),
        ('T16', 'Demonstrate the ability to perform EMI analysis'),
        ('T17', 'Demonstrate the ability to perform TBM tailoring'),
        ('T18', 'Conduct defense planning for cruise missile/ABT low altitude keep out zone'),
        ('T19', 'Demonstrate the ability to conduct ABT defense planning'),
        ('T20', 'Demonstrate the ability to conduct passive emplacement'),
        ('T21', 'Know what radar sensor analysis consists of'),
        ('T22', 'Know and understand alternate search sectors'),
        ('T23', 'Conduct TCS planning and preparation for the ICC and fire units'),
        ('T24', 'Input and delete an ACM database from a defense plan'),
        ('T25', 'Develop and activate a defense plan'),
    ]
    return table_5


def tcs_t6():
    table_6 = [
        ('T1', 'Perform prepare for movement of the TCS and EPU collectively with the ICC'),
        ('T2', 'Perform emplacement of the TCS and EPU collectively with the ICC'),
        ('T3', 'Establish and operate a TCS with a provided communications plan'),
        ('T4', 'Perform ready for action drills, correctly configuring the system for a directed alert state'),
    ]
    return table_6


def tcs_t7():
    table_7 = [
        ('T1', 'Demonstrate operator level PMCS on the Tactical Control System (TCS) vehicle'),
        ('T2', 'Demonstrate operator level PMCS on the TCS'),
        ('T3', 'Demonstrate operator level PMCS on the 30 kw tactical quiet generator'),
        ('T4', 'Demonstrate operator level PMCS on SINCGARS'),
        ('T5', 'Demonstrate operator level PMCS on the DAGR'),
        ('T6', 'Demonstrate operator level PMCS on the SKL'),
        ('T7', 'Demonstrate operator level PMCS on the FOCA'),
        ('T8', 'Demonstrate collective prepare for movement of the TCS and EPUs with the ICC'),
        ('T9', 'Demonstrate collective emplacement of the TCS and EPUs with the ICC'),
        ('T10', 'Establish and operate a TCS with provided communications plan'),
        ('T11', 'Demonstrate ready-for-action drills, configuring the system for a directed alert state'),
        ('T12', 'Conduct air defense operations using ABMLs 10 or 11, while controlling 2 or more fire units'),
        ('T13', 'Perform maintenance sustainment operations'),
    ]
    return table_7


def tcs_t8():
    table_8 = [
        ('T1', 'Demonstrate operator level PMCS on the Tactical Control System (TCS) vehicle'),
        ('T2', 'Demonstrate operator level PMCS on the TCS'),
        ('T3', 'Demonstrate operator level PMCS on the 30 kw tactical quiet generator'),
        ('T4', 'Demonstrate operator level PMCS on SINCGARS'),
        ('T5', 'Demonstrate operator level PMCS on the DAGR'),
        ('T6', 'Demonstrate operator level PMCS on the SKL'),
        ('T7', 'Demonstrate operator level PMCS on the FOCA'),
        ('T8', 'Demonstrate collective prepare for movement of the TCS and EPUs with the ICC'),
        ('T9', 'Demonstrate collective emplacement of the TCS and EPUs with the ICC'),
        ('T10', 'Establish and operate a TCS with provided communications plan'),
        ('T11', 'Demonstrate ready-for-action drills, configuring the system for a directed alert state'),
        ('T12', 'Conduct air defense operations using ABML 11, while controlling 2 or more fire units'),
        ('T13', 'Perform maintenance sustainment operations'),
    ]
    return table_8


def tcs_t9():
    table_9 = [
        ('T1', 'Conduct PMCS on TCS and all associated equipment during on going operations'),
        ('T2', 'Sustain manning and communications requirements during on going operations'),
        ('T3', 'Update status reports and demonstrate understanding of current equipment status'),
        ('T4', 'Perform ready for action drills, configuring the system for a directed alert state'),
        ('T5', 'React to a STO directing at least two fire units to an alert state 1, 2, or 3'),
        ('T6', 'Submit required tactical reports to a HEU'),
        ('T7', 'Perform maintenance sustainment operations in a steady state environment'),
    ]
    return table_9


def tcs_t10():
    table_10 = [
        ('T1', 'Create a Battalion level defense design given specific threats and assets'),
        ('T2', 'Perform ready for action drills configuring the system for air defense operations'),
        ('T3',
         'Conduct Patriot AD operations using ABML 12-13 while controlling two or more fire units and managing the '
         'operations of one or more LCSs'),
    ]
    return table_10


def tcs_t11():
    table_11 = [
        ('T1', 'Demonstrate PMCS on TCS and all associated equipment during on going operations'),
        ('T2', 'Demonstrate managing TCS at an alert state 5-1, maintaining manning and communications requirements'),
        ('T3', 'Conduct oversight of the fire units, including fire units controlling RL-3 sites'),
        ('T4', 'Update status reports and demonstrate understanding of current equipment status'),
        ('T5', 'Demonstrate reacting to a STO directing at least two fire units to an alert state 1, 2, or 3'),
        ('T6', 'Demonstrate submitting required tactical reports to HEU'),
        ('T7',
         'Demonstrate Patriot AD operations using ABMLs 14-16 while controlling two or more fire units and managing the'
         'operations of one or more LCSs'),
        ('T8', 'Demonstrate maintenance operations in a steady state environment'),
    ]
    return table_11


def tcs_t12():
    table_12 = [
        ('T1', 'Demonstrate PMCS on TCS and all associated equipment during on going operations'),
        ('T2', 'Demonstrate managing TCS at an alert state 5-1, maintaining manning and communications requirements'),
        ('T3', 'Conduct oversight of the fire units, including fire units controlling RL-3 sites'),
        ('T4', 'Update status reports and demonstrate understanding of current equipment status'),
        ('T5', 'Demonstrate reacting to a STO directing at least two fire units to an alert state 1, 2, or 3'),
        ('T6', 'Demonstrate submitting required tactical reports to HEU'),
        ('T7',
         'Demonstrate Patriot AD operations using ABML 16 while controlling two or more fire units and managing the'
         'operations of one or more LCSs'),
        ('T8', 'Demonstrate maintenance operations in a steady state environment'),
    ]
    return table_12


def crg_t1():
    table_1 = [
        ('T1', 'Perform maintenance/display procedures for using the DA 5988E worksheet'),
        ('T2', 'Perform operator level PMCS on the Communications Relay Group (CRG) vehicle'),
        ('T3', 'Perform operator level PMCS on the CRG system'),
        ('T4', 'Perform operator level PMCS on the Electronic Power Unit (EPU) 30kW'),
        ('T5', 'Perform operator level PMCS on the Single Channel Ground and Airborne Radio System (SINGARS)'),
        ('T6', 'Perform operator level PMCS on the Defense Advanced GPS Receiver (DAGR)'),
        ('T7', 'Perform operator level PMCS on the Simple Key Loader (SKL)'),
        ('T8', 'Perform LCU diagnostics for routing logic radio interface unit'),
        ('T9', 'Perform prepare for movement on the CRG and EPU'),
        ('T10', 'Perform emplacement on CRG and EPU'),
        ('T11', 'Perform parallel operations between the 30kW generator sets'),
        ('T12', 'Perform power-up and power-down of the CRG system'),
    ]
    return table_1


def crg_t2():
    table_2 = [
        ('T1', 'Establish communications per communications plan'),
        ('T2', 'Learn and understand CRG system capabilities and limitations'),
        ('T3', 'Learn function of the CRG switches, controls, and indicators'),
        ('T4', 'Perform RFA drills, correctly configuring system for directed alert state'),
        ('T5', 'Select and interpret Lightweight Computer Unit (LCU) tabular displays'),
        ('T6', 'Perform LCU initialization/diagnostics using the Patriot communications operator handbook'),
        ('T7', 'Perform initialization of Switch Multiplexer Unit (SMU)'),
        ('T8', 'Learn to identify fault indicators and indications'),
    ]
    return table_2


def crg_t3():
    table_3 = [
        ('T1', 'Establish communications per communications plan'),
        ('T2', 'Select and interpret Lightweight Computer Unit (LCU) tabular displays'),
        ('T3', 'Perform maintenance sustainment operations'),
    ]
    return table_3


def crg_t4():
    table_4 = [
        ('T1', 'Demonstrate operator level PMCS on the vehicle'),
        ('T2', 'Demonstrate operator level PMCS on the ICC vehicle'),
        ('T3', 'Demonstrate operator level PMCS on the Communications Relay Group (CRG) system'),
        ('T4', 'Demonstrate operator level PMCS on the Electronic Power Unit (EPU) 30kw'),
        ('T5', 'Demonstrate operator level PMCS on the Single Channel Ground and Airborne Radio System (SINGARS)'),
        ('T6', 'Demonstrate operator level PMCS on the Defense Advanced GPS Receiver (DAGR)'),
        ('T7', 'Demonstrate operator level PMCS on the Simple Key Loader (SKL)'),
        ('T8', 'Demonstrate prepare for movement drills on CRG and EPU'),
        ('T9', 'Demonstrate emplacement drill on CRG and EPU'),
        ('T10', 'Demonstrate LCU and SMU initialization'),
        ('T11', 'Demonstrate power-up and power-down of the CRG system'),
        ('T12', 'Demonstrate parallel operations between the 30kw generator sets'),
        ('T13', 'Establish communications per communications plan'),
        ('T14', 'Demonstrate fault reporting on CRG, EPU, and associated equipment'),
    ]
    return table_4


def crg_t5():
    table_5 = [
        ('T1', 'Perform CRG initialization as an Launcher Control Station (LCS)'),
        ('T2', 'Learn how an LCS is utilized in a Patriot defense design'),
    ]
    return table_5


def crg_t6():
    table_6 = [
        ('T1', 'Perform prepare for movement of the CRG, AMG, and EPUs collectively'),
        ('T2', 'Perform emplacement of the CRG, AMG, and EPUs collectively'),
        ('T3', 'Establish communications per BN communications plan'),
        ('T4', 'Perform RFA drills, correctly configuring system for directed alert state'),
        ('T5', 'Receive and manage tactical information'),
    ]
    return table_6


def crg_t7():
    table_7 = [
        ('T1', 'Demonstrate operator level PMCS on the vehicle'),
        ('T2', 'Demonstrate operator level PMCS on the ICC vehicle'),
        ('T3', 'Demonstrate operator level PMCS on the Communications Relay Group (CRG) system'),
        ('T4', 'Demonstrate operator level PMCS on the Electronic Power Unit (EPU) 30kw'),
        ('T5', 'Demonstrate operator level PMCS on the Single Channel Ground and Airborne Radio System (SINGARS)'),
        ('T6', 'Demonstrate operator level PMCS on the Defense Advanced GPS Receiver (DAGR)'),
        ('T7', 'Demonstrate operator level PMCS on the Simple Key Loader (SKL)'),
        ('T8', 'Demonstrate prepare for movement of the CRG, AMG, and EPUs collectively'),
        ('T9', 'Demonstrate emplacement of the CRG, AMG, and EPUs collectively'),
        ('T10', 'Establish communications per BN communications plan'),
        ('T11', 'Demonstrate RFA drill, correctly configuring system for directed alert state'),
        ('T12', 'Receive and manage tactical information'),
        ('T13', 'Demonstrate initialization as an LCS'),
        ('T14', 'Perform maintenance sustainment operations on all assigned equipment'),
    ]
    return table_7


def crg_t8():
    table_8 = [
        ('T1', 'Demonstrate operator level PMCS on the vehicle'),
        ('T2', 'Demonstrate operator level PMCS on the ICC vehicle'),
        ('T3', 'Demonstrate operator level PMCS on the Communications Relay Group (CRG) system'),
        ('T4', 'Demonstrate operator level PMCS on the Electronic Power Unit (EPU) 30kw'),
        ('T5', 'Demonstrate operator level PMCS on the Single Channel Ground and Airborne Radio System (SINGARS)'),
        ('T6', 'Demonstrate operator level PMCS on the Defense Advanced GPS Receiver (DAGR)'),
        ('T7', 'Demonstrate operator level PMCS on the Simple Key Loader (SKL)'),
        ('T8', 'Demonstrate prepare for movement of the CRG, AMG, and EPUs collectively'),
        ('T9', 'Demonstrate emplacement of the CRG, AMG, and EPUs collectively'),
        ('T10', 'Establish communications per BN communications plan'),
        ('T11', 'Demonstrate RFA drill, correctly configuring system for directed alert state'),
        ('T12', 'Receive and manage tactical information'),
        ('T13', 'Demonstrate initialization as an LCS'),
        ('T14', 'Perform maintenance sustainment operations on all assigned equipment'),
    ]
    return table_8


def crg_t9():
    table_9 = [
        ('T1', 'Perform CRG system PMCS/fault recognition and associated equipment PMCS during on-going operations'),
        ('T2', 'Support operations as a CRG or an LCS depending on the communication plan and tactical requirements'),
        ('T3', 'Demonstrate understanding of current equipment status'),
        ('T4', 'Perform maintenance sustainment operations'),
    ]
    return table_9


def crg_t10():
    table_10 = [
        ('T1', 'Perform LCS operations and learn to establish/control a launcher hotcrew'),
    ]
    return table_10


def crg_t11():
    table_11 = [
        ('T1', 'Demonstrate PMCS during on-going operations'),
        ('T2', 'Demonstrate the ability to interpret Patriot communications plan'),
        ('T3', 'Demonstrate how to initialize as an LCS and manage remote launch operations'),
        ('T4', 'Receive and manage tactical information and reports from an ICC or fire unit'),
        ('T5', 'Perform maintenance sustainment and reporting operations'),
    ]
    return table_11


def crg_t12():
    table_12 = [
        ('T1', 'Demonstrate PMCS during on-going operations'),
        ('T2', 'Demonstrate the ability to interpret Patriot communications plan'),
        ('T3', 'Demonstrate how to initialize as an LCS and manage remote launch operations'),
        ('T4', 'Receive and manage tactical information and reports from an ICC or fire unit'),
        ('T5', 'Perform maintenance sustainment and reporting operations'),
    ]
    return table_12


def epp_t1():
    table_1 = [
        ('T1', 'Perform maintenance/display procedures for using the DA 5988E worksheet'),
        ('T2', 'EPP crew members perform operator level PMCS on the vehicle'),
        ('T3', 'EPP crew members perform PMCS on the 150kW generator set'),
        ('T4', 'EPP crew members perform PDU system PMCS and associated equipment PMCS'),
        ('T5', 'Perform prepare for movement on the Electronic Power Plant (EPP)'),
        ('T6', 'Perform emplacement on EPP'),
        ('T7', 'Perform power-up of the 150kW generator and close circuit to send power to ECS'),
        ('T8', 'Perform operator PMCS on any other applicable assigned equipment')
    ]
    return table_1


def epp_t2():
    table_2 = [
        ('T1', 'Learn to identify indications of a fault'),
        ('T2', 'Perform parallel operations between the 150kW generator sets'),
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
