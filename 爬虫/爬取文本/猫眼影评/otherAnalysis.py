from pyecharts import Bar
import logging


def analysis4():
    with open('./dataSource.txt', 'r', encoding='utf-8')as f:
        rows = f.readlines()
        try:
            for data in rows:
                print(data)
                data["hour"] = data["startTime"].dt.hour
                data["startTime"] = data["startTime"].dt.date
                need_date = data[["startTime","hour"]]
                def get_hour_size(data):
                    hour_data = data.groupby(by="hour")["hour"].size().reset_index(name="count")
                    return hour_data
                data = need_date.groupby(by="startTime").apply(get_hour_size)

                data_reshape = data.pivot_table(index="startTime",columns="hour",values="count")

                bar = Bar("分时评论分析",width =1200,height=600,title_pos ="center")
                data_reshape.fillna(0,inplace=True)
                print(data_reshape)
                for index,row in data_reshape.T.iterrows():
                    print(data_reshape.index)
                    v1 = list(row.values)
                    bar.add(str(index)+"时",row.index,v1,is_legend_show=True,legend_pos="80%",legend_text_size=8)
                    bar.render("html/1.html")
        except Exception as e:
            logging.exception(e)

analysis4();