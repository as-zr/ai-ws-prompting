# Übung 2 — Kontext + CRAFT

**Zeit:** 12 min Arbeit + 4 min Debrief (nach Block 3 + 4)  
**Modus:** Paare oder Einzel  
**Ziel:** Prompt aus Übung 1 mit **Kontextarten** und **CRAFT** vervollständigen

## Ausgangspunkt

Euer verbesserter Prompt aus **Übung 1** (derselbe Code: `sample/orderCalculator.js`, Funktion `calculateTotal`).

Projekt sollte bereits laufen (`exercises/setup.ps1` bzw. `./setup.sh`).

## Aufgabe

1. Ergänzt fehlenden **Kontext** (Ziel, Stand, Randbedingungen, „nicht ändern“).
2. Strukturiert den Prompt mit **CRAFT**:
   - **C** — Kontext (Datei, Funktion, Stack: Node, natives `node:test`)
   - **R** — Rolle
   - **A** — Aufgabe (welche Tests?)
   - **F** — Format (`node:test`, `node:assert`, deutsche Testnamen)
   - **T** — Constraints (keine Packages, kein Prod-Code ändern, …)
3. Optional: in Copilot ausführen, Tests übernehmen und mit `node --test orderCalculator.test.js` prüfen.

## Debrief-Fragen (Trainer)

- Was war der Unterschied zwischen „schärfer“ (Ü1) und „strukturiert“ (Ü2)?
- Welcher CRAFT-Baustein hat am meisten gebracht?
- Was würdet ihr beim nächsten Mal zuerst ergänzen?

## Musterlösung

Nur Trainer: siehe `solutions/01-good-prompt.md`
