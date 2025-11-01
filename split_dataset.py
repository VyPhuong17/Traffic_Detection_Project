import os, shutil
from pathlib import Path

# === Cấu hình ===
datasets_root = Path(r'C:\Users\W11\Desktop\Dataset_con')      # thư mục chứa các dataset con
output_root = Path(r'C:\Users\W11\Desktop\Traffic_Detection_Project')        # nơi lưu dataset tổng
output_root.mkdir(exist_ok=True)

# (Tùy chọn) Map tên class khác nhau về cùng tên chuẩn
# Nếu các dataset có tên class khác nhau, bạn chỉnh tại đây
# Ví dụ: 'stop' và 'bien_dung' đều là 'dung_lai'
name_mapping = {
    'stop': 'dung_lai',
    'bien_dung': 'dung_lai',
    'no_entry': 'cam_vao',
    'prohibitory': 'cam_re_trai',
    'speed_limit': 'gioi_han_toc_do',
    # Thêm nếu có
}

# === Hàm copy ảnh ===
def copy_images(src_dir, dst_dir, prefix):
    dst_dir.mkdir(parents=True, exist_ok=True)
    for img_path in src_dir.glob('*.*'):
        if img_path.suffix.lower() not in ['.jpg', '.jpeg', '.png', '.bmp']:
            continue
        new_name = f"{prefix}_{img_path.name}"
        shutil.copy(img_path, dst_dir / new_name)

# === Gom dữ liệu ===
for dataset in datasets_root.iterdir():
    if not dataset.is_dir():
        continue
    print(f"🔹 Gộp từ: {dataset.name}")
    for split in ['train', 'val', 'test']:
        split_dir = dataset / split
        if not split_dir.exists():
            continue
        for cls_dir in split_dir.iterdir():
            if not cls_dir.is_dir():
                continue
            cls_name = name_mapping.get(cls_dir.name, cls_dir.name)
            out_dir = output_root / split / cls_name
            copy_images(cls_dir, out_dir, dataset.name)

print("\n✅ Đã gộp xong toàn bộ dataset!")