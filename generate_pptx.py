"""Generate Lernwoche 2026 deck — custom design (no template.pptx)."""

import sys
from pathlib import Path

from pptx_custom import (
    DEFAULT_OUTPUT,
    new_presentation,
    save,
    slide_agenda,
    slide_chapter,
    slide_compare,
    slide_craft,
    slide_end,
    slide_exercise,
    slide_hero,
    slide_insight,
    slide_takeaway,
    slide_workflow,
)

TITLE = "Besser prompten für Coding-KI"
SUBTITLE = "Von Zufallsergebnissen zu verlässlichen Coding-Antworten"
SESSION = "10. Juni 2026 · 16:50–18:20 · Präsenz · max. 15 TN"


def _add_notes(prs, bullets: list[str]) -> None:
    """Attach speaker notes (bullet points) to the latest slide."""
    slide = prs.slides[-1]
    notes = slide.notes_slide.notes_text_frame
    notes.clear()
    for i, bullet in enumerate(bullets):
        p = notes.paragraphs[0] if i == 0 else notes.add_paragraph()
        p.text = f"- {bullet}"


def build_deck(output_path: Path | None = None) -> Path:
    prs = new_presentation()

    slide_hero(
        prs,
        TITLE,
        SUBTITLE,
        meta=SESSION,
        tag="Lernwoche 2026 · GitHub Copilot",
    )
    _add_notes(
        prs,
        [
            "Begrüße die Runde und stelle dich kurz vor.",
            "Positioniere das Niveau: geeignet für KI-Einsteiger und Nutzer mit ersten Erfahrungen.",
            "Nenne das Ziel: Jede Person nimmt ein direkt nutzbares Prompt-Template mit.",
        ],
    )

    slide_agenda(
        prs,
        "Heute — 90 Minuten",
        [
            ("Warum Prompt-Qualität im Coding-Alltag zählt", "~8 min"),
            ("Mentales Modell: Garbage in, garbage out", "~8 min"),
            ("Prompt-Bausteine für technische Aufgaben", "~12 min"),
            ("Live-Demo: unklarer vs. klarer Prompt", "~10 min"),
            ("Halluzinationen + Qualitätscheck", "~8 min"),
            ("Übung 1 · Prompt verbessern", "~17 min"),
            ("Workflow für Coding-Use-Cases", "~12 min"),
            ("Übung 2 · Template + Transfer", "~17 min"),
            ("Q&A + Mitnehmen", "~8 min"),
        ],
    )
    _add_notes(
        prs,
        [
            "Gehe die Agenda in 30–45 Sekunden durch.",
            "Betone: wenig Theorie, viel direkt anwendbare Praxis.",
            "Erkläre: Einsteiger bekommen Struktur, erfahrenere Nutzer bekommen Qualitäts- und Review-Patterns.",
        ],
    )

    slide_chapter(prs, "01 — Einstieg", "Warum Prompt-Qualität\nim Coding zählt")
    _add_notes(
        prs,
        [
            "Leite in den Grundlagen-Block über.",
            "Formuliere Erwartung: Wir halten Begriffe einfach und praktisch.",
        ],
    )

    slide_insight(
        prs,
        "KI hilft — aber sie braucht einen guten Auftrag",
        [
            "Coding-KI liefert Vorschläge, keine geprüften Engineering-Entscheidungen",
            "Je klarer Aufgabe, Kontext und Grenzen sind, desto besser wird die Antwort",
            "Du bleibst verantwortlich: lesen, testen, reviewen, entscheiden",
        ],
        footer="Ziel heute: verlässliche Antworten statt Zufallstreffer",
    )
    _add_notes(
        prs,
        [
            "Erkläre KI als Assistenzsystem, nicht als Ersatz für Engineering-Urteil.",
            "Gib ein kurzes Beispiel: KI liefert einen Entwurf, der noch validiert werden muss.",
            "Betone: Qualität entsteht durch guten Prompt plus Review.",
        ],
    )

    slide_chapter(prs, "02 — Prinzip", "Garbage in,\ngarbage out")
    _add_notes(
        prs,
        [
            "Kündige das Kernprinzip des Workshops an.",
            "Sage: Die Qualität der Frage bestimmt die Qualität der Antwort.",
        ],
    )

    slide_insight(
        prs,
        "Warum schlechte Prompts schlechte Antworten erzeugen",
        [
            "Vage Frage rein → vage Antwort raus",
            "Fehlt Kontext, „rät“ die KI häufiger",
            "Klarheit + Struktur verbessern Qualität sofort",
        ],
        footer="Merksatz: KI spiegelt die Qualität deiner Eingabe",
    )
    _add_notes(
        prs,
        [
            "Führe den Merksatz ein: vage rein, vage raus.",
            "Zeige kurz ein negatives Alltagsbeispiel wie „Mach das besser“.",
            "Überleitung: Mit einer Struktur wird es sofort besser.",
        ],
    )

    slide_chapter(prs, "03 — Methode", "CRAFT für technische Prompts")
    _add_notes(
        prs,
        [
            "Leite auf die CRAFT-Methode als gemeinsames Grundgerüst über.",
            "Sag: Einsteiger nutzen es als Checkliste, erfahrenere Nutzer als Qualitätsvertrag.",
        ],
    )

    slide_craft(prs)
    _add_notes(
        prs,
        [
            "Gehe C-R-A-F-T Schritt für Schritt durch.",
            "Zeige, dass Kontext und Constraints im Coding besonders wichtig sind.",
            "Stretch für OK-Nutzer: Ausgabeformat und Qualitätskriterien bewusst festlegen.",
        ],
    )

    slide_compare(prs)
    _add_notes(
        prs,
        [
            "Vergleiche die zwei Prompts laut und langsam.",
            "Frage die Gruppe: Welcher Prompt ist messbar und überprüfbar?",
            "Betone, dass Klarheit Zeit spart statt Zeit kostet.",
        ],
    )

    slide_insight(
        prs,
        "Halluzinationen: Qualitätscheck statt blind vertrauen",
        [
            "Mehr Kontext reduziert Ratespiele",
            "Constraints begrenzen falsche Lösungswege",
            "Review-Fragen machen Annahmen und Risiken sichtbar",
        ],
        footer="Standardfrage: „Welche Annahmen, Risiken und offenen Fragen siehst du?“",
    )
    _add_notes(
        prs,
        [
            "Definiere Halluzination in einem Satz: plausibel klingend, aber falsch.",
            "Gib den Review-Prompt als festen Qualitätscheck mit.",
            "Erkläre: Bei fehlenden Infos zuerst Rückfragen statt Code erzeugen lassen.",
        ],
    )

    slide_exercise(
        prs,
        1,
        "Prompt verbessern",
        [
            "Paararbeit — 17 Minuten (12 + 5 Debrief)",
            "Start: unklarer Prompt + kurzer Codeausschnitt",
            "Ziel: CRAFT vollständig + 1–2 Constraints",
            "Stretch: Ausgabeformat + Review-Frage ergänzen",
        ],
        meta="12 min + 5 min",
    )
    _add_notes(
        prs,
        [
            "Starte den Timer sichtbar für 12 Minuten Arbeitszeit.",
            "Gehe im Raum herum und helfe bei CRAFT-Formulierung.",
            "Debrief: 2 Teams zeigen ihren Prompt; frage nach Kontext, Constraints und Reviewbarkeit.",
        ],
    )

    slide_workflow(prs)
    _add_notes(
        prs,
        [
            "Zeige den 4-Schritte-Flow einmal komplett durch.",
            "Übertrage ihn auf Implementierung, Refactoring, Tests, Debugging und Doku.",
            "Erinnere: Nach KI-Antwort immer Tests, Diff und Annahmen prüfen.",
        ],
    )

    slide_exercise(
        prs,
        2,
        "Dein Template mitnehmen",
        [
            "Einzel — 17 Minuten",
            "1 Template für einen echten Use Case aus deinem Alltag",
            "Pflicht: Kontext, Aufgabe, Format, Constraints",
            "Stretch: Qualitätskriterien + Rückfragen-Mechanik",
        ],
        meta="17 min",
    )
    _add_notes(
        prs,
        [
            "Ziel nennen: Jede Person baut ein eigenes Template für Montag.",
            "Gib nach 10 Minuten den Hinweis: Constraints und Review-Frage ergänzen.",
            "Am Ende 2–3 Freiwillige ihr Template kurz vorstellen lassen.",
        ],
    )

    slide_takeaway(
        prs,
        [
            ("Struktur", "CRAFT als Mindeststandard für technische Prompts"),
            ("Qualität", "Antworten gegen Scope, Tests und Risiken prüfen"),
            ("Transfer", "1 Template im Alltag nutzen und im Team teilen"),
        ],
    )
    _add_notes(
        prs,
        [
            "Fasse die drei Kernaussagen in maximal 60 Sekunden zusammen.",
            "Bitte jede Person um einen konkreten nächsten Schritt im Alltag.",
            "Leite zur Teamfrage über: Welche Mindestbestandteile sollen für Prompts gelten?",
        ],
    )

    slide_end(prs, "Fragen & Diskussion")
    _add_notes(
        prs,
        [
            "Öffne Q&A und balanciere Grundlagenfragen mit Praxisfragen.",
            "Biete an, nach dem Termin 1–2 Team-Templates kurz zu reviewen.",
            "Bedanke dich und nenne den nächsten Austauschpunkt im Team.",
        ],
    )

    return save(prs, output_path or DEFAULT_OUTPUT)


if __name__ == "__main__":
    cli_output = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    print(f"Saved: {build_deck(cli_output)}")
