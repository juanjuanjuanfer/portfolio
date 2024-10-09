import streamlit as st
import base64
from PIL import Image
import requests
from io import BytesIO

# Page configuration
st.set_page_config(
    page_title="Juan Fernandez | Portfolio",
    page_icon="⚡",
    layout="wide"
)

# Custom CSS with brutalist/minimalist design
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;600&display=swap');
    
    * {
        font-family: 'JetBrains Mono', monospace !important;
    }
    
    .main {
        background-color: #f0f0f0;
        padding: 2rem;
    }
    
    h1 {
        font-size: 2.5rem !important;
        font-weight: 600 !important;
        letter-spacing: -1px !important;
        margin-bottom: 1rem !important;
    }
    
    h2 {
        font-size: 1.8rem !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        border-bottom: 2px solid #333 !important;
        padding-bottom: 0.5rem !important;
    }
    
    h3 {
        font-size: 1.2rem !important;
        font-weight: 400 !important;
        letter-spacing: 1px !important;
    }
    
    .stButton>button {
        width: 100%;
        background-color: #333 !important;
        color: white !important;
        border: none !important;
        border-radius: 0 !important;
        padding: 1rem !important;
        font-size: 1rem !important;
        transition: background-color 0.3s !important;
    }
    
    .stButton>button:hover {
        background-color: #000 !important;
    }
    
    .profile-container {
        border: 2px solid #333;
        padding: 1rem;
        margin-bottom: 2rem;
    }
    
    .profile-img {
        border: none;
        filter: grayscale(100%);
        transition: filter 0.3s;
    }
    
    .profile-img:hover {
        filter: grayscale(0%);
    }
    
    .social-links {
        display: flex;
        gap: 1rem;
        margin: 2rem 0;
    }
    
    .expander-content {
        background-color: #fff;
        border: 1px solid #333;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    
    .contact-form {
        background-color: #fff;
        padding: 2rem;
        border: 2px solid #333;
    }
    
    .contact-form input, .contact-form textarea {
        width: 100%;
        padding: 0.8rem;
        margin: 0.5rem 0;
        border: 1px solid #333;
        background-color: #f8f8f8;
        font-family: 'JetBrains Mono', monospace !important;
    }
    
    .contact-form button {
        background-color: #333;
        color: white;
        padding: 1rem 2rem;
        border: none;
        cursor: pointer;
        width: 100%;
        transition: background-color 0.3s;
    }
    
    .contact-form button:hover {
        background-color: #000;
    }
    
    .stExpander {
        border: none !important;
        box-shadow: none !important;
    }
    
    .stExpander > div[role="button"] {
        background-color: #333 !important;
        color: white !important;
        border: none !important;
        border-radius: 0 !important;
    }
    
    .custom-divider {
        height: 2px;
        background-color: #333;
        margin: 2rem 0;
    }
    
    </style>
    """, unsafe_allow_html=True)

# Header section with minimal design
st.markdown('<div class="profile-container">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 2])

with col1:
    response = requests.get("https://media.licdn.com/dms/image/v2/D4E03AQG9sHFsjmveYg/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1728439522209?e=1733961600&v=beta&t=XZ3CW6OW8_0RP-lwt02ZKTrY5iHVs2nzOY5G1zgtbIw")
    img = Image.open(BytesIO(response.content))
    st.image(img, width=250, output_format="PNG")

with col2:
    st.title("JUAN FERNANDEZ")
    st.markdown("### DATA ANALYST | DATA ENGINEER")
    st.markdown("```python\n# About me\ndef professional_summary():\n    return '''Aspiring Data Analyst and Engineer\n           focused on AI, LLM, and Software Development\n           with expertise in data management and analysis.'''")

st.markdown('</div>', unsafe_allow_html=True)

# Minimal Social Links
st.markdown("## CONNECT")
cols = st.columns(4)
social_links = {
    "GITHUB": "https://github.com/juanjuanjuanfer",
    "LINKEDIN": "https://www.linkedin.com/in/juan-antonio-fernandez-cruz/",
    "LETTERBOXD": "https://letterboxd.com/fer_nwn/",
    "EMAIL": "mailto:fercruzjuan2002@gmail.com"
}

for col, (platform, link) in zip(cols, social_links.items()):
    with col:
        st.markdown(f"[{platform}]({link})")

# CV Download
st.markdown("## RESUME")
st.markdown(f'''
    <a href="https://drive.google.com/file/d/1SM-Q4Kcns-oygMUbmoUgLWGLdp7FE4g6/view?usp=sharing" target="_blank">
        <button style="width:100%; background-color:#333; color:white; padding:1rem; border:none; cursor:pointer; font-family:'JetBrains Mono',monospace;">
            DOWNLOAD CV.pdf
        </button>
    </a>
''', unsafe_allow_html=True)

# Experience Section
st.markdown("## EXPERIENCE")

experiences = [
    {
        "title": "DATA ANALYST INTERN | Instituto Laneduc",
        "period": "APR 2024 - JUL 2024",
        "details": [
            "Led data-driven English program improvement project",
            "Analyzed student performance trends across multiple generations",
            "Delivered strategic teaching recommendations",
            "ACHIEVEMENT: Identified about 27% improvement opportunity in student performance through data analysis"
        ]
    },
    {
        "title": "DATA SCIENCE INTERN | Smartia",
        "period": "JAN 2023 - APR 2023",
        "details": [
            "Developed real-time OpenCV pothole detection system",
            "Created infrastructure planning density maps",
            "Implemented data visualization dashboards",
            "ACHIEVEMENT: Improved Merida's street maintenance efficiency with a 98% confidence rate in pothole detection"
        ]
    }
]

# Update the experience section styling to highlight achievements
st.markdown("""
    <style>
    .achievement {
        margin-top: 1rem;
        padding: 0.5rem;
        border-left: 2px solid #333;
        background-color: #333333;
        font-family: 'JetBrains Mono', monospace !important;
    }
    </style>
""", unsafe_allow_html=True)

for exp in experiences:
    with st.expander(f"{exp['title']} | {exp['period']}"):
        for detail in exp['details']:
            if detail.startswith("ACHIEVEMENT:"):
                st.markdown(f"""
                    <div class="achievement">
                    ⚡ {detail}
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"- {detail}")  
# Education Section
st.markdown("## EDUCATION")
st.markdown("""
```plaintext
UNIVERSIDAD POLITÉCNICA DE YUCATÁN
B.S. DATA ENGINEERING | 2021 - 2025

CORE COMPETENCIES:
| Python | SQL | ETL | Database Management |
| Real-time Analysis | Business Intelligence |
| Data Modeling | System Architecture |
```
""")

