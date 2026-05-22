# Agent instructions: PPTX generation (Lernwoche 2026)

## Default: custom design (no template)

The main deck is built with **`pptx_custom.py`** — modern layout, navy/orange palette, no `template.pptx`.

```bash
python generate_pptx.py
# → output/Lernwoche-2026-Prompting-SW.pptx (mixed-audience deck, 15 slides)

# if the default file is open/locked:
python generate_pptx.py output/Lernwoche-2026-Prompting-SW-mixed-audience-notes.pptx
```

Session content targets KI-Einsteiger through OK-level KI users: kurzer Einstieg → GiGo → CRAFT → Qualitätscheck → 2 Übungen.

## Slide map

| # | Type | Content |
|---|------|---------|
| 1 | Hero | Title, Termin |
| 2 | Agenda | Timed blocks |
| 3 | Chapter | Prompt quality |
| 4 | Insight | KI as assistive tool |
| 5 | Chapter | GiGo |
| 6 | Insight | Input quality |
| 7 | Chapter | CRAFT |
| 8 | CRAFT cards | 5 building blocks |
| 9 | Compare | Bad vs Good prompts |
| 10 | Insight | Hallucinations + quality check |
| 11 | Exercise 1 | Pair, 17 min |
| 12 | Workflow | 4-step coding flow |
| 13 | Exercise 2 | Template + transfer |
| 14 | Takeaway | 3 columns |
| 15 | End | Q&A |

## Legacy: corporate template

[`pptx_lib.py`](pptx_lib.py) + local `template.pptx` (gitignored) remain for corporate master slides if needed — **not** used by `generate_pptx.py` anymore.

## Content sources

- Outline: [`content/outline-prompting-sw-einsteiger.md`](content/outline-prompting-sw-einsteiger.md)
- Exercises: [`exercises/`](exercises/)

## Editing design

Colors and layout helpers live in `pptx_custom.py` (`NAVY`, `ORANGE`, `slide_*` functions). Prefer adding a new `slide_*` helper over one-off shapes in `generate_pptx.py`.
