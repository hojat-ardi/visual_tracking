import os
import cv2

# داده‌ها
data = [
    # {"name": "car1_2", "path": "/home/ardi/Desktop/project/visual/images/car1", "startFrame": 751, "endFrame": 1627},
    # {"name": "uav1_1", "path": "/home/ardi/Desktop/project/visual/images/uav1", "startFrame": 1, "endFrame": 1555},
    # {"name": "group3_4", "path": "/home/ardi/Desktop/project/visual/images/group3", "startFrame": 4369, "endFrame": 5527},
    # {"name": "person14_1", "path": "/home/ardi/Desktop/project/visual/images/person14", "startFrame": 1, "endFrame": 847},
    # {"name": "person19_2", "path": "/home/ardi/Desktop/project/visual/images/person19", "startFrame": 1243, "endFrame": 2791},
    # {"name": "person19_3", "path": "/home/ardi/Desktop/project/visual/images/person19", "startFrame": 2791, "endFrame": 4357},
    # {"name": "car15", "path": "/home/ardi/Desktop/project/visual/images/car15", "startFrame": 1, "endFrame": 469},
    # {"name": "car9", "path": "/home/ardi/Desktop/project/visual/images/car9", "startFrame": 1, "endFrame": 1879},
    # {"name": "uav2", "path": "/home/ardi/Desktop/project/visual/images/uav2", "startFrame": 1, "endFrame": 133},
    # {"name": "uav5", "path": "/home/ardi/Desktop/project/visual/images/uav5", "startFrame": 1, "endFrame": 139},
    # {"name": "car1_s", "path": "/home/ardi/Desktop/project/visual/images/car1_s", "startFrame": 1, "endFrame": 1475},
    # {"name": "person10", "path": "/home/ardi/Desktop/project/visual/images/person10", "startFrame": 1, "endFrame": 1021},
    # {"name": "person9", "path": "/home/ardi/Desktop/project/visual/images/person9", "startFrame": 1, "endFrame": 661},
    # {"name": "wakeboard6", "path": "/home/ardi/Desktop/project/visual/images/wakeboard6", "startFrame": 1, "endFrame": 1165},
    # {"name": "group2_1", "path": "/home/ardi/Desktop/project/visual/images/group2", "startFrame": 1, "endFrame": 907},
    # {"name": "wakeboard5", "path": "/home/ardi/Desktop/project/visual/images/wakeboard5", "startFrame": 1, "endFrame": 1675},
    # {"name": "couple", "path": "/home/ardi/Desktop/project/visual/images/couple", "startFrame": 1, "endFrame": 1826},
    # {"name": "duck1_2", "path": "/home/ardi/Desktop/project/visual/images/duck1_2", "startFrame": 1, "endFrame": 1551},
    # {"name": "vanet", "path": "/home/ardi/Desktop/project/demo/frame_3", "startFrame": 1, "endFrame": 393},
    # {"name": "neysan", "path": "/home/ardi/Desktop/project/demo/frame_6", "startFrame": 1, "endFrame": 740},
    # {"name": "person", "path": "/home/ardi/Desktop/project/demo/frame_2", "startFrame": 1, "endFrame": 850},
    # {"name": "bike9_1", "path": "/home/ardi/Desktop/dataset/UAVTrack112/data_seq/bike9_1", "startFrame": 1, "endFrame": 401},
    # {"name": "group3_2", "path": "/home/ardi/Desktop/dataset/UAVTrack112/data_seq/group3_2", "startFrame": 1, "endFrame": 250},
    # {"name": "tower_crane", "path": "/home/ardi/Desktop/dataset/UAVTrack112/data_seq/tower_crane", "startFrame": 1, "endFrame": 886},
    # {"name": "S1304", "path": "/home/ardi/Desktop/dataset/uavdt/sot/sequences/S1304", "startFrame": 1, "endFrame": 519},
    # {"name": "car5", "path": "/home/ardi/Desktop/dataset/UAV123/data_seq/UAV123/car5", "startFrame": 1, "endFrame": 745},
    # {"name": "S0303", "path": "/home/ardi/Desktop/dataset/uavdt/sot/sequences/S0303", "startFrame": 1, "endFrame": 110},


]

# مسیر اصلی شامل پوشه‌های مدل‌ها
models_directory = "/home/ardi/Desktop/anno"
# مسیر خروجی برای تصاویر ترکیبی
output_directory = "/home/ardi/Desktop/project/visual/real"
os.makedirs(output_directory, exist_ok=True)

# تنظیم رنگ‌های واضح و قابل تشخیص برای مدل‌ها
# این لیست شامل رنگ‌های با کنتراست بالا و تفاوت‌های رنگی واضح است
colors = [
    (0, 255, 0),       # سبز
    # (0, 0, 255),       # آبی
    # (255, 0, 0),       # قرمز
    # (255, 255, 0),     # زرد
    # (255, 0, 255),     # ارغوانی
    # (0, 255, 255),     # فیروزه‌ای
    # (255, 165, 0),     # نارنجی
    # (128, 0, 128),     # بنفش
    # (0, 128, 0),       # سبز تیره
    # (128, 128, 0),     # زیتونی
    # (0, 128, 128),     # فیروزه‌ای تیره
    # (128, 0, 0),       # قرمز تیره
    # (0, 0, 128),       # آبی تیره
    # (128, 128, 128),   # خاکستری
    # (0, 255, 127),     # اسپرسو
    # (255, 20, 147),    # صورتی عمیق
    # (75, 0, 130)        # ایندیگو
]

