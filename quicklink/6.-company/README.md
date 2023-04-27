> Companies

提交人: contr4l_[2903026]

提交日期: 2023-04-27

原文地址: https://wiki.torn.com/wiki/Company

内部超链接:

!> TODO: 内部大量超链接没有制作

# 6.公司

## 获取方式

有两种方法可以收购一家公司。你可以启动一个新的公司：通过进入报纸上的工作列表页面，点击你想启动的公司，然后支付统一的费用，只需支付默认设置的基本费用。

或者你可以从其他玩家那里获得一个成熟的公司（通过直接转让或交易），成熟的公司可能会有员工、库存（库存物品和公司金库）和/或升级。

- 将公司赠送给另一个雇员（细微差别尚未确认）。
- 与一个拥有未分配职位和零工资的员工发起交易。

## 运营

你必须至少达到3级才能在公司工作，至少达到10级才能拥有公司。

为了经营一家公司，董事要对公司的每个方面进行微观管理。他们必须：

- 雇佣玩家雇员
  - 将员工分配到对公司有利的岗位上
  - 预算员工的工资
  - 培训员工以提高他们的潜力（初级+50，中级+25）。
- 管理货物
  - 调整商品的价格，使利润最大化
  - 订购库存以补充货物
- 预算广告以吸引更多客户
- 在公司金库中保持足够的资金，以便能够支付员工和广告预算一整个星期的费用。

所有这些方面归结为3种类型的测量，以检查你的公司做得如何：受欢迎程度、效率和环境

### 受欢迎程度

受欢迎程度是你的周收入与你公司类型的最高周收入相比的百分比，不考虑评级。

即：如果你的收入是500万美元，而最好的公司收入是1000万美元，那么你的人气就是50%。这只是一个快速工具，可以看到你与该类型的其他公司相比的情况，这对了解你在十星级排名系统中获得排名的接近程度很有用。

### 效率

效率可能是需要关注的最重要的一条。它显示了你的雇员的平均效率。理想情况下，你会希望尽可能保持在100%。效率本身的上限是100%。然而，如果你有表现出色的员工，真实值可能会高于这个数值：可能会掩盖其他员工的低效率。

### 员工效能

有几个因素会影响雇员的效率。这些因素可以在公司页面的 "雇员 "部分找到，每个雇员都有一个工具提示。

这些因素是：：

