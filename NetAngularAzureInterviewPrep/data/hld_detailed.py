"""Merge HLD detailed content."""

from data.hld_detailed_part1 import HLD_DETAILED_PART1
from data.hld_detailed_part2 import HLD_DETAILED_PART2

HLD_DETAILED: dict[str, dict] = {**HLD_DETAILED_PART1, **HLD_DETAILED_PART2}
