from pathlib import Path
from threading import Lock
from typing import Optional

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
OUTPUTS_DIR = BASE_DIR / "outputs"
MODELS_DIR = OUTPUTS_DIR / "models"
RESULTS_DIR = OUTPUTS_DIR / "results"


class DataPath:
    _instance: Optional["DataPath"] = None
    _lock: Lock = Lock()

    def __new__(cls) -> "DataPath":
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if getattr(self, "_initialized", False):
            return
        with self._lock:
            if getattr(self, "_initialized", False):
                return
            self.base_dir = BASE_DIR
            self.data_dir = DATA_DIR
            self.raw_data_dir = RAW_DATA_DIR
            self.processed_data_dir = PROCESSED_DATA_DIR
            self.outputs_dir = OUTPUTS_DIR
            self.models_dir = MODELS_DIR
            self.results_dir = RESULTS_DIR

            self.train_path = RAW_DATA_DIR / "train.txt"
            self.dev_path = RAW_DATA_DIR / "dev.txt"
            self.test_path = RAW_DATA_DIR / "test.txt"
            self.class_path = RAW_DATA_DIR / "class.txt"
            self.stopwords_path = RAW_DATA_DIR / "stopwords.txt"
            self._initialized = True

    def ensure_dirs(self) -> None:
        for directory in (self.processed_data_dir, self.models_dir, self.results_dir):
            directory.mkdir(parents=True, exist_ok=True)


data_path = DataPath()


if __name__ == "__main__":
    print("base_dir:", data_path.base_dir)
    print("train_path:", data_path.train_path)
    print("dev_path:", data_path.dev_path)
    print("test_path:", data_path.test_path)
    print("class_path:", data_path.class_path)
    print("stopwords_path:", data_path.stopwords_path)
