# SNA
Social Network Analysis

config.py 配置了接口调用需要使用到的token
lookup_users.py 和 lookup_follows.py 都是参照twitter的API v2接口进行了微调。（如果需要，也可以单独执行这两个文件，只需要手工修改输入参数即可）
get_data.py 是调用了以上两个接口下载数据，并将结果保存在了json文件夹下，目前这个twitter开发者账号，限制了每个request请求的返回结果的条数（100条）。也可以根据需要手工修改输入参数然后再执行。
tools.py 提供了一些方法，如有需要，可以调用。主要说明一下 aggregate_nodes() 方法，它是接受一个列表，这个列表元素是每个request请求收到的response的json数据，并将这些数据融合成一个文件。
