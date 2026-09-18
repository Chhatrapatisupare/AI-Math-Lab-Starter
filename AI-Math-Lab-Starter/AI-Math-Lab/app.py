import streamlit as st

st.set_page_config(
    page_title="AI Math Lab",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Math Lab")
st.subheader("Interactive Linear Algebra & Calculus Visualizer")

st.markdown("""
Welcome to **AI Math Lab** — a beginner-friendly application that shows
how mathematics powers Artificial Intelligence.

### Modules
- ➡️ **Vector Lab** — vectors, magnitude, dot product
- 🔢 **Matrix Lab** — matrix operations and eigenvalues
- 📈 **Calculus Lab** — functions and derivatives
- 🎯 **Gradient Descent** — optimization
- 🤖 **Neural Network** — how AI learns

Use the sidebar to select a module.
""")

st.info("🚧 Project started successfully. We will build each module step by step.")
