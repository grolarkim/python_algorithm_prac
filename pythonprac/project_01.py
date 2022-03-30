my_station=['야탑','모란','이매','선릉','한티','왕십리']

def station_list(arr):
    for a in arr:
        print(a)

def station_point(arr):
    for a in arr:
        if a == '선릉':
            print(a)

station_list(my_station)
station_point(my_station)