import pandas as pd 
import os
import shutil
import random
file_path="chest_xray\metadata.csv"
images_path="chest_xray\images"
df=pd.read_csv(file_path)
print(df.shape)
target_dir="Dataset\Covid"
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print("Covid folder created")
cnt =0
for (i,row) in df.iterrows():
    if row["finding"]=="Pneumonia/Viral/COVID-19" and row["view"]=="PA":
        filename=row["filename"]
        image_path=os.path.join(images_path,filename)
        image_copy_path=os.path.join(target_dir,filename)
        shutil.copy2(image_path,image_copy_path)
        cnt+=1
print(cnt)
kaggle_file_path="chest_xray_kaggle\train\normal"
target_normal_dir="Dataset\normal"
image_names=os.listdir(kaggle_file_path)
random.shuffle(image_names)
for i in range(205):
    image_name=image_names[i]
    image_path=os.path.join(kaggle_file_path,image_name)
    image_copy_path=os.path.join(target_normal_dir,image_name)
    shutil.copy2(image_path,image_copy_path)

