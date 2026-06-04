import streamlit as st
from PIL import Image

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Apoorva Sharma | AI/ML Developer",
    page_icon="🚀",
    layout="wide"
)

# ---------------- THEME TOGGLE ---------------- #

theme_mode = st.toggle("", value=True)

# ---------------- CUSTOM CSS ---------------- #


if theme_mode:

    background = "#0F172A"
    card_bg = "#111827"
    text = "white"
    secondary_text = "#CBD5E1"
    footer_text = "#94A3B8"

else:

    background = "#F8FAFC"
    card_bg = "#FFFFFF"
    text = "#0F172A"
    secondary_text = "#334155"
    footer_text = "#0F172A"

st.markdown(f"""
<style>

/* Main Background */
.stApp {{
    background-color: {background};
}}

/* Remove top padding */
.block-container {{
    padding-top: 2rem;
    padding-left: 5rem;
    padding-right: 5rem;
}}

/* Title */
.main-title {{
    font-size: 70px;
    font-weight: 700;
    color: {text};
}}

/* Subtitle */
.sub-title {{
    font-size: 30px;
    color: #38BDF8;
}}

/* Description */
.description {{
    font-size: 20px;
    color: {secondary_text};
    line-height: 1.8;
}}

/* Section Heading */
.section-heading {{
    font-size: 45px;
    font-weight: bold;
    color: {text};
    margin-top: 100px;
    margin-bottom: 30px;
}}

/* Card */
.custom-card {{
    background-color: {card_bg};
    padding: 35px;
    border-radius: 20px;
    border: 1px solid #1E293B;
}}

/* About Text */
.about-text {{
    font-size: 20px;
    line-height: 1.9;
    color: {secondary_text};
}}

/* Buttons */
.stButton > button {{
    background-color: #38BDF8;
    color: black;
    border-radius: 10px;
    height: 50px;
    width: 220px;
    font-size: 18px;
    font-weight: bold;
    border: none;
}}

.stButton > button:hover {{
    background-color: {text};
    color: black;
}}

/* Links */
a {{
    text-decoration: none !important;
}}

/* Toggle Container */
div[data-testid="stToggle"] {{
    position: fixed;
    top: 14px;
    right: 120px;
    z-index: 9999;
    background-color: transparent;
}}

/* Toggle Label */
div[data-testid="stToggle"] label p {{
    color: {text} !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}}

/* Toggle Switch */
div[data-testid="stToggle"] div[role="switch"] {{
    background-color: #38BDF8 !important;
}}

/* Toggle background */
div[data-testid="stToggle"] div[role="switch"] {{
    background-color: #38BDF8 !important;
}}

/* Skill Cards */
.skill-card,
.project-card,
.timeline-card,
.cert-card,
.contact-card {{
    background-color: {card_bg};
    padding: 30px;
    border-radius: 20px;
    border: 1px solid #1E293B;
    margin-bottom: 25px;
}}

/* Card Headings */
.skill-card h3,
.project-card h2,
.timeline-card h2,
.cert-card h2,
.contact-card h3 {{
    color: {text} !important;
}}

/* Card Paragraphs & Lists */
.skill-card,
.project-card p,
.project-card ul,
.timeline-card p,
.timeline-card ul,
.cert-card p,
.contact-card p {{
    color: {secondary_text} !important;
    font-size: 18px;
    line-height: 1.8;
}}

body {{
    opacity: 1 !important;
}}

div[data-testid="stToggle"] {{
    position: fixed;
    top: 20px;
    right: 80px;
    z-index: 999;
}}

</style>
""", unsafe_allow_html=True)

# ---------------- MAIN SECTION ---------------- #

col1, col2 = st.columns([2, 1])

