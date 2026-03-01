"""
session.py
Streamlit session state helpers for tracking extraction results and stop requests.
"""

import streamlit as st

from ..invoice_extractor import ExtractionResult


def get_results() -> list[ExtractionResult]:
    return st.session_state.get("results", [])


def set_results(results: list[ExtractionResult]) -> None:
    st.session_state["results"] = results


def clear_results() -> None:
    st.session_state.pop("results", None)


def is_stop_requested() -> bool:
    return st.session_state.get("stop_requested", False)


def request_stop() -> None:
    st.session_state["stop_requested"] = True


def clear_stop() -> None:
    st.session_state["stop_requested"] = False
