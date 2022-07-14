import warnings

warnings.filterwarnings('ignore')

import numpy as np
import scipy.io as sio

def b(file_path):
    attr_list_b = []
    RealCE_binary = sio.loadmat(f'{file_path}/binaryAtt_splits.mat')['att'].transpose()
    for att in RealCE_binary:
        att = np.array(att)
        attr_list_b.append(att)
    return attr_list_b, 'binaryAtt_splits.mat'

def c(file_path):
    attr_list_c = []
    attr = sio.loadmat(f'{file_path}/att_splits.mat')
    RealCE_continous = [att for att in attr['original_att'].transpose()]
    for att in RealCE_continous:
        att = np.array(att)
        attr_list_c.append(att)
    return attr_list_c, 'att_splits.mat'

def cmm(file_path):
    attr_list_cmm = []
    attr = sio.loadmat(f'{file_path}/att_splits.mat')
    RealCE_continous = [att for att in attr['original_att'].transpose()]
    for att in RealCE_continous:
        att = np.array(att)
        att = (att - np.min(att)) / (np.max(att) - np.min(att))
        attr_list_cmm.append(att)
    return attr_list_cmm, 'att_splits.mat'

def cms(file_path):
    attr_list_cms = []
    attr = sio.loadmat(f'{file_path}/att_splits.mat')
    RealCE_continous = [att for att in attr['original_att'].transpose()]
    for att in RealCE_continous:
        att = np.array(att)
        att = (att - np.mean(att)) / np.std(att)
        attr_list_cms.append(att)
    return attr_list_cms, 'att_splits.mat'