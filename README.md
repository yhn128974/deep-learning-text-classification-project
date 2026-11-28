# Deep Learning Text Classification Project

中文文本分类深度学习项目。

## 目录结构

```text
deep-learning-text-classification-project/
├── .gitignore
├── .vscode/
│   └── settings.json      # 指定 dl_project Conda 解释器与 PYTHONPATH
├── configs/               # 路径与超参数配置
│   ├── __init__.py
│   └── data_path.py
├── data/
│   ├── raw/               # 原始只读数据集（train/dev/test/class/stopwords）
│   └── processed/         # 预处理后的中间数据（Git 忽略）
├── src/                   # 核心源码包
│   ├── data/              # 数据加载与预处理
│   ├── models/            # 模型定义（如 RF / FastText / BERT）
│   └── utils/             # 通用工具函数
├── outputs/
│   ├── models/            # 训练保存的模型权重（Git 忽略）
│   └── results/           # 预测结果与评估输出（Git 忽略）
├── train.py               # 训练入口
├── predict.py             # 推理入口
└── README.md
```

## 运行方式

激活 `dl_project` 环境（或直接使用环境解释器）在项目根目录运行：

```bash
conda activate dl_project
python train.py
python -m src.data.loader
python predict.py
```
