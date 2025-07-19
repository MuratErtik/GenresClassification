import os
import shutil

source_dirs = [
    "/Users/muratertik/Desktop/genresClassification/actions5638",
    "/Users/muratertik/Desktop/genresClassification/animation5665",
    "/Users/muratertik/Desktop/genresClassification/comedy5637",
    "/Users/muratertik/Desktop/genresClassification/horror5806",
    "/Users/muratertik/Desktop/genresClassification/scifi5821"








]

target_dir = "/Users/muratertik/Desktop/genresClassification/dataset1"
os.makedirs(target_dir, exist_ok=True)

counter = 1

for src_dir in source_dirs:
    for filename in sorted(os.listdir(src_dir)):
        if filename.lower().endswith(".jpg"):
            new_name = f"{counter}.jpg"
            src_path = os.path.join(src_dir, filename)
            dst_path = os.path.join(target_dir, new_name)

            shutil.copy2(src_path, dst_path)
            print(f"{src_path} -> {dst_path}")
            counter += 1
