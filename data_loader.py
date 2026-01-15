import pandas as pd


QMSUM_URLS = {
    "train": "https://huggingface.co/datasets/pszemraj/qmsum-cleaned/resolve/main/data/train-00000-of-00001.parquet",
    "validation": "https://huggingface.co/datasets/pszemraj/qmsum-cleaned/resolve/main/data/validation-00000-of-00001.parquet",
    "test": "https://huggingface.co/datasets/pszemraj/qmsum-cleaned/resolve/main/data/test-00000-of-00001.parquet",
}


def load_qmsum(split="train"):
    """
    Load QMSum cleaned dataset directly from HuggingFace.

    split: 'train' | 'validation' | 'test'
    """
    if split not in QMSUM_URLS:
        raise ValueError(f"Invalid split: {split}")

    return pd.read_parquet(
        QMSUM_URLS[split], engine="pyarrow"
    )
