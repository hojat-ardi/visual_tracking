import os
import shutil

# داده‌ها به صورت لیستی از دیکشنری‌ها
data = [
    {"name": "uav_car1_2", "path": "/home/ardi/Desktop/project/visual/images/car1", "startFrame": 751, "endFrame": 1627},
    {"name": "uav_car1_1", "path": "/home/ardi/Desktop/project/visual/images/car1", "startFrame": 1, "endFrame": 751},
    {"name": "uav_uav1_1", "path": "/home/ardi/Desktop/project/visual/images/uav1", "startFrame": 1, "endFrame": 1555},
    {"name": "uav_group3_4", "path": "/home/ardi/Desktop/project/visual/images/group3", "startFrame": 4369, "endFrame": 5527},
    {"name": "uav_person14_1", "path": "/home/ardi/Desktop/project/visual/images/person14", "startFrame": 1, "endFrame": 847},
    {"name": "uav_person19_2", "path": "/home/ardi/Desktop/project/visual/images/person19", "startFrame": 1243, "endFrame": 2791},
    {"name": "uav_person19_3", "path": "/home/ardi/Desktop/project/visual/images/person19", "startFrame": 2791, "endFrame": 4357},
    {"name": "uav_car15", "path": "/home/ardi/Desktop/project/visual/images/car15", "startFrame": 1, "endFrame": 469,},
    {"name": "uav_car9", "path": "/home/ardi/Desktop/project/visual/images/car9", "startFrame": 1, "endFrame": 1879},
    {"name": "uav_uav2", "path": "/home/ardi/Desktop/project/visual/images/uav2", "startFrame": 1, "endFrame": 133},
    {"name": "uav_uav5", "path": "/home/ardi/Desktop/project/visual/images/uav5", "startFrame": 1, "endFrame": 139},
    {"name": "uav_car1_s", "path": "/home/ardi/Desktop/project/visual/images/car1_s", "startFrame": 1, "endFrame": 1475},
    {"name": "uav_person10", "path": "/home/ardi/Desktop/project/visual/images/person10", "startFrame": 1, "endFrame": 1021},
    {"name": "uav_person9", "path": "/home/ardi/Desktop/project/visual/images/person9", "startFrame": 1, "endFrame": 661},
    {"name": "uav_wakeboard6", "path": "/home/ardi/Desktop/project/visual/images/wakeboard6", "startFrame": 1, "endFrame": 1165}

]

# مسیر دایرکتوری مقصد برای ذخیره زیرپوشه‌ها
output_directory = "/home/ardi/Desktop/project/visual/processed_images"

# ایجاد دایرکتوری مقصد اگر وجود ندارد
os.makedirs(output_directory, exist_ok=True)

for entry in data:
    source_path = entry["path"]
    destination_folder = os.path.join(output_directory, entry["name"])
    
    # ایجاد زیرپوشه برای هر نام
    os.makedirs(destination_folder, exist_ok=True)
    
    # پیمایش شماره فریم‌ها
    for frame_number in range(entry["startFrame"], entry["endFrame"] + 1):
        # فرمت پیش‌فرض نام فایل‌ها (6 رقم)
        file_name = f"{frame_number:06d}.jpg"  # به عنوان مثال: 000001.jpg
        source_file = os.path.join(source_path, file_name)
        destination_file = os.path.join(destination_folder, file_name)
        
        # بررسی وجود فایل و کپی آن
        if os.path.exists(source_file):
            shutil.copy(source_file, destination_file)
            print(f"Copied: {source_file} -> {destination_file}")
        else:
            print(f"File not found: {source_file}")

print("Done!")
