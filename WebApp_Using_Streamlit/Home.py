import streamlit as st
from streamlit_option_menu import option_menu

# =========================================
# PAGE CONFIG
# =========================================
st.set_page_config(
    page_title="Cattle & Breed Detection",
    page_icon="🐄",
    layout="wide"
)

# =========================================
# NAVBAR
# =========================================
selected = option_menu(
    menu_title=None,
    options=["Home", "Detect Breed"],
    icons=["house", "search"],
    orientation="horizontal"
)

# =========================================
# HOME PAGE
# =========================================
if selected == "Home":

    # =========================================
    # TITLE
    # =========================================
    st.title("🐄 Cattle Breed Detection & Classification System")

    st.markdown("""
    ## AI-Powered 2-Tier Cattle Intelligence System

    This project is a deep learning based cattle detection and breed
    classification system developed using a two-stage AI architecture.

    The application combines:
    - YOLO26 for cattle detection
    - ResNetV2-50 for breed classification
    - Generative AI Veterinary Assistant
    - Streamlit Interactive Dashboard

    The system is trained on **13,000+ cattle images**
    consisting of multiple cow and buffalo breeds.
    """)

    st.markdown("---")

    # =========================================
    # ABOUT PROJECT
    # =========================================
    st.subheader("📌 About The Project")

    st.write("""
    This project is designed to automatically detect cattle
    and classify their breed using advanced Computer Vision
    and Deep Learning techniques.

    The system can process:
    - Single image uploads
    - Multiple image uploads
    - Batch cattle analysis

    The project also integrates an AI-powered veterinary
    assistant named MR. Doctor to provide:
    - cattle healthcare guidance
    - disease-related information
    - feeding suggestions
    - vaccination guidance
    """)

    st.markdown("---")

    # =========================================
    # ARCHITECTURE + OUTPUT
    # =========================================
    st.subheader("🏗️ System Architecture & Detection Results")

    col1, col2 = st.columns(2)

    with col1:

        st.image(
            "assets/Buffalo_luit_116.jpg",
            caption="YOLO26 Detection Result - Buffalo",
            use_container_width=True
        )

    with col2:

        st.image(
            r"D:\Academic Projects\Cattle And Breed Detection Model\Project_Using_Streamlit\assets\Cow_Red_Sindhi_89.jpg",
            caption="YOLO26 Detection Result - cow",
            use_container_width=True
        )

    st.markdown("---")

    # =========================================
    # TWO TIER ARCHITECTURE
    # =========================================
    st.subheader("🏗️ Two-Tier AI Architecture")

    col1, col2 = st.columns([1.3, 1])

    # =========================================
    # TEXT DESCRIPTION
    # =========================================
    with col1:

        st.write("""
        The application follows a two-stage deep learning pipeline:
        """)

        st.markdown("""
        ## 🔹 Tier 1 — Cattle Detection

        - YOLO26 model is used for object detection
        - Detects cows and buffaloes from uploaded images
        - Generates bounding boxes around detected cattle
        - Crops detected cattle internally for classification

        ## 🔹 Tier 2 — Breed Classification

        - ResNetV2-50 model is used for breed classification
        - Cropped cattle images are passed to the classifier
        - Predicts the breed of detected cattle
        - Displays breed name with confidence score
        """)

    # =========================================
    # ARCHITECTURE IMAGE
    # =========================================
    with col2:

        st.image(
            r"assets/architecture.png",
            caption="Two-Tier AI Architecture Pipeline",
            use_container_width=True
        )

    st.markdown("---")

    # =========================================
    # DATASET DETAILS
    # =========================================
    st.subheader("📊 Dataset Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Images", "13,000+")

    with col2:
        st.metric("Detection Model", "YOLO26")

    with col3:
        st.metric("Classification Model", "ResNetV2-50")

    st.write("""
    The dataset contains multiple breeds of:
    - Cows
    - Buffaloes

    Images were collected and preprocessed for:
    - detection training
    - breed classification
    - cropped breed datasets
    """)

    st.markdown("---")

    # =========================================
    # FEATURES
    # =========================================
    st.subheader("✨ Features")

    feature1, feature2, feature3 = st.columns(3)

    with feature1:

        st.info("""
        🐄 Cattle Detection

        Detect cows and buffaloes
        using YOLO26 object detection.
        """)

    with feature2:

        st.success("""
        🧠 Breed Classification

        Predict cattle breed
        using ResNetV2-50.
        """)

    with feature3:

        st.warning("""
        👨‍⚕️ MR. Doctor AI

        AI-powered veterinary
        assistant for cattle care.
        """)

    st.markdown("---")

    # =========================================
    # HOW TO USE
    # =========================================
    st.subheader("🚀 How To Use The Application")

    st.markdown("""
    Follow these simple steps to use the application:
    """)

    # =========================================
    # STEP 1
    # =========================================
    st.markdown("## 🔹 Step 1 — Open Detect Breed Page")

    col1, col2 = st.columns([1, 1.2])

    with col1:

        st.markdown("""
        - Click on **Detect Breed**
        from the navigation bar.

        - This opens the main
        prediction dashboard.
        """)

    with col2:

        st.image(
            "assets/navbar.png",
            caption="Navigation Bar",
            use_container_width=True
        )

    st.markdown("---")

    # =========================================
    # STEP 2
    # =========================================
    st.markdown("## 🔹 Step 2 — Choose Upload Type")

    col1, col2 = st.columns([1, 1.2])

    with col1:

        st.markdown("""
        Select upload mode:
        - Image Upload
        - Video Upload
        - Folder Upload

        according to your requirement.
        """)

    with col2:

        st.image(
            "assets/upload_option.png",
            caption="Upload Type Selection",
            use_container_width=True
        )

    st.markdown("---")

    # =========================================
    # STEP 3
    # =========================================
    st.markdown("## 🔹 Step 3 — Use MR. Doctor Assistant")

    col1, col2 = st.columns([1, 1.2])

    with col1:

        st.markdown("""
        Use the AI Veterinary Assistant
        named **MR. Doctor** for:
        
        - cattle healthcare guidance
        - nutrition suggestions
        - vaccination guidance
        - disease information
        """)

    with col2:

        st.image(
            "assets/mr_doctor.png",
            caption="MR. Doctor AI Assistant",
            use_container_width=True
        )

    st.markdown("---")

    # =========================================
    # FINAL STEP
    # =========================================
    st.markdown("""
    ## ✅ Final Output

    The system will:
    - Detect cattle using YOLO26
    - Classify breed using ResNetV2-50
    - Display confidence scores
    - Provide AI veterinary assistance
    """)

    # =========================================
    # TECHNOLOGY STACK
    # =========================================
    st.subheader("🛠️ Technology Stack")

    tech1, tech2, tech3, tech4 = st.columns(4)

    with tech1:
        st.metric("Detection", "YOLO26")

    with tech2:
        st.metric("Classification", "ResNetV2-50")

    with tech3:
        st.metric("Frontend", "Streamlit")

    with tech4:
        st.metric("LLM", "Groq API")

    st.markdown("---")

    st.success("""
    ✅ Built using Deep Learning, Computer Vision,
    and Generative AI technologies.
    """)

# =========================================
# DETECT BREED PAGE
# =========================================
elif selected == "Detect Breed":

    with open(
        "Detect_Breed.py",
        encoding="utf-8"
    ) as f:
        exec(f.read())