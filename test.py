# from ultralytics import YOLO
# import os
# print("Running from:", os.getcwd())
# model = YOLO("best.pt")

# results = model.predict(
#     source=r"D:\Academic Projects\Cattle And Breed Detection Model\resnet_dataset\train\Buffalo_Chhattisgarhi", 
#     show=True,      
#     # save=True,     
#     conf=0.4,
#     save_crop=True, 
#     save_dir=r"resnet_croped_train_dataset\Buffalo_Chhattisgarhi"
# )
# print("Detection completed.")


# from ultralytics import YOLO

# model = YOLO("best.pt")
# import os
# print("Running from:", os.getcwd())
# # Run inference on a video
# results = model.predict(source="test_video.mp4", show=True, save=True, conf=0.25,save_dir=r"yolo/runs/detect/yolo26_results/video_results")
# print("Video detection completed.")


from ultralytics import YOLO
import os

# Load model
model = YOLO("best.pt")

# Dataset paths
input_root = r"resnet_dataset\train"
output_root = r"D:\Academic Projects\Cattle And Breed Detection Model\resnet_croped_train_dataset"

print("Running from:", os.getcwd())

# Loop through each breed folder
for folder in os.listdir(input_root):

    input_path = os.path.join(input_root, folder)

    # Skip if not a directory
    if not os.path.isdir(input_path):
        continue

    print(f"\nProcessing folder: {folder}")

    # YOLO prediction
    model.predict(
        source=input_path,
        conf=0.4,
        save=False,          # don't save full images
        save_crop=True,      # save only cropped detections
        project=output_root, # main output folder
        name=folder,         # keep same folder name
        exist_ok=True
    )

print("\nAll folders processed successfully.")