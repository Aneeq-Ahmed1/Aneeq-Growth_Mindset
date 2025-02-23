# import streamlit as st
# import random
# import time
# import pandas as pd
# import plotly.express as px
# from streamlit_lottie import st_lottie
# import requests
# import sys
# import subprocess

# # Page configuration
# st.set_page_config(
#     page_title="Ultimate Growth Mindset Challenge",
#     page_icon="🚀",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Custom CSS styling (Black & White Theme with modern look)
# st.markdown("""
# <style>
# [data-testid="stAppViewContainer"] {
#     background: #f5f5f5;
#     color: #000000;
# }

# .stButton>button {
#     background: #2a2a2a !important;
#     color: #FFD700 !important;
#     border: 1px solid #FFD700 !important;
#     transition: all 0.3s ease !important;
# }

# .stButton>button:hover {
#     background: #FFD700 !important;
#     color: #000000 !important;
# }

# .motivation-quote {
#     border-left: 3px solid #000000;
#     padding: 15px;
#     margin: 20px 0;
#     background: #e0e0e0;
#     border-radius: 5px;
#     font-style: italic;
# }

# .stProgress > div > div > div {
#     background-color: #000000 !important;
# }
# </style>
# """, unsafe_allow_html=True)

# # Lottie animations setup
# def load_lottieurl(url):
#     r = requests.get(url)
#     return r.json() if r.status_code == 200 else None

# celebration_anim = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_5njp3vgg.json")
# focus_anim = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_tno6cg2w.json")

# # Session state initialization
# if 'progress_history' not in st.session_state:
#     st.session_state.progress_history = []

# if 'challenges' not in st.session_state:
#     st.session_state.challenges = [
#         {"task": "Learn one new Python concept", "completed": False},
#         {"task": "Solve a coding problem", "completed": False},
#         {"task": "Read tech article for 30 mins", "completed": False},
#         {"task": "Practice debugging", "completed": False}
#     ]

# if 'current_quote' not in st.session_state:
#     st.session_state.current_quote = random.choice([
#         "The only way to do great work is to love what you do. - Steve Jobs",
#         "Success is not final, failure is not fatal: It is the courage to continue that counts. - Churchill",
#         "The harder you work for something, the greater you'll feel when you achieve it. - Unknown"
#     ])

# if 'weekly_goal' not in st.session_state:
#     st.session_state.weekly_goal = ""

# # Progress visualization function
# def show_progress_chart():
#     if st.session_state.progress_history:
#         df = pd.DataFrame(st.session_state.progress_history, columns=["Date", "Progress"])
#         fig = px.line(df, x="Date", y="Progress", title="Your Progress Journey", markers=True, line_shape="spline")
#         fig.update_layout(plot_bgcolor="#ffffff", paper_bgcolor="#f5f5f5", font_color="#000000")
#         st.plotly_chart(fig, use_container_width=True)

# # Main app layout
# st.title("🚀 Ultimate Growth Mindset Challenge")
# st.markdown("---")

# # Motivation Section
# col1, col2 = st.columns([3, 1])
# with col1:
#     st.header("Daily Motivation 💪")
#     st.markdown(f'<div class="motivation-quote">✨ {st.session_state.current_quote}</div>', unsafe_allow_html=True)

# with col2:
#     st_lottie(focus_anim, height=150, key="focus_anim")
#     if st.button("New Motivation 🌟"):
#         st.session_state.current_quote = random.choice([
#             "Every expert was once a beginner. - Aristotle",
#             "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
#             "The secret of getting ahead is getting started. - Mark Twain"
#         ])
#         st.rerun()

# # Weekly Goal Section
# st.markdown("---")
# st.header("🎯 Set Your Weekly Goal")
# st.session_state.weekly_goal = st.text_input("This week's goal:", value=st.session_state.weekly_goal, key="weekly_goal_input")

# # Progress Section
# st.markdown("---")
# st.header("📈 Your Progress Dashboard")
# completed_tasks = sum(1 for c in st.session_state.challenges if c["completed"])
# total_tasks = len(st.session_state.challenges)

# col1, col2 = st.columns([2, 3])
# with col1:
#     st.subheader("Daily Progress")
#     progress = completed_tasks / total_tasks if total_tasks > 0 else 0
#     st.progress(progress)

#     if completed_tasks == total_tasks and celebration_anim:
#         st_lottie(celebration_anim, height=200, key="celebration")

# with col2:
#     show_progress_chart()

# # Challenges Section
# st.markdown("---")
# st.header("✅ Daily Challenges with Reflections & Difficulty Ratings")

# for i, challenge in enumerate(st.session_state.challenges):
#     completed = st.checkbox(
#         challenge["task"], 
#         value=challenge["completed"],
#         key=f"challenge_{i}",
#         on_change=lambda i=i: (
#             st.session_state.challenges[i].update({"completed": not st.session_state.challenges[i]["completed"]}),
#             st.session_state.progress_history.append((time.strftime("%Y-%m-%d"), sum(1 for c in st.session_state.challenges if c["completed"]) / len(st.session_state.challenges)))
#         )
#     )

