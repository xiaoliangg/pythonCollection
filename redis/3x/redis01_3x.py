# 用于删除用户缓存播单，从而在查询播单时调用akka
import redis

def listKeys(conn):
    keys = conn.keys()
    print(type(keys))
    print(keys)

# conn = redis.Redis()
conn = redis.Redis(host='10.129.18.143',port=6379,db=0)

listKeys(conn)

# conn.delete('AI_RADIO_USER_PLAYLIST_1200000000696_1674_5f379cd69f19c83781162b4efc562237')

listKeys(conn)

v123 = conn.get('AI_RADIO_USER_LIST_1200000000696_1674_20220627')
print(v123)
print(conn.get('main_label_info_1239'))
conn.get('AI_RADIO_USER_PLAYLIST_1200000000696_1674_5f379cd69f19c83781162b4efc562237')

