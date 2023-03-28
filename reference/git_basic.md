> 作者：contr4l_

# Git及Github基本功能介绍  
Git以及github是目前可以说是流行最广的代码管理方案（类似的方案有时代的眼泪之SVN、同样基于git的gitlab、gitee等等），在本教程中，将手把手教读者完成git的安装、github仓库的拉取、代码的修改及提交等事务，为拥抱开源打下基础。

## Git的安装
git作为一个命令行程序，提供了一系列代码下载、提交、分支管理的功能，其下载地址为：[Git Download](https://git-scm.com/downloads)，对于Windows，通常选择**Standalone Installer：64-bit Setup**即可（如果是非常老旧的32bit系统，也可选择32-bit Setup）。
<figure><img src="../.gitbook/assets/1.png" alt=""><figcaption></figcaption></figure>

此时按下`Win+R`，输入`powershell`并运行，在窗口中输入`git -v`，应当出现如下字样：
```bash
PS C:\Users\ctrl> git -v
git version 2.40.0.windows.1
```
!> 1. 版本信息可能根据安装的git版本有所变化  
2. 如果提示报错，需要考虑git安装过程是否出现问题或是是否将git.exe所在的路径正确添加进了系统的环境变量

## Github的注册、添加SSH Key  
首先需要[注册github账号](https://github.com/signup)，在此请自行解决与github/google的网络连接问题（一般情况下github直连是顺畅的，但在某些教育网系统中毛病颇多，与地区网络服务供应商有关）。  

> 现在的注册页面真是酷炫，谷歌是伟大的公司233

现在你可以在github登录自己的账号。

在我们进行`git clone`之前，需要做一项很重要的事情，那就是将本机的`SSH key`放进自己的`github account`，操作步骤如下：  
```sh
# 1. 在powershell中，输入ssh-keygen.exe，并一路回车
# 此处我增加了-f选项是为了不覆盖已生成的公钥
PS C:\Users\ctrl> ssh-keygen.exe -f github
Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in github
Your public key has been saved in github.pub
The key fingerprint is:
SHA256:JJ+NVRVXLj2aWTGQj+5Jx6edEnpQG146uqvMmbR9uhI ctrl@CtrlPC
The key's randomart image is:
+---[RSA 3072]----+
|            .o=++|
|           . . +o|
|      . . .   +oo|
|       + =   +=+.|
|        S . ++*  |
|         E . O o.|
|         .. * =oo|
|        +.=o *...|
|         Bo*B .  |
+----[SHA256]-----+
# 2. 继续输入cat ~/.ssh/id_rsa.pub
PS C:\Users\ctrl> cat ~/.ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDcCfsovN+G4aM+08k3pOCUBveQWztAnbj0wg1JY8MDEgWu116Riol4SCXI8WyLM6AApeZ/pb2xO9M3iaIwZ/
C3JNINVRwfzXNdn6hC3MqObdT1p0wD7ZTzIlBkpKi5PZn614K5o4/VXQWIknw+DIvq30NGNk/QNCIYQ48hYvxz2iwv9gpm6nrvies83CV0J+hc/PGKFXvao/NXSZHiatO92mgVWycMplBFAVSdI/zub/
NRXhYUNyTlbP1TDhi0l9zVtPsej/RQK0auF+Hl6RHkrKJYGS8TeYWxvXydWpNWBNz9ABorAQLx/Afmkvt+3E1Qx5/nxzZgFys4/eDWj0k5jYmEDCAhrX5FVl2AkYMzS2somkhh
+SeZsV2p5b3Dp3bhH0NQVf6JzTwp4WKuVhPIYYC0nWm0WJinr9WEIfNAlXeBVJ1Blbh/aYz2nxnKl3IdGLBdvE7sZveLLscP/CwLBgu8dziINacJEM1d0M4D0yOvCC9cvB31z7KgSfQqdfs= ctrl@CtrlPC
# 3. 将屏幕上ssh-rsa开头的一长串字符串复制下来
# 4. 在github页面，依次点击右上角自己头像-Settings-SSH and GPG keys-New SSH key
# 5. 将刚才复制的一长串内容粘贴进Key的文本框，并点击Add SSH key，Title可以留空
```
<figure><img src="../.gitbook/assets/2023032802.png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/2023032803.png" alt=""><figcaption></figcaption></figure>

## Github仓库的拉取  
现在你需要访问我们的[wiki所在的repo](https://github.com/contr4l/contr4l.github.io)。

首先你需要将这个仓库`fork`到你的仓库内，这是能够进行修改并提交的基础。  

!> 注意选项`clone main branch only`一定要取消勾选！因为我们是基于gh-pages分支进行开发的。  
<figure><img src="../.gitbook/assets/2023032804.png" alt=""><figcaption></figcaption></figure>


现在你可以看到`contr4l.github.io`已经位于你的名下了，如下图所示。  
<figure><img src="../.gitbook/assets/2023032805.png" alt=""><figcaption></figcaption></figure>

接下来我们进行代码拉取，首先找到SSH的代码拉取地址，如下图所示，然后在`powershell`中输入`git clone {刚才你复制的以.git结尾的地址}`。  
<figure><img src="../.gitbook/assets/2023032806.png" alt=""><figcaption></figcaption></figure>


```bash
PS C:\Users\ctrl> git clone git@github.com:fakeContr4l/contr4l.github.io.git
Cloning into 'contr4l.github.io'...
remote: Enumerating objects: 242, done.
remote: Counting objects: 100% (242/242), done.
remote: Compressing objects: 100% (145/145), done.
remote: Total 242 (delta 69), reused 202 (delta 35), pack-reused 0Receiving objects:  67% (163/242), 1.63 MiB | 39.00 Ki

Receiving objects: 100% (242/242), 1.69 MiB | 45.00 KiB/s, done.
Resolving deltas: 100% (69/69), done.
```  
此时你当前目录下会多出一个`contr4l.github.io`为名的文件夹，就是我们的工作目录。

### Test

