> Battle Stats


提交人: contr4l_[2903026]

提交日期: 2023-04-27

原文地址: https://wiki.torn.com/wiki/Battle_Stats

内部超链接:  

!> TODO: 内部大量超链接没有制作

# 5.战斗数值

你的战斗属性是攻击其他玩家时使用的属性。它们是力量、速度、防御和灵活性。

## 基础信息

每个战斗状态在战斗中都有不同的效果：

力量

- 增加你每次攻击的伤害。

防御

- 减少你每次击中的伤害。

速度

- 增加击中对手的机会。
- 减少你的对手从你手中逃脱的机会。

灵巧性

- 增加你躲避攻击的机会。
- 增加你隐身攻击的机会。
- 减少你的对手隐身攻击的机会。
- 增加你从对手手中逃脱的机会。

这四种战斗状态在训练时都会成倍增长。历史上有一个5000万的软上限，也被称为 "状态上限"，之后它们以相对固定的速度增长，然而这在2022年8月被取消[1] 。

提高你的战斗状态的主要方法是在[健身房](gym.md)用[能量](energy.md)训练。

## 属性权重

战斗状态的权重是基于最初的攻击2.0公告线程中提供的权重，并对一些更多的间隔进行了计算。[2] 速度与灵巧的对比使用了基于现有信息的最佳近似值。

<table class="wikitable table table-striped table table-striped prettyTable">
    <tbody>
        <tr>
            <th class="header" colspan="2">Battle Stat Weights
            </th>
        </tr>
        <tr>
            <th class="subheader">Speed versus 10,000,000 Dexterity
            </th>
            <th class="subheader">Defense versus 10,000,000 Strength
            </th>
        </tr>
        <tr>
            <td>156,250 speed&#160;: 0% hit chance</td>
            <td>312,500 defense&#160;: 0% damage mitigation
            </td>
        </tr>
        <tr>
            <td>500,000 speed&#160;: 5.63% hit chance</td>
            <td>625,000 defense&#160;: 10.00% damage mitigation
            </td>
        </tr>
        <tr>
            <td>1,000,000 speed&#160;: 10.93% hit chance</td>
            <td>1,250,000 defense&#160;: 20.00% damage mitigation
            </td>
        </tr>
        <tr>
            <td>2,000,000 speed&#160;: 18.41% hit chance</td>
            <td>2,500,000 defense&#160;: 30.00% damage mitigation
            </td>
        </tr>
        <tr>
            <td>5,000,000 speed&#160;: 33.26% hit chance</td>
            <td>5,000,000 defense&#160;: 40.00% damage mitigation
            </td>
        </tr>
        <tr>
            <td>10,000,000 speed&#160;: 50.00% hit chance</td>
            <td>10,000,000 defense&#160;: 50.00% damage mitigation
            </td>
        </tr>
        <tr>
            <td>15,000,000 speed&#160;: 60.49% hit chance</td>
            <td>15,000,000 defense&#160;: 57.68% damage mitigation
            </td>
        </tr>
        <tr>
            <td>20,000,000 speed&#160;: 66.74% hit chance</td>
            <td>20,000,000 defense&#160;: 63.14% damage mitigation
            </td>
        </tr>
        <tr>
            <td>30,000,000 speed&#160;: 74.15% hit chance</td>
            <td>30,000,000 defense&#160;: 70.81% damage mitigation
            </td>
        </tr>
        <tr>
            <td>40,000,000 speed&#160;: 78.57% hit chance</td>
            <td>40,000,000 defense&#160;: 76.26% damage mitigation
            </td>
        </tr>
        <tr>
            <td>50,000,000 speed&#160;: 81.59% hit chance</td>
            <td>50,000,000 defense&#160;: 80.49% damage mitigation
            </td>
        </tr>
        <tr>
            <td>60,000,000 speed&#160;: 83.81% hit chance</td>
            <td>60,000,000 defense&#160;: 83.95% damage mitigation
            </td>
        </tr>
        <tr>
            <td>70,000,000 speed&#160;: 85.54% hit chance</td>
            <td>70,000,000 defense&#160;: 86.87% damage mitigation
            </td>
        </tr>
        <tr>
            <td>80,000,000 speed&#160;: 86.94% hit chance</td>
            <td>80,000,000 defense&#160;: 89.40% damage mitigation
            </td>
        </tr>
        <tr>
            <td>90,000,000 speed&#160;: 88.10% hit chance</td>
            <td>90,000,000 defense&#160;: 91.63% damage mitigation
            </td>
        </tr>
        <tr>
            <td>100,000,000 speed&#160;: 89.07% hit chance</td>
            <td>100,000,000 defense&#160;: 93.63% damage mitigation
            </td>
        </tr>
        <tr>
            <td>200,000,000 speed&#160;: 94.37% hit chance</td>
            <td>110,000,000 defense&#160;: 95.43% damage mitigation
            </td>
        </tr>
        <tr>
            <td>400,000,000 speed&#160;: 98.11% hit chance</td>
            <td>120,000,000 defense&#160;: 97.08% damage mitigation
            </td>
        </tr>
        <tr>
            <td>500,000,000 speed&#160;: 99.06% hit chance</td>
            <td>130,000,000 defense&#160;: 98.60% damage mitigation
            </td>
        </tr>
        <tr>
            <td>640,000,000 speed&#160;: 100% hit chance</td>
            <td>140,000,000 defense&#160;: 100% damage mitigation
            </td>
        </tr>
    </tbody>
