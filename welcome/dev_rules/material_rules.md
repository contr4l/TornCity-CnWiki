# 悬赏材料格式规范

### 格式要求

1. 必须按照Markdown语法提交
2. 提交文件必须以`.md`作为后缀名，语法规则请参考参考文献中的[**Markdown基本语法**](/reference/markdown_basic.md)
   1. 必须要遵守的语法格式包括：N级标题、加粗、下划线
   2. 如果内部有超链接内容，请在开头注明TODO项，将由前端统一处理
3. 内容**不需要**额外<u>添加目录</u>和<u>回到顶端</u>选项，docsify将通过插件的方式统一添加。
4. 如果当前页面内容中存在更深层次的超链接，在repo中的结构应该是：`title/README.md`，其中`title`是本文的名字，**也是文件夹名**，如`mission`，`README.md`中是本文的全部内容。

### 内容模板

```
提交人：Nickname[Torn id]
提交日期：20xx-xx-xx
原文地址：www.tornwiki.com/example
内部超链接：
- [ ] 未完成链接一
- [ ] 未完成链接二
- [ ] 未完成链接三

# 一级标题
内容

## 二级标题
内容

## 二级标题
内容

### 三级标题
表格
图片
```

### Markdown 编辑器

1. 使用Vscode并安装Markdown All in One扩展，下载地址：[https://code.visualstudio.com/](https://code.visualstudio.com/)
   1. ctrl+shift+x安装扩展
   2. ctrl+shift+p选择Preview in the side实时预览
2. 使用Marktext，下载地址：[https://github.com/marktext/marktext/releases](https://github.com/marktext/marktext/releases)
   1. 所见即所得，开箱即用，ctrl+E切换源码模式和预览模式

3. 详细教程参考[VsCode安装教程](/reference/vscode_install.md)