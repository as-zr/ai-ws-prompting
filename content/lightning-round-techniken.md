# Lightning Round — Arbeitsweisen mit Coding-KI

**Block 6 · ~8 Min · ~50–55 Sek. pro Technik**  
**Ziel:** Überblick — „Das gibt es auch“ — keine Vertiefung, kein Dogma.  
**Folien:** 1 Folie pro Technik (Name + 1 Satz + Mini-Prompt) oder 1 Übersicht + 9 Karten.

**Moderation:** Schnell durchklicken, je Technik nur **Wann · Kern · Beispiel** vorlesen. Abschluss: „Gleich in Übung 3 **eine** Technik kurz testen.“

---

## 1) Plan-first

| | |
|---|---|
| **Wann** | Größeres Feature, mehrere Dateien, unklarer Lösungsweg |
| **Kern** | Erst strukturierten Plan — du prüfst — dann Code in kleinen Schritten |
| **Beispiel** | `Erstelle einen nummerierten Umsetzungsplan für [Feature] in orderCalculator.js. Kein Code. Max. 8 Schritte. Nenne Risiken.` |

---

## 2) TDD mit KI

| | |
|---|---|
| **Wann** | Neue Logik, Regression vermeiden, Tests fehlen |
| **Kern** | Erst Tests/Testliste — dann Implementierung — dann Randfälle nachziehen |
| **Beispiel** | `Liste Testfälle für calculateTotal (happy, leer, ungültiger Rabatt). Dann Implementierung nur wenn Tests grün werden sollen. node:test, AAA.` |

---

## 3) Spec-driven Prompting

| | |
|---|---|
| **Wann** | Anforderung aus Ticket/Story, Akzeptanzkriterien vorhanden |
| **Kern** | Mini-Spec oder ACs ins Prompt — KI arbeitet dagegen — du prüfst pro Kriterium |
| **Beispiel** | `Umsetze nur diese ACs: 1) Summe korrekt 2) leere Liste = 0 3) negative Beträge = Exception. Markiere erfüllt/offen.` |

---

## 4) Rubber-Duck Debugging

| | |
|---|---|
| **Wann** | Bug, flaky Test, unklares Verhalten |
| **Kern** | Symptom + Kontext beschreiben — Hypothesen priorisieren — nächste Prüfschritte, kein Raten-Code |
| **Beispiel** | `CalculateTotal liefert bei leerer Order 0 statt Exception. Letzte Änderung: Rabattlogik. Top-3 Hypothesen + je 1 Prüfschritt. Kein Code ändern.` |

---

## 5) Review-first

| | |
|---|---|
| **Wann** | Legacy, fremder Code, hohes Risiko vor Änderung |
| **Kern** | Zuerst Review (Risiken, Edge Cases, Verständlichkeit) — dann gezielte, kleine Änderung |
| **Beispiel** | `Review nur: markierter Code. Risiken, fehlende Tests, Verständlichkeit. Keine Änderungen. Danach separat: nur Test für null customerId.` |

---

## 6) Refactoring Guardrails

| | |
|---|---|
| **Wann** | Aufräumen ohne Verhaltensänderung |
| **Kern** | Explizit: Verhalten gleich, API stabil, Regressionen benennen |
| **Beispiel** | `Refactor CalculateTotal lesbarer. Verhalten identisch. Öffentliche Signatur unverändert. Nenne mögliche Regressionen vor dem Diff.` |

---

## 7) Explain-before-change

| | |
|---|---|
| **Wann** | Unbekannter Code, vor dem Anfassen Verständnis sichern |
| **Kern** | Erklärung → du validierst → erst dann Änderung beauftragen |
| **Beispiel** | `Erkläre CalculateTotal in 5 Bullet Points: Eingaben, Ausgabe, Edge Cases, Abhängigkeiten. Kein Code ändern.` → _(prüfen)_ → `Jetzt nur Test für negative Beträge.` |

---

## 8) Diff-only Prompting

| | |
|---|---|
| **Wann** | Kleine Fixes, PR-Review, wenig Rauschen |
| **Kern** | Nur geänderte Stellen / Dateien — keine Romane |
| **Beispiel** | `Gib nur den Diff für CalculateTotal: Exception bei negativem Betrag. Keine Erklärung, max. 15 Zeilen Code.` |

---

## 9) Test-gap Analysis

| | |
|---|---|
| **Wann** | Bestehende Tests, unsicher ob Abdeckung reicht |
| **Kern** | Lücken in Happy Path / Edge / Regression finden — priorisierte Liste |
| **Beispiel** | `Welche Tests fehlen für CalculateTotal? Gruppiere: Happy Path, Edge Cases, Regression. Priorisiere Top-5. Kein Code.` |

---

## Trainer-Cheat-Sheet (Timing)

| # | Technik | Sek. |
|---|---------|------|
| 1 | Plan-first | 55 |
| 2 | TDD | 50 |
| 3 | Spec-driven | 50 |
| 4 | Rubber-Duck | 50 |
| 5 | Review-first | 50 |
| 6 | Refactoring Guardrails | 50 |
| 7 | Explain-before-change | 50 |
| 8 | Diff-only | 45 |
| 9 | Test-gap | 50 |
| — | **Summe** | **~8 Min** |

**Überleitung zu Kapitel 7 (Übung 3):** „Wählt **eine** Technik — kurz ausprobieren.“
