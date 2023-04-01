from deepl_translate import translate_agent

def test_translate(agent : translate_agent):
    en = "Hello world!"
    cn = agent.send_data(en)
    if cn:
        print("test pass")
        print("en = {} and cn = {}".format(en, cn))

def test_glossary(agent: translate_agent, filename: str):
    agent.set_glossary_id(filename)
    test_translate(agent)

SINGLE_TRANS_SIZE = 1000
def recursive_translate(agent: translate_agent):
    # find_all_markdown_files
    filelist = []
    for file in filelist:
        # locate save path
        savepath = ""
        g = open(savepath, 'w')
        with open(file, "r") as f:
            content = f.readlines()
            # translate html to markdown info
            en_content = "\n".join(content).replace("\t", "*制表符*")
            cur = 0
            while cur < len(en_content):
                res = agent.send_data(en_content[cur:cur+SINGLE_TRANS_SIZE])
                g.write(res)
                cur += SINGLE_TRANS_SIZE
        g.close()

import sys
if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: python3 main.py {{DEEPL API_KEY}}")
        exit(1)
    
    api = sys.argv[1]
    agent = translate_agent(api)

    test_translate(agent)