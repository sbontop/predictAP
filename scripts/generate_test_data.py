import os
import shutil
import json
from PIL import Image
from io import BytesIO

# Directory paths
base_dir = "samuel_test_data"
data_dir = os.path.join(base_dir, "data")

# Create the base directory if it doesn't exist
os.makedirs(base_dir, exist_ok=True)

# Create the 'data' directory
os.makedirs(data_dir, exist_ok=True)

# Create dummy user JSON files in the 'data' directory
user1_data = {"name": "User 1", "age": 30}
user2_data = {"name": "User 2", "age": 25}

with open(os.path.join(data_dir, "user1.json"), "w") as user1_file:
    json.dump(user1_data, user1_file, indent=4)

with open(os.path.join(data_dir, "user2.json"), "w") as user2_file:
    json.dump(user2_data, user2_file, indent=4)

# Create dummy image files
image_size = (100, 100)
dummy_image = Image.new("RGB", image_size)
image_data = BytesIO()
dummy_image.save(image_data, format="JPEG")

for i in range(3):
    with open(os.path.join(base_dir, f"dummy_image_{i}.jpg"), "wb") as image_file:
        image_file.write(image_data.getvalue())


print("Test data directory with dummy data created successfully.")
