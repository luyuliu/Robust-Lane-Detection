from torch.utils.data import Dataset
from PIL import Image
import torch
import config
import torchvision.transforms as transforms
import numpy as np
from sklearn import preprocessing
import glob

def readTxt(file_path):
    img_list = []
    with open(file_path, 'r') as file_to_read:
        while True:
            lines = file_to_read.readline()
            if not lines:
                break
            item = lines.strip().split()
            img_list.append(item)
    file_to_read.close()
    return img_list

class RoadSequenceDataset(Dataset):

    def __init__(self, file_path, transforms):

        self.img_list = glob.glob(file_path + "/*.jpg")
        self.dataset_size = len(self.img_list)
        self.transforms = transforms
    def __len__(self):
        return self.dataset_size

    def __getitem__(self, idx):
        img_path_list = self.img_list[idx]
        data = Image.open(img_path_list[4])
        label = Image.open(img_path_list[5])
        data = self.transforms(data)
        label = torch.squeeze(self.transforms(label))
        sample = {'data': data, 'label': label}
        return sample

class RoadSequenceDatasetList(Dataset):

    def __init__(self, file_path, transforms):

        self.img_list = glob.glob(file_path + "/*.jpg")
        print(len(self.img_list))
        self.dataset_size = len(self.img_list)
        self.transforms = transforms
    def __len__(self):
        return self.dataset_size

    def __getitem__(self, idx):
        img_path_list = self.img_list[idx]
        data = []
        data.append(torch.unsqueeze(self.transforms(Image.open(img_path_list)), dim=0))
        data = torch.cat(data, 0)
        sample = {'data': data}
        return sample


