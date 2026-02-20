import streamlit as st

# ─────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Dwight Angelo Sabandal - Portfolio",
    page_icon="assets/spiral-solid-full.svg",
    layout="wide",
)

# ─────────────────────────────────────────────
#  LOAD FONT AWESOME & CUSTOM CSS
# ─────────────────────────────────────────────
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap');

html, body, [class*="css"] { font-family: 'Outfit', sans-serif; }
.stApp { background: #0e0e0e; color: #d4d0cb; }

/* Sidebar */
[data-testid="stSidebar"] { background: #161616; border-right: 1px solid #242424; }
[data-testid="stSidebar"] * { color: #c8c4be !important; }
[data-testid="stSidebar"] .stRadio label { font-size: 0.8rem !important; letter-spacing: 2.5px !important; text-transform: uppercase !important; color: #6b6560 !important; padding: 8px 0 !important; }
[data-testid="stSidebar"] .stRadio label:hover { color: #d4d0cb !important; }
[data-testid="stSidebar"] hr { border-color: #242424 !important; }
[data-testid="stSidebar"] .stMetric { background: #1e1e1e !important; border: 1px solid #2a2a2a !important; border-radius: 10px !important; }
[data-testid="stSidebar"] [data-testid="stMetricLabel"] { color: #6b6560 !important; font-size: 0.7rem !important; letter-spacing: 2px !important; text-transform: uppercase !important; }
[data-testid="stSidebar"] [data-testid="stMetricValue"] { color: #d4d0cb !important; font-family: 'Playfair Display', serif !important; }

/* Hero */
.hero { background: linear-gradient(135deg, #161616 0%, #1a1a1a 100%); border: 1px solid #242424; border-radius: 18px; padding: 3.5rem 3rem; margin-bottom: 2rem; position: relative; overflow: hidden; }
.hero::before { content: ''; position: absolute; top: 0; right: 0; width: 400px; height: 400px; background: radial-gradient(circle at top right, #4ade8010 0%, transparent 65%); }
.hero-label { font-size: 0.7rem; letter-spacing: 4px; text-transform: uppercase; color: #4ade80; margin-bottom: 1rem; }
.hero-name { font-family: 'Playfair Display', serif; font-size: clamp(2.6rem, 5vw, 4rem); font-weight: 600; color: #f0ede8; line-height: 1.1; margin: 0; }
.hero-role { font-family: 'Playfair Display', serif; font-size: 1.3rem; font-style: italic; color: #6b6560; margin-top: 0.5rem; }
.hero-bio { font-size: 0.92rem; color: #8a8680; line-height: 1.8; max-width: 560px; margin-top: 1.2rem; }
.hero-links { margin-top: 1.8rem; display: flex; gap: 12px; flex-wrap: wrap; }
.hero-link { display: inline-flex; align-items: center; gap: 7px; background: #1e1e1e; border: 1px solid #2e2e2e; color: #8a8680 !important; border-radius: 8px; padding: 8px 16px; font-size: 0.74rem; letter-spacing: 1.5px; text-transform: uppercase; text-decoration: none !important; transition: border-color 0.2s, color 0.2s; }
.hero-link:hover { border-color: #4ade8060; color: #4ade80 !important; }

/* Section headers */
.sec-eyebrow { font-size: 0.68rem; letter-spacing: 4px; text-transform: uppercase; color: #4ade80; margin-bottom: 0.3rem; }
.sec-heading { font-family: 'Playfair Display', serif; font-size: 2rem; font-weight: 400; color: #f0ede8; border-bottom: 1px solid #242424; padding-bottom: 0.5rem; margin-bottom: 1.5rem; }

/* Cards */
.card { background: #161616; border: 1px solid #242424; border-radius: 14px; padding: 1.5rem; margin-bottom: 0.8rem; transition: border-color 0.25s, transform 0.2s; }
.card:hover { border-color: #4ade8040; transform: translateY(-2px); }
.card-title { font-family: 'Playfair Display', serif; font-size: 1.1rem; color: #f0ede8; margin-bottom: 4px; }
.card-meta { font-size: 0.74rem; letter-spacing: 2px; text-transform: uppercase; color: #6b6560; margin-bottom: 10px; }
.card-body { font-size: 0.88rem; color: #8a8680; line-height: 1.75; }

/* Project Cards */
.proj-card { background: #161616; border: 1px solid #242424; border-radius: 14px; overflow: hidden; transition: border-color 0.25s, transform 0.2s; margin-bottom: 1rem; }
.proj-card:hover { border-color: #4ade8040; transform: translateY(-3px); }
.proj-card-img { width: 100%; height: 100%; object-fit: cover; display: block; }
.proj-card-img-placeholder { width: 100%; height: 180px; background: #111; display: block; border-bottom: 1px solid #1e1e1e; }
.proj-card-body { padding: 1.2rem; }
.proj-card-title { font-family: 'Playfair Display', serif; font-size: 1.05rem; color: #f0ede8; margin-bottom: 4px; }
.proj-card-meta { font-size: 0.72rem; letter-spacing: 2px; text-transform: uppercase; color: #6b6560; margin-bottom: 8px; }
.proj-card-desc { font-size: 0.85rem; color: #8a8680; line-height: 1.65; margin-bottom: 12px; }

/* Tags */
.tag { display: inline-block; background: #1e1e1e; border: 1px solid #2e2e2e; color: #8a8680; border-radius: 6px; padding: 3px 10px; font-size: 0.72rem; letter-spacing: 1px; text-transform: uppercase; margin: 2px; }

/* Status pills */
.pill-live { background: #0d2e1a; color: #4ade80; border-radius: 20px; padding: 2px 12px; font-size: 0.7rem; letter-spacing: 1px; text-transform: uppercase; font-weight: 600; }
.pill-beta { background: #2a1f0a; color: #f59e0b; border-radius: 20px; padding: 2px 12px; font-size: 0.7rem; letter-spacing: 1px; text-transform: uppercase; font-weight: 600; }
.pill-wip  { background: #1a1a2e; color: #818cf8; border-radius: 20px; padding: 2px 12px; font-size: 0.7rem; letter-spacing: 1px; text-transform: uppercase; font-weight: 600; }

/* Timeline */
.tl { border-left: 1px solid #2a2a2a; padding-left: 1.5rem; margin-bottom: 1.8rem; position: relative; }
.tl::before { content: ''; width: 8px; height: 8px; background: #4ade80; border-radius: 50%; position: absolute; left: -5px; top: 5px; }
.tl-yr { font-size: 0.68rem; letter-spacing: 2px; text-transform: uppercase; color: #4ade80; margin-bottom: 2px; }
.tl-title { font-family: 'Playfair Display', serif; font-size: 1rem; color: #f0ede8; }
.tl-org { font-size: 0.82rem; color: #6b6560; margin-top: 2px; }
.tl-desc { font-size: 0.86rem; color: #8a8680; margin-top: 6px; line-height: 1.6; }

/* Skill Progress Bars */
.skill-row { margin-bottom: 1rem; }
.skill-label { display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px; }
.skill-name { font-size: 0.82rem; color: #d4d0cb; letter-spacing: 1px; }
.skill-pct { font-size: 0.72rem; color: #4ade80; font-family: 'Playfair Display', serif; }
.skill-track { width: 100%; background: #1e1e1e; border-radius: 4px; height: 5px; border: 1px solid #2a2a2a; overflow: hidden; }
.skill-fill { height: 100%; background: linear-gradient(90deg, #4ade80, #22c55e); border-radius: 4px; }
.skill-category-label { font-size: 0.65rem; letter-spacing: 3px; text-transform: uppercase; color: #4ade80; margin: 1.2rem 0 0.8rem; border-bottom: 1px solid #1e1e1e; padding-bottom: 6px; }

/* Cert card */
.cert-card { background: #161616; border: 1px solid #242424; border-radius: 12px; padding: 1rem 1.3rem; margin-bottom: 0.6rem; display: flex; align-items: flex-start; gap: 14px; }
.cert-icon { color: #4ade80; font-size: 1.1rem; margin-top: 2px; flex-shrink: 0; }
.cert-title { font-size: 0.9rem; color: #d4d0cb; font-weight: 500; }
.cert-sub { font-size: 0.76rem; color: #6b6560; margin-top: 2px; }

/* Metrics */
[data-testid="stMetric"] { background: #161616; border: 1px solid #242424; border-radius: 12px; padding: 1.2rem; }
[data-testid="stMetricLabel"] { font-size: 0.7rem; letter-spacing: 2px; text-transform: uppercase; color: #6b6560 !important; }
[data-testid="stMetricValue"] { font-family: 'Playfair Display', serif; font-size: 1.9rem; color: #f0ede8 !important; }

/* Tabs */
.stTabs [data-baseweb="tab-list"] { background: #161616; border: 1px solid #242424; border-radius: 10px; padding: 4px; gap: 4px; }
.stTabs [data-baseweb="tab"] { border-radius: 7px; font-size: 0.75rem; letter-spacing: 2px; text-transform: uppercase; color: #6b6560; padding: 8px 18px; }
.stTabs [aria-selected="true"] { background: #1e1e1e !important; color: #f0ede8 !important; border: 1px solid #2e2e2e !important; }

/* Inputs */
.stTextInput input, .stTextArea textarea { background: #161616 !important; border-color: #2a2a2a !important; border-radius: 9px !important; color: #d4d0cb !important; }
.stTextInput label, .stTextArea label, .stSelectbox label, .stFileUploader label, .stCheckbox label { color: #8a8680 !important; font-size: 0.78rem !important; letter-spacing: 1px !important; }

/* Buttons */
.stButton button, .stDownloadButton button, .stFormSubmitButton button {
    background: #f0ede8 !important; color: #0e0e0e !important; border: none !important; border-radius: 9px !important;
    letter-spacing: 2px !important; text-transform: uppercase !important; font-size: 0.74rem !important; font-weight: 600 !important;
    padding: 10px 22px !important; transition: opacity 0.2s !important;
}
.stButton button:hover { opacity: 0.8 !important; }

/* Progress */
.stProgress > div > div { background: #4ade80 !important; border-radius: 4px !important; }
.stProgress > div { background: #1e1e1e !important; border-radius: 4px !important; }

/* Expander */
[data-testid="stExpander"] { background: #161616 !important; border: 1px solid #242424 !important; border-radius: 12px !important; }
[data-testid="stExpander"] summary { color: #d4d0cb !important; font-size: 0.9rem !important; }

hr { border-color: #1e1e1e !important; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown(f"""
    <div style='text-align:center;padding:1.5rem 0 1rem;'>
        <div style='width:88px;height:88px;border-radius:50%;margin:0 auto 1rem;overflow:hidden;border:1px solid #4ade8040;'>
            <img src="https://raw.githubusercontent.com/daas-me/portfolio/main/assets/sabandal.jpg"
                 style="width:100%;height:100%;object-fit:cover;border-radius:50%;">
        </div>
        <div style='font-family:Playfair Display,serif;font-size:1.2rem;color:#f0ede8;'>Dwight Angelo Sabandal</div>
        <div style='color:#6b6560;font-size:0.72rem;letter-spacing:3px;text-transform:uppercase;margin-top:5px;'>Designer · Developer</div>
        <div style='margin-top:12px;'>
            <span style='background:#0d2e1a;color:#4ade80;border-radius:20px;padding:3px 14px;
                         font-size:0.7rem;letter-spacing:1px;text-transform:uppercase;font-weight:600;'>
                <i class="fa-solid fa-circle" style="font-size:0.4rem;vertical-align:middle;margin-right:4px;"></i>
                Available for Work
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    page = st.radio(
        "Navigate",
        ["Home", "About Me", "Portfolio", "Experience", "Contact"],
        label_visibility="collapsed",
    )

    st.divider()

    st.markdown("<div style='font-size:0.65rem;letter-spacing:3px;text-transform:uppercase;color:#3a3a3a;margin-bottom:0.7rem;'>Quick Stats</div>", unsafe_allow_html=True)
    st.metric("Projects", "3+", "portfolio")
    st.metric("Experience", "4 roles", "professional")
    st.metric("Location", "Cebu", "PH")

    st.divider()
    show_anim = st.toggle("Celebrations", value=True)

# ─────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────
def sh(eyebrow, heading):
    st.markdown(f'<div class="sec-eyebrow">{eyebrow}</div><div class="sec-heading">{heading}</div>', unsafe_allow_html=True)

def make_tags(lst):
    return "".join(f'<span class="tag">{t}</span>' for t in lst)

def skill_bar(name, pct):
    st.markdown(f"""
    <div class="skill-row">
        <div class="skill-label">
            <span class="skill-name">{name}</span>
            <span class="skill-pct">{pct}%</span>
        </div>
        <div class="skill-track">
            <div class="skill-fill" style="width:{pct}%;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def proj_card(proj):
    pill_map = {"Live": "pill-live", "Beta": "pill-beta", "WIP": "pill-wip"}
    pill_class = pill_map.get(proj["status"], "pill-live")
    tags_html = make_tags(proj["tags"])
    img_html = (
        f'<img src="{proj["img_url"]}" class="proj-card-img" alt="{proj["name"]} preview">'
        if proj.get("img_url")
        else '<div class="proj-card-img-placeholder"></div>'
    )
    link = proj.get("link", "#")
    st.markdown(f"""
    <div class="proj-card">
        {img_html}
        <div class="proj-card-body">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:6px;">
                <div>
                    <div class="proj-card-title">{proj['name']}</div>
                    <div class="proj-card-meta">{proj['cat']}</div>
                </div>
                <span class="{pill_class}">{proj['status']}</span>
            </div>
            <p class="proj-card-desc">{proj['desc']}</p>
            <div style="margin-bottom:14px;">{tags_html}</div>
            <a href="{link}" target="_blank" style="
                display:inline-block;background:#f0ede8;color:#0e0e0e;
                border-radius:8px;padding:7px 18px;font-size:0.72rem;font-weight:600;
                letter-spacing:2px;text-transform:uppercase;text-decoration:none;">
                View Project →
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  PROJECT DATA  (sorted newest → oldest)
# ─────────────────────────────────────────────
PROJECTS = [
    {
        "name": "NavU - Campus Navigation App",
        "year": 2025,
        "cat": "Mobile UI / UX Research",
        "desc": "Designed a campus navigation app that caters not only to academic institutions but also to large corporate campuses. Conducted user interviews and usability testing with over 50 participants to validate design decisions.",
        "status": "Live",
        "tags": ["Figma", "UX Research", "Prototyping", "Mobile"],
        "img_url": "https://raw.githubusercontent.com/daas-me/portfolio/main/assets/navu_splash.jpg", 
        "link": "https://www.figma.com/design/h981ildHFNZQXtHN6IOe5o/NavU-Mockup?node-id=0-1&t=WVygcCgq8vdul8Qf-1",   
    },
    {
        "name": "HarborHop - Ferry Booking Platform",
        "year": 2025,
        "cat": "Web App / Front-End Dev",
        "desc": "Built a web application for booking ferry rides between islands in the Philippines. Implemented the front-end using CSS and JavaScript, integrating real-time schedule data using a third-party API, user-friendly booking interface, and admin dashboard.",
        "status": "Live",
        "tags": ["HTML", "CSS", "JavaScript", "Django", "API Integration", "Supabase", "Web App"],
        "img_url": "",
        "link": "https://www.harborhop.onrender.com",
    },
    {
        "name": "Lexicon - Hotel Booking App",
        "year": 2024,
        "cat": "Mobile UI Design / Brand Identity",
        "desc": "Crafted a UI design and brand identity for a hotel booking app that focuses on simple yet sophisticated aesthetics. Created a design system in Figma, developed high-fidelity prototypes, and developed full-scale branding assets including logo, color palette, and typography guidelines.",
        "status": "Live",
        "tags": ["Figma", "Canva", "Accessibility", "Branding", "Mobile Design"],
        "img_url": "",
        "link": "https://www.figma.com/design/Y2TdAsPcxmYgs7MFRCPJ2q/Lexicon---Sabandal?t=WVygcCgq8vdul8Qf-1",
    },
    {
    
        "name": "Author Website - Template Design & Development",
        "year": 2023,
        "cat": "UI / UX Design",
        "desc": "Designed and developed a responsive author website template using HTML, CSS, and JavaScript. The template is fully customizable and includes features like a blog section, contact form, and portfolio showcase.",
        "status": "Live",
        "tags": ["HTML", "CSS", "JavaScript", "Figma", "Web App"],
        "img_url": "",
        "link": "https://www.figma.com/design/nBaoUTHL1nhS3lC43pnrTX/Author-Website?node-id=0-1&t=vZdOKKX48TGTIMee-1",
    },
]
PROJECTS.sort(key=lambda p: p["year"], reverse=True)


# ══════════════════════════════════════════════
#  HOME
# ══════════════════════════════════════════════
if page == "Home":

    st.markdown("""
    <div class="hero">
        <div class="hero-label">
            <i class="fa-solid fa-wand-magic-sparkles" style="margin-right:6px;"></i>
            Portfolio &amp; Biography
        </div>
        <h1 class="hero-name">Dwight Angelo<br>Sabandal</h1>
        <p class="hero-role">UI/UX Designer &amp; Front-End Developer</p>
        <p class="hero-bio">
            I design and build thoughtful digital experiences — from the first sketch
            to deployed code. Based in Cebu, Philippines, I blend research-driven design
            with clean front-end engineering to create interfaces that are both beautiful
            and genuinely usable.
        </p>
        <div class="hero-links">
            <a class="hero-link" href="mailto:sabandaldwightangelo@gmail.com">
                <i class="fa-solid fa-envelope"></i> Email
            </a>
            <a class="hero-link" href="https://www.linkedin.com/in/dwight-angelo-sabandal-b2463b247" target="_blank">
                <i class="fa-brands fa-linkedin"></i> LinkedIn
            </a>
            <a class="hero-link" href="https://www.github.com/daas-me" target="_blank">
                <i class="fa-brands fa-github"></i> GitHub
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Projects", "3+", "delivered")
    k2.metric("Experience", "4 roles", "professional")
    k3.metric("Education", "BSIT", "in progress")
    k4.metric("Location", "Cebu", "Philippines")

    st.divider()

    sh("Expertise", "What I Do")
    d1, d2, d3 = st.columns(3)
    with d1:
        st.markdown("""
        <div class="card" style="text-align:center;padding:2rem 1.5rem;">
            <i class="fa-solid fa-palette" style="color:#4ade80;font-size:2rem;margin-bottom:14px;display:block;"></i>
            <div class="card-title" style="margin-bottom:8px;">UI/UX Design</div>
            <div class="card-body">From Figma wireframes to polished prototypes, I design interfaces that are grounded in how people actually think and behave — not just how they look on a mockup.</div>
        </div>
        """, unsafe_allow_html=True)
    with d2:
        st.markdown("""
        <div class="card" style="text-align:center;padding:2rem 1.5rem;">
            <i class="fa-solid fa-code" style="color:#4ade80;font-size:2rem;margin-bottom:14px;display:block;"></i>
            <div class="card-title" style="margin-bottom:8px;">Front-End Dev</div>
            <div class="card-body">I've been writing HTML, CSS, and JavaScript since 2017. Today I build with React and Python — turning designs into real, working products without needing a middleman.</div>
        </div>
        """, unsafe_allow_html=True)
    with d3:
        st.markdown("""
        <div class="card" style="text-align:center;padding:2rem 1.5rem;">
            <i class="fa-solid fa-comments" style="color:#4ade80;font-size:2rem;margin-bottom:14px;display:block;"></i>
            <div class="card-title" style="margin-bottom:8px;">Client Communication</div>
            <div class="card-body">Years of customer-facing work — from travel sales to lead generation — mean I know how to listen well, manage expectations, and keep projects moving smoothly.</div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    sh("Selected Work", "Featured Projects")
    fp1, fp2 = st.columns(2)
    for i, proj in enumerate(PROJECTS[:2]):
        with (fp1 if i == 0 else fp2):
            proj_card(proj)

    if st.button("See All Projects →", type="primary", use_container_width=True):
        if show_anim:
            st.balloons()
        st.info("Head to the **Portfolio** section in the sidebar to see all projects.")

    st.divider()

    sh("How I Work", "My Process")
    pr1, pr2, pr3, pr4 = st.columns(4)
    steps = [
        ("01", "fa-solid fa-ear-listen",   "Listen", "Every project starts with understanding — the client's goals, the end user's frustrations, and the constraints that actually matter. I ask a lot of questions before touching any tools."),
        ("02", "fa-solid fa-pen-ruler",    "Structure", "I map out user flows, information architecture, and content hierarchy before any visuals. Good structure makes everything downstream easier."),
        ("03", "fa-solid fa-bezier-curve", "Design", "Rough sketches become wireframes, wireframes become prototypes. I test early, iterate often, and only polish when the foundation is solid."),
        ("04", "fa-solid fa-laptop-code",  "Build", "Where possible, I build it myself — HTML, CSS, JavaScript, React, or Python. Handing off to a developer is a last resort, not the default."),
    ]
    for col, (num, icon, title, body) in zip([pr1, pr2, pr3, pr4], steps):
        with col:
            st.markdown(f"""
            <div class="card" style="padding:1.5rem;">
                <div style="font-size:0.65rem;letter-spacing:3px;color:#4ade80;margin-bottom:10px;">{num}</div>
                <i class="{icon}" style="color:#4ade80;font-size:1.3rem;margin-bottom:10px;display:block;"></i>
                <div class="card-title" style="font-size:0.95rem;margin-bottom:6px;">{title}</div>
                <div class="card-body" style="font-size:0.82rem;">{body}</div>
            </div>
            """, unsafe_allow_html=True)

    st.divider()

    sh("Let's Connect", "Open to Opportunities")
    st.markdown("""
    <div class="card" style="padding:2.5rem;text-align:center;background:linear-gradient(135deg,#0d1f0d,#161616);">
        <div style="font-family:Playfair Display,serif;font-size:1.5rem;color:#f0ede8;margin-bottom:0.6rem;">
            Available for freelance &amp; full-time roles
        </div>
        <div style="font-size:0.9rem;color:#8a8680;max-width:480px;margin:0 auto 1.8rem;">
            I'm currently open to UI/UX design and front-end development opportunities —
            remote or based in Cebu. Let's build something great together.
        </div>
        <a href="mailto:sabandaldwightangelo@gmail.com" style="
            display:inline-block;background:#4ade80;color:#0e0e0e;
            border-radius:9px;padding:11px 30px;
            font-size:0.74rem;font-weight:700;letter-spacing:2px;
            text-transform:uppercase;text-decoration:none;">
            Get In Touch →
        </a>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════
#  ABOUT ME
# ══════════════════════════════════════════════
elif page == "About Me":

    sh("Autobiography", "My Story")

    col_bio, col_card = st.columns([3, 2])

    with col_bio:
        st.markdown("""
        <div class="card">
            <p class="card-body">
                Hi — I'm <strong style="color:#d4d0cb;">Dwight Angelo Sabandal</strong>, an aspiring UI/UX designer and
                front-end developer from Cebu, Philippines. My passion sits at the intersection of aesthetics
                and engineering — I believe the best digital products are crafted by people who are equally
                fluent in pixels and code.
            </p>
            <p class="card-body" style="margin-top:1rem;">
                I'm currently pursuing a <strong style="color:#d4d0cb;">Bachelor of Science in Information Technology</strong>
                at Cebu Institute of Technology – University. Over the past year, I've worked across the full product lifecycle —
                from user research and information architecture through high-fidelity Figma prototypes to
                production-ready web and mobile applications.
            </p>
            <p class="card-body" style="margin-top:1rem;">
                Outside of screens, I draw inspiration from architecture, editorial photography, and the quiet
                discipline of calligraphy — influences that show up in the care I give to whitespace, typography,
                and visual hierarchy in my work.
            </p>
            <p class="card-body" style="margin-top:1rem;">
                My core belief: <em style="color:#d4d0cb;">design and development are not separate disciplines —
                they are two sides of the same craft.</em>
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col_card:
        st.markdown(f"""
        <div class="card" style="padding:2rem;">
            <div style="width:70px;height:70px;border-radius:50%;margin:0 auto 1.2rem;overflow:hidden;border:1px solid #4ade8040;">
                <img src="https://raw.githubusercontent.com/daas-me/portfolio/main/assets/sabandal.jpg"
                     style="width:100%;height:100%;object-fit:cover;border-radius:50%;">
            </div>
            <div style="font-family:Playfair Display,serif;font-size:1.15rem;color:#f0ede8;text-align:center;">Dwight Angelo Sabandal</div>
            <div style="color:#4ade80;font-size:0.7rem;letter-spacing:3px;text-transform:uppercase;margin:6px 0 16px;text-align:center;">Designer & Developer</div>
            <hr style="border-color:#2a2a2a;margin-bottom:16px;"/>
            <div style="font-size:0.83rem;color:#6b6560;line-height:2.8;">
                <i class="fa-solid fa-location-dot fa-fw" style="color:#4ade80;margin-right:10px;"></i>Cebu City, Philippines<br>
                <i class="fa-solid fa-graduation-cap fa-fw" style="color:#4ade80;margin-right:10px;"></i>BSIT — CIT-University<br>
                <i class="fa-solid fa-briefcase fa-fw" style="color:#4ade80;margin-right:10px;"></i>1+ Year Work Experience<br>
                <i class="fa-solid fa-language fa-fw" style="color:#4ade80;margin-right:10px;"></i>English · Filipino<br>
                <i class="fa-solid fa-globe fa-fw" style="color:#4ade80;margin-right:10px;"></i>Remote-Friendly<br>
                <i class="fa-solid fa-hammer fa-fw" style="color:#4ade80;margin-right:10px;vertical-align:middle;"></i>Available for Work
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # ── Skills ──
    sh("Proficiency", "Skills & Expertise")

    sk1, sk2, sk3 = st.columns(3)
    with sk1:
        st.markdown('<div class="skill-category-label"><i class="fa-solid fa-palette fa-fw" style="margin-right:6px;"></i>Design</div>', unsafe_allow_html=True)
        skill_bar("UI/UX Design", 92)
        skill_bar("Figma", 90)
        skill_bar("Wireframing", 85)
        skill_bar("Prototyping", 82)
        skill_bar("Design Systems", 75)
        skill_bar("Canva", 95)
    with sk2:
        st.markdown('<div class="skill-category-label"><i class="fa-solid fa-code fa-fw" style="margin-right:6px;"></i>Development</div>', unsafe_allow_html=True)
        skill_bar("HTML / CSS", 92)
        skill_bar("JavaScript", 78)
        skill_bar("React", 55)
        skill_bar("Java", 84)
        skill_bar("Python", 70)
        skill_bar("Streamlit", 65)
    with sk3:
        st.markdown('<div class="skill-category-label"><i class="fa-solid fa-wrench fa-fw" style="margin-right:6px;"></i>Tools & Other</div>', unsafe_allow_html=True)
        skill_bar("Git / GitHub", 80)
        skill_bar("VS Code", 90)
        skill_bar("Jira", 65)
        skill_bar("User Research", 80)
        skill_bar("Communication", 88)
        skill_bar("Problem Solving", 85)

    st.divider()

    # ── Interests ──
    sh("Beyond Work", "Personal Interests")

    interests = [
        ("fa-solid fa-user-astronaut",   "Astronomy", "I enjoy stargazing and astrophotography — a humbling reminder of our place in the universe and a source of endless inspiration for design."),
        ("fa-solid fa-camera",    "Photography", "I have a soft spot for nature and landscape photography. I find that the principles of composition and lighting in photography deeply inform my approach to visual design."),
        ("fa-solid fa-person-hiking", "Hiking/Exploring", "I enjoy exploring the outdoors especially if it is away from the city. I find that being in nature helps me reset and often sparks creative ideas for my design work."),
        ("fa-solid fa-gamepad",   "Gaming", "I play games that are rich in narrative and world-building — I find that well-designed games can teach us a lot about user engagement, feedback loops, and immersive experience design."),
    ]
    i1, i2, i3, i4 = st.columns(4)
    for col, (icon, title, body) in zip([i1, i2, i3, i4], interests):
        with col:
            st.markdown(f"""
            <div class="card" style="text-align:center;padding:1.5rem 1rem;">
                <i class="{icon}" style="color:#4ade80;font-size:1.6rem;margin-bottom:10px;display:block;"></i>
                <div class="card-title" style="font-size:0.92rem;margin-bottom:6px;">{title}</div>
                <div class="card-body" style="font-size:0.8rem;">{body}</div>
            </div>
            """, unsafe_allow_html=True)

    st.divider()

    # ── Education ──
    sh("Academic Background", "Education")

    education = [
        {"title": "Bachelor of Science in Information Technology",
         "org": "Cebu Institute of Technology – University", "year": "Aug 2023 – Present",
         "desc": "Specializing in web systems and UI/UX design."},
        {"title": "Senior High School – STEM Strand",
         "org": "Cebu Institute of Technology – University", "year": "Jun 2019 – Oct 2021",
         "desc": "Graduated with honors."},
        {"title": "Junior High School",
         "org": "St. Mary's Academy – Oslob", "year": "Jun 2015 – Apr 2019",
         "desc": "Consistent honor student. Taught computer subject as a student teacher."},
        {"title": "Elementary",
         "org": "Oslob Central Elementary School", "year": "Jun 2009 – Apr 2015", "desc": ""},
    ]

    for educ in education:
        st.markdown(f"""
        <div class="tl">
            <div class="tl-yr">{educ['year']}</div>
            <div class="tl-title">{educ['title']}</div>
            <div class="tl-org">{educ['org']}</div>
            {"" if not educ['desc'] else f'<div class="tl-desc">{educ["desc"]}</div>'}
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # ── Certifications ──
    sh("Credentials", "Certifications")

    certs = [
        ("fa-solid fa-certificate", "Java Object-Oriented Programming Certification",  "CodeChum · May 2025"),
        ("fa-solid fa-certificate", "Data Visualization",  "Kaggle · December 2025"),
        ("fa-solid fa-certificate", "ICT Student Congress 2025", "PSiTE7 · May 2025"),
        ("fa-solid fa-certificate", "Graphic Design Essentials", "Canva · September 2024"),
        ("fa-solid fa-certificate", "Introduction to Java", "Sololearn · May 2025"),
        ("fa-solid fa-certificate", "Digital Marketing", "HubSpot Academy · April 2025 - May 2026"),
    ]
    c1, c2 = st.columns(2)
    for i, (icon, title, sub) in enumerate(certs):
        with (c1 if i % 2 == 0 else c2):
            st.markdown(f"""
            <div class="cert-card">
                <i class="{icon} cert-icon"></i>
                <div>
                    <div class="cert-title">{title}</div>
                    <div class="cert-sub">{sub}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

# ══════════════════════════════════════════════
#  PORTFOLIO
# ══════════════════════════════════════════════
elif page == "Portfolio":

    sh("Portfolio", "Selected Projects")

    all_years = sorted(set(p["year"] for p in PROJECTS), reverse=True)
    year_options = ["All"] + [str(y) for y in all_years]

    filter_col, _, count_col = st.columns([2, 3, 2])
    with filter_col:
        selected = st.selectbox("Filter by year", year_options, label_visibility="collapsed")
    with count_col:
        filtered = PROJECTS if selected == "All" else [p for p in PROJECTS if str(p["year"]) == selected]
        st.markdown(f"""
        <div style="text-align:right;padding-top:8px;font-size:0.75rem;color:#6b6560;letter-spacing:2px;text-transform:uppercase;">
            {len(filtered)} project{"s" if len(filtered) != 1 else ""}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom:0.5rem;'></div>", unsafe_allow_html=True)

    if filtered:
        cols_per_row = 2
        for row_start in range(0, len(filtered), cols_per_row):
            row_items = filtered[row_start: row_start + cols_per_row]
            cols = st.columns(cols_per_row)
            for col, proj in zip(cols, row_items):
                with col:
                    proj_card(proj)
    else:
        st.info(f"No projects found for {selected}.")


# ══════════════════════════════════════════════
#  EXPERIENCE
# ══════════════════════════════════════════════
elif page == "Experience":

    sh("Work Experience", "My Career Journey")

    experiences = [
        {
            "year": "July 2025 – October 2025",
            "title": "Travel Sales Representative",
            "org": "Dyninno — Cebu City",
            "desc": "Assisted customers in booking travel arrangements, providing excellent service and support. Handled inquiries, resolved issues, and contributed to a positive customer experience.",
            "tags": ["Customer Service", "Travel Planning", "Sales", "Problem Solving"],
        },
        {
            "year": "October 2022 – June 2023",
            "title": "Lead Generation Specialist",
            "org": "Worldwide Innovative Publications — Oslob, Cebu",
            "desc": "Generated and qualified leads for the sales team through targeted outreach and research. Utilized CRM tools to track interactions and optimize lead conversion strategies.",
            "tags": ["CRM", "Lead Qualification", "Sales Enablement", "Data Analysis"],
        },
        {
            "year": "January 2022 – July 2022",
            "title": "Merchandise Checker",
            "org": "Gaisano Grand Mall — Oslob, Cebu",
            "desc": "Ensured accurate pricing and labeling of merchandise, checked for item damage, and maintained inventory records. Interacted with customers to assist with product inquiries.",
            "tags": ["Attention to Detail", "Customer Service", "Inventory Management", "Problem Solving"],
        },
        {
            "year": "August 2017 – Present",
            "title": "Freelance Designer & Developer",
            "org": "Self-Employed",
            "desc": "Designed and developed websites for clients across various industries. Focused on responsive design, user experience, and clean code.",
            "tags": ["UI/UX Design", "Web Development", "Responsive Design", "Client Collaboration"],
        },
    ]

    for exp in experiences:
        tags_html = make_tags(exp["tags"])
        st.markdown(f"""
        <div class="tl">
            <div class="tl-yr">{exp['year']}</div>
            <div class="tl-title">{exp['title']}</div>
            <div class="tl-org">{exp['org']}</div>
            <div class="tl-desc">{exp['desc']}</div>
            <div style="margin-top:10px;">{tags_html}</div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # ── What I Bring ──
    sh("Value Proposition", "What I Bring to a Team")

    v1, v2, v3 = st.columns(3)
    values = [
        ("fa-solid fa-arrows-left-right", "Design + Dev Fluency",
         "I bridge both worlds — from high-fidelity Figma prototypes to production-ready front-end code. No handoff friction, no lost-in-translation moments."),
        ("fa-solid fa-headset",           "People-First Communicator",
         "Years of customer-facing roles in sales and service have sharpened my ability to listen actively, communicate clearly, and deliver exactly what people need."),
        ("fa-solid fa-chart-line",        "Detail-Oriented & Data-Aware",
         "A background in lead qualification and inventory management means I bring structured, analytical thinking to every design decision — nothing ships without purpose."),
    ]
    for col, (icon, title, body) in zip([v1, v2, v3], values):
        with col:
            st.markdown(f"""
            <div class="card" style="text-align:center;padding:1.8rem 1.4rem;">
                <i class="{icon}" style="color:#4ade80;font-size:1.8rem;margin-bottom:12px;display:block;"></i>
                <div class="card-title" style="font-size:0.95rem;margin-bottom:8px;">{title}</div>
                <div class="card-body" style="font-size:0.82rem;">{body}</div>
            </div>
            """, unsafe_allow_html=True)

    st.divider()

    # ── Tools ──
    sh("Toolkit", "Tools I Use Daily")

    tools = {
        "Design":      ["Figma", "Canva", "Adobe Illustrator", "Blender"],
        "Development": ["HTML / CSS", "JavaScript", "React", "VS Code"],
        "Workflow":    ["Git", "GitHub", "Jira", "Streamlit"],
        "Sales & CRM": ["CRM Tools", "Google Forms", "Google Sheets", "HubSpot"],
    }
    t1, t2, t3, t4 = st.columns(4)
    for col, (category, tool_list) in zip([t1, t2, t3, t4], tools.items()):
        with col:
            items_html = "".join(
                f'<div style="background:#1e1e1e;border:1px solid #2a2a2a;border-radius:8px;padding:8px 12px;margin-bottom:6px;font-size:0.82rem;color:#d4d0cb;">{t}</div>'
                for t in tool_list
            )
            st.markdown(f"""
            <div class="card" style="padding:1.2rem;">
                <div class="skill-category-label" style="margin-top:0;">{category}</div>
                {items_html}
            </div>
            """, unsafe_allow_html=True)

    st.divider()

    # ── Resume Download ──
    with open("assets/sabandal_cv.pdf", "rb") as f:
        pdf_data = f.read()

    st.download_button(
        label="⬇  Download Resume",
        data=pdf_data,
        file_name="sabandal_cv.pdf",
        mime="application/pdf",
        use_container_width=True,
    )


# ══════════════════════════════════════════════
#  CONTACT
# ══════════════════════════════════════════════
elif page == "Contact":

    sh("Let's Talk", "Get In Touch")

    st.markdown("""
    <div class="card" style="padding:1.5rem 2rem;">
        <p class="card-body" style="font-size:0.92rem;">
            Whether you have a project in mind, a role to fill, or just want to say hello —
            I'd love to hear from you. I typically respond within 24 hours.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="card" style="text-align:center;padding:1.8rem;">
            <i class="fa-solid fa-envelope" style="font-size:1.8rem;color:#4ade80;margin-bottom:10px;display:block;"></i>
            <div class="card-title" style="font-size:0.9rem;margin-bottom:6px;">Email</div>
            <div style="font-size:0.78rem;color:#8a8680;">sabandaldwightangelo@gmail.com</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card" style="text-align:center;padding:1.8rem;">
            <i class="fa-brands fa-linkedin" style="font-size:1.8rem;color:#4ade80;margin-bottom:10px;display:block;"></i>
            <div class="card-title" style="font-size:0.9rem;margin-bottom:6px;">LinkedIn</div>
            <div style="font-size:0.78rem;color:#8a8680;">dwight-angelo-sabandal-b2463b247</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="card" style="text-align:center;padding:1.8rem;">
            <i class="fa-brands fa-github" style="font-size:1.8rem;color:#4ade80;margin-bottom:10px;display:block;"></i>
            <div class="card-title" style="font-size:0.9rem;margin-bottom:6px;">GitHub</div>
            <div style="font-size:0.78rem;color:#8a8680;">github.com/daas-me</div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    with st.form("contact_form"):
        st.markdown('<div class="sec-eyebrow">Direct Message</div><div style="font-family:Playfair Display,serif;font-size:1.4rem;color:#f0ede8;margin-bottom:1.2rem;">Send a Message</div>', unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Your Name *", placeholder="Jane Smith")
        with c2:
            email = st.text_input("Your Email *", placeholder="jane@example.com")

        subject = st.selectbox("Subject", [
            "Freelance Project", "Full-Time Opportunity", "Collaboration", "General Question", "Just Saying Hi",
        ])
        message = st.text_area("Message *", placeholder="Tell me about your project, timeline, and what you're looking for...", height=160)
        attachment = st.file_uploader("Attach a file (optional)", type=["pdf", "jpg", "png"])

        col_check, col_date = st.columns([2, 1])
        with col_check:
            agree = st.checkbox("I confirm I'm not a robot 🤖")
        with col_date:
            preferred_date = st.date_input("Preferred response by (optional)")

        submitted = st.form_submit_button("Send Message →", type="primary", use_container_width=True)

        if submitted:
            if not name or not email or not message:
                st.error("Please fill in all required fields (Name, Email, Message).")
            elif not agree:
                st.error("Please confirm you're human!")
            elif "@" not in email or "." not in email:
                st.error("Please enter a valid email address.")
            else:
                st.success(f"Thanks, {name.split()[0]}! Your message has been sent — I'll get back to you soon.")
                if show_anim:
                    st.balloons()

    st.divider()


# ── Footer ──
st.markdown("""
<div style="text-align:center;padding:1rem 0 0.5rem;font-size:0.72rem;color:#3a3a3a;letter-spacing:2px;">
    © 2026 DWIGHT ANGELO SABANDAL &nbsp;
</div>
""", unsafe_allow_html=True)