# Дан список строк: ФИО + даты и суммы. Типа клиент или продавец и его траты/счета. в виде дата:сумма

# Получить это в виде словаря: ключ-Кортеж ФИО, значение-словарь поквартальная сумма для человека

# lst_data = ["Иванов иван ИваНович:2019.09.05:345.28 2018/03/01:869.6 2019/01/07:963.48 2020.02.09:133.48 2020.03.12:719.44 2018.06.23:772.85 2018.07.30:284.38 ",

# "Салтыков-щедрин Михаил Евграфович:2019.09.18:945.44 2020.09.06:905.67 2021.02.21:983.65 2021/08/11:142.54 2018.01.11:563.47 2019/10/21:656.57 2021.11.29:509.69 ",

# "Соколов ИлЬЯ Петрович:2019.08.07:749.45 2019/02/20:563.5 2021.02.27:960.06 2021/09/21:802.23 2021.02.06:509.04 2019.05.01:322.67 2021.07.12:501.81 2018.08.12:914.51 2021/02/14:501.38 ",

# "Сидоров Петр Петрович:2018/05/21:371.99 2020.07.30:972.27 2021/02/28:475.7 2021/04/18:483.18 2018/07/25:371.64 2021/09/18:704.83 2021/03/05:368.09 2019/10/03:327.98 2021.02.04:983.45 2019/12/23:414.03 2021.12.08:917.2 2019/07/23:926.91 ",

# "Петров Василий Иванович:2020.01.30:109.37 2019.03.10:654.37 2021/05/01:703.21 2021/10/05:332.71 2018/06/14:885.57 2019/04/14:715.17 2021.01.23:637.77 2020.04.30:895.71 2020/10/26:151.22 2021/12/29:371.89 2019.04.03:718.48 2019.03.24:625.51 2020.05.12:219.69 2021.10.12:534.14 2020.03.27:261.65 ",

# ]

lst_data = ["Иванов иван ИваНович:2019.09.05:345.28 2018/03/01:869.6 2019/01/07:963.48 2020.02.09:133.48 2020.03.12:719.44 2018.06.23:772.85 2018.07.30:284.38 ",

"Салтыков-щедрин Михаил Евграфович:2019.09.18:945.44 2020.09.06:905.67 2021.02.21:983.65 2021/08/11:142.54 2018.01.11:563.47 2019/10/21:656.57 2021.11.29:509.69 ",

"Соколов ИлЬЯ Петрович:2019.08.07:749.45 2019/02/20:563.5 2021.02.27:960.06 2021/09/21:802.23 2021.02.06:509.04 2019.05.01:322.67 2021.07.12:501.81 2018.08.12:914.51 2021/02/14:501.38 ",

"Сидоров Петр Петрович:2018/05/21:371.99 2020.07.30:972.27 2021/02/28:475.7 2021/04/18:483.18 2018/07/25:371.64 2021/09/18:704.83 2021/03/05:368.09 2019/10/03:327.98 2021.02.04:983.45 2019/12/23:414.03 2021.12.08:917.2 2019/07/23:926.91 ",

"Петров Василий Иванович:2020.01.30:109.37 2019.03.10:654.37 2021/05/01:703.21 2021/10/05:332.71 2018/06/14:885.57 2019/04/14:715.17 2021.01.23:637.77 2020.04.30:895.71 2020/10/26:151.22 2021/12/29:371.89 2019.04.03:718.48 2019.03.24:625.51 2020.05.12:219.69 2021.10.12:534.14 2020.03.27:261.65 ",

]

for persona in lst_data:
 #"Иванов иван ИваНович:2019.09.05:345.28 2018/03/01:869.6 2019/01/07:963.48 2020.02.09:133.48 2020.03.12:719.44 2018.06.23:772.85 2018.07.30:284.38 "   
 
    # names = (persona[:persona.find(':')].split())
    # print(names)
    # for i in range(len(names)):
    #     names[i] = (names[i]).title()
    # names = tuple(names)
    
    amount_by_quarter_string = (persona[persona.find(':')+1:]).split()
    print(amount_by_quarter_string)
    for j in range(len(amount_by_quarter_string)):
       # '2019.09.05:345.28'
       
        
    
    

        
    
    
    
       
    










# {('Иванов', 'Иван', 'Иванович'): {'2018-Q1': [869.6],

# '2018-Q2': [772.85],

# '2018-Q3': [284.38],

# '2019-Q1': [963.48],

# '2019-Q3': [345.28],

# '2020-Q1': [133.48, 719.44]},

# ('Петров', 'Василий', 'Иванович'): {'2018-Q2': [885.57],

# '2019-Q1': [654.37, 625.51],

# '2019-Q2': [715.17, 718.48],

# '2020-Q1': [109.37, 261.65],

# '2020-Q2': [895.71, 219.69],

# '2020-Q4': [151.22],

# '2021-Q1': [637.77],

# '2021-Q2': [703.21],

# '2021-Q4': [332.71, 371.89, 534.14]},

# ('Салтыков-Щедрин', 'Михаил', 'Евграфович'): {'2018-Q1': [563.47],

# '2019-Q3': [945.44],

# '2019-Q4': [656.57],

# '2020-Q3': [905.67],

# '2021-Q1': [983.65],

# '2021-Q3': [142.54],

# '2021-Q4': [509.69]},

# ('Сидоров', 'Петр', 'Петрович'): {'2018-Q2': [371.99],

# '2018-Q3': [371.64],

# '2019-Q3': [926.91],

# '2019-Q4': [327.98, 414.03],

# '2020-Q3': [972.27],

# '2021-Q1': [475.7, 368.09, 983.45],

# '2021-Q2': [483.18],

# '2021-Q3': [704.83],

# '2021-Q4': [917.2]},

# ('Соколов', 'Илья', 'Петрович'): {'2018-Q3': [914.51],

# '2019-Q1': [563.5],

# '2019-Q2': [322.67],

# '2019-Q3': [749.45],

# '2021-Q1': [960.06, 509.04, 501.38],

# '2021-Q3': [802.23, 501.81]}}