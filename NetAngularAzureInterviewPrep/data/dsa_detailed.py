"""Merge DSA detailed content parts."""

from data.dsa_detailed_part1 import DSA_DETAILED_PART1
from data.dsa_detailed_part2 import DSA_DETAILED_PART2

DSA_DETAILED: dict[str, dict] = {**DSA_DETAILED_PART1, **DSA_DETAILED_PART2}
