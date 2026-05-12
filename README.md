# Cattle Breed Detection & Classification System 🐄🤖

An AI-powered **2-Tier Cattle Intelligence System** designed to detect cattle types (**Cow vs Buffalo**) and classify their breeds using advanced deep learning models.

The system combines **YOLOv8 object detection**, **ResNetV2-50 breed classification**, and a **Generative AI Veterinary Assistant** powered by the Groq API to provide breed-specific insights and guidance.

---

# 🚀 Features

- ✅ Detects **Cow** and **Buffalo** using YOLOv8
- ✅ Classifies specific cattle breeds with confidence scores
- ✅ Supports:
  - Image Upload
  - Video Upload
  - Folder Upload
- ✅ Real-time visualization with bounding boxes
- ✅ AI Veterinary Assistant ("Mr. Doctor")
- ✅ Streamlit Interactive Dashboard
- ✅ Flask Lightweight Web Application
- ✅ Modular Crop-and-Classify AI Pipeline

---

# 🧠 System Architecture

The project follows a **2-Tier Deep Learning Pipeline**.

## Tier 1 — Cattle Detection

- Uses **YOLOv8** for object detection
- Detects:
  - Cow
  - Buffalo
- Generates accurate bounding boxes
- Crops detected cattle regions for breed classification

## Tier 2 — Breed Classification

- Cropped cattle images are passed into **ResNetV2-50**
- Predicts cattle breed with confidence scores

## AI Veterinary Assistant — "Mr. Doctor"

- Powered by the Groq API
- Provides:
  - Breed-specific healthcare tips
  - Basic veterinary guidance
  - Livestock management suggestions

---

# 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Detection Model | YOLOv8 |
| Classification Model | ResNetV2-50 |
| Frontend Dashboard | Streamlit |
| Lightweight Web App | Flask |
| Generative AI | Groq API |
| Deep Learning Framework | PyTorch |
| Computer Vision | OpenCV |
| Language | Python |
| Utilities | NumPy |

---

# 📊 Dataset Information

## Detection Dataset

- Trained on **1,000+ annotated images**
- Classes:
  - Cow
  - Buffalo

## Classification Dataset

- Trained on **13,000+ cattle images**
- Includes multiple breeds such as:
  - Gir
  - Sahiwal
  - Murrah
  - HF Cross
  - Jersey
  - Red Sindhi
  - And more

---

# 🖥️ Web Interfaces

## 1️⃣ Streamlit Interactive Dashboard (Recommended)

A complete AI dashboard with enhanced user interaction.

### Features

- Multi-mode uploads:
  - Image
  - Video
  - Folder
- Real-time detection visualization
- Breed confidence scores
- AI Veterinary Assistant integration
- Interactive UI experience

### Run Streamlit App

```bash
streamlit run WebApp_Using_Streamlit/Home.py
```

---

## 2️⃣ Flask Web Application

A lightweight web application focused on core prediction functionality.

### Features

- Image upload
- Video upload
- Fast and minimal interface

### Run Flask App

```bash
python FLask_Web_App/app.py
```

---

# 📂 Project Structure

```bash
├── FLask_Web_App/                 # Flask implementation
│   ├── static/
│   ├── templates/
│   └── app.py
│
├── WebApp_Using_Streamlit/        # Streamlit Dashboard
│   ├── Bot/
│   │   └── ChatBot.py             # Groq-powered AI Assistant
│   │
│   ├── assets/                    # UI assets
│   │
│   ├── utils/
│   │   ├── predict.py             # Inference logic
│   │   └── Detect_Breed.py        # Detection + Classification pipeline
│   │
│   └── Home.py                    # Streamlit entry point
│
├── Notebooks/                     # Training notebooks
│
├── yolo/                          # YOLO configurations and weights
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Namanjain122/Image-based-Cattle-Buffalo-Breed-Classifier.git

cd Image-based-Cattle-Buffalo-Breed-Classifier
```

---

## 2️⃣ Create Virtual Environment (Recommended)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Usage

## Run Streamlit Dashboard

```bash
streamlit run WebApp_Using_Streamlit/Home.py
```

---

## Run Flask Application

```bash
python FLask_Web_App/app.py
```

---

# 📸 Workflow

1. Upload Image / Video / Folder
2. YOLOv8 detects cattle
3. Detected cattle is cropped
4. ResNetV2-50 predicts breed
5. Results displayed with confidence score
6. Ask "Mr. Doctor" for veterinary insights

---

# 🎯 Supported Breeds

Some supported breeds include:

- Gir
- Sahiwal
- Murrah
- HF Cross
- Jersey
- Red Sindhi
- And more

---

# 📈 Future Improvements

- 🔹 Real-time webcam support
- 🔹 Mobile application deployment
- 🔹 Cloud deployment with API endpoints
- 🔹 Disease prediction module
- 🔹 Cattle tracking and analytics
- 🔹 Multilingual veterinary chatbot

---

# 🤝 Contributing

Contributions are welcome.

If you'd like to improve the project:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

# 👨‍💻 Author

## Naman Jain

- AI/ML Developer
- B.Tech CSE — Galgotias University

### Connect With Me

- GitHub: https://github.com/Namanjain122
- LinkedIn: https://www.linkedin.com/

---

# ⭐ Acknowledgements

- Ultralytics YOLOv8
- PyTorch
- Streamlit
- Flask
- OpenCV
- Groq API

---

# 📜 License

This project is licensed under the MIT License.
