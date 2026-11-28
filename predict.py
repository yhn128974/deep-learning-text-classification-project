from configs.data_path import data_path


def main() -> None:
    print("models_dir:", data_path.models_dir)
    print("results_dir:", data_path.results_dir)


if __name__ == "__main__":
    main()
