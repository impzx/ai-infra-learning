# AI Infra 日知录 · 配套代码

[AI Infra 日知录](https://impzx.github.io/series/ai-infra/)的实验与示例代码，按子系列和文章编号组织。

## 模型架构基础

沿着架构演进、训练方法和推理落地展开。完整文章规划见[系列导读](https://impzx.github.io/posts/model-architecture-roadmap/)。

| 编号 | 主题 | 代码与说明 | 文章状态 |
| --- | --- | --- | --- |
| 01 | 语言模型究竟在学什么 | [实验目录](model-architecture/01-language-model/) | 本地初稿，待发布 |

## 快速开始

第一篇仅依赖 Python 3 标准库，无需 GPU，无需下载数据。

```bash
python3 model-architecture/01-language-model/experiment.py
```

已在 Python 3.12.3 下验证。输出见对应实验目录的 `expected-output.txt`。

## 目录约定

```text
model-architecture/
  01-language-model/
    README.md
    experiment.py
    expected-output.txt
```

后续文章使用 `编号-英文主题` 的目录名；每篇独立记录运行命令、依赖版本、数据来源、硬件需求、结果与限制。第三方数据和模型权重不直接存入仓库。目录只收录已经准备好的实验，未完成的计划在博客导读中维护。

## 实验记录

简化实现用于理解机制，不等同于复现完整论文。涉及随机训练时记录种子、数据划分与训练配置；涉及性能比较时记录精度、软硬件环境、预热和同步方式。