- 工作状态 - 员工的工作状态越高，这个系数就越大。如果一个员工的工作状态达到了他们被分配到的工作的确切状态要求，这将显示为90。
工作状态效率的完整公式是：
```
$efficiency = FLOOR(MIN(45, (45 / $required) * $stat) + MAX(0, (5 * LOG($stat / $required, 2)))))
```
[[3]](#ref_3)

- 安置 - 员工在公司每连续工作24小时，这个奖励就会增加+1，最高为+10（需要10天）。
- 主任教育 - 这个奖励来自于下一节中列出的教育课程
- 功绩 - 员工效力的功绩在这个功绩分支中每增加一点，效力就会增加+1。这使得状态较差的玩家能够与不愿意花费功勋的优秀玩家竞争，早期的数字表明，状态完全升级后可以增加4倍的基础水平。
- 成瘾 - 这对效率有负面影响，基于员工积累的成瘾点数--见毒品。
- 不活跃 - 这将根据雇员在撕裂中不活跃的时间长短对效力产生负面影响。注意：活跃是指在游戏中实际采取行动，而不是简单的登录，根据这个补丁。

### 环境

环境是基于员工室的大小和员工的数量。吸毒者和不活跃的员工会降低你的环境得分。为了补偿，购买更大的员工室或雇用清洁工和经理，因为环境得分低会降低收入，最高可达1/3。

清洁工会更多地提升环境。根据他们对公司成功的关键程度，他们也可能创造利润。环境被提升的程度取决于清洁工/经理的效率。

雇员少于员工室的容量会使你的环境得到非常小的提升，因为他们会有更多的空间来工作。较大的公司会更努力地保持他们的环境得分，但如果环境得分略有下降，也不是世界末日。你可能会发现，与其把一个员工设置为清洁工或经理来补足环境分，不如把他留在一个重要的工作岗位上。


### 广告

为了帮助吸引顾客，董事们可以设定每天的广告预算。通过拥有一名被认为是 "营销人员 "的员工，完成BUS2400和LAW2100教育课程，以及拥有TGP的利益块，可以提高广告的效果。

广告对公司的基本影响最大为40%，并将根据竞争公司的数量和它们的广告预算而减少。如果有80家同类型的公司有广告预算，拥有最高预算的公司将获得40%的奖金，第二高的公司获得39.5%的奖金，第三高的公司获得39%的奖金，等等[4] 。

### 应聘流程

- 玩家现在最多可以同时拥有10个公司的待定申请。这意味着他们可以同时向几家公司申请，大大增加了他们迅速进入一家公司的机会。这解决了向一家公司申请，等待答复，然后再向另一家公司申请的繁琐过程。
- 公司董事将不再收到每个收到的申请的新闻或事件的垃圾邮件。相反，我们已经实施了一个单独的通知系统，提醒那些有权限的人注意待定的申请。
- 玩家可以在申请发出后的任何时候编辑他们的申请，或通过相关的公司简介撤回他们。
- 一旦一个申请被接受，所有其他相关的申请将被删除。因此，作为公司主管，你看到的所有申请都是来自现在可以加入的玩家。
- 如果一个申请被拒绝，该玩家将不能在7天内再次申请。这些7天的重新申请限制可以由公司通过切换 "允许申请 "关闭和打开来推翻。
- 如果申请没有被接受或拒绝，72小时后就会过期。

## 特殊职位

特殊职位是每家公司都有的角色，有助于提升公司的某一方面。他们是在一些与公司销售的产品不直接相关的领域给公司带来推动力的职位，但却影响到员工、环境或广告。一个员工的效率将决定这些影响有多强。

这些角色也可能会产生利润，这取决于公司的情况。

<table class="wikitable table table-striped table table-striped prettyTable">
    <tbody>
        <tr>
            <th class="header" colspan="2">Special Positions
            </th>
        </tr>
        <tr>
            <th class="subheader">Position
            </th>
            <th class="subheader">Effect
            </th>
        </tr>
        <tr>
            <td>Cleaner</td>
            <td>Helps keep your environment up
            </td>
        </tr>
        <tr>
            <td>Manager</td>
            <td>Increases your employee effectiveness
            </td>
        </tr>
        <tr>
            <td>Marketer</td>
            <td>Increases the effectiveness of your advertising budget
            </td>
        </tr>
        <tr>
            <td>Secretary</td>
            <td>Shows you how much your employees are earning you in detail
            </td>
        </tr>
        <tr>
            <td>Trainer</td>
            <td>Gives you extra trains (Maximum of 3)
            </td>
        </tr>
    </tbody>
</table>

## 公司排名

公司排名是一个十星级的排名系统，基于你的公司一直以来的表现，以毛利为量化标准。为了改善公司，你应该努力争取最好的利润，因为利润只有通过有效地经营公司才能得到。公司的排名只能达到一定的上限--普遍认为是基于总收入：如果公司在其一生中创造了更多的收入，它就有能力获得更高的排名。

公司排名可以影响到授予多少工作点数（每1星1个工作点数），以及公司董事获得多少统计资料。公司董事根据公司排名的高低获得工作状态：

- 1星 - 每天5个单位的工作状态
- 2颗星--10个单位
- 3颗星--20个单位
- 4颗星 - 35个单位
- 5颗星以上 - 50个单位

你的员工工资并不影响你的公司升星的能力（一个常见的误解）。

公司有能力在每个星期天自动上升或下降排名。

## 员工

在申请公司时，你的[工作数据](working_stat.md)将帮助主任确定你的职位。公司主管决定每个员工的工资数额（最高上限为25,000,000美元。所有职位都有不同的工作状态要求（主要和次要），并将以不同的方式帮助公司。主要和次要的工作状态是对你加入的公司有帮助的状态：它们越高，你在该角色上就越有效，即获得更多的客户，保持工作场所的清洁，更快地建立硬件，等等。次要工作状态在等级上的影响力是你主要工作状态的一半。

在一个公司里，你是存在的。你的参与是由其他因素自动决定的（工作统计、吸毒和最低日常活动）。大部分的工作是在主任那边完成的（见上文）。

主任可以对你进行训练，使你的主要和次要属性分别增加50和25的工作属性。工作特长和主任培训将为新雇用的员工锁定72小时。

## 工作特别要求

[工作特技](job_special.md)是一种特殊的能力，可以主动获得（通过花费在关门时间获得的工作点数），也可以被动使用（没有成本）。要解锁使用工作特长，公司必须在其公司排名中达到所需的星级水平。

基于能量的特殊工作的重复性被限制在每天100次的使用。

## 关闭时间

在公司的一天结束时（大约在TCT下午6点），公司的业绩被计算出来。这可以从当天的客户数量和总收入的数量看出。同时，工作状态收益被自动应用，工作积分被授予（公司排名每上升一星就有一个积分），员工工资被自动分配，员工火车被生成，供主管使用。这一操作可能需要15分钟才能反映出结果。

虽然一个不活跃的员工对公司来说是一个很大的损害，但没有一个活跃的董事，公司也可以自己漂浮起来；员工火车只会堆积到上限，而不会被分配，股票最终也会耗尽。

## 影响公司的股票和教育
### 董事

[股票市场](stock_market.md)上有各种股票，如果持有利益块，可以帮助公司董事。直接使公司受益的股票有：

- Tell Group Plc.(TGP) - 让你的公司广告效益大幅提升。
- TC Media Productions (TCP) - 给你的公司带来10%的利润增长。
- Syscore MFG (SYS)--通过Intricate Hack公司效益保护你的公司不被玩家入侵（对储存大量资金的公司有好处）。

以下是可以间接帮助董事的股票：

- Messaging Inc.（MSG）--允许在报纸上免费刊登广告，可以帮助招聘员工。
- Yazoo（YAZ）--在报纸上给出免费的广告标语，这可以帮助招聘员工。

所学的[教育](education.md)课程，除了从每个课程中获得的被动工作状态外，还可以对你拥有的公司（作为董事）产生影响。这些公司包括

- 所有[商业管理](buss_management.md)课程，以各种方式。
- BUS2200, BUS2500, BUS2800, BUS2100, BUS2120 - 为您的公司获得2%的生产力
- BUS2300 - 为您的公司获得5%的员工效率
- BUS2400 - 为您的公司提高广告效益
- BUS2600 - 为您的公司获得7%的员工效益
- BUS2700 - 获得将产品价格提高10%而不失去客户的能力
- BUS2900 - 获得将产品价格提高5%而不失去客户的能力
- BUS2110 - 获得员工在公司工作状态的被动奖励
- BUS3130 - 解锁新的尺寸、存储尺寸和员工房间的升级，以供购买

- 课程MTH2280

有助于提高公司生产力1%。

- 课程LAW2100

为您的公司获得广告效益的提高

### 员工

作为一个雇员，完成[教育](education.md)课程可以授予你不同数量的工作统计。你可以通过以下方式提高你完成教育课程的速度：

- 一星级[健身中心](fitness_center.md)的特殊 "辅导"
- 7星级[发廊](hair_salon.md)特制 "切角"
- 每申请一个功绩，可获得2%的功绩（最多10个功绩，总减少20%）。
- 西南大学的福利金块（总共减少10%）。
- 教育工作中的校长职位（被动特殊）。

## 升级

公司有各种可以应用的升级，以帮助公司更快地工作。


### 公司规模

公司规模的升级增加了你的公司可以容纳的员工数量。每次升级的费用为初始启动费用的10%，每次升级可增加25%的雇员人数。最后两个公司规模的升级，只有在公司主管完成了以下工作的情况下才能进行

BUS3130

<table class="wikitable table table-striped table table-striped prettyTable">
    <tbody>
        <tr>
            <th class="header" colspan="2">Company Size Upgrades
            </th>
        </tr>
        <tr>
            <th class="subheader">Size
            </th>
            <th class="subheader">Cost
            </th>
        </tr>
        <tr>
            <td>Starting size</td>
            <td><i>Startup</i>
            </td>
        </tr>
        <tr>
            <td>125% startup size</td>
            <td>10% of startup cost
            </td>
        </tr>
        <tr>
            <td>150% startup size</td>
            <td>20% of startup cost
            </td>
        </tr>
        <tr>
            <td>175% startup size</td>
            <td>30% of startup cost
            </td>
        </tr>
        <tr>
            <td>200% startup size</td>
            <td>40% of startup cost
            </td>
        </tr>
        <tr>
            <td>225% startup size</td>
            <td>50% of startup cost
            </td>
        </tr>
        <tr>
            <td>250% startup size</td>
            <td>60% of startup cost
            </td>
        </tr>
        <tr>
            <th class="subheader">Total
            </th>
            <td><b>210% of startup cost</b>
            </td>
        </tr>
    </tbody>
</table>


### 员工休息室

员工室的升级有助于保持你的环境在100%。当你有更多员工时，你需要更大的员工室。最后两个员工室的升级，只有在公司主管完成了

BUS3130

<table class="wikitable table table-striped table table-striped prettyTable">
    <tbody>
        <tr>
            <th class="header" colspan="2">Staff Room Upgrades
            </th>
        </tr>
        <tr>
            <th class="subheader">Size
            </th>
            <th class="subheader">Cost
            </th>
        </tr>
        <tr>
            <td>No staff room</td>
            <td><i>Startup</i>
            </td>
        </tr>
        <tr>
            <td>Small staff room</td>
            <td>2.5% of startup cost
            </td>
        </tr>
        <tr>
            <td>Standard staff room</td>
            <td>5% of startup cost
            </td>
        </tr>
        <tr>
            <td>Large staff room</td>
            <td>7.5% of startup cost
            </td>
        </tr>
        <tr>
            <td>Very large staff room</td>
            <td>10% of startup cost
            </td>
        </tr>
        <tr>
            <td>Huge staff room</td>
            <td>12.5% of startup cost
            </td>
        </tr>
        <tr>
            <td>Colossal staff room</td>
            <td>15% of startup cost
            </td>
        </tr>
        <tr>
            <th class="subheader">Total
            </th>
            <td><b>52.5% of startup cost</b>
            </td>
        </tr>
    </tbody>
</table>

### 仓库

仓库持有库存。并非所有的公司都需要仓库，一个仓库能容纳的物品数量取决于公司的情况。

<table class="wikitable table table-striped table table-striped prettyTable">
    <tbody>
        <tr>
            <th class="header" colspan="2">Warehouse Upgrades
            </th>
        </tr>
        <tr>
            <th class="subheader">Size
            </th>
            <th class="subheader">Cost
            </th>
        </tr>
        <tr>
            <td>Small room</td>
            <td><i>Startup</i>
            </td>
        </tr>
        <tr>
            <td>Standard room</td>
            <td>5% of startup cost
            </td>
        </tr>
        <tr>
            <td>Large room</td>
            <td>10% of startup cost
            </td>
        </tr>
        <tr>
            <td>Huge room</td>
            <td>15% of startup cost
            </td>
        </tr>
        <tr>
            <td>Warehouse</td>
            <td>20% of startup cost
            </td>
        </tr>
        <tr>
            <td>Large warehouse</td>
            <td>25% of startup cost
            </td>
        </tr>
        <tr>
            <td>Huge warehouse</td>
            <td>30% of startup cost
            </td>
        </tr>
        <tr>
            <th class="subheader">Total
            </th>
            <td><b>105% of startup cost</b>
            </td>
        </tr>
    </tbody>
</table>

## 公司回购

当你把一个公司卖回给系统时，你可以得到该公司75%的成本，包括在该公司上花费的任何升级费用（仍然是75%），再加上其生命周期内总收入的5%。(同时，你还可以得到储存在你的金库中的任何资金的100%！)。

## 公司

如需了解每家公司的详细情况，请访问[公司列表](company_list.md)页。对于一个具体的公司，请使用下面的表格并导航到该公司的页面。

如需了解公司特价产品的清单，请访问[特价清单](special_list.md)页面。

<table class="wikitable table table-striped table table-striped prettyTable sortable">
    <tbody>
        <tr>
            <th class="header" colspan="3">Companies List
            </th>
        </tr>
        <tr>
            <th class="subheader">Company
            </th>
            <th class="subheader">Cost
            </th>
            <th class="subheader">Size
            </th>
        </tr>
        <tr>
            <td><a href="/wiki/Adult_Novelties" title="Adult Novelties">Adult Novelties</a></td>
            <td>$1,750,000</td>
            <td>4 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Amusement_Park" title="Amusement Park">Amusement Park</a></td>
            <td>$100,000,000</td>
            <td>8 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Candle_Shop" title="Candle Shop">Candle Shop</a></td>
            <td>$500,000</td>
            <td>4 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Car_Dealership" title="Car Dealership">Car Dealership</a></td>
            <td>$6,000,000</td>
            <td>4 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Clothing_Store" title="Clothing Store">Clothing Store</a></td>
            <td>$1,000,000</td>
            <td>5 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Cruise_Line" title="Cruise Line">Cruise Line</a></td>
            <td>$300,000,000</td>
            <td>6 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Cyber_Cafe" title="Cyber Cafe">Cyber Cafe</a></td>
            <td>$3,000,000</td>
            <td>4 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Detective_Agency" title="Detective Agency">Detective Agency</a></td>
            <td>$12,000,000</td>
            <td>4 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Farm" title="Farm">Farm</a></td>
            <td>$5,250,000</td>
            <td>5 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Firework_Stand" title="Firework Stand">Firework Stand</a></td>
            <td>$500,000</td>
            <td>4 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Fitness_Center" title="Fitness Center">Fitness Center</a></td>
            <td>$17,000,000</td>
            <td>8 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Flower_Shop" title="Flower Shop">Flower Shop</a></td>
            <td>$500,000</td>
            <td>4 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Furniture_Store" title="Furniture Store">Furniture Store</a></td>
            <td>$2,500,000</td>
            <td>4 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Game_Shop" title="Game Shop">Game Shop</a></td>
            <td>$1,250,000</td>
            <td>4 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Gas_Station" title="Gas Station">Gas Station</a></td>
            <td>$25,000,000</td>
            <td>4 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Gents_Strip_Club" title="Gents Strip Club">Gents Strip Club</a></td>
            <td>$5,000,000</td>
            <td>4 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Grocery_Store" title="Grocery Store">Grocery Store</a></td>
            <td>$2,000,000</td>
            <td>5 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Gun_Shop" title="Gun Shop">Gun Shop</a></td>
            <td>$2,500,000</td>
            <td>4 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Hair_Salon" title="Hair Salon">Hair Salon</a></td>
            <td>$750,000</td>
            <td>4 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Ladies_Strip_Club" title="Ladies Strip Club">Ladies Strip Club</a></td>
            <td>$5,000,000</td>
            <td>4 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Law_Firm" title="Law Firm">Law Firm</a></td>
            <td>$4,000,000</td>
            <td>4 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Lingerie_Store" title="Lingerie Store">Lingerie Store</a></td>
            <td>$1,750,000</td>
            <td>4 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Logistics_Management" title="Logistics Management">Logistics Management</a></td>
            <td>$1,800,000,000</td>
            <td>6 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Meat_Warehouse" title="Meat Warehouse">Meat Warehouse</a></td>
            <td>$4,000,000</td>
            <td>5 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Mechanic_Shop" title="Mechanic Shop">Mechanic Shop</a></td>
            <td>$3,000,000</td>
            <td>4 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Mining_Corporation" title="Mining Corporation">Mining Corporation</a></td>
            <td>$4,500,000,000</td>
            <td>8 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Music_Store" title="Music Store">Music Store</a></td>
            <td>$1,500,000</td>
            <td>4 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Nightclub" title="Nightclub">Nightclub</a></td>
            <td>$7,500,000</td>
            <td>5 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Oil_Rig" title="Oil Rig">Oil Rig</a></td>
            <td>$10,500,000,000</td>
            <td>12 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Private_Security_Firm" title="Private Security Firm">Private Security Firm</a></td>
            <td>$950,000,000</td>
            <td>6 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Property_Broker" title="Property Broker">Property Broker</a></td>
            <td>$750,000</td>
            <td>4 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Pub" title="Pub">Pub</a></td>
            <td>$1,250,000</td>
            <td>4 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Restaurant" title="Restaurant">Restaurant</a></td>
            <td>$1,000,000</td>
            <td>4 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Software_Corporation" title="Software Corporation">Software Corporation</a></td>
            <td>$6,000,000</td>
            <td>5 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Sweet_Shop" title="Sweet Shop">Sweet Shop</a></td>
            <td>$1,000,000</td>
            <td>4 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Television_Network" title="Television Network">Television Network</a></td>
            <td>$8,000,000,000</td>
            <td>8 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Theater" title="Theater">Theater</a></td>
            <td>$50,000,000</td>
            <td>6 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Toy_Shop" title="Toy Shop">Toy Shop</a></td>
            <td>$2,000,000</td>
            <td>5 employees
            </td>
        </tr>
        <tr>
            <td><a href="/wiki/Zoo" title="Zoo">Zoo</a></td>
            <td>$300,000,000</td>
            <td>6 employees
            </td>
        </tr>
    </tbody>
</table>

## 历史注释

- 在2014年1月27日的更新之前，广告费用曾经被划分为 "廉价""标准 "和 "昂贵
"的广告费用。其各自的费用是各自公司费用的一半、同等或两倍，如果董事在TGP有股票利益，则免费。广告将持续一个星期，届时必须以同样的费用重新启动。广告的目的是为了提高知名度，从而使利润增加。现在人气只是业绩的一个标志，对收入没有直接影响。
-
在2014年1月的更新之前，公司所有者还必须使用1-5日的火车（基于公司星级）来防止效率下降。据报道，现在不再是这种情况了。这有一定的道理，因为在更新之后，一个公司现在最多可以保存20辆火车。公司每天获得的火车与公司的星级相等，1\*的公司每天获得1列火车，而5\*的公司每天获得5列火车。这可以通过任命一些员工为培训师来增加。
- 在2015年2月25日医疗2.0更新后的几周内，五星级和十星级公司被添加到游戏中。
- 按照Chedburn的公告，私人保安公司的奖金 "条例 "从10%改为25%。
- 根据Chedburn的评论，工作点的限制现在是 "每个撕裂日"，而不是24小时。

## 杂项注释

可以通过将售出产品的价格设定在RRP以下来创造客户忠诚度。创造客户忠诚度需要数年时间，并使公司能够获得更多的客户或以更高的价格销售。


## 引用

<div class="mw-references-wrap">
    <ol class="references">
        <li id="cite_note-1"><span class="mw-cite-backlink"><a href="#cite_ref-1">↑</a></span> <span
                class="reference-text"> Chedburn, <a rel="nofollow" class="external text"
                    href="https://www.torn.com/old_forums.php?forumID=1&amp;ID=1088915">Addition: Companies</a>
                (14/4/07) </span>
        </li>
        <li id="cite_note-2"><span class="mw-cite-backlink"><a href="#cite_ref-2">↑</a></span> <span
                class="reference-text">Chedburn, <a rel="nofollow" class="external text"
                    href="https://www.torn.com/forums.php#/p=threads&amp;t=16187257&amp;to=20817319">Bad calculation for
                    stats efficiency </a> 27/09/20</span>
        </li>
        <li id="cite_note-3"><span class="mw-cite-backlink"><a href="#cite_ref-3">↑</a></span> <span
                class="reference-text"> KingLouisCLXXII [2070312],<a rel="nofollow" class="external text"
                    href="https://www.torn.com/forums.php#/p=threads&amp;t=16227240">Efficiency Calculation</a>
                24/05/21</span>
        </li>
        <li id="cite_note-4"><span class="mw-cite-backlink"><a href="#cite_ref-4">↑</a></span> <span
                class="reference-text">Chedburn, Private Communication (28/10/21)</span>
        </li>
    </ol>
</div>