# بررسی تعداد مدل‌ها با رنگ‌های موجود
model_folders = sorted(os.listdir(models_directory))
num_models = len(model_folders)
if num_models > len(colors):
    raise ValueError(f"Not enough distinct colors for {num_models} models. Please extend the colors list.")

# ایجاد یک دیکشنری برای نگهداری رنگ هر مدل
model_color_map = {model: colors[i] for i, model in enumerate(model_folders)}

# پردازش هر دنباله
for entry in data:
    sequence_name = entry["name"]
    image_folder = entry["path"]
    start_frame = entry["startFrame"]
    end_frame = entry["endFrame"]

    # ایجاد پوشه خروجی برای این دنباله
    sequence_output_folder = os.path.join(output_directory, sequence_name)
    os.makedirs(sequence_output_folder, exist_ok=True)
    
    # پیمایش فریم‌ها
    for frame_idx in range(start_frame, end_frame + 1):
        # تلاش برای پیدا کردن نام فایل با 6 رقم
        frame_name_6 = f"img{frame_idx:06d}.jpg"
        image_path_6 = os.path.join(image_folder, frame_name_6)
        
        # اگر فایل با 6 رقم وجود ندارد، تلاش برای پیدا کردن با 5 رقم
        if os.path.exists(image_path_6):
            frame_name = frame_name_6
            image_path = image_path_6
        else:
            frame_name_5 = f"img{frame_idx:05d}.jpg"
            image_path_5 = os.path.join(image_folder, frame_name_5)
            if os.path.exists(image_path_5):
                frame_name = frame_name_5
                image_path = image_path_5
            else:
                print(f"Image not found for frame {frame_idx}: {image_folder}/{{5 or 6 digit}}.jpg")
                continue
        
        output_path = os.path.join(sequence_output_folder, frame_name)
        
        # خواندن تصویر
        image = cv2.imread(image_path)
        if image is None:
            print(f"Failed to read image: {image_path}")
            continue
        
        # پیمایش مدل‌ها
        for model_folder in model_folders:
            color = model_color_map[model_folder]
            model_txt_file = os.path.join(models_directory, model_folder, f"{sequence_name}_gt.txt")
            
            # بررسی وجود فایل txt
            if not os.path.exists(model_txt_file):
                print(f"Bounding box file not found for model {model_folder}: {model_txt_file}")
                continue
            
            # خواندن فایل txt
            with open(model_txt_file, "r") as f:
                bounding_boxes = f.readlines()
            
            # محاسبه ایندکس فریم نسبت به شروع
            frame_relative_idx = frame_idx - start_frame
            if frame_relative_idx < 0 or frame_relative_idx >= len(bounding_boxes):
                print(f"Frame index {frame_idx} out of range for {sequence_name} in model {model_folder}")
                continue
            
            # گرفتن باندینگ باکس مربوط به این فریم
            bbox = bounding_boxes[frame_relative_idx].strip().split(",")
            if len(bbox) != 4:
                print(f"Invalid bounding box format in {model_txt_file} at line {frame_relative_idx + 1}")
                continue
            
            try:
                x, y, w, h = map(float, bbox)
            except ValueError:
                print(f"Non-numeric bounding box values in {model_txt_file} at line {frame_relative_idx + 1}")
                continue
            
            # رسم باندینگ باکس روی تصویر
            top_left = (int(x), int(y))
            bottom_right = (int(x + w), int(y + h))
            thickness = 2
            cv2.rectangle(image, top_left, bottom_right, color, thickness)
    
        # اگر این فریم اولین فریم دنباله است، رسم نقشه مدل به رنگ روی تصویر
        if frame_idx == start_frame:
            # تنظیم موقعیت شروع برای رسم نقشه
            legend_x = 10
            legend_y = 30
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.6
            font_thickness = 2
            rectangle_size = 20
            spacing = 5

            for model, color in model_color_map.items():
                # رسم مستطیل رنگ
                cv2.rectangle(image, (legend_x, legend_y), 
                              (legend_x + rectangle_size, legend_y + rectangle_size), 
                              color, -1)
                # نوشتن نام مدل
                text_x = legend_x + rectangle_size + spacing
                text_y = legend_y + rectangle_size - 5
                cv2.putText(
                    image,
                    model,
                    (text_x, text_y),
                    font,
                    font_scale,
                    color,
                    font_thickness,
                    cv2.LINE_AA
                )
                # به روز رسانی موقعیت برای مدل بعدی
                legend_y += rectangle_size + spacing
        
        # ذخیره تصویر
        cv2.imwrite(output_path, image)
        print(f"Processed: {output_path}")

print("All sequences processed!")

# چاپ نقشه مدل به رنگ
print("\nModel Color Legend:")
for model, color in model_color_map.items():
    # تبدیل رنگ از BGR به RGB برای نمایش صحیح در ترمینال
    r, g, b = color[2], color[1], color[0]
    print(f"{model}: RGB({r}, {g}, {b})")
