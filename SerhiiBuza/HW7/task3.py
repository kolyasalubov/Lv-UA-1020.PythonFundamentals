def create_dict(st):
    dict_res = {}
    for item in st:
        if item in dict_res:
            dict_res[item] += 1
        else:
            dict_res[item] = 1
    return dict_res


result_ = create_dict("HelllllooooooOO")
print(result_)
