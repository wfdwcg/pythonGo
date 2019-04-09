import jieba
from wordcloud import STOPWORDS, WordCloud
import matplotlib.pyplot as plt



def paint_word_cloud():
    comments = []
    with open('./dataSource.txt', 'r', encoding='utf-8')as f:
        rows = f.readlines()
        try:
            for row in rows:
                comment = row.split(':')[2]
                if comment != '':
                    comments.append(comment)
            print(comments)
        except Exception as e:
            print(e)
    comment_after_split = jieba.cut(str(comments), cut_all=False)
    words = ' '.join(comment_after_split)
    print(words)
    # 多虑没用的停止词
    stopwords = STOPWORDS.copy()
    stopwords.add('电影')
    stopwords.add('一部')
    stopwords.add('一个')
    stopwords.add('没有')
    stopwords.add('什么')
    stopwords.add('有点')
    stopwords.add('感觉')
    stopwords.add('海王')
    stopwords.add('就是')
    stopwords.add('觉得')
    stopwords.add('但是')
    bg_image = plt.imread('./cloudBack.jpg')
    print('load image success')
    print(words)
    wc = WordCloud(
        # 画布的宽度和高度，如果设置mask不生效
        #width=1024, height=768,
        # 背景色
        background_color='white',
        # 词云形状
        mask=bg_image,
        # 字体路径，若有中文，必须添加这句代码，否则中文变方框
        font_path='/Users/lichuang.lc/Desktop/python/out/STZHONGS.TTF',
        # 设置停用时间
        stopwords=stopwords,
        # 最大字号，如果不指定则为图像高度
        max_font_size=400,
        #有多少种配色方案
        random_state=50)
    wc.generate_from_text(words)
    wc.to_file('./man.jpg')
    plt.imshow(wc)
    plt.axis('off')
    plt.show()


paint_word_cloud()
