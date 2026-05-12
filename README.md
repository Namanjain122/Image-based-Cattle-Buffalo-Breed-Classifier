



https://github.com/user-attachments/assets/2f17632b-7b16-4c28-9e54-303866b715f5



# Image-Based Cattle & Buffalo Breed Classifier

A deep learning-based computer vision project that performs **two-stage cattle and buffalo breed classification** using **YOLOv8** and **ResNet** models.

The system first detects whether the animal is a **cow or buffalo**, crops the detected region, and then classifies the breed using a ResNet-based classifier.

---

# 🚀 Features

- Cow vs Buffalo Detection using YOLOv8
- Breed Classification using ResNet
- Image Prediction Support
- Video Prediction Support
- Flask-based Web Interface
- Real-time Bounding Box Detection
- Automatic Cropping Pipeline
- Deep Learning-based Classification

---

# 🧠 Model Pipeline

## 1️⃣ YOLOv8 Detection Model
- Detects:
  - Cow
  - Buffalo
- Crops detected animal region
- Trained on **1000+ annotated images**

## 2️⃣ ResNet Breed Classification Model
- Takes cropped animal image as input
- Predicts breed of cattle/buffalo
- Trained on **12,000+ breed images**

---

# 🛠️ Tech Stack

- Python
- YOLOv8
- ResNet
- Flask
- OpenCV
- PyTorch
- NumPy

---

# 📂 Project Structure

```bash
├── Project/
│   ├── static/
│   ├── templates/
│   ├── utils/
│   └── app.py
│
├── ResNet/
├── yolo/
│
├── .gitignore
├── Cattle and Breed Detecton Resnet.ipynb
├── Cattle and Buffaloes Breed.ipynb
├── Rename_images.py
├── test.py
└── test_Video.mp4
```

---

# 📊 Dataset Details

| Model | Dataset Size |
|------|------|
| YOLOv8 Detection | 1000+ Images |
| ResNet Classification | 12,000+ Images |

---

# ⚠️ Important Note

Large model files (`.pt`, `.pth`) and datasets are excluded from this repository because of GitHub storage limitations.

The repository contains:
- Source code
- Flask application
- Training notebooks
- Utility scripts
- Project structure

---

# ▶️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Namanjain122/Image-based-Cattle-Buffalo-Breed-Classifier.git

cd Image-based-Cattle-Buffalo-Breed-Classifier
```

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 3️⃣ Run Flask Application

```bash
python Project/app.py
```

---

# 📷 Supported Inputs

- Images
- Videos

---

# 🎯 Future Improvements

- Real-time webcam detection
- Model optimization
- Mobile deployment
- Cloud deployment
- Improved breed accuracy

---

# 👨‍💻 Author

## Naman Jain

AI/ML Developer

GitHub Repository:  
https://github.com/Namanjain122/Image-based-Cattle-Buffalo-Breed-Classifier

Linkedin:
[🎥View Demo on LinkedIn](https://www.linkedin.com/posts/naman-jain-9136732aa_artificialintelligence-machinelearning-deeplearning-ugcPost-7459465247511171072-XSW1?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEp-OF8BoZi6dSyYN5Xrf1kujyocZc_kzTM)
