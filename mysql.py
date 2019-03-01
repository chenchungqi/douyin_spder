import pymysql
import json

#cursor.execute("drop table if exists COMMENTS")
# sql = """create table COMMENTS (
#          text char(200) not null,
#          aweme_id char(30),
#          create_time int,
#          nickname char(20),
#          gender int,
#          birthday char(20)
#          )  """
# cursor.execute(sql)

comment_bac={}
headers=["text", 'aweme_id','create_time','nickname','gender','birthday']
db = pymysql.connect("localhost","root","123456","douyin")
cursor = db.cursor()
ls=0
count=1
while True:
    with open("G:\\apytemp\\user1.txt", 'r', encoding='utf-8') as f:
        l = f.read()
        d = json.loads(l)
        comment = {}
        #print(d)
        if d['comments'][0]['text']==comment_bac:
            pass
        else:
            try:
                comment_bac=d['comments'][0]['text']
                for i in range(0,20):
                    comment['text'] = d['comments'][i]['text']
                    comment['aweme_id'] = d['comments'][i]['aweme_id']
                    comment['create_time'] = d['comments'][i]['create_time']
                    comment['nickname'] = d['comments'][i]['user']['nickname']
                    comment['gender'] = d['comments'][i]['user']['gender']
                    comment['birthday'] = d['comments'][i]['user']['birthday']
                   # print(comment['aweme_id'])
                   # print(comment)
                    sql = "INSERT INTO comments (text,aweme_id,create_time,nickname,gender,birthday) VALUES ('%s','%s','%d','%s','%d','%s')" % (comment['text'], comment['aweme_id'], comment['create_time'], comment['nickname'], comment['gender'],comment['birthday'])
                    cursor.execute(sql)
                    db.commit()
                    print('成功插入，目前有', count, '条数据')
                    count += 1
            except:
                pass

# sql = """insert into EMPLOYEE(FirstName,
#          LastName,Age,Sex,Income)
#          values('Mac','Mohan',20,'M',2000);"""

# try:
#     # 执行 sql 语句
#     cursor.execute(sql)
#     # 提交到数据库执行
#     db.commit()
#     print ('提交完毕')
# except:
#     # 如果发生错误则进行回滚
#     db.rollback()
#     print ('\n Some Error happend ! \n')
#

# 关闭数据库连接
db.close()