import pyecharts;
from pyecharts import Bar
from pyecharts.base import Base


def paint_geo():
    citys = []
    data = []
    with open('./dataSource.txt', 'r', encoding='utf-8')as f:
        rows = f.readlines()
        try:
            for row in rows:
                city = row.split(':')[1]
                if city != '':
                    if city in citys:
                        data = city_plus_one(city, data)
                    else:
                        citys.append(city)
                        data.append((city, 1))
        except Exception as e:
            print(e)
    print(data)

    # geo = Geo("《海王》观影城市分布", "数据来源：猫眼 截止", title_color="#fff", title_pos="center", width=1200, height=600,
    #           background_color='#404a59')
    # attr, value = geo.cast(data)
    # geo.add('', attr, value, visual_range=[0, 1000],
    #         visual_text_color='#fff', symbol_size=15,
    #         is_visualmap=True, is_piecewise=False, visual_split_number=10)
    # geo.show_config()
    # geo.render("观影城市分布地理坐标图.html")
    # 根据元组第2个元素，即观影人数到序
    data.sort(key=take_second, reverse=True);
    # 获取前20个光影人数的城市和数量
    data_top20 = data[:20]
    bar = Bar('《海王》观众来源排行TOP20', '数据来源：猫眼 2018-12-15 -- 2018-12-17 16:00:00', title_pos='center', width=1200, height=600)
    # 将字典或元组返回成key和value
    attr, value = Base.cast(data_top20)
    bar.add('', attr, value, is_visualmap=True, visual_range=[0, 3500], visual_text_color='#fff', is_more_utils=True,
            is_label_show=True)
    bar.render('观众来源排行-柱状图.html')


##如果城市相同，则加1
def city_plus_one(key, list):
    for tuple in list:
        if key == tuple[0]:
            t = (key, tuple[1] + 1)
            list.remove(tuple)
            list.append(t)
    return list


##获取元组第二个元素
def take_second(elem):
    return elem[1]

paint_geo();
