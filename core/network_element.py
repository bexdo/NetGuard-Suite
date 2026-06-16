"""Logical network node: simulated SNMP-style metrics; traffic rows from ``sim``."""

import random
import time
from typing import List, Optional

from sim.traffic_generator import generate_synthetic_flows

# Brief simulated outage: each scan, a small chance the node stays “down” for a few seconds.
_OUTAGE_PROBABILITY = 0.14
_OUTAGE_MIN_SECONDS = 1.5
_OUTAGE_MAX_SECONDS = 3.5


class NetworkElement:
    pass