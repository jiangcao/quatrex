# Copyright (c) 2024-2026 ETH Zurich and the authors of the quatrex package.
import json
from pathlib import Path

EXPECTED_MIN_INLINE_PNG_CELLS = 2


def test_contact_surface_notebook_contains_inline_figure_outputs() -> None:
    notebook_path = (
        Path(__file__).resolve().parents[3]
        / "docs/user_guide/examples/jupyter/contact_surface_greens_function_study.ipynb"
    )

    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))

    image_output_cells = [
        cell
        for cell in notebook["cells"]
        if cell.get("cell_type") == "code"
        and any(
            output.get("output_type") == "display_data"
            and "image/png" in output.get("data", {})
            for output in cell.get("outputs", [])
        )
    ]

    assert len(image_output_cells) >= EXPECTED_MIN_INLINE_PNG_CELLS
