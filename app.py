import streamlit as st
from PIL import Image
import datetime

st.set_page_config(page_title="Glaucoma & Keratonococcus Help", layout="wide")

# ---- HEADER ----
st.markdown("<h1 style='text-align: center; color: #2e7bcf;'>👁️ Glaucoma & Keratonococcus Help Portal</h1>", unsafe_allow_html=True)
st.markdown("### Diagnose. Understand. Act Early.")

# ---- SIDEBAR NAV ----
st.markdown("""
    <style>
    /* Sidebar with gradient */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1E3A8A, #2563EB); /* Royal blue to bright blue */
        color: white;
    }
    
    /* Sidebar text & radio button labels */
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Radio button styles */
    .stRadio > label {
        font-size: 16px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar content
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to", 
    ["🏠 Home", "📤 Upload Report", "🩺 Doctor Recommendation"]
)

# ---- HOME PAGE ----
if page == "🏠 Home":
    st.subheader("What is Glaucoma?")
    st.write("""
    Glaucoma is a group of eye conditions that damage the optic nerve, often due to high eye pressure. It can lead to vision loss or blindness if untreated.
    """)

    st.subheader("What is Keratonococcus?")
    st.write("""
    Keratonococcus refers to an infection or inflammation of the cornea caused by bacterial invasion. Early detection and treatment are crucial.
    """)

    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Normal_vs_glaucoma_visual_field.jpg/1024px-Normal_vs_glaucoma_visual_field.jpg", caption="Normal vs Glaucoma vision", use_column_width=True)

# ---- UPLOAD PAGE ----
elif page == "📤 Upload Report":
    st.subheader("Upload Your Medical Report")
    uploaded_file = st.file_uploader("Upload Eye Scan or Report (PDF, JPG, PNG)", type=["pdf", "jpg", "jpeg", "png"])
    
    if uploaded_file:
        file_details = {
            "filename": uploaded_file.name,
            "type": uploaded_file.type,
            "size (KB)": round(uploaded_file.size / 1024, 2),
            "upload time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        st.json(file_details)

        if uploaded_file.type.startswith("image"):
            st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        else:
            st.success("Report uploaded successfully.")

        st.info("📍 Feature Coming Soon: Automatic Stage Detection & Doctor Matching")

# ---- DOCTOR PAGE ----
elif page == "🩺 Doctor Recommendation":
    st.subheader("AI-based Doctor Suggestion")
    
    city = st.selectbox("Select your city", ["Delhi", "Mumbai", "Bangalore", "Chennai", "Other"])
    condition = st.radio("Select condition", ["Glaucoma", "Keratonococcus"])
    
    if st.button("Suggest Doctor"):
        st.success(f"Here are some top doctors for **{condition}** in **{city}**:")
        
        if condition == "Glaucoma":
            st.markdown("""
            - 👨‍⚕️ Dr. Sameer Sharma - AIIMS Delhi  
            - 👩‍⚕️ Dr. Nivedita Arora - Centre for Sight  
            - 👨‍⚕️ Dr. Rohit Bansal - Shroff Eye Centre  
            """)
        else:
            st.markdown("""
            - 👨‍⚕️ Dr. Kavita Mahajan - Apollo Hospitals  
            - 👨‍⚕️ Dr. Akhil Mehra - Sankara Eye Foundation  
            - 👩‍⚕️ Dr. Renu Das - LV Prasad Eye Institute  
            """)

        st.info("This is a simulated list. Consult a certified ophthalmologist for official diagnosis.")

