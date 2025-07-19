import os
from PIL import Image
import matplotlib.pyplot as plt

base_path = "/Users/muratertik/Desktop/genresClassification"

widths = []
heights = []

for genre_folder in os.listdir(base_path):
    genre_path = os.path.join(base_path, genre_folder)
    if os.path.isdir(genre_path):
        for file_name in os.listdir(genre_path):
            if file_name.lower().endswith(".jpg"):
                img_path = os.path.join(genre_path, file_name)
                try:
                    with Image.open(img_path) as img:
                        w, h = img.size
                        widths.append(w)
                        heights.append(h)
                except Exception as e:
                    print(f"Error: {img_path} -> {e}")

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(widths, bins=30, color='royalblue')
plt.title("Actual Width Distribution")
plt.xlabel("Width (px)")
plt.ylabel("Count")

plt.subplot(1, 2, 2)
plt.hist(heights, bins=30, color='tomato')
plt.title("Actual Height Distribution")
plt.xlabel("Height (px)")
plt.ylabel("Count")

plt.tight_layout()
plt.show()
