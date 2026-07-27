import kagglehub
from pathlib import Path


def main() -> None:
    # Download latest version of the dataset into the script's directory.
    output_dir = Path(__file__).resolve().parent / "global-superstore-dataset"
    path = kagglehub.dataset_download(
        "fatihilhan/global-superstore-dataset",
        output_dir=str(output_dir),
    )
    print("Path to dataset files:", path)


if __name__ == "__main__":
    main()