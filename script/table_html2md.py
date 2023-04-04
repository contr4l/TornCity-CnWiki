import re

def process_data(align_="", data=""):
    return data.strip()

def html_table_to_markdown(html):
    # 匹配表格元素
    table_re = re.compile(r'<table[^>]*>(.*?)</table>', re.DOTALL)
    tr_re = re.compile(r'<tr([^>]*)>(.*?)</tr>', re.DOTALL)
    th_re = re.compile(r'<th([^>]*)>(.*?)</th>', re.DOTALL)
    td_re = re.compile(r'<td([^>]*)>(.*?)</td>', re.DOTALL)

    # 查找表格元素
    table_match = table_re.findall(html)
    if not table_match:
        return ''

    def gen_from_table_data(data):
        # 解析表格数据
        table_data = []
        for _, tr_match in tr_re.findall(data):
            row_data = []
            for th_match in th_re.findall(tr_match):
                row_data.append(process_data(th_match[0], th_match[1]))
            for td_match in td_re.findall(tr_match):
                row_data.append(process_data("", td_match[1]))
            table_data.append(row_data)

        # 格式化表格数据为Markdown
        markdown = ''
        if table_data:
            num_cols = len(table_data[0])
            # 准备表头
            markdown += ('| ' + ' | '.join(table_data[0]) + ' |\n').replace(":", "")

            markdown += '| ' + ' | '.join([":-:"] * num_cols) + ' |\n'
            # 添加行
            for row_data in table_data[1:]:
                markdown += '| ' + ' | '.join(row_data) + ' |\n'

        return markdown
    
    res = []
    for data in table_match:
        res.append(gen_from_table_data(data))
    return res

if __name__ == '__main__':
    f = open("test.html", "r")
    res = html_table_to_markdown(f.read())
    for md in res:
        print(md)
        print("================================\n")
    f.close()