import json
import pymysql

video_info_bac={}
db = pymysql.connect("localhost","root","123456","douyin")
cursor = db.cursor()
ls=0
count=1

# sql = """create table video_info (
#          aweme_id char(30) not null,
#          desc1 char(100),
#          music char(30),
#          create_time int,
#          forward_count int,
#          digg_count int,
#          comment_count int,
#          share_count int
#          )  """
# cursor.execute(sql)
while True:
    with open("G:\\apytemp\\user1.txt", 'r', encoding='gb2312') as f:
         l = f.read()
         d = json.loads(l)
         data = {}
         #print(d)
         if d['data'][0]['aweme_info']['aweme_id'] == video_info_bac:
             pass
         else:
             video_info_bac = d['data'][0]['aweme_info']['aweme_id']
             for i in range(0,25):
                 try:
                    data['aweme_id'] = d['data'][i]['aweme_info']['aweme_id']
                    data['desc1'] = d['data'][i]['aweme_info']['desc']
                    data['music'] = d['data'][i]['aweme_info']['music']['id_str']  #uri
                    data['create_time'] = d['data'][i]['aweme_info']['create_time']
                    data['forward_count'] = d['data'][i]['aweme_info']['statistics']['forward_count']
                    data['digg_count'] = d['data'][i]['aweme_info']['statistics']['digg_count']
                    data['comment_count'] = d['data'][i]['aweme_info']['statistics']['comment_count']
                    data['share_count'] = d['data'][i]['aweme_info']['statistics']['share_count']
                    #print(data)
                    sql = "INSERT INTO video_info (aweme_id,desc1,music,create_time,forward_count,digg_count,comment_count,share_count) VALUES ('%s','%s','%s','%d','%d','%d','%d','%d')" % (
                    data['aweme_id'], data['desc1'], data['music'], data['create_time'], data['forward_count'],data['digg_count'],data['comment_count'],data['share_count']
                    )
                    cursor.execute(sql)
                    db.commit()
                    print('成功插入，目前有', count, '条数据')
                    count += 1
                 except:
                     pass
db.close()