</table>

<p><br />
</p>
<p><img src="https://i.gyazo.com/92727e8fe68f603a912d50a4f7d0aeae.png" alt="92727e8fe68f603a912d50a4f7d0aeae.png" />
</p>
<p><br />
</p>

## 提高/降低战斗属性值

你的战斗状态可以通过几种方法增加或减少，或由于你可能拥有的特权。

### 提高健身房收益

- 教育  
运动科学课程
  - SPT3510：运动科学学士学位+1%，提升所有健身房收益
  - SPT2440：力量与调理--在健身房获得1%的力量提升奖励
  - SPT2450：生理测试 - 在健身房获得1%的速度收益奖励
  - SPT2460：人体运动分析--在健身房获得1%的防守收益奖励。
  - SPT2470：技能的生物机械决定因素--在健身房中获得1%的灵活性收益奖励。

- 物品  
[书](books.md)

<table class="wikitable table table-striped table table-striped prettyTable sortable">
    <tbody>
        <tr>
            <th class="header" colspan="5">Books
            </th>
        </tr>
        <tr>
            <th class="subheader">Image
            </th>
            <th class="subheader">ID
            </th>
            <th class="subheader">Name
            </th>
            <th class="subheader">Effect
            </th>
            <th class="subheader">Cost (Credits)
            </th>
        </tr>
        <tr>
            <td><img src="https://www.torn.com/images/items/757/large.png" alt="large.png" /></td>
            <td>757</td>
            <td>Book&#160;: Get Hard Or Go Home</td>
            <td>Increases all gym gains by 20% for 31 days.</td>
            <td>1343 - 1810
            </td>
        </tr>
        <tr>
            <td><img src="https://www.torn.com/images/items/758/large.png" alt="large.png" /></td>
            <td>758</td>
            <td>Book&#160;: Gym Grunting - Shouting To Success</td>
            <td>Increases Strength gym gains by 30% for 31 days.</td>
            <td>1623 - 1970
            </td>
        </tr>
        <tr>
            <td><img src="https://www.torn.com/images/items/759/large.png" alt="large.png" /></td>
            <td>759</td>
            <td>Book&#160;: Self Defense In The Workplace</td>
            <td>Increases Defense gym gains by 30% for 31 days.</td>
            <td>1488 - 1950
            </td>
        </tr>
        <tr>
            <td><img src="https://www.torn.com/images/items/760/large.png" alt="large.png" /></td>
            <td>760</td>
            <td>Book&#160;: Speed 3 - The Rejected Script</td>
            <td>Increases Speed gym gains by 30% for 31 days.</td>
            <td>1115 - 1784
            </td>
        </tr>
        <tr>
            <td><img src="https://www.torn.com/images/items/761/large.png" alt="large.png" /></td>
            <td>761</td>
            <td>Book&#160;: Limbo Lovers 101</td>
            <td>Increases Dexterity gym gains by 30% for 31 days.</td>
            <td>1501 - 1995
            </td>
        </tr>
    </tbody>
