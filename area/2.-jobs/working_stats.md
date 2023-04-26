# 工作数值

## 基本信息
要加入Torn City[工作](README.md)或玩家经营的[公司](company.md)，你必须达到一定的工作状态。


有三个类别：

- **体力劳动(MAN)**
- **智力(INT)**
- **耐力(END)**

一些撕裂的城市[工作](README.md)需要特定数量的三种工作状态才能加入。

- 军队、杂货店和赌场的工作可以在你来到托恩的第一天开始。
- 教育、医疗和法律方面的工作都需要你在被雇佣前获得一些工作状态。

有关托恩市工作状态要求的详情，请参见[工作](README.md)。

[公司](company.md)只要求三个工作状态中的两个，也被称为主要工作状态和次要工作状态。这些数据是用来计算你受雇时的效率。

计算效率（你的工作状态与职位要求相比）的公式是[[1]](https://www.torn.com/forums.php#/p=threads&t=16227240)

```
$efficiency = FLOOR(MIN(45, (45 / $required) * $stat) + MAX(0, (5 * LOG($stat / $required, 2))))
```


## 增加工作统计的方法
**每天从工作和公司获得的间接收益**

当你在撕裂的城市[工作](README.md)时，你会根据你的等级和工作获得不同数量的体力、智力和耐力。


公司主管根据他们公司的星级获得收益，在1\*时他们每天获得5个工作状态，在2\*时获得10个，在3\*时获得20个，在4\*时获得35个，在5\*或以上的公司，每天获得50个。


作为一个玩家经营的公司的**雇员**，你每天根据你的效率获得主要和次要的工作状态。效率是基于你的工作状态与职位要求的接近程度。你获得的工作状态与公司职位要求的工作状态相同。


公司工作状态的获得和要求是在报纸的工作列表页上，如下图所示：

<table class="wikitable table table-striped table table-striped"
    style="font-size: 1.0em; background: #000000; color:white">
    <tbody>
        <tr>
            <th>Oil Rig Ranks</th>
            <th></th>
            <th></th>
            <th>
            </th>
        </tr>
        <tr style="text-align: center; font-size: 1.0em; background: #000000; color:white">
            <td>Positions</td>
            <td>Primary requirement</td>
            <td>Secondary requirement</td>
            <td>Passive daily stat gain
            </td>
        </tr>
        <tr style="background: white; color:black">
            <td>Driller</td>
            <td>Primary Stat: 150,000 MAN</td>
            <td>Secondary Stat: 75,000 INT</td>
            <td>Stat Gain: 70 MAN / 35 INT
            </td>
        </tr>
        <tr style="background: white; color:black">
            <td>Roughneck</td>
            <td>Primary Stat: 75,000 MAN</td>
            <td>Secondary Stat: 37,500 END</td>
            <td>Stat Gain: 65 MAN / 33 END
            </td>
        </tr>
        <tr style="background: white; color:black">
            <td>Derrick Hand</td>
            <td>Primary Stat: 94,000 MAN</td>
            <td>Secondary Stat: 47,000 END</td>
            <td>Stat Gain: 67 MAN &amp; 34 END
            </td>
        </tr>
        <tr style="background: white; color:black">
            <td>Secretary</td>
            <td>Primary Stat: 112,500 END</td>
            <td>Secondary Stat: 56,250 INT</td>
            <td>Stat Gain: 68 END &amp; 34 INT
            </td>
        </tr>
        <tr style="background: white; color:black">
            <td>Inspector</td>
            <td>Primary Stat: 225,000 INT</td>
            <td>Secondary Stat: 112,500 END</td>
            <td>Stat Gain: 74 INT &amp; 37 END
            </td>
        </tr>
        <tr style="background: white; color:black">
            <td>Sales Executive</td>
            <td>Primary Stat: 131,500 INT</td>
            <td>Secondary Stat: 65,750 END</td>
            <td>Stat Gain: 69 INT &amp; 35 END
            </td>
        </tr>
        <tr style="background: white; color:black">
            <td>Motor Hand</td>
            <td>Primary Stat: 112,500 MAN</td>
            <td>Secondary Stat: 56,250 INT</td>
            <td>Stat Gain: 68 MAN &amp; 34 INT
            </td>
        </tr>
    </tbody>
</table>

**来自公司的董事培训**

作为玩家经营的公司的员工，你每天最多可以接受二十（20）次董事培训。公司每天都会增加培训，速度为每一星等级一个培训。一个公司最多可以容纳20辆火车。如果你有能力与董事协商，以这种方式培训你，这是提高你工作状态的**最快方法**。


根据职位的要求，每个主任的培训总是给你**50个初级和25个二级工作状态**。这与你在工作中的效率无关。这使得他们非常适合那些几乎没有工作状态的玩家，不像被动的工作状态收益。[实例图片](https://i.gyazo.com/7c72fc50e92807ac8b5a1d8b7dfd155e.png)

*重要提示：董事只能培训他们的员工，如果不放弃对公司的控制权，就不能培训自己。*


**其他公司工作的特殊性**

有两家公司可以只增加你的耐力工作状态。

<table class="wikitable table table-striped table table-striped">
    <tbody>
        <tr>
            <th colspan="10" style="font-size: 1.2em; background: #CEDFF2;">Clothing Store Specials
            </th>
        </tr>
        <tr align="center">
            <th>Stars</th>
            <th>Special Name</th>
            <th>Cost (Job Points)</th>
            <th>Effect
            </th>
        </tr>
        <tr align="center">
            <td>3</td>
            <td>Nine to five</td>
            <td>10</td>
            <td>+ 100 Endurance
            </td>
        </tr>
    </tbody>
</table>

<table class="wikitable table table-striped table table-striped">
    <tbody>
        <tr>
            <th colspan="10" style="font-size: 1.2em; background: #CEDFF2;">Lingerie Store Specials
            </th>
        </tr>
        <tr align="center">
            <th>Stars</th>
            <th>Special Name</th>
            <th>Cost (Job Points)</th>
            <th>Effect
            </th>
        </tr>
        <tr align="center">
            <td>3</td>
            <td>Nine to five</td>
            <td>10</td>
            <td>+ 100 Endurance
            </td>
        </tr>
    </tbody>
</table>

**撕裂的城市工作 - 教育**

教育工作可以获得三个工作的特殊性：

- 每10点工作点数可增加100点体力
- 每10点工作点数+100智力
- 每10个工作点+100个耐力

在教育学的**首席**等级中，你可以获得7个工作点数，或者每天最多可获得+70手动、+70智力或+70耐力的收益。


**读书**工作9至5：完成后所有工作状态增加5%，每项增加2500。在完成这本书时，你的每项工作属性应达到50,000，以获得工作属性的最高提升。


**完成教育课程**
大多数教育课程在工作状态方面都有小幅提升。最大的收益在下表中显示。长度是指在不减少时间的情况下完成一个课程所需的时间（周）。效率是指获得的工作状态的总和除以获得这些状态所需的周数。因此，一周内提供100个数据的课程比四周内提供150个数据的课程效率更高。介绍性课程是指；所有其他课程都有一个先决条件，必须首先满足。

<table class="wikitable table table-striped table table-striped">
    <tbody>
        <tr>
            <th>Course No
            </th>
            <th>Intro Course?
            </th>
            <th>MAN
            </th>
            <th>INT
            </th>
            <th>END
            </th>
            <th>TOTAL
            </th>
            <th>LENGTH
            </th>
            <th>EFFICIENCY
            </th>
        </tr>
        <tr>
            <td>DEF 1700</td>
            <td>Yes</td>
            <td>50</td>
            <td>50</td>
            <td>50</td>
            <td>150</td>
            <td>1</td>
            <td>150
            </td>
        </tr>
        <tr>
            <td>BIO 2390</td>
            <td></td>
            <td>5</td>
            <td>170</td>
            <td>120</td>
            <td>295</td>
            <td>2</td>
            <td>148
            </td>
        </tr>
        <tr>
            <td>CMT 2590</td>
            <td></td>
            <td>0</td>
            <td>250</td>
            <td>30</td>
            <td>280</td>
            <td>2</td>
            <td>140
            </td>
        </tr>
        <tr>
            <td>CMT 2570</td>
            <td></td>
            <td>0</td>
            <td>150</td>
            <td>95</td>
            <td>245</td>
            <td>2</td>
            <td>123
            </td>
        </tr>
        <tr>
            <td>HIS 2150</td>
            <td></td>
            <td>15</td>
            <td>135</td>
            <td>75</td>
            <td>225</td>
            <td>2</td>
            <td>113
            </td>
        </tr>
        <tr>
            <td>CMT 2600</td>
            <td></td>
            <td>0</td>
            <td>275</td>
            <td>55</td>
            <td>330</td>
            <td>3</td>
            <td>110
            </td>
        </tr>
        <tr>
            <td>LAW 2101</td>
            <td></td>
            <td>0</td>
            <td>175</td>
            <td>40</td>
            <td>215</td>
            <td>2</td>
            <td>108
            </td>
        </tr>
        <tr>
            <td>CBT 1780</td>
            <td>Yes</td>
            <td>50</td>
            <td>50</td>
            <td>0</td>
            <td>100</td>
            <td>1</td>
            <td>100
            </td>
        </tr>
        <tr>
            <td>CMT 1520</td>
            <td>Yes</td>
            <td>0</td>
            <td>45</td>
            <td>50</td>
            <td>95</td>
            <td>1</td>
            <td>95
            </td>
        </tr>
        <tr>
            <td>GEN 1114</td>
            <td>Yes</td>
            <td>0</td>
            <td>75</td>
            <td>15</td>
            <td>90</td>
            <td>1</td>
            <td>90
            </td>
        </tr>
        <tr>
            <td>HAF 1103</td>
            <td>Yes</td>
            <td>75</td>
            <td>0</td>
            <td>15</td>
            <td>90</td>
            <td>1</td>
            <td>90
            </td>
        </tr>
        <tr>
            <td>MTH 2270</td>
            <td></td>
            <td>0</td>
            <td>165</td>
            <td>15</td>
            <td>180</td>
            <td>2</td>
            <td>90
            </td>
        </tr>
    </tbody>
</table>