with col1:

    st.markdown(
        "<div class='main-title'>Apoorva Sharma</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='sub-title'>Computer Science Graduate | AI/ML Developer</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='description'>
        BARC Research Intern building AI systems with
        Computer Vision, NLP, FastAPI and Deep Learning.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # Resume Download
    with open("assets/resume.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name="Apoorva_Sharma_Resume.pdf",
        mime="application/pdf"
    )

    st.write("")

    st.markdown(f"""
    <a href='https://github.com/Apoorva-22' target='_blank'>
    <span style='color:#38BDF8; font-size:20px; margin-right:25px;'>
    GitHub
    </span>
    </a>

    <a href='https://www.linkedin.com/in/apoorva-sharma-a6842a22a/' target='_blank'>
    <span style='color:#38BDF8; font-size:20px;'>
    LinkedIn
    </span>
    </a>
    """, unsafe_allow_html=True)

with col2:

    image = Image.open("assets/profile.png")
    st.image(image, width=320)

# ---------------- ABOUT SECTION ---------------- #

st.markdown(
    "<div class='section-heading'>About Me</div>",
    unsafe_allow_html=True
)

st.markdown(f"""
<div class='custom-card'>

<div class='about-text'>

I am a Computer Science graduate focused on
Computer Vision, NLP and real-world AI systems.

My experience includes developing autonomous
robotics solutions during my research internship
at Bhabha Atomic Research Centre (BARC) and
building multimodal AI applications using
PyTorch, FastAPI, OpenCV and Transformer models.

I enjoy solving practical problems through
machine learning, backend engineering and
deployable AI products.

</div>

</div>
""", unsafe_allow_html=True)

st.divider()
# ---------------- SKILLS SECTION ---------------- #

st.markdown(
    "<div class='section-heading'>Highlights</div>",
    unsafe_allow_html=True
)

c1,c2,c3,c4 = st.columns(4)

c1.metric("Projects","3+")
c2.metric("Internship","BARC")
c3.metric("Core Area","AI/ML")
c4.metric("Focus","CV + NLP")

st.divider()

st.markdown(
    "<div class='section-heading'>Technical Skills</div>",
    unsafe_allow_html=True
)

skill_col1, skill_col2 = st.columns(2)

with skill_col1:

    st.markdown(f"""
    <div class='skill-card'>

    <h3>AI / Machine Learning</h3>

    • PyTorch <br>
    • Deep Learning <br>
    • Transformers <br>
    • CNNs <br>
    • OpenCV <br>
    • YOLO <br>
    • NLP <br>
    • Computer Vision

    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class='skill-card'>

    <h3>Backend & APIs</h3>

    • FastAPI <br>
    • Flask <br>
    • REST APIs <br>
    • Firebase <br>
    • MySQL

    </div>
    """, unsafe_allow_html=True)

with skill_col2:

    st.markdown(f"""
    <div class='skill-card'>

    <h3>Programming</h3>

    • Python <br>
    • C++ <br>
    • SQL <br>
    • Git & GitHub

    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class='skill-card'>

    <h3>Tools & Deployment</h3>

    • Streamlit <br>
    • GitHub <br>
    • VS Code <br>
    • Raspberry Pi <br>
    • Arduino

    </div>
    """, unsafe_allow_html=True)

st.divider()
# ---------------- PROJECTS SECTION ---------------- #

st.markdown(
    "<div class='section-heading'>Featured Projects</div>",
    unsafe_allow_html=True
)

# ---------- PROJECT 1 ---------- #

st.image("assets/manosamvada.png")

st.markdown(f"""
<div class='project-card'>

<h2 style='color:{text};'>
ManoSamvada – AI Mental Wellness Chatbot
</h2>

<p style='color:#CBD5E1; font-size:18px; line-height:1.8;'>

AI-powered mental wellness chatbot designed for emotion-aware
conversational support using LLM APIs and backend analytics systems.

</p>

<p style='color:#38BDF8;'>
Flask • MySQL • Groq API • Python
</p>

<ul style='color:#CBD5E1; line-height:2;'>

<li>Built modular chatbot backend architecture</li>

<li>Implemented emotional analytics workflows</li>

<li>Designed crisis keyword detection pipeline</li>

<li>Created authentication & session management APIs</li>

</ul>

</div>
""", unsafe_allow_html=True)

_ = st.link_button(
    "🔗 View Project",
    "https://github.com/Apoorva-22/ManoSamvada"
)

_ = st.link_button(
    "🔗 Live Demo",
    "https://manosamvada.onrender.com/"
)

st.divider()

# ---------- PROJECT 2 ---------- #

st.image("assets/emotion_system.png")

st.markdown(f"""
<div class='project-card'>

<h2 style='color:{text};'>
Multimodal Emotion Recognition System
</h2>

<p style='color:#CBD5E1; font-size:18px; line-height:1.8;'>

A real-time multimodal AI system integrating facial expression,
speech emotion, and text sentiment analysis using Deep Learning,
Transformers, and Computer Vision pipelines.

</p>

<p style='color:#38BDF8;'>
PyTorch • FastAPI • OpenCV • YOLO • DistilBERT • Librosa
</p>

<ul style='color:#CBD5E1; line-height:2;'>

<li>Integrated ResNet18, LSTM, and DistilBERT models</li>

<li>Designed confidence-aware multimodal fusion pipeline</li>

<li>Built scalable FastAPI inference backend</li>

<li>Implemented real-time webcam, audio, and text inference</li>

</ul>

</div>
""", unsafe_allow_html=True)

_ = st.link_button(
    "🔗 View Project",
    "https://github.com/Apoorva-22/multimodal-emotion-recognition-system"
)

st.write("")

# ---------- PROJECT 3 ---------- #

st.markdown(f"""
<div class='project-card'>

<h2 style='color:{text};'>
AI-Based Autonomous Robot
</h2>

<p style='color:#CBD5E1; font-size:18px; line-height:1.8;'>

AI-assisted autonomous robotic system developed for real-time face
recognition and intelligent navigation workflows using edge-based
computer vision pipelines.

</p>

<p style='color:#38BDF8;'>
Python • OpenCV • Raspberry Pi • Arduino
</p>

<ul style='color:#CBD5E1; line-height:2;'>

<li>Implemented face recognition workflows using OpenCV</li>

<li>Built hardware-software communication pipelines</li>

<li>Worked on intelligent navigation systems</li>

<li>Developed during BARC research internship</li>

</ul>

</div>
""", unsafe_allow_html=True)

_ = st.link_button(
    "🔗 View Project",
    "https://github.com/Apoorva-22/vision-guided-autonomous-robot"
)

_ = st.link_button(
    "📜 Internship Certificate",
    "https://drive.google.com/file/d/1rSkF51zzsnKZmAKsBPbO2xW2o9lr3Oul/view?pli=1"
)

st.write("")


# ---------------- EXPERIENCE SECTION ---------------- #

st.markdown(
    "<div class='section-heading'>Experience</div>",
    unsafe_allow_html=True
)

st.markdown(f"""
<div class='timeline-card'>

<h2 style='color:{text};'>
Research Intern — Bhabha Atomic Research Centre (BARC)
</h2>

<p style='color:#38BDF8; font-size:18px;'>
Jul 2024 – Nov 2024
</p>

<ul style='color:#CBD5E1; line-height:2; font-size:18px;'>

<li>
Developed AI-assisted autonomous robotics
solutions using OpenCV, Raspberry Pi and Arduino.
</li>

<li>
Built computer vision workflows for face
recognition and object tracking.
</li>

<li>
Integrated hardware and software modules for
real-time robotic navigation.
</li>

<li>
Worked within a research-driven environment at
BARC on intelligent systems applications.
</li>

</ul>

</div>
""", unsafe_allow_html=True)

st.divider()
# ---------------- CERTIFICATIONS SECTION ---------------- #

st.markdown(
    "<div class='section-heading'>Certifications</div>",
    unsafe_allow_html=True
)

st.markdown(f"""
<div class='cert-card'>

<h2 style='color:{text};'>
BARC Research Internship Certificate
</h2>

<p style='color:#CBD5E1; font-size:18px; line-height:1.8;'>

Successfully completed research internship focused on
AI-assisted autonomous robotics, computer vision,
and intelligent navigation systems.

</p>

<p style='color:#38BDF8;'>
Organization: Bhabha Atomic Research Centre (BARC)
</p>

</div>
""", unsafe_allow_html=True)

_ = st.link_button(
    "📜 View Certificate",
    "https://drive.google.com/file/d/1rSkF51zzsnKZmAKsBPbO2xW2o9lr3Oul/view?pli=1"
)

st.divider()
# ---------------- CONTACT SECTION ---------------- #

st.markdown(
    "<div class='section-heading'>Contact Me</div>",
    unsafe_allow_html=True
)

st.markdown(f"""
<div class='contact-card'>

<h3 style='color:white;'>
Let's Connect
</h3>

<p style='color:#CBD5E1; font-size:18px;'>

Open to AI/ML internships, freelance opportunities,
research collaborations, and intelligent systems projects.

</p>

</div>
""", unsafe_allow_html=True)

# ---------------- CONTACT FORM ---------------- #

st.markdown("""
<form action="https://formspree.io/f/mvznowqg"
      method="POST">

<input type="text"
       name="name"
       placeholder="Your Name"
       required>

<br><br>

<input type="email"
       name="email"
       placeholder="Your Email"
       required>

<br><br>

<textarea name="message"
          placeholder="Your Message"
          required></textarea>

<br><br>

<button type="submit">
Send Message
</button>

</form>
""", unsafe_allow_html=True)

st.write("")

col1, col2, col3 = st.columns(3)

with col1:

    _ = st.link_button(
        "GitHub Profile: github.com/Apoorva-22",
        "https://github.com/Apoorva-22"
    )

with col2:

    _ = st.link_button(
        "LinkedIn Profile: linkedin.com/in/apoorva-sharma-a6842a22a ",
        "https://www.linkedin.com/in/apoorva-sharma-a6842a22a/"
    )

with col3:

    _ = st.link_button(
        "Email: apoorv6627@gmail.com",
        "mailto:apoorv6627@gmail.com"
    )

# ---------------- FOOTER ---------------- #

st.write("")
st.write("")

st.divider()

st.markdown(
    f"""
    <style>
    .footer-text {{
        text-align: center;
        padding-top: 20px;
        padding-bottom: 30px;
        font-size: 18px;
        font-weight: 500;
        color: {footer_text} !important;
        opacity: 1 !important;
    }}
    </style>

    <div class="footer-text">

    Designed & Developed by Apoorva Sharma

    <br><br>

    AI/ML Developer • Computer Vision & NLP

    </div>
    """,
    unsafe_allow_html=True
)
