

from datetime import datetime


data = datetime(2024,3,4)
data = datetime(2024, 3, 4, 20, 56, 48)
print( data)

data_str_data = '2024/03/04 20:56:48'
date_str_fmt = '%Y/%m/%d %H:%M:%S'

data = datetime.strptime(data_str_data, date_str_fmt)
print(data)