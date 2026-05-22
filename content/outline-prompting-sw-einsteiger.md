# Lernwoche 2026: Prompting für SW-Entwickler (Mixed Audience Outline)

## Titel
Besser prompten für Coding-KI: präzisere Ergebnisse in kürzerer Zeit

## Termin
10. Juni 2026, 16:50-18:20 (90 Minuten)

## Zielgruppe (optimiert)
- Software-Entwickler und technische Teammitglieder mit wenig bis solider KI-Erfahrung
- Personen, die Coding-AI neugierig ausprobieren oder bereits "okay" nutzen
- Teams, die KI im Coding-Alltag verlässlicher und bewusster einsetzen wollen

## Lernziele (für Einsteiger bis OK-Nutzer)
Nach dem Seminar können die Teilnehmenden:
- KI-Antworten realistisch einschätzen: hilfreich, aber prüfpflichtig
- den Zusammenhang zwischen Input-Qualität und Output-Qualität praktisch anwenden
- erkennen, warum **Context is king** bei Coding-KI gilt
- Prompts mit klarer Struktur für Coding-Aufgaben formulieren
- KI-Antworten mit einfachen Vertrauens- und Review-Fragen bewerten
- den Katalog gängiger Arbeitsweisen (Lightning Round) überblicken und einmal ausprobieren
- die zentralen Bausteine eines guten Coding-Prompts im Überblick wiedergeben

## Kernbotschaft
KI ist kein magischer Problemlöser.
Gute Ergebnisse entstehen, wenn Entwickler klaren Kontext, Ziele und Qualitätskriterien liefern.

---

## Didaktische Leitlinie für eure Audience
- **Ablauf:** 1 + 2 → Ü1 → 3 + 4 → Ü2 → Vertrauen → Lightning Round → **7 Übung 3** → **8 Zusammenfassung**
- Einstieg niedrigschwellig, aber nicht oberflächlich
- Jedes Konzept sofort mit Entwicklerbeispiel verbinden
- Für Einsteiger: klare Struktur und einfache Begriffe
- Für OK-Nutzer: optionale Vertiefung über Constraints, Review und Arbeitsmethoden

---

## 90-Minuten-Ablauf (Mixed Audience, exakt 90 Min)

**Prinzip:** Zwei inhaltliche Schwerpunkte mit Praxisphasen, danach Vertrauen, **Lightning Round**, **Übung 3**, **Zusammenfassung**.

| Phase                                 | Min    |
| ------------------------------------- | ------ |
| 1 + 2 + Übung 1 (GiGo)                | 26     |
| 3 + 4 + Übung 2 (Kontext + CRAFT)     | 30     |
| 5 · 6 · 7 Übung 3 · 8 Zusammenfassung | 30     |
| Q&A                                   | 4      |
| **Summe**                             | **90** |

---

### Fokusthema 1 — Qualität der Eingabe (1, 2)

#### 1) Einstieg: Warum Prompt-Qualität im Coding-Alltag zählt (5 Min)
- Problemrahmen: KI liefert oft "irgendwas", aber nicht zuverlässig das Richtige
- Zielbild: schneller zu brauchbaren Ergebnissen kommen, ohne Qualität abzugeben
- Erfolgsmaßstab: Antwort ist verständlich, prüfbar und passt zum Kontext

#### 2) Mentales Modell: Garbage in, garbage out (7 Min)
- Vager Prompt -> vage oder zufällige Antwort
- Unvollständiger Kontext -> KI kompensiert mit Annahmen
- Präzise Problemformulierung + Randbedingungen -> bessere Ergebnisqualität
- Merksatz: KI spiegelt die Qualität deiner Eingabe

**Fokusthema 1 gesamt (ohne Übung): ~12 Min**

---

### Übung 1 — nach 1 + 2 (14 Min)

- Paararbeit (10 Min Arbeit + 4 Min Debrief)
- Material: `exercises/01-vague-prompt.md` (Ausgangs-Prompt + Codeausschnitt)
- Ziel: **GiGo anwenden** — vagen Prompt präziser formulieren (Ziel, Scope, erkennbare Lücken schließen)
- Noch **ohne** vollständiges CRAFT-Raster; Fokus: „Was fehlt der KI, damit sie nicht raten muss?“
- Optional: einmal in Copilot ausführen und Antwort in einem Satz bewerten
- Debrief: 2 Paare zeigen Vorher/Nachher — Was hat die Qualität am stärksten verbessert?

---

### Fokusthema 2 — Kontext und Struktur (3, 4)

