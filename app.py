import os
import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt
from core.network_element import NetworkElement

st.set_page_config(page_title="NetGuard-Suite Europe", layout="wide")

_APP_DIR = os.path.dirname(os.path.abspath(__file__))
_DEVICES_JSON = os.path.join(_APP_DIR, "devices.json")

st.title("🛡️ NetGuard-Suite: European Infrastructure Monitoring")
st.caption("Educational NOC view: inventory from JSON, simulated SNMP-style scan.")
st.caption("Brief random offline blips (~2s) that clear on the next scan.")
st.caption("Synthetic UDP/TCP/ICMP flows — no background simulator or raw sockets.")

# Bump when devices.json shape or inventory logic changes (clears Streamlit cache)
_INVENTORY_SESSION_VERSION = 3

if st.session_state.get("_inventory_session_version") != _INVENTORY_SESSION_VERSION:
    st.session_state.pop("inventory", None)
    st.session_state["_inventory_session_version"] = _INVENTORY_SESSION_VERSION