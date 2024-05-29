# 第一步：获取执行完token接口后的当前时间
# 获取当前时间
import datetime

# 获取当前时间
current_time = datetime.datetime.now()
# 获取时分秒
hour = current_time.hour
minute = current_time.minute
second = current_time.second
# 输出结果
print(f"当前时间的时分秒为：{hour}:{minute}:{second}")
# 第二步： 生成一个2h

# 第一步 + 第二步 = 过期时间