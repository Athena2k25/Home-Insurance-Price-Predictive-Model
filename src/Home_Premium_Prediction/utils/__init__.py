import os
import yaml
import pandas as pd
from pathlib import Path
from ensure import ensure_annotations



@ensure_annotations
def read_yaml(path_to_yaml: Path):
    """
    Reads a yaml file and returns a ConfigBox object.
    """
    try:
        with open(path_to_yaml, mode= "r") as yaml_file:
             content= yaml.safe_load(yaml_file)
             return content
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create directories
    """
    for directory in path_to_directories:
        os.makedirs(directory, exist_ok=True)
        if verbose:
            print(f"created directory at: {directory}")

@ensure_annotations
def frequency_encode_column(X):
    """Assumes X is a 2D array with one column"""
    if isinstance(X, pd.DataFrame):
        col = X.iloc[:, 0]
    else:
        col = pd.Series(X.ravel())

    freq = col.value_counts(normalize=True)
    encoded = col.map(freq).fillna(0).values.reshape(-1, 1)
    return encoded