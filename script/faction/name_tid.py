from od_detector import set_key,faction_dict, get_user_list

def save_name_tid():
    f = open("name_tid.csv", "w")
    f.write("tid,name\n")
    for faction_id in faction_dict:
        users = get_user_list(faction_id)
        for torn_id in users:
            f.write("{},{}\n".format(torn_id, users[torn_id]))
    f.close()

def get_name_tid():
    res = {}
    for faction_id in faction_dict:
        users = get_user_list(faction_id)
        res = dict(list(res.items()) + list(users.items()))
    return res

# set_key("GkGCcSyK7Fa359MT")
# save_name_tid()