</table>

- 运动型运动鞋：如果你的库存中有此物品，可将你在健身房训练中的速度收益提高5%。可在迪拜以140亿美元的价格购买。
- 派别津贴--坚定不移：分支机构内的每一级都会增加分支机构类型的健身训练1%。例如，力量训练七级将增加7%的健身房力量收益。
- 公司特价
- 女士脱衣舞俱乐部：10*有抱负的锻炼被动：+10％的防御性健身房收益
- 男士脱衣舞俱乐部：10*有抱负的锻炼被动项：+10%灵巧度的健身房收益
- 健身中心：10* 训练制度被动：所有健身器材收益增加3%。

### 积极地提高/降低战斗属性值

- 利用能量在健身房训练
- 增益剂
一次性使用，永久增加状态

  - 滑板：速度+1％。
  - 降落伞：灵巧度+1
  - 拳击手套：+1％的防御
  - 哑铃：力量+1

- 物品
[书](books.md)

<table class="wikitable table table-striped table table-striped prettyTable sortable">
    <tbody>
        <tr>
            <th class="header" colspan="5">Books
            </th>
        </tr>
        <tr>
            <th class="subheader">Image
            </th>
            <th class="subheader">ID
            </th>
            <th class="subheader">Name
            </th>
            <th class="subheader">Effect
            </th>
            <th class="subheader">Cost (Credits)
            </th>
        </tr>
        <tr>
            <td><img src="https://www.torn.com/images/items/744/large.png" alt="large.png" /></td>
            <td>744</td>
            <td>Book&#160;: Brawn Over Brains</td>
            <td>Increases strength by 5% up to 10m upon completion.</td>
            <td>1543 - 1825
            </td>
        </tr>
        <tr>
            <td><img src="https://www.torn.com/images/items/745/large.png" alt="large.png" /></td>
            <td>745</td>
            <td>Book&#160;: Time Is In The Mind</td>
            <td>Increases speed by 5% up to 10m upon completion.</td>
            <td>1611 - 1985
            </td>
        </tr>
        <tr>
            <td><img src="https://www.torn.com/images/items/746/large.png" alt="large.png" /></td>
            <td>746</td>
            <td>Book&#160;: Keeping Your Face Handsome</td>
            <td>Increases defense by 5% up to 10m upon completion.</td>
            <td>1756
            </td>
        </tr>
        <tr>
            <td><img src="https://www.torn.com/images/items/747/large.png" alt="large.png" /></td>
            <td>747</td>
            <td>Book&#160;: A Job For Your Hands</td>
            <td>Increases dexterity by 5% up to 10m upon completion.</td>
            <td>1119
            </td>
        </tr>
        <tr>
            <td><img src="https://www.torn.com/images/items/784/large.png" alt="large.png" /></td>
            <td>784</td>
            <td>Book&#160;: Ugly Energy</td>
            <td>Increases maximum energy and energy refills by 100 for 31 days.</td>
            <td>1590
            </td>
        </tr>
    </tbody>
</table>

- 公司特价
  - 家具店：3*举重特价：在你目前的健身房里，每个工作点大约有4.5E的力量提升。
  - 采矿公司：5*岩盐特技：在你目前的健身房里，每个工作点可以获得价值约4.5E的防御力。
  - 电视网：10*记者证特别项目：（约0.25%的随机数据。）
  - 健身中心：5*罗伊德狂暴特技：在你目前的健身房里，每个工作点可以获得价值约4.5E的力量收益。

系统工作：

- 军队
  - 每个工作点的防御增益
  - 每个工作点的力量增益

### 被动地提高/降低战斗属性值

