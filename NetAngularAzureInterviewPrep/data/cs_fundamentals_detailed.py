"""Merge CS Fundamentals detailed content."""

from data.cs_fundamentals_detailed_part1 import CS_DETAILED_PART1
from data.cs_fundamentals_detailed_part2 import CS_DETAILED_PART2

CS_DETAILED: dict[str, dict] = {**CS_DETAILED_PART1, **CS_DETAILED_PART2}
