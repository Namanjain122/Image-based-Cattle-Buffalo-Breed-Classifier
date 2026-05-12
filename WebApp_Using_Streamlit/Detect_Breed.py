import streamlit as st
from PIL import Image
import tempfile
from utils.predict import detect_and_classify_image, process_video
from Bot.ChatBot import ask_doctor

st.set_page_config(
    page_title="Cattle & Breed Detection",
    layout="wide"
)

st.title("Cattle & Breed Detection System")

upload_type = st.selectbox(
    "Choose Upload Type",
    ["Image", "Video", "Folder"]
)

# =========================================
# IMAGE
# =========================================
if upload_type == "Image":

    uploaded_image = st.file_uploader(
        "Upload Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_image is not None:

        image = Image.open(
            uploaded_image
        ).convert("RGB")

        detected_img, predictions = (
            detect_and_classify_image(image)
        )

        st.subheader("Detection Result")

        st.image(
            detected_img,
            channels="BGR",
            use_container_width=True
        )

        st.subheader("Breed Predictions")

        if len(predictions) == 0:

            st.warning("No cattle detected")

        else:

            for i, pred in enumerate(predictions):

                st.write(
                    f"Animal {i+1}: "
                    f"{pred['breed']} "
                    f"({pred['confidence']:.2f})"
                )

# =========================================
# VIDEO
# =========================================
elif upload_type == "Video":

    uploaded_video = st.file_uploader(
        "Upload Video",
        type=["mp4", "avi", "mov"]
    )

    if uploaded_video is not None:

        tfile = tempfile.NamedTemporaryFile(
            delete=False
        )

        tfile.write(uploaded_video.read())

        st.subheader("Uploaded Video")

        st.video(tfile.name)

        st.info("Processing video...")

        output_path, predictions = process_video(
            tfile.name
        )

        st.success("Processing Complete")

        st.subheader("Detection Result")

        video_file = open(output_path, "rb")

        video_bytes = video_file.read()

        st.video(video_bytes)

        st.subheader("Breed Predictions")

        if len(predictions) == 0:

            st.warning("No cattle detected")

        else:

            unique_predictions = list(
                set(predictions)
            )

            for pred in unique_predictions:

                st.write(pred)

# =========================================
# FOLDER
# =========================================
elif upload_type == "Folder":

    uploaded_files = st.file_uploader(
        "Upload Multiple Images",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True
    )

    if uploaded_files:

        for file in uploaded_files:

            st.divider()

            st.subheader(file.name)

            image = Image.open(
                file
            ).convert("RGB")

            detected_img, predictions = (
                detect_and_classify_image(image)
            )

            st.image(
                detected_img,
                channels="BGR",
                use_container_width=True
            )

            if len(predictions) == 0:

                st.warning("No cattle detected")

            else:

                for i, pred in enumerate(predictions):

                    st.write(
                        f"Animal {i+1}: "
                        f"{pred['breed']} "
                        f"({pred['confidence'] * 100:.2f}%)"
                    )
# =========================================
# CHAT HISTORY
# =========================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================================
# SIDEBAR CHATBOT
# =========================================
with st.sidebar:

    st.title("🐄 MR. Doctor")

    st.markdown(
        "AI Veterinary Assistant"
    )

    # Chat History
    if "messages" not in st.session_state:

        st.session_state.messages = []

    # Show Previous Messages
    for msg in st.session_state.messages:

        with st.chat_message(msg["role"]):

            st.write(msg["content"])

    # Chat Input
    prompt = st.chat_input(
        "Ask about cattle health..."
    )

    # User Query
    if prompt:

        # Save User Message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        # Show User Message
        with st.chat_message("user"):

            st.write(prompt)

        # Generate AI Response
        with st.spinner("MR. Doctor is thinking..."):

            response = ask_doctor(prompt)

        # Save Assistant Message
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

        # Show Assistant Message
        with st.chat_message("assistant"):

            st.write(response)