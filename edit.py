import os
import shutil

# مسیر دایرکتوری مبدا و مقصد
source_dir = r'/home/ardi/Desktop/project/visual/images/S1607'  # یا "/home/user/MainDirectory" در سیستم‌های Unix
# destination_dir = r'/home/ardi/Desktop/project/toolkit/time'  # یا "/home/user/TargetDirectory"

# # ایجاد دایرکتوری مقصد در صورت عدم وجود
# if not os.path.exists(destination_dir):
#     os.makedirs(destination_dir)

# پیمایش دایرکتوری‌ها
for root, dirs, files in os.walk(source_dir):
    for file in files:
        file_lower = file.lower()
        file_path = os.path.join(root, file)
        
        # بررسی وجود عبارت 'time' در نام فایل (غیر حساس به حروف بزرگ و کوچک)
        if 'time' in file_lower:
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
        
        # بررسی وجود عبارت 'uav' در نام فایل (غیر حساس به حروف بزرگ و کوچک)
        elif '_gt' in file_lower:
            # حذف تمامی موارد 'uav' از نام فایل (بدون حساسیت به حروف بزرگ و کوچک)
            # برای حفظ حروف بزرگ و کوچک اصلی فایل، از re استفاده می‌کنیم
            import re
            new_file = re.sub(r'_gt', '', file, flags=re.IGNORECASE)
            new_file = new_file.replace("  ", " ").strip()  # حذف فاصله‌های اضافی احتمالی
            
            # مسیر جدید فایل
            new_file_path = os.path.join(root, new_file)
            
            # اطمینان از اینکه مسیر جدید تکراری نیست
            if not os.path.exists(new_file_path):
                try:
                    os.rename(file_path, new_file_path)
                    print(f"Renamed: {file_path} to {new_file_path}")
                except Exception as e:
                    print(f"Failed to rename {file_path}. Reason: {e}")
            else:
                print(f"Cannot rename {file_path} to {new_file_path} because the destination file already exists.")

print("انتقال و اصلاح فایل‌ها به پایان رسید.")
