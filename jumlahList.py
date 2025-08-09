def jumlah_list(list):
    if not list:
        return 0
    return list[0] + jumlah_list(list[1:])

print(jumlah_list([1,2,3,4])) 
