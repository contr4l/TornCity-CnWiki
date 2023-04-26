import requests
from deepl_glossary import glossary_agent

import os
class translate_agent:
    def __init__(self, api):
        self.glossary_id = ""
        self.api = api

    def set_glossary_id(self, filename):
        if not os.path.exists(filename):
            return
        glossary = glossary_agent(filename)
        found, self.glossary_id = glossary.find_glossary_map(self.api)
        if not found:
            response = glossary.create_glossary_map(self.api)
            print(response)
            if response["ready"] == True:
                self.glossary_id = response["glossary_id"]
        print("glossary_id = ", self.glossary_id)

    def send_data(self, en : str) -> str:
        assert len(en) < 100 * 1024, "Data too large, please split into multiple sentences."
            
        url = 'https://api-free.deepl.com/v2/translate'

        headers = {
            'Authorization': 'DeepL-Auth-Key ' + self.api,
        }

        data = {
            'text': en,
            'source_lang': 'en',
            'target_lang': 'zh',
            'preserve_formatting': 1,
            'glossary_id': ""
        }
        response = requests.post(url, headers=headers, data=data)

        if response.status_code != 200:
            print("HTTP response error: {}".format(response.status_code))
            return None

        return response.json()["translations"][0]["text"]
