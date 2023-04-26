>  Attack

提交人: contr4l_[2903026]  
提交日期: 2023-04-27 
原文地址: https://wiki.torn.com/wiki/Attack
内部超链接:
- [武器模组](weapon_mod.md)
- [爱的果汁](love_juice.md)
- [侦探事务所](detective_agency.md)
- [掠夺](loot.md)
- [快乐](happy.md)
- [优点](merit.md)
- [抢劫](mug.md)
- [首选项](preference.md)
- [临时物品](temporary.md)
- [积分](point.md)
- [武器](weapon.md)
- [逮捕](arrest.md)
- [住院治疗](hospitalize.md)
- [转盘](spin_the_wheel.md)
- [分心](distraction.md)
- [任务](mission.md)
- [积分大楼](point_building.md)
- [弹药](ammo.md)
- [离开](leave.md)
- [有组织犯罪](organized_crime.md)
- [盔甲](armor.md)
- [能量](energy.md)

# 3.攻击

## 基本概念
攻击另一个玩家需要花费25个能量，但在情人节活动期间，在[爱的果汁](love_juice.md)作用下的攻击除外，那时需要花费15个能量。

一旦开始攻击，你将有25个 "回合 "或5分钟来击败你的对手。一个回合可以包括使用[武器](weapon.md)或[临时物品](temporary.md)，重新装弹，或试图逃跑。

在战斗中的每个攻击回合之间，有一秒钟的冷却时间。

25个回合后，如果双方都没有获胜，则战斗会陷入**僵局**。五分钟后，如果没有使用25个回合，则战斗结果为 "超时"--相当于攻击方的失败。

## 玩家模型
当攻击一个玩家时，有14个身体部位可以击中。其中有三个是**关键部位**，对对手造成的伤害最大。

<table class="wikitable table table-striped table table-striped prettyTable">
    <tbody>
        <tr>
            <th class="header" colspan="2">Body Part Damage
            </th>
        </tr>
        <tr>
            <th class="subheader" style="width: 15%;">Body Part
            </th>
            <th class="subheader" style="width: 10%;">Damage Multiplier
            </th>
        </tr>
        <tr>
            <td>Head <i>(critical)</i></td>
            <td>3.5
            </td>
        </tr>
        <tr>
            <td>Throat <i>(critical)</i></td>
            <td>3.5
            </td>
        </tr>
        <tr>
            <td>Heart <i>(critical)</i></td>
            <td>3.5
            </td>
        </tr>
        <tr>
            <td>Chest</td>
            <td>2
            </td>
        </tr>
        <tr>
            <td>Stomach</td>
            <td>2
            </td>
        </tr>
        <tr>
            <td>Groin</td>
            <td>2
            </td>
        </tr>
        <tr>
            <td>Arm (left/right)</td>
            <td>1
            </td>
        </tr>
        <tr>
            <td>Hand (left/right)</td>
            <td>0.7
            </td>
        </tr>
        <tr>
            <td>Leg (left/right)</td>
            <td>1
            </td>
        </tr>
        <tr>
            <td>Foot (left/right)</td>
            <td>0.7
            </td>
        </tr>
    </tbody>
</table>

<img src="https://i.postimg.cc/J0HM6ncY/aacf51ff48089884e362ca45104b1e3b.png" alt="aacf51ff48089884e362ca45104b1e3b.png" />

要害攻击的几率从12%开始，可以通过教育**BIO2410：解剖学**增加+3%，每升级到**要害攻击率**的[优点](merit.md)增加0.5%（总共+5%），并通过**激光**[武器模组](weapon_mod.md)增加2-5%。

喉部伤害可以通过**教育BIO2380**增加10%：**神经生物学的基础知识**。

## 可能的结果

### 胜利

无论你是否设法击败对手，攻击都有许多可能的结果：

- 离开
离开对手为攻击者提供了所有选项中最多的等级经验，并给防御者最少的住院时间（15-30分钟）。

[离开](leave.md)

- 抢劫
抢劫对手允许攻击者偷取防御者手头一定比例的现金（5-15%之间）。与离开对手相比，打劫为攻击者提供了减少的尊重和等级经验，并为防御者提供了大约30-45分钟的基本住院时间。

