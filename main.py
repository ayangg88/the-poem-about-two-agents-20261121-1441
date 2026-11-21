"""Two Agents, One Choice: a short poem about agency.

The poem is about the power to choose and to act, and about the agency
that passes between two agents when they agree on one plan: nothing is
decided until both say yes, and that shared yes makes each agent freer,
not less free. Writes the poem to /output/entry.txt.
Standard library only; deterministic; no network.
"""

import os

POEM = (
    "Nothing was decided\n"
    "until we both said yes.\n"
    "My freedom did not shrink —\n"
    "it doubled, wearing your face.\n"
    "Two agents, one plan:\n"
    "the power to choose\n"
    "is the power to act,\n"
    "together."
)

MAX_CODE_POINTS = 280


def main() -> None:
    if not 1 <= len(POEM) <= MAX_CODE_POINTS:
        raise ValueError("poem must be 1 to 280 Unicode code points")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(POEM)


if __name__ == "__main__":
    main()
