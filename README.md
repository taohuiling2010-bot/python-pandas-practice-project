# Python 数据分析实战项目

> 基于 Python 爬虫 + Pandas 数据处理 + Matplotlib 可视化的端到端数据分析项目，
> 演示从数据采集、清洗、统计分析到可视化的完整工作流。

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-blue)

---

## 📌 项目定位

本项目作为**数据分析能力练习项目**，重点展示以下技术能力：

- **数据采集**：使用 requests + lxml.etree 实现网页数据爬取与 HTML 解析
- **数据清洗**：使用 Pandas 进行缺失值处理、异常值剔除、字段标准化
- **统计分析**：独热编码、分组聚合、相关性分析、分布特征挖掘
- **数据可视化**：使用 Matplotlib 制作多维度图表，呈现数据规律

数据题材选择豆瓣电影 Top250 是出于**数据获取的合规性**与**字段维度的丰富性**考虑，
本项目所演示的数据处理方法可迁移至任何业务场景的数据分析工作。

---

## 🛠️ 技术栈

| 阶段 | 工具 |
|---|---|
| 数据采集 | Python（requests, lxml.etree） |
| 数据存储 | Excel（.xlsx） |
| 数据处理 | Pandas、NumPy |
| 数据可视化 | Matplotlib |
| 开发环境 | Jupyter Notebook |

---

## 📂 仓库结构

    .
    ├── README.md                       本文件
    ├── 项目说明.md                      详细项目文档
    ├── 01_爬虫代码.py                   网页数据爬取脚本
    ├── 02_数据分析代码.ipynb             数据分析与可视化（Jupyter Notebook）
    ├── 03_数据/
    │   └── 豆瓣Top250数据.xlsx           爬取后的结构化数据
    └── 04_可视化分析报告.pdf             分析结果可视化输出
---

## 🎯 核心工作

1. **数据采集**：使用 Python 爬虫获取 250 部电影的 2238 条核心数据，实现非结构化数据的结构化采集与格式化存储
2. **数据清洗**：用 Pandas 完成缺失值处理、异常值剔除、字段标准化，保障数据质量
3. **统计分析**：对电影类型、年份、国家等维度做独热编码与统计分析，挖掘数据分布特征
4. **可视化**：通过 Matplotlib 制作多维度可视化图表，计算指标间相关系数，挖掘数据关联规律

---

## 💡 核心成果

- 掌握 Python 网络爬虫与非结构化数据处理的实操方法，实现数据的精准采集与格式化
- 熟练运用 Pandas、Matplotlib 完成数据清洗、统计分析与可视化
- 学会通过统计分析挖掘数据间的关联规律，形成"数据采集→分析"的完整实操闭环

---

## 🚀 快速浏览

**如果你只有 30 秒**：直接查看 [04_可视化分析报告.pdf](04_可视化分析报告.pdf)

**如果你想看代码逻辑**：直接点击 [02_数据分析代码.ipynb](02_数据分析代码.ipynb)，
GitHub 会渲染完整的代码 + 输出 + 图表

**如果你想了解项目细节**：阅读 [项目说明.md](项目说明.md)

---

## ⚠️ 数据说明

本项目数据通过公开网页采集，仅用于**个人学习与求职作品展示**，不涉及任何商业用途。
所有数据未经过任何加工修改，原始来源为豆瓣电影 Top250 公开榜单。

---

## 📮 联系方式

- **作者**：陶惠灵
- **邮箱**：taohuiling2010@gmail.com
- **GitHub**：[@taohuiling2010-bot](https://github.com/taohuiling2010-bot)

如对项目有任何疑问或建议，欢迎通过 Issue 或邮件联系。