#### 3) Context is king: Was muss die KI wissen? (8 Min)
- Kontext ist nicht "mehr Text", sondern relevante Information
- Wichtige Kontextarten:
  - Ziel / gewünschtes Ergebnis
  - betroffener Codebereich oder Datei
  - aktueller Stand / Problembeobachtung
  - Randbedingungen (Performance, API, Legacy, Tests)
  - Dinge, die stabil bleiben müssen
- Faustregel: erst Kontext sammeln, dann prompten
- Brücke zu Übung 2: Kontext aus Übung 1 gezielt ergänzen

#### 4) Prompt-Bausteine für technische Aufgaben (CRAFT) (8 Min)
- Context: Dateien, Modul, aktueller Stand, Randbedingungen
- Role/Persona: gewünschte Perspektive (Implementer, Reviewer, Tester)
- Action: konkreter Arbeitsauftrag mit Scope
- Format: gewünschte Struktur der Antwort
- Constraints: was darf nicht passieren?
- Example/Few-Shot: gewünschtes Ergebnis zeigen statt nur beschreiben

**Fokusthema 2 gesamt (ohne Übung): ~16 Min**

---

### Übung 2 — nach 3 + 4 (14 Min)

- Paararbeit oder Einzel (10 Min Arbeit + 4 Min Debrief)
- Material: `exercises/02-craft-prompt.md` (baut auf demselben Code-Snippet wie Übung 1 auf)
- Ziel: Prompt aus Übung 1 mit **Kontextarten + CRAFT** vervollständigen (alle 5 Bausteine, mindestens 1 Constraint)
- Optional: in Copilot ausführen; Output kurz gegen CRAFT-Checkliste prüfen
- Debrief: Unterschied zwischen „schärfer“ (Ü1) und „strukturiert“ (Ü2) in einem Satz

---

### Block C — Prüfen, ausprobieren, zusammenfassen

#### 5) Wie kann ich dem Output vertrauen? (7 Min)
- Grundhaltung: KI-Antworten sind Vorschläge, keine Freigaben
- Vertrauens-Check:
  - Welche Annahmen triffst du?
  - Was könnte daran falsch sein?
  - Welche Tests fehlen?
  - Welche Risiken oder Seiteneffekte gibt es?
  - Welche Informationen brauchst du noch?
- Praktische Prüfung: Diff lesen, Tests ausführen, Randfälle ansehen
- Review-Prompt: „Annahmen, Unsicherheiten, fehlende Tests — nichts am Code ändern“
- **Überleitung:** Danach Lightning Round — Katalog Arbeitsweisen

#### 6) Lightning Round — Arbeitsweisen mit Coding-KI (8 Min)
- Format: schnell durch alle Techniken, je ~1 Min
- Trainer-Material: [`content/lightning-round-techniken.md`](lightning-round-techniken.md)
- 9 Techniken:
  - Plan-first
  - TDD
  - Spec-driven
  - Rubber-Duck
  - Review-first
  - Refactoring Guardrails
  - Explain-before-change
  - Diff-only
  - Test-gap Analysis
- Botschaft: Katalog zum Mitnehmen — im Alltag **eine** passende Technik pro Aufgabe
- **Überleitung:** Jetzt **eine** Technik in Übung 3 kurz testen

#### 7) Übung: Eine Technik ausprobieren (10 Min)
- Paararbeit (8 Min Arbeit + 2 Min optional kurzer Debrief)
- Material: `exercises/03-technique-tryout.md`
- Ziel: **eine** Technik aus Block 6 auswählen und kurz anwenden (Mini-Prompt)
- Optional: in Copilot ausführen

#### 8) Zusammenfassung der Präsentation (5 Min)
- Kurz alle Kapitel durchgehen (Folie oder mündlich):
  1. **Warum Prompt-Qualität** — KI braucht guten Auftrag
  2. **GiGo** — Input-Qualität = Output-Qualität
  3. **Context is king** — relevante Infos vor dem Prompt
  4. **CRAFT** — strukturierte Coding-Prompts
  5. **Vertrauen** — prüfen, nicht blind übernehmen; Review-Prompt
  6. **Arbeitsweisen** — Katalog (Lightning); situativ wählen
- Merksatz wiederholen: KI spiegelt deine Eingabe — du bleibst verantwortlich
- Nächster Schritt: Montag einen echten Task mit GiGo + Kontext + CRAFT + Review angehen

**Block C gesamt: ~30 Min** (7 + 8 + 10 + 5)

_Compliance/Privacy: nicht im Workshop — ggf. Vorab-Mail._
