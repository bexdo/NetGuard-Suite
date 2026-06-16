# NetGuard-Suite

## European network monitoring lab

A **Streamlit dashboard** loads an inventory from **`devices.json`**, runs a **simulated SNMP-style scan** (latency, uptime, CPU — all computed in Python), and a **Net-Inspector** view that builds **synthetic inter-node traffic** (UDP, TCP, and ICMP-style rows) using only addresses from your inventory. The same tables and pie chart as before, without **sockets** or **threads** in the learning path.

---

## For teachers (student brief, no solution)

A printable **project specification in Italian** (requirements only, no sample code) is in **`docs/Brief_Progetto_NetGuard_Studenti.pdf`**. **Architecture** (classes, methods, dashboard, Streamlit / TCP-UDP-ICMP / **SNMP** primers) is in **`docs/NetGuard_Suite_Architecture.pdf`** (English). To rebuild either PDF, see **`docs/README.md`**.

---

## What this project does

| Area | Description |
|------|-------------|
| **Inventory** | `devices.json` lists logical nodes (hostname, IP, `snmp_port`, `uptime_base`, `cpu_base`). |
| **Dashboard** | `app.py` — node table, scan button, per-node synthetic capture, protocol pie chart. |
| **Core model** | `core/network_element.py` — `NetworkElement` (`check_status`, `fetch_snmp_data`, `start_sniffing`). |
| **Traffic generator** | `sim/traffic_generator.py` — `generate_synthetic_flows()` builds UDP/TCP/ICMP-style rows (pure `random`, no sockets). |

**One command:** `streamlit run app.py` (no second terminal).

Optional: `python -m sim.traffic_generator` prints a short sample of generated rows.

---

## Repository layout

```
NetGuard-Suite/
├── app.py                 # Streamlit UI
├── devices.json           # Device inventory ({"devices": [ ... ]})
├── requirements.txt       # streamlit, pandas, matplotlib
├── requirements-docs.txt  # Optional: rebuild PowerPoint (python-pptx)
├── core/
│   ├── __init__.py
│   └── network_element.py # NetworkElement class
├── sim/
│   ├── __init__.py
│   └── traffic_generator.py  # generate_synthetic_flows()
└── README.md
```

---

## Requirements

- **Python 3.9+**
- Python packages listed in **`requirements.txt`** (Streamlit, Pandas, Matplotlib)

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## How to run

```bash
streamlit run app.py
```

Open the URL Streamlit prints (usually `http://localhost:8501`).

1. **Run network scan** — fills status, latency, uptime, CPU from simulated logic and `devices.json` hints.
2. Pick a node and **Capture network traffic** — generates a table of UDP/TCP/ICMP-style rows between that node and random peers, plus the pie chart.

---

## `devices.json` format

Top-level object with a **`devices`** array. Each entry typically includes:

- `ip_address` — logical LAN IP (shown in the UI and in flow rows).
- `hostname` — display name.
- `snmp_port` — used to derive **display** destination ports for **UDP** and **TCP** rows only (`snmp_port + 10000` / `+ 15000`). ICMP rows omit **Dst_Port** (ICMP has no port).
- `uptime_base`, `cpu_base` — strings/numbers used when simulating SNMP-style fields.

---

## Design notes

- **Brief random outages**: on each scan, each node has a small chance to enter a **simulated offline** state for about **1.5–3.5 seconds** (wall clock). If you run **scan again** after that window, it can show **Online** again (unless another random outage triggers). The table shows **~Xs** while the blip is active.
- **Traffic is synthetic**: rows look like a capture (source, destination, protocol, length, dst port) but are built with `random` so every run differs slightly.
- **ICMP rows** mimic ping-style summaries (fixed typical length); **Dst_Port** is omitted — ICMP has no TCP/UDP port.

---

