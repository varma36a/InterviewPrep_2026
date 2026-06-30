"""Dedicated DSA section — Love Babbar 450 problems topic-wise with TC/SC."""


def apply_dsa_section(sections: dict, detailed: dict) -> None:
    """Register Love Babbar 450 DSA section with detailed time/space complexity."""
    from data.dsa_450_catalog import DSA_450_SECTION
    from data.dsa_450_detailed import DSA_450_DETAILED

    detailed.update(DSA_450_DETAILED)
    sections["dsa"] = DSA_450_SECTION