#     # Reflection Input (unique key to avoid duplication)
#     st.text_input("Reflection:", placeholder="Write your thoughts here...", key=f"reflection_{i}")

#     # Difficulty Slider (unique key)
#     st.slider("Rate difficulty:", 1, 5, value=3, key=f"difficulty_{i}")
#     st.markdown("---")

# # Coding Challenges Section
# st.header("💻 Coding Challenges")

# coding_challenges = {
#     "Easy": [
#         ("FizzBuzz", "Write a program that prints numbers from 1 to 100, but multiples of 3 print 'Fizz', multiples of 5 print 'Buzz'"),
#         ("Palindrome Check", "Write a function to check if a given string is a palindrome")
#     ],
#     "Medium": [
#         ("Fibonacci Sequence", "Generate the first N Fibonacci numbers using recursion"),
#         ("Prime Number Check", "Create a function to check if a number is prime efficiently")
#     ],
#     "Hard": [
#         ("Binary Search Tree", "Implement a binary search tree with insertion and traversal methods"),
#         ("Sorting Algorithm", "Implement merge sort or quick sort algorithm from scratch")
#     ]
# }

# difficulty = st.selectbox("Select Difficulty Level", list(coding_challenges.keys()), key="challenge_difficulty")
# challenge = st.selectbox("Select Challenge", [c[0] for c in coding_challenges[difficulty]], key="challenge_name")

# selected_description = [c[1] for c in coding_challenges[difficulty] if c[0] == challenge][0]
# st.markdown(f"**Challenge Description:**  {selected_description}")

# # Code Editor
# st.subheader("Code Playground 🛠️")
# user_code = st.text_area("Write your Python code here:", height=300, key="editor")

# if st.button("Run Code 🚀"):
#     try:
#         with st.spinner("Executing code..."):
#             with open("temp_code.py", "w") as f:
#                 f.write(user_code)

#             result = subprocess.run(
#                 [sys.executable, "temp_code.py"],
#                 capture_output=True,
#                 text=True,
#                 timeout=10
#             )

#             st.subheader("Execution Results:")
#             if result.stdout:
#                 st.success(result.stdout)
#             if result.stderr:
#                 st.error(result.stderr)
#     except Exception as e:
#         st.error(f"Error: {str(e)}")

# st.markdown("---")
# st.markdown("🔥 **Keep Growing:** Track your progress daily and watch your skills improve!")



































import streamlit as st
import random
import time
import pandas as pd
import plotly.express as px
from streamlit_lottie import st_lottie
import requests
import sys
import subprocess
from io import BytesIO


st.set_page_config(
    page_title="Ultimate Growth Mindset Challenge",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS 
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: #f5f5f5;
    color: #000000;
}

.stButton>button {
    background: #2a2a2a !important;
    color: #FFD700 !important;
    border: 1px solid #FFD700 !important;
    transition: all 0.3s ease !important;
}

.stButton>button:hover {
    background: #FFD700 !important;
    color: #000000 !important;
}

.motivation-quote {
    border-left: 3px solid #000000;
    padding: 15px;
    margin: 20px 0;
    background: #e0e0e0;
    border-radius: 5px;
    font-style: italic;
}

