"""
sidebar.py
Sidebar configuration panel — API key, model selection, export settings.
"""

import html
import os

import streamlit as st

from ..gemini_manager import GeminiManager


def render_sidebar(default_model: str) -> tuple[str, str, str]:
    """Render the sidebar and return (api_key, model_choice, export_filename)."""
    with st.sidebar:
        st.markdown("### Configuration")

        # Check if key already loaded from .env
        env_key = os.getenv("GOOGLE_API_KEY", "")

        if env_key:
            st.markdown(
                '<div class="status-box status-ok">API key loaded from .env</div>',
                unsafe_allow_html=True,
            )
            api_key = env_key
        else:
            api_key = st.text_input(
                "Gemini API Key",
                type="password",
                placeholder="AIza...",
                help="Or set GOOGLE_API_KEY in your .env file",
            )

        # Validate key and list models
        manager = GeminiManager(api_key=api_key)
        status = manager.check_status()

        if not api_key:
            st.markdown(
                '<div class="status-box status-warn">Enter API key above or add to .env</div>',
                unsafe_allow_html=True,
            )
            model_choice = default_model
        elif status.connected:
            st.markdown(
                '<div class="status-box status-ok">Gemini connected</div>',
                unsafe_allow_html=True,
            )
            default_index = (
                status.available_models.index(default_model) if default_model in status.available_models else 0
            )
            model_choice = st.selectbox("Model", status.available_models, index=default_index)
        else:
            safe_error = html.escape(str(status.error))
            st.markdown(
                f'<div class="status-box status-err">API key invalid<br>{safe_error}</div>',
                unsafe_allow_html=True,
            )
            model_choice = st.text_input("Model name", value=default_model)

        st.markdown("---")
        st.markdown("### Export")
        export_filename = st.text_input("Excel filename", value="invoices_extracted.xlsx")

        st.markdown("---")
        st.markdown("### Setup Guide")
        with st.expander("Steps"):
            st.markdown("""
**1. Get a free Gemini API key**
Go to [aistudio.google.com](https://aistudio.google.com),
sign in and click **Get API Key**.

**2. Add key to .env**
```
GOOGLE_API_KEY=AIza...your_key
```

**3. Install dependencies**
```
pip install -r requirements.txt
```

**4. Run this app**
```
streamlit run invoice_extraction/app.py
```

**Remote access via Tailscale:**
Install Tailscale on both machines,
sign in with same account, then open:
`http://<desktop-ip>:8501`
            """)

    return api_key, model_choice, export_filename, status
