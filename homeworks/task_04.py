# Задача 4
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
# Для того, чтобы задавать случайные значения, используйсте модуль random
# import random 

import random as rn

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

times=[]
for name,time in my_favorite_songs:
    times.append(time)

i=0
alltime=0.00
ch_times=[]
while i<3:
    x=rn.randint(0,8)
    ch_times.append(times[x-1])
    alltime=alltime+times[x-1]
    i+=1

print('Три песни звучат',round(alltime,2),'минут')