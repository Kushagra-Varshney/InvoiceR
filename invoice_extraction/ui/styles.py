"""
styles.py
Custom CSS for the Invoice Parser Streamlit app.
"""

import streamlit as st

CUSTOM_CSS = """
<style>
    .main, .stApp { background-color: #0f1117; }

    .header-box {
        background: linear-gradient(135deg, #1a1f2e, #252d3d);
        border: 1px solid #2d3748; border-radius: 12px;
        padding: 24px 32px; margin-bottom: 24px;
    }
    .header-box h1 { color: #e2e8f0; font-size: 28px; margin: 0 0 4px 0; }
    .header-box p  { color: #718096; margin: 0; font-size: 14px; }

    .status-box {
        background: #1a1f2e; border: 1px solid #2d3748;
        border-radius: 8px; padding: 14px 18px;
        margin: 8px 0; font-size: 14px; color: #a0aec0;
    }
    .status-ok   { border-left: 3px solid #48bb78; }
    .status-err  { border-left: 3px solid #fc8181; }
    .status-warn { border-left: 3px solid #f6ad55; }

    .metric-card {
        background: #1a1f2e; border: 1px solid #2d3748;
        border-radius: 10px; padding: 16px 20px; text-align: center;
    }
    .metric-card .val { font-size: 26px; font-weight: 700; color: #63b3ed; }
    .metric-card .lbl { font-size: 12px; color: #718096; margin-top: 4px; }

    .stButton > button {
        background: linear-gradient(135deg, #3182ce, #2b6cb0);
        color: white; border: none; border-radius: 8px;
        padding: 10px 24px; font-weight: 600; width: 100%;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #2b6cb0, #2c5282);
    }
</style>
"""


def apply_styles() -> None:
    """Inject custom CSS into the Streamlit page."""
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
