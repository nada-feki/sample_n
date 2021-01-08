import argparse
import pandas as pd
from pathlib import Path

parser = argparse.ArgumentParser(description='Sample')

parser.add_argument('--n', type=float, default=100, help='number of lines to sample')
parser.add_argument('--input-dataset-path', type=str, required=True, help='input dataset')
parser.add_argument('--output-dataset-path', type=str, required=True, help='output dataset')

args = parser.parse_args()
df = pd.read_csv(args.input_dataset_path)

if 0 < args.n < len(df):
    df = df.sample(n=args.n)

Path(args.output_dataset_path).parent.mkdir(parents=True, exist_ok=True)
df.to_csv(args.output_dataset_path, index=False)
