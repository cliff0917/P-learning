# P-learning(with custom dataset)

## Installation
```
git clone https://github.com/cliff0917/P-learning.git
conda create -n pl python=3.7
conda activate pl
pip install -r requirements.txt
```

## Data preparation
Download & unzip plant dataset from the drive link shared below to `P-learning/data/`

https://drive.google.com/drive/folders/1H3XxMuVjJaLFQ1asAxrDWxPpV-fSV7Fh?usp=sharing

## Execution
The order of execution:
1. run `Make_2048Features&Attr.ipynb` to get ft & attr of dataset
2. run `P_Learning.ipynb` to get our `cvae model`
3. `resnet101` and `cvae model` will generate `res101.mat` & `att_splits.mat` separately (the input of tfvaegan)
4. clone https://github.com/akshitac8/tfvaegan repo & create the tfvaegan environment
5. copy `res101.mat` & `att_splits.mat` from `P-learning/data/$dataset/mat/$attr_type/` to `tfvaegan/datesets/$dataset/` (e.g. tfvaegan/datesets/AWA2/)
6. activate tfvaegan environment & run tfvaegan with our input (e.g. `python scripts/run_awa_tfvaegan.py`)