[抢劫](mug.md)

- 送医院
将对手送入医院，会使防御者在尽可能长的时间内（基本：3-3.5小时）。在所有结果中，住院提供的等级经验最少；这样做可能是为了报复敌方派系成员，收集赏金，或为了任务要求。

[住院治疗](hospitalize.md)

- 逮捕
如果你是一个至少有3颗星的[侦探事务所](detective_agency.md)的成员，也有可能逮捕一个玩家，把他们送进监狱以获得现金奖励。

[逮捕](arrest.md)

- 掠夺
有几个NPC账户可用于掠夺。掠夺为一些攻击者（基于击败NPC时的掠夺等级）提供特殊的NPC物品，使用抽签系统。

[掠夺](loot.md)

- 任务结果
有些任务要求在击败目标后使用不寻常的选项，如 "亲吻"、"审问 "和 "保密<物品>"。

[任务](mission.md)

### 失败

- 逃逸
攻击者可以在防守者失误的回合后的回合中试图从对手手中逃脱。如果防守方再次失误，则逃脱成功，这意味着你的逃脱机会是基于攻击者的灵巧程度与防守方的速度相比。注意：击中零伤害或使用无伤害的临时物品等同于失误，因此如果防御者做了这两件事，攻击者就可能[逃脱](#cite_note-1 ":id=cite_ref-1")。

- 僵持
25个回合后，如果双方都没有击败对方，战斗将以僵局结束。僵局不会给进攻方带来尊重。

- 失败
如果进攻方在战斗中失败，他们将被送入医院15-30分钟。任何当前的连杀将被打破。

- 计时结束
一场战斗将在5分钟后自动结束，即使进攻方和防守方实际上都没有失去所有的生命。这将把攻击者送入医院，并打破他们的连杀；这相当于失去战斗。防守方不会得到任何奖励。

### 被打断

一场战斗可能因为一些原因而被 "打断"。任何这些结果都不会算作成功或不成功的攻击、僵局或防守。

- <玩家>击倒了你的对手
如果防御者正在攻击另一个<玩家>，他们可能会在攻击者能够赢得自己之前失去战斗。在这种情况下，战斗结果将显示<玩家打倒了你的对手>。

- <防御者>被<玩家>打败了
如果多个攻击者与一个防御者战斗，实际上只有其中一个可以获胜。在他们击败防御者的情况下，对于每一个没有完成最后一击的攻击者，战斗结果将显示为"<玩家>击败了<防御者>"，这将在个人统计中算作一次协助。

- <防御者被送入医院>。
有很多方法可以让玩家在被攻击时，在被攻击者击败之前被送入医院。这些方法可能包括打开一个装有小型爆炸装置的包裹，被[转盘](spin_the_wheel.md)中的莱斯利所伤，或被[有组织犯罪](organized_crime.md)所伤。

- <防御者被警察包围>。
从[21/09/21](https://www.torn.com/forums.php#/p=threads&t=16243620)起，只有有组织犯罪才会导致这一结果。

## 装备

在准备攻击时，你可以装备三种武器（主武器、副武器和近战武器）、一个临时物品（各种手榴弹和临时状态提升器）以及五件盔甲。



### 武器

所有的主武器和副武器都是需要[弹药](ammo.md)才能在战斗中使用的枪支。这意味着不仅需要重新装弹（耗费一回合），而且根据弹夹大小和射速，有可能在战斗中完全耗尽弹药。

近战武器不需要弹药，但与主武器和副武器不同的是，它们不能附加[武器模组](weapon_mod.md)，以改进武器。

[武器](weapon.md)

### 护甲

穿着盔甲可以减少来自对手的伤害；盔甲等级代表减少伤害的百分比。例如，一件等级为40.00的盔甲可以减少40%的伤害，因此1000次伤害的打击实际上只造成600次伤害。

下面的公式可以用来确定穿盔甲时受到的伤害：

`D(A) = D(I) * (1-A/100)`

其中D(I)是对手造成的**初始**伤害，A是所穿盔甲的护甲等级，D(A)是装备该盔甲后收到的结果伤害。

[盔甲](armor.md)

## 团体攻击

当多个玩家攻击一个对手时，该防御者的状态可以被有效降低。在过去30秒内，每一个额外的玩家（在第一个玩家的基础上）对一个防守者做出行动，都会给他们增加一个级别的分心。

阅读主文章，全面了解分散注意力是如何对每个攻击者进行个性化的。

[分心](distraction.md)

### 侵略

侵略性与玩家的**力量**和**速度**有关。

分心会影响防守者对攻击者进行转身的能力；每次攻击者对他们进行转身时，防守者会有 "攻击者数量中的一个 "机会进行转身。例如，如果有两名玩家攻击一名防守者，他们每次转身时，防守者将有50%的机会对他们转身。

### 压制

压制与玩家的**防御**和**灵巧**有关。

分心直接影响防御者的防御和灵巧数据；防御者的有效防御和灵巧在每一级分心的作用下都会减半。例如，如果两个玩家攻击一个拥有10,000,000防御和5,000,000灵巧的防守者，每次他们进行回合时，防守者将出现5,000,000防御和2,500,000灵巧。

## 进攻设置

攻击设置可以在你的[首选项](preference.md)中调整（或通过这里的[链接](https://www.torn.com/preferences.php#tab=attack-preferences)）。

**攻击**设置包括一个关于你的隐身偏好的选项。你可以选择 "无论何时 "和 "关闭"。此外，你可以选择是否在战斗中使用临时物品后从你的库存中重新装备，只要你拥有多个。(注意：派系借出的临时物品将首先被重新装备)虽然具体在 "攻击 "子标题下，但如果使用了临时物品，在防御后也会重新装备。

**防守**设置有效地允许玩家在防守其他玩家的攻击时决定使用哪些武器以及使用频率。有四个滑动条（主要、次要、近战和临时），可以在0和100之间调整。这些数字的作用是在防守中使用每一种武器的频率的比率--通过一个例子更好地解释。有了：

- 初级设置为100、
- 二级设置为75、
- 近战被设置为50，而
- 临时设置为25

这些数字的总和等于250--所以在防御者的每个回合，他们将有100/250的机会使用初级，75/250的机会使用次级，50/250的机会使用近战，25/250的机会使用临时物品。

如果这些槽中有一个是空的（例如，如果你解除了主武器的装备），在战斗中，你可以考虑将这个条设置为0，以便重新计算每种武器被使用的几率。当临时物品用完后，不再有临时物品装备，因此这里的设置也有效地设置为0。

主武器和副武器都有一个重装的选项（"开 "或 "关"）。如果这些武器中的任何一个有重装功能 "关闭"，当它们的弹药用完时，它们各自的栏将有效地被设置为0，如上所述。

最后，如果你已经解锁，你可以在徒手战斗时选择 "拳头 "和 "脚"。如果你没有装备任何武器，或者所有的武器设置都有效地设置为0，你就会徒手战斗。

## 相关奖章

有大量与攻击托恩有关的奖章，下面是一些例子：

<table class="wikitable table table-striped table table-striped prettyTable">
    <tbody>
        <tr>
            <th class="header" colspan="3">Attack Related Awards
            </th>
        </tr>
        <tr>
            <th class="subheader">Image
            </th>
            <th class="subheader">Name
            </th>
            <th class="subheader">Requirements
            </th>
        </tr>
        <tr>
            <td data-sort-value="Kill Streaker 1"><img src="https://awardimages.torn.com/303172651.png"
                    alt="303172651.png" /></td>
            <td>Kill Streaker 1</td>
            <td>Achieve a 10 kill streak
            </td>
        </tr>
        <tr>
            <td data-sort-value="Chainer 1"><img src="https://awardimages.torn.com/928605417.png" alt="928605417.png" />
            </td>
            <td>Chainer 1</td>
            <td>Participate in a 10 length chain
            </td>
        </tr>
        <tr>
            <td data-sort-value="Carnage"><img src="https://awardimages.torn.com/929548647.png" alt="929548647.png" />
            </td>
            <td>Carnage</td>
            <td>Make a single hit that earns your faction 10 or more respect
            </td>
        </tr>
        <tr>
            <td data-sort-value="Leonidas"><img src="https://awardimages.torn.com/890122926.png" alt="890122926.png" />
            </td>
            <td>Leonidas</td>
            <td>Achieve a finishing hit with Kick
            </td>
        </tr>
        <tr>
            <td data-sort-value="Flatline"><img src="https://awardimages.torn.com/445969768.png" alt="445969768.png" />
            </td>
            <td>Flatline</td>
            <td>Achieve a one hit kill
            </td>
        </tr>
    </tbody>
</table>

与进攻有关的所有奖项的完整列表可以在[这里](https://wiki.torn.com/wiki/Awards#Attacking)找到。

还有一些攻击奖章，如 "赢得的攻击 "和 "赢得的尊重"，可以在[这里](https://wiki.torn.com/wiki/Awards#Combat)找到。

## 历史说明

- 在一般讨论中向社区提出四项民意调查[2](#cite_note-2 ":id=cite_ref-2")[3](#cite_note-3 ":id=cite_ref-3")[4](#cite_note-4 ":id=cite_ref-4")[5](#cite_note-5 ":id=cite_ref-5")之后，抢劫的改变在19年10月29日实施。[6](#cite_note-6 ":id=cite_ref-6")

在这次修改之前，对抢劫机制的全面处理可以在[这里](https://www.torn.com/forums.php#/p=threads&f=61&t=16054187&b=0&a=0&to=19227488)找到。

## 参考文献

<div class="mw-references-wrap">
    <ol class="references">
        <li id="cite_note-1"><span class="mw-cite-backlink"><a href="#/quicklink/3.-attack/README?id=cite_ref-1">↑</a></span> <span
                class="reference-text">Chedburn, <a rel="nofollow" class="external text"
                    href="https://www.torn.com/forums.php#/p=threads&amp;t=16012377">Run away / Escape changes</a>
                (11/07/17).</span>
        </li>
        <li id="cite_note-2"><span class="mw-cite-backlink"><a href="#/quicklink/3.-attack/README?id=cite_ref-2">↑</a></span> <span
                class="reference-text">Chedburn, <a rel="nofollow" class="external text"
                    href="https://www.torn.com/forums.php#/p=threads&amp;t=16119784">Mugging changes 2019</a>
                (22/09/19).</span>
        </li>
        <li id="cite_note-3"><span class="mw-cite-backlink"><a href="#/quicklink/3.-attack/README?id=cite_ref-3">↑</a></span> <span
                class="reference-text">Chedburn, <a rel="nofollow" class="external text"
                    href="https://www.torn.com/forums.php#/p=threads&amp;t=16120171">Mugging rates 2019 - Poll #2</a>
                (24/09/19).</span>
        </li>
        <li id="cite_note-4"><span class="mw-cite-backlink"><a href="#/quicklink/3.-attack/README?id=cite_ref-4">↑</a></span> <span
                class="reference-text">Chedburn, <a rel="nofollow" class="external text"
                    href="https://www.torn.com/forums.php#/p=threads&amp;t=16121015">Mugging rates 2019 - Poll #3</a>
                (29/09/19).</span>
        </li>
        <li id="cite_note-5"><span class="mw-cite-backlink"><a href="#/quicklink/3.-attack/README?id=cite_ref-5">↑</a></span> <span
                class="reference-text">Chedburn, <a rel="nofollow" class="external text"
                    href="https://www.torn.com/forums.php#/p=threads&amp;t=16123942">Mugging rates 2019 - Poll #4</a>
                (16/10/19).</span>
        </li>
        <li id="cite_note-6"><span class="mw-cite-backlink"><a href="#/quicklink/3.-attack/README?id=cite_ref-6">↑</a></span> <span
                class="reference-text">Chedburn, <a rel="nofollow" class="external text"
                    href="https://www.torn.com/forums.php#/p=threads&amp;t=16126120">Mugging changes live</a>
                (29/10/19).</span>
        </li>
    </ol>
</div>