# Projects Section
st.markdown("## PROJECTS")

projects = [
    {
        "title": "LETTERBOXD NETWORK ANALYSIS",
        "period": "APR 2024 - PRESENT",
        "link": "https://github.com/juanjuanjuanfer/Letterboxd-Network-Analysis",
        "details": [
            "Social network analysis implementation",
            "Custom scraper development",
            "Community detection algorithms",
            "Genre preference clustering"
        ]
    },
    {
        "title": "PYBOXD LIBRARY",
        "period": "SEP 2024 - PRESENT",
        "link": "https://github.com/juanjuanjuanfer/PyBoxd",
        "details": [
            "Web scraping library development",
            "OOP implementation with BeautifulSoup",
            "Comprehensive data extraction",
            "GitHub Copilot integration"
        ]
    },
    {
        "title": "LETTERBOXD FILM TRACKER",
        "period": "SEP 2024 - PRESENT",
        "link": "https://github.com/juanjuanjuanfer/yet_to_be_named",
        "details": [
            "In collaboration with Ramayo, J. https://www.linkedin.com/in/juliana-ramayo-cardoso-286017226/",
            "Film recommendation system implementation",
            "User-based collaborative filtering",
            "Content-based filtering",
            "Collaborative filtering algorithms"
        ]
    }
]

for project in projects:
    with st.expander(f"{project['title']} | {project['period']})"):
        for detail in project['details']:
            st.markdown(f"- {detail}")
        st.markdown(f"[SOURCE CODE]({project['link']})")    

# Contact Form with brutalist design
st.markdown("## CONTACT")
contact_form = """
<div class="contact-form">
    <form action="https://formsubmit.co/fercruzjuan2002@gmail.com" method="POST">
        <input type="text" name="name" placeholder="NAME" required>
        <input type="email" name="email" placeholder="EMAIL" required>
        <textarea name="message" placeholder="MESSAGE" rows="5" required></textarea>
        <button type="submit">SEND MESSAGE</button>
    </form>
</div>
"""

st.markdown(contact_form, unsafe_allow_html=True)

