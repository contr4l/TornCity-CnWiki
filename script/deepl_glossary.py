import requests
import simplejson as json

class glossary_agent:
    GLOSSARY_NAME = "Torn"

    def __init__(self, filename):
        self.content = []
        self.map = {}
        self.read_csv(filename)

    def read_csv(self, filename):
        with open(filename, 'r') as f:
            for line in f.readlines():
                self.content.append(line)
    
    def generate_glossary_map(self):
        for line in self.content:
            if "," not in line:
                print("broken line, content is {}".format(line))
                continue
            
            kv = line.split(",")
            if len(kv) != 2:
                print("broken line, content is {}".format(line))
                continue
        
            self.map[kv[0]] = kv[1]

    def generate_glossary_entries(self):
        entires_list = []
        for en in self.map:
            entires = en + "%09" + self.map[en]
            entires_list.append(entires.replace(" ", "%20"))
        return "%09".join(entires_list)

    def create_glossary_map(self, api) -> json:

        self.generate_glossary_map()

        entries = self.generate_glossary_entries()

        url = 'https://api-free.deepl.com/v2/glossaries'
        headers = {
            'Authorization' : 'DeepL-Auth-Key ' + api,
        }

        data = {
            'name': glossary_agent.GLOSSARY_NAME,
            'source_lang': 'EN',
            'target_lang': 'ZH',
            'entries': entries,
            'entries_format': 'tsv',
        }

        response = requests.post(url, headers=headers, data=data)
        return response.json()

    def find_glossary_map(self, api):
        url = 'https://api-free.deepl.com/v2/glossaries'
        headers = {
            'Authorization' : 'DeepL-Auth-Key ' + api,
        }
        
        print(url, headers)

        response = requests.get(url, headers=headers)
        print(response.status_code)
        for entries in response.json()["glossaries"]:
            if entries["name"] == glossary_agent.GLOSSARY_NAME:
                assert entries["ready"] == "true", "Glossary exists but not ready"
                return True, entries["glossary_id"]
        print("Glossary with name {} not exists".format(glossary_agent.GLOSSARY_NAME))
        return False, ""
