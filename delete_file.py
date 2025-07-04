import os

# لیست فایل‌هایی که باید حفظ شوند
files_to_keep = {
    "uav_car1_2.txt",
    "uav_car1_s.txt",
    "uav_car9.txt",
    "uav_car15.txt",
    "uav_group2_1.txt",
    "uav_uav1_1.txt",
    "uav_uav2.txt",
    "uav_uav5.txt",
    "uav_person9.txt",
    "uav_wakeboard6.txt",
    "uav_person19_2.txt",
    "uav_person19_3.txt",
    "uav_person14_1.txt",
    "uav_person10.txt",
    "uav_group3_4.txt"
    }

# مسیر دایرکتوری اصلی
root_directory = "/home/ardi/Desktop/project/visual/annos"

# پیمایش تمامی پوشه‌ها و فایل‌ها
for subdir, _, files in os.walk(root_directory):
    for file_name in files:
        file_path = os.path.join(subdir, file_name)
        
        # بررسی اینکه فایل در لیست فایل‌های مجاز هست یا خیر
        if file_name not in files_to_keep:
            # حذف فایل
            os.remove(file_path)
            print(f"Deleted: {file_path}")

print("Done!")
