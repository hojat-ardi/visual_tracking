import os
import glob
import re
import shutil

def replace_spaces_with_commas_in_txt_files(source_dir, backup=True, delete_backup=False):
    """
    جایگزینی فاصله‌ها (اعم از فاصله‌های ساده و تب‌ها) با کاما در تمامی فایل‌های .txt موجود در فولدر مشخص‌شده.
    پس از پردازش، می‌توان فایل‌های پشتیبان را حذف کرد.

    Parameters:
    - source_dir (str): مسیر فولدری که فایل‌های .txt در آن قرار دارند.
    - backup (bool): اگر True باشد، قبل از ویرایش فایل‌ها نسخه پشتیبان با پسوند .bak ایجاد می‌شود.
    - delete_backup (bool): اگر True باشد، پس از ویرایش فایل‌ها نسخه پشتیبان حذف می‌شود.
    """
    
    # اطمینان حاصل کنید که مسیر فولدر وجود دارد
    if not os.path.isdir(source_dir):
        print(f"مسیر فولدر '{source_dir}' وجود ندارد.")
        return
    
    # یافتن تمامی فایل‌های .txt در فولدر مبدا
    txt_files = glob.glob(os.path.join(source_dir, "*.txt"))
    
    if not txt_files:
        print("هیچ فایل .txtی در فولدر مشخص‌شده یافت نشد.")
        return
    
    for file_path in txt_files:
        try:
            # ایجاد نسخه پشتیبان (اختیاری)
            if backup:
                backup_path = file_path + ".bak"
                shutil.copyfile(file_path, backup_path)
                print(f"ایجاد نسخه پشتیبان: {backup_path}")
            
            # باز کردن فایل برای خواندن
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            
            # پردازش هر خط
            new_lines = []
            for line in lines:
                # حذف فاصله‌های اضافی در ابتدا و انتهای خط
                stripped_line = line.strip()
                # جایگزینی یک یا چند فاصله با کاما
                # \s+ به معنای یک یا چند فاصله (شامل تب‌ها) است
                new_line = re.sub(r'\s+', ',', stripped_line)
                new_lines.append(new_line + '\n')  # اضافه کردن خط جدید
            
            # باز کردن فایل برای نوشتن (ویرایش)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.writelines(new_lines)
            
            print(f"ویرایش شده: {file_path}")
            
            # حذف نسخه پشتیبان (اختیاری)
            if backup and delete_backup:
                try:
                    os.remove(backup_path)
                    print(f"حذف نسخه پشتیبان: {backup_path}")
                except Exception as e:
                    print(f"خطا در حذف نسخه پشتیبان {backup_path}: {e}")
        
        except Exception as e:
            print(f"خطا در پردازش فایل {file_path}: {e}")
    
    print("تمامی فایل‌ها با موفقیت پردازش شدند.")

# مثال استفاده از تابع
if __name__ == "__main__":
    # مسیر فولدر مبدا را به دلخواه تغییر دهید
    source_directory = r'/home/ardi/Desktop/project/visual/annos/TSiamTPN'  # در سیستم‌های Unix به صورت "/home/user/MainDirectory" نوشته شود
    
    # فراخوانی تابع با حذف نسخه پشتیبان
    replace_spaces_with_commas_in_txt_files(source_directory, backup=True, delete_backup=True)
