import matplotlib.pyplot as plt

labels = ["comedy", "action", "animation", "horror", "scifi"]
counts = [5136, 5178, 5428, 5232, 5520]

plt.figure(figsize=(8, 5))
plt.bar(labels, counts, color='skyblue')
plt.title("data count of classes")
plt.xlabel(" (Genre)")
plt.ylabel("count")
plt.grid(axis='y')
plt.tight_layout()

plt.show()
