import requests, json, os

class TornLogCatcher:
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__)) + "/"

    FAC_DICT = {
        "36134": "SH",
        "16335": "NOV",
        "27902": "CCRC",
        "9356": "PTA",
        "20465": "Main",
        "10741": "Tri",
        "16424": "MHY",
        "11796": "BSU",
    }

    def __init__(self, key):
        self.api_key = key

    def _general_request(self, url):
        url = url + "&key=" + self.api_key

        print("send requests {}".format(url))
        
        res = requests.get(url)
        if res.status_code != 200:
            print("api request gets negative response!")
            raise TimeoutError
        
        content = json.loads(res.text)
        
        if "error" in content:
            print("errcode = {}, errmsg = {}".format(content["error"]["code"], content["error"]["error"]))
            raise PermissionError

        return content
    
    def get_all_log(self):
        url = "https://api.torn.com/user/?selections=log"
        return self._general_request(url)
        
    def _support_from_to(self, url, from_, to_):
        if not from_ and not to_:
            return url
        
        elif not from_:
            url += "&to={}".format(
                to_
            )
            
        elif not to_:
            url += "&from={}".format(
                from_
            )
        
        else:
            url += "&from={}&to={}".format(
                from_, to_
            )
        return url

    def get_log_in_period(self, from_ = None, to_ = None):
        assert from_ or to_, "At least [from] or [to] should be set"

        url = "https://api.torn.com/user/?selections=log"
        url = self._support_from_to(url, from_, to_)

        return self._general_request(url)
    
    def get_log_with_types(self, log_types, from_=None, to_=None):
        url = "https://api.torn.com/user/?selections=log&log={}".format(
            log_types
        )

        url = self._support_from_to(url, from_, to_)
        return self._general_request(url)
    
    def get_log_with_categories(self, log_cates, from_ = None, to_ = None):
        url = "https://api.torn.com/user/?selections=log&cat={}".format(
            log_cates
        )

        url = self._support_from_to(url, from_, to_)
        return self._general_request(url)

    def get_faction_data_json(self, faction_id) -> json:
        url = "https://api.torn.com/faction/{}?selections=basic".format(
            faction_id
        )
        return self._general_request(url)

    def get_user_data_json(self, user, selections) -> json:
        url = "https://api.torn.com/user/{}?selections={}".format(
            user, selections
        )
        return self._general_request(url)

    def get_user_list(self, faction_id) -> json:
        users = {
                    #"torn_id" : "nickname"
                }
        
        data = self.get_faction_data_json(faction_id)
        
        ppl_list = data["members"]

        for ppl_id in ppl_list:
            users[ppl_id] = ppl_list[ppl_id]["name"]
        
        return users

    def save_tid_name_map(self, filename = None):
        save_path = filename if filename else "tid_name.csv"
        save_path = TornLogCatcher.CURRENT_DIR + save_path

        f = open(save_path, "w", encoding="utf-8")
        f.write("tid,name\n")
        for faction_id in TornLogCatcher.FAC_DICT:
            users = self.get_user_list(faction_id)
            for torn_id in users:
                f.write("{},{}\n".format(torn_id, users[torn_id]))
        f.close()
        return save_path

    def read_tid_name_map(self, filename = None):
        if not os.path.exists(filename):
            filename = self.save_tid_name_map(filename)

        map_ = {}
        with open(filename, "r", encoding="utf8") as f:
            for line in f.readlines()[1:]:
                tid, name = line.split(",")
                map_[int(tid)] = name
        return map_