.stProgress > div > div > div {
    background-color: #000000 !important;
}
</style>
""", unsafe_allow_html=True)

#Lottie ani
def load_lottieurl(url):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

celebration_anim = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_5njp3vgg.json")
focus_anim = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_tno6cg2w.json")

# Initialize session state
if 'progress_history' not in st.session_state:
    st.session_state.progress_history = []

if 'challenges' not in st.session_state:
    st.session_state.challenges = [
        {"task": "Learn one new Python concept", "completed": False, "reflection": "", "difficulty": 3},
        {"task": "Solve a coding problem", "completed": False, "reflection": "", "difficulty": 3},
        {"task": "Read tech article for 30 mins", "completed": False, "reflection": "", "difficulty": 3},
        {"task": "Practice debugging", "completed": False, "reflection": "", "difficulty": 3}
    ]

if 'current_quote' not in st.session_state:
    st.session_state.current_quote = random.choice([
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Churchill",
        "The harder you work for something, the greater you'll feel when you achieve it. - Unknown"
    ])

if 'weekly_goal' not in st.session_state:
    st.session_state.weekly_goal = ""

# Show progress chart
def show_progress_chart():
    if st.session_state.progress_history:
        df = pd.DataFrame(st.session_state.progress_history, columns=["Date", "Progress"])
        fig = px.line(df, x="Date", y="Progress", title="Your Progress Journey", markers=True, line_shape="spline")
        fig.update_layout(plot_bgcolor="#ffffff", paper_bgcolor="#f5f5f5", font_color="#000000")
        st.plotly_chart(fig, use_container_width=True)

# Generate downloadable report
def generate_report():
    data = [{
        "Task": challenge["task"],
        "Completed": "Yes" if challenge["completed"] else "No",
        "Reflection": challenge["reflection"],
        "Difficulty": challenge["difficulty"]
    } for challenge in st.session_state.challenges]
    
    df = pd.DataFrame(data)
    buffer = BytesIO()
    df.to_csv(buffer, index=False)
    buffer.seek(0)
    return buffer

# Run user code safely
def execute_user_code(code):
    try:
        with st.spinner("Executing code..."):
            with open("temp_code.py", "w") as f:
                f.write(code)
            
            result = subprocess.run(
                [sys.executable, "temp_code.py"],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            st.subheader("Execution Results:")
            if result.stdout:
                st.success(result.stdout)
            if result.stderr:
                st.error(result.stderr)
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Layout setup
st.title("🚀 Ultimate Growth Mindset Challenge")
st.markdown("---")

# Motivation section
col1, col2 = st.columns([3, 1])
with col1:
    st.header("Daily Motivation 💪")
    st.markdown(f'<div class="motivation-quote">✨ {st.session_state.current_quote}</div>', unsafe_allow_html=True)

with col2:
    st_lottie(focus_anim, height=150, key="focus_anim")
    if st.button("New Motivation 🌟"):
        st.session_state.current_quote = random.choice([
            "Every expert was once a beginner. - Aristotle",
            "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
            "The secret of getting ahead is getting started. - Mark Twain"
        ])
        st.rerun()

# Weekly goal section
st.markdown("---")
st.header("🎯 Set Your Weekly Goal")
st.session_state.weekly_goal = st.text_input("This week's goal:", value=st.session_state.weekly_goal, key="weekly_goal_input")

# Progress section
st.markdown("---")
st.header("📈 Your Progress Dashboard")
completed_tasks = sum(1 for c in st.session_state.challenges if c["completed"])
total_tasks = len(st.session_state.challenges)

col1, col2 = st.columns([2, 3])
with col1:
    st.subheader("Daily Progress")
    progress = completed_tasks / total_tasks if total_tasks > 0 else 0
    st.progress(progress)

    if completed_tasks == total_tasks and celebration_anim:
        st_lottie(celebration_anim, height=200, key="celebration")

with col2:
    show_progress_chart()

# Daily challenges section
st.markdown("---")
st.header("✅ Daily Challenges with Reflections & Difficulty Ratings")

for i, challenge in enumerate(st.session_state.challenges):
    completed = st.checkbox(
        challenge["task"], 
        value=challenge["completed"],
        key=f"challenge_{i}",
        on_change=lambda i=i: (
            st.session_state.challenges[i].update({"completed": not st.session_state.challenges[i]["completed"]}),
            st.session_state.progress_history.append((time.strftime("%Y-%m-%d"), sum(1 for c in st.session_state.challenges if c["completed"]) / len(st.session_state.challenges)))
        )
    )

    reflection = st.text_input("Reflection:", value=challenge["reflection"], placeholder="Write your thoughts here...", key=f"reflection_{i}")
    st.session_state.challenges[i]["reflection"] = reflection

    difficulty = st.slider("Rate difficulty:", 1, 5, value=challenge["difficulty"], key=f"difficulty_{i}")
    st.session_state.challenges[i]["difficulty"] = difficulty

    st.markdown("---")

# Coding challenges section
st.header("💻 Coding Challenges")

coding_challenges = {
    "Easy": [
        ("FizzBuzz", "Write a program that prints numbers from 1 to 100, but multiples of 3 print 'Fizz', multiples of 5 print 'Buzz'"),
        ("Palindrome Check", "Write a function to check if a given string is a palindrome")
    ],
    "Medium": [
        ("Fibonacci Sequence", "Generate the first N Fibonacci numbers using recursion"),
        ("Prime Number Check", "Create a function to check if a number is prime efficiently")
    ],
    "Hard": [
        ("Binary Search Tree", "Implement a binary search tree with insertion and traversal methods"),
        ("Sorting Algorithm", "Implement merge sort or quick sort algorithm from scratch")
    ]
}

difficulty = st.selectbox("Select Difficulty Level", list(coding_challenges.keys()))
challenge = st.selectbox("Select Challenge", [c[0] for c in coding_challenges[difficulty]])
selected_description = [c[1] for c in coding_challenges[difficulty] if c[0] == challenge][0]

st.markdown(f"**Challenge Description:**\n\n{selected_description}")

st.subheader("Code Playground 🛠️")
user_code = st.text_area("Write your Python code here:", height=300, key="editor")

if st.button("Run Code 🚀"):
    execute_user_code(user_code)

# Download report button
st.header("📄 Download Your Progress Report")
report = generate_report()
st.download_button(
    label="Download Report as CSV 📥",
    data=report,
    file_name="growth_mindset_report.csv",
    mime="text/csv"
)

st.markdown("🔥 **Keep Growing:** Track your progress daily and watch your skills improve!")
st.markdown("Created By Aneeq Ahmed")