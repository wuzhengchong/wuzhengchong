import random
from pyecharts import options as opts
from pyecharts.charts import Bar3D
data = [[x,y,random.randint(10,35)]for y in range(7) for x in range(24)]
hours = ['12a','1a','2a','3a','4a','5a','6a','7a','8a','9a','10a','11a','12p','1p','2p','3p','4p','5p',
         '6p','7p','8p','9p','10p','11p',]
weeks = ['星期六','星期五','星期四','星期三','星期二','星期一','星期日']
c = (
     Bar3D(init_opts=opts.InitOpts(width='1200px',height='600px'))
     .add(
         '',
         data,
         xaxis3d_opts=opts.Axis3DOpts(name='小时',data=hours),
         yaxis3d_opts=opts.Axis3DOpts(name='星期',data=weeks),
         zaxis3d_opts=opts.Axis3DOpts(name='温度'),
    )
         .set_global_opts(
             visualmap_opts=opts.VisualMapOpts(max_=50,min_=0),
             title_opts=opts.TitleOpts(title='111111'),
        )
            .render(r'D:/a/3d.html'))