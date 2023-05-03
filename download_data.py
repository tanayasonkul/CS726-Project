import os
import sys
import urllib.request
import zipfile

# create the directory for storing datasets
os.makedirs("datasets", exist_ok=True)

# check if a dataset is provided as argument
if len(sys.argv) < 2:
    print("Please provide the name of the dataset to download.")
    print("Available datasets are: apple2orange, summer2winter_yosemite, horse2zebra, monet2photo, cezanne2photo, ukiyoe2photo, vangogh2photo, maps, cityscapes, facades, iphone2dslr_flower, ae_photos")
    sys.exit(1)
else:
    FILE = sys.argv[1]

# check if the provided dataset name is valid
valid_datasets = ["ae_photos", "apple2orange", "summer2winter_yosemite", "horse2zebra", "monet2photo", "cezanne2photo", "ukiyoe2photo", "vangogh2photo", "maps", "cityscapes", "facades", "iphone2dslr_flower"]
if FILE not in valid_datasets:
    print("Invalid dataset name.")
    print("Available datasets are: apple2orange, summer2winter_yosemite, horse2zebra, monet2photo, cezanne2photo, ukiyoe2photo, vangogh2photo, maps, cityscapes, facades, iphone2dslr_flower, ae_photos")
    sys.exit(1)

URL = f"https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/{FILE}.zip"
ZIP_FILE = f"./datasets/{FILE}.zip"
TARGET_DIR = f"./datasets/{FILE}/"

# download the dataset zip file
urllib.request.urlretrieve(URL, ZIP_FILE)

# extract the contents of the zip file to the target directory
with zipfile.ZipFile(ZIP_FILE, 'r') as zip_ref:
    zip_ref.extractall(TARGET_DIR)

# remove the downloaded zip file
os.remove(ZIP_FILE)
