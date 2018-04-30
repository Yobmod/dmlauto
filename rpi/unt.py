import redis
import channels_redis


r = redis.StrictRedis.from_url(
    'redis://h:p84b17fa6712667a51f6db2ee8de35ad4861c31b543a5545c24ed2f63ebf8dee8@ec2-35-173-173-75.compute-1.amazonaws.com:65359')

s = redis.Redis.from_url(
    'redis://h:p84b17fa6712667a51f6db2ee8de35ad4861c31b543a5545c24ed2f63ebf8dee8@ec2-35-173-173-75.compute-1.amazonaws.com:65359')

rp = r.ping()
sp = r.ping()
print(rp)
print(sp)

t = channels_redis.core.
