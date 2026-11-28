from pathlib import Path
from typing import Literal
import pandas as pd
from configs.data_path import data_path

SplitName = Literal["train", "dev", "test"]


def load_dataset(split: SplitName = "train") -> pd.DataFrame:
    path_map = {
        "train": data_path.train_path,
        "dev": data_path.dev_path,
        "test": data_path.test_path,
    }

    file_path: Path = path_map[split]

    return pd.read_csv(
        file_path,
        sep="\t",
        header=None,
        names=["text", "label"],
        encoding="utf-8",
    )


def load_classes() -> list[str]:
    with data_path.class_path.open("r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def load_stopwords() -> set[str]:
    with data_path.stopwords_path.open("r", encoding="utf-8") as f:
        return {line.strip() for line in f if line.strip()}


if __name__ == "__main__":
    test_df = load_dataset("test")
    print(test_df.head())
    print("test shape:", test_df.shape)
