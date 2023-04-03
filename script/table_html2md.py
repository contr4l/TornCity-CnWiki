import re

def html_table_to_markdown(html):
    # 匹配表格元素
    table_re = re.compile(r'<table>(.*?)</table>', re.DOTALL)
    tr_re = re.compile(r'<tr>(.*?)</tr>', re.DOTALL)
    th_re = re.compile(r'<th>(.*?)</th>', re.DOTALL)
    td_re = re.compile(r'<td>(.*?)</td>', re.DOTALL)

    # 查找表格元素
    table_match = table_re.search(html)
    if not table_match:
        return ''

    # 解析表格数据
    table_data = []
    for tr_match in tr_re.findall(table_match.group(1)):
        row_data = []
        for td_match in td_re.findall(tr_match):
            row_data.append(td_match.strip())
        table_data.append(row_data)

    # 格式化表格数据为Markdown
    markdown = ''
    if table_data:
        num_cols = len(table_data[0])
        # 准备表头
        markdown += '| ' + ' | '.join([''] * num_cols) + ' |\n'
        markdown += '| ' + ' | '.join(['---'] * num_cols) + ' |\n'
        # 添加行
        for row_data in table_data:
            markdown += '| ' + ' | '.join(row_data) + ' |\n'

    return markdown