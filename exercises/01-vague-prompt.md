# Übung 1 — Prompt schärfen (GiGo)

**Zeit:** 10 min Arbeit + 4 min Debrief (nach Block 1 + 2)  
**Modus:** Paare  
**Ziel:** Vagen Prompt **präziser** machen — ohne vollständiges CRAFT-Raster

## Vorbereitung (einmalig, ~30 Sek)

Repo auschecken — im Ordner `exercises/` liegt **`node.exe`** (Windows, mit im Repo). Dann:

```powershell
.\setup.ps1
```

```bash
# macOS / Linux: system node oder ./node neben sample/
./setup.sh
```

Das Script führt `node --test` aus — wenn grün, ist das Projekt bereit. **Kein npm, keine Packages.**

Alternativ direkt:

```powershell
cd exercises/sample
..\node.exe --test orderCalculator.test.js
```

**Ohne gebündelte Binary:** Node.js 18+ (`node --version`) reicht ebenfalls.

## Ausgangs-Prompt (vage)

```text
make unit tests
```

## Code-Kontext

1. IDE öffnen: `exercises/sample/` (nur 2 Dateien: `orderCalculator.js` + `orderCalculator.test.js`)
2. Datei `orderCalculator.js` — Funktion `calculateTotal` markieren
3. Tests nutzen natives **`node:test`** und **`node:assert`** — siehe `orderCalculator.test.js`

## Aufgabe

1. Formuliert den Prompt so um, dass die KI **nicht raten** muss.
2. Prüft mit GiGo-Fragen:
   - Was ist das **Ziel**?
   - Was ist der **Scope** (welche Funktion, welches Verhalten)?
   - Was fehlt noch (Stack, Test-Runner, Randbedingungen)?
3. Optional: Prompt einmal ausführen — passt die Antwort besser als bei „make unit tests“?
4. Optional: generierte Tests einfügen und `node --test orderCalculator.test.js` erneut ausführen

**Noch nicht Pflicht:** CRAFT-Labels oder alle fünf Bausteine — das kommt in Übung 2.

## Debrief-Fragen (Trainer)

- Was hat am meisten geholfen?
- Was würdet ihr weglassen?
- Unterschied zu „make unit tests“ in einem Satz?

## Musterlösung (Orientierung)

Nur Trainer: siehe `solutions/01-good-prompt.md` (vereinfachte GiGo-Version reicht für Debrief)
