"""
Synthetic inter-node traffic for the Net-Inspector (UDP / TCP / ICMP-style rows).

Pure Python: no sockets, no threads. The dashboard calls ``generate_synthetic_flows``
via ``NetworkElement.start_sniffing``.

Run this file directly to print a small sample (optional sanity check):

    python -m sim.traffic_generator
"""

from __future__ import annotations

import random
from typing import List, Optional, Sequence, Tuple

# Display-only destination ports for UDP/TCP rows (ICMP has no L4 port — omitted)
_MOCK_UDP_PORT_OFFSET = 10000
_MOCK_TCP_PORT_OFFSET = 15000

# Default mix for the pie chart (UDP / TCP / ICMP)
_PROTOCOL_WEIGHTS = (0.38, 0.42, 0.20)


def main():
    pass


if __name__ == "__main__":
    main()
