from configs.data_path import data_path
from src.data.loader import load_classes, load_dataset


def main() -> None:
    data_path.ensure_dirs()
    classes = load_classes()
    test_df = load_dataset("test")
    print("train_path:", data_path.train_path)
    print("classes:", classes)
    print("test sample shape:", test_df.shape)


if __name__ == "__main__":
    main()
