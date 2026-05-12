from ultralytics import YOLO
import torch
import timm
from torchvision import transforms, datasets
from PIL import Image
import cv2

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ---------------- LOAD YOLO ----------------
yolo_model = YOLO(r"D:\Academic Projects\Cattle And Breed Detection Model\Project\models\best.pt")

# ---------------- LOAD RESNET ----------------
num_classes = 67

resnet_model = timm.create_model(
    "resnetv2_50",
    pretrained=False,
    num_classes=num_classes
)

resnet_model.load_state_dict(
    torch.load(r"Project/models/resnetv2_breed_classifier.pth", map_location=device)
)

resnet_model.to(device)
resnet_model.eval()

# ---------------- LOAD CLASS NAMES ----------------
dataset = datasets.ImageFolder(
    "D:\\Academic Projects\\Cattle And Breed Detection Model\\ResNet\\resnet_croped_train_dataset"
)

classes = dataset.classes

# ---------------- TRANSFORM ----------------
transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor()
])


# ---------------- DETECT + CLASSIFY FRAME ----------------
def detect_and_classify_frame(frame):

    results = yolo_model(frame)

    breed_predictions = []

    for r in results:

        plotted_frame = r.plot()

        if r.boxes is None:
            return plotted_frame, breed_predictions

        boxes = r.boxes.xyxy.cpu().numpy()

        for box in boxes:

            x1,y1,x2,y2 = map(int, box)

            crop = frame[y1:y2, x1:x2]

            if crop.size == 0:
                continue

            crop_pil = Image.fromarray(
                cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)
            )

            crop_tensor = transform(crop_pil).unsqueeze(0).to(device)

            with torch.no_grad():

                output = resnet_model(crop_tensor)

                probs = torch.softmax(output, dim=1)

                pred = torch.argmax(probs,1).item()

                confidence = probs[0][pred].item()*100

            breed = classes[pred]

            breed_predictions.append(
                f"{breed} ({confidence:.2f}%)"
            )

    return plotted_frame, breed_predictions


# ---------------- IMAGE PROCESS ----------------
def process_image(image_path, output_path):

    image = cv2.imread(image_path)

    result_frame, breeds = detect_and_classify_frame(image)

    cv2.imwrite(output_path, result_frame)

    return breeds


# ---------------- VIDEO PROCESS ----------------
def process_video(video_path, output_path):

    cap = cv2.VideoCapture(video_path)

    width = int(cap.get(3))
    height = int(cap.get(4))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    writer = cv2.VideoWriter(
        output_path,
        cv2.VideoWriter_fourcc(*'mp4v'),
        fps,
        (width,height)
    )

    last_predictions = []

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frame, breeds = detect_and_classify_frame(frame)

        if breeds:
            last_predictions = breeds

        writer.write(frame)

    cap.release()
    writer.release()

    return last_predictions