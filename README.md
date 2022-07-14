# P-learning

## Installation
```
git clone https://github.com/cliff0917/P-learning.git
conda create -n pl python=3.7
conda activate pl
pip install -r requirements.txt
```

## Data preparation
Download & unzip AWA2, CUB, SUN datasets from the drive link shared below to `P-learning/data/`

https://drive.google.com/drive/folders/16Xk1eFSWjQTtuQivTogMmvL3P6F_084u?usp=sharing

## Execution
The order of execution:
1. run `P_Learning.ipynb` to train our `cvae model`
2. clone https://github.com/akshitac8/tfvaegan repo & create the tfvaegan environment(or other zero-shot learning model)
3. copy our new `res101.mat` & `att_splits.mat` from `P-learning/data/$dataset/` to `tfvaegan/datesets/$dataset/` (e.g. tfvaegan/datesets/AWA2/)
4. activate tfvaegan environment & run tfvaegan with our input (e.g. `python scripts/run_awa_tfvaegan.py`)
