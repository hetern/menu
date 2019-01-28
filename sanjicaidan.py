menu = {
'四川':{
    '成都市':{
        '武侯区':{},
        '锦江区':{},
        '青羊区':{}
        },
    '绵阳市':{
        '涪城区':{},
        '游仙区':{},
        '安州区':{},
        },
    },
'河南':{
    '郑州市':{
        '金水区':{},
        '中原区':{},
        '惠济区':{},
        },
    '洛阳市':{
        '涧西区':{},
        '西工区':{},
        '瀍河区':{},
        }
    }
}
tag=True
while tag:
    m1=menu
    for key in m1:
        print(key)

    choice1 = input('第一层》：').strip()
    if choice1=='b':
        print('已经是第一层')
        continue
    if choice1 == 'q':
        tag=False
        continue
    if choice1 not in m1:
        print('输入错误')
        continue
    while tag:
        m2=m1[choice1]
        for key in m2:
             print(key)
        choice2=input('第二层》：').strip()
        if choice2=='b':
            break
        if choice2=='q':
            tag=False
            continue
        if choice2 not in m2:
            print('输入错误')
            continue
        while tag:
            m3=m2[choice2]
            for key in m3:
                 print(key)
            choice3=input('第三层》：').strip()
            if choice3=='b':
                break
            if choice3=='q':
                tag=False
                continue
            if choice3 not in m2:
                print('输入错误')
