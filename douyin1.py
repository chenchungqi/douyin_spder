import json
import pymysql
import time
user_bac={}
headers=["nickname", 'birthday','avatar','dongtai','constellation','favoriting_count','location','following_count','gender','short_id','signature','total_favorited','mplatform_followers_count']
# 数据库配置
config = {
    'host': '127.0.0.1',  localhost
    'port': 3306,         3306
    'user': 'root',       root
    'password': '123456', 123456
    'db': 'douyin',       douyin
    'charset': 'utf8',    utf-8

}
# 连接数据库
connect=pymysql.connect(**config)
# 创建游标
cursor = connect.cursor()
ls=0
count=1
# 循环读取文件
while True:
    with open ("C:\\Users\\chenc\\Desktop\\user11.txt",'r',encoding='utf-8') as f:
        l=f.read()
        d=json.loads(l)
        user={}
        # 用户名，生日，头像，作品数量，星座，喜欢的作品数，地址，关注数，性别，抖音号，个性签名，个性签名，获赞数，粉丝数
        user["nickname"]=d['user']['nickname']#用户名
        user['birthday']=d['user']['birthday']#生日
        user['avatar']=d['user']['avatar_larger']['url_list'][0]#头像
        user['dongtai']=str(d['user']['dongtai_count'])#作品数量
        user['constellation']=str(d['user']['constellation'])#星座
        user['favoriting_count']=str(d['user']['favoriting_count'])#喜欢的作品数
        user['location']=d['user']['location']#地址
        user['following_count']=str(d['user']['following_count'])#关注数
        user['gender']=str(d['user']['gender'])#性别
        user['short_id']=d['user']['short_id']#抖音号
        user['signature']=d['user']['signature']#个性签名
        user['total_favorited']=str(d['user']['total_favorited'])#获赞数
        user['mplatform_followers_count']=str(d['user']['mplatform_followers_count'])#粉丝数
        if user==user_bac:
            pass
        else:
            try:
                user_bac=user
                print(user_bac)
                sql = "INSERT INTO user (name,birthday,avatar,dongtai,constellation,favoriting_count,location,following_count,gender,short_id,signature,total_favorited,mplatform_followers_count) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(user_bac['nickname'], user_bac['birthday'], user_bac['avatar'], user_bac['dongtai'], user_bac[ 'constellation'], user_bac['favoriting_count'], user_bac['location'], user_bac['following_count'],user_bac['gender'], user_bac['short_id'], user_bac['signature'], user_bac['total_favorited'], user_bac[ 'mplatform_followers_count'])
                cursor.execute(sql)
                connect.commit()

                print('成功插入，目前有',count, '条数据')
                count+=1
            except:
                pass
    time.sleep(0.5)