- 教育

    所有来自教育的被动状态增加摘要如下
    力量 = +5%
    速度 = +14%
    防御 = +11%
    灵巧 = +19%
    所有健身房的收益为+2%。

    - 运动科学课程

    SPT2490: 营养科学 - 获得2%的速度和力量的被动奖励
    SPT2500: 分析与表现 - 获得2%的防御和灵活性的被动奖励

    - 健康与健身课程

    HAF2104: 有氧运动 - 获得1%的灵巧被动奖励
    HAF2105: 杂技 - 获得1%的速度被动奖励
    HAF2106：举重--获得1%的力量被动加成
    HAF2107：瑜伽--获得2%的力量被动奖励。
    HAF2108: 游泳 - 获得1%的灵活性被动加成
    HAF2109：马拉松训练 - 获得3%的速度被动奖励

    - 数学课程

    MTH2240: 基础数学 - 获得1%的速度被动奖励
    MTH2250: 中级数学 - 获得1%的速度被动奖励
    MTH2260：几何学 - 获得1%的被动防御加成
    MTH2320：几何学2 - 获得2%的被动防御奖励

    - 心理学课程

    PSY2640：记忆与决策 - 获得1%的灵巧被动奖励
    PSY2650：大脑与行为 - 获得2%的灵巧被动奖励
    PSY2660：心理学的定量方法 - 获得4%的灵巧性被动奖励
    PSY2670：应用决策方法 - 获得8%的灵巧被动奖励

    - 自卫课程

    DEF2710：柔道 - 获得1%的被动防御奖励
    DEF2730: Krav Maga - 获得1%的被动防御奖励。
    DEF2740：柔术 - 获得3%的防御被动加成
    DEF2750: 跆拳道 - 获得2%的速度被动加成
    DEF2760: 泰拳 - 获得3%的速度被动加成

    - 搏击训练课程

    CBT2790：军事心理学 - 获得1%的速度被动加成

- 派别津贴

侵略 - 主分支的每次升级都会被动地增加速度和力量，每次升级增加1%。

压制 - 主分支的每一次升级都会被动地增加1%的防御和灵巧能力。

- 优点

膂力 - 每点给力量带来3%的被动奖励，最高+30%。

保护 - 每点提供3%的被动防御奖励，最高+30%。

锋利 - 每点提供3%的速度被动加成，最大加成为30%。

躲避 - 给予灵巧的被动奖励，每点3%，最高+30%。

- 药物

大麻：力量-20%，防御-25%，速度-35%。

氯胺酮：力量和速度-20%，防御+50%。

LSD：力量+30%，防御+50%，速度和灵活性-30%。

鸦片：防御力+30%。

PCP：力量和灵活性+20%。

蘑菇：对所有属性的影响为-20%。

速度：灵巧度-20%，速度+20%。

维柯丁（Vicodin）：+所有属性增加25%。

赞安诺：所有状态为-35%。

爱的果汁：速度+50%，灵活度+25%。

注意：过量服用PCP会使力量和防御力永久下降6倍（当前等级），过量服用速度会使速度永久下降10倍（当前等级）。

## 历史注释

- 在17/11/14，Chedburn发布了一个关于DEF与STR曲线的一些拟议变化的投票。
- 14年11月18日，Chedburn发布了一个主题，揭示了当时的SPD vs DEX曲线。
- 14年12月2日，Chedburn发布了一份关于对上述攻击曲线、DEF vs STR和SPD vs DEX进行修改的公告。


## 引用

<div class="mw-references-wrap">
    <ol class="references">
        <li id="cite_note-1"><span class="mw-cite-backlink"><a href="#cite_ref-1">↑</a></span> <span
                class="reference-text">Chedburn,<a rel="nofollow" class="external text"
                    href="https://www.torn.com/forums.php#/p=threads&amp;t=16288778">Gym training&#160;: Stat cap
                    removal</a> (02/08/22)</span>
        </li>
        <li id="cite_note-2"><span class="mw-cite-backlink"><a href="#cite_ref-2">↑</a></span> <span
                class="reference-text">Chedburn, <a rel="nofollow" class="external text"
                    href="https://www.torn.com/forums.php#/p=threads&amp;t=15924203">Addiction, Plushies &amp;
                    Attacking</a> (02/12/14).</span>
        </li>
    </ol>
</div>