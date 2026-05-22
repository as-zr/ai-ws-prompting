# Übung 1 — Musterlösung (nur Trainer)

## CRAFT-Prompt (Copilot Chat)

```text
Role: You are a senior developer in our Node.js service codebase.
Context: calculateTotal in exercises/sample/orderCalculator.js — selected function.
          Use Node built-in test runner (node:test + node:assert/strict), same style as orderCalculator.test.js.
Action: Write unit tests for: happy path (multiple line items), empty line items array,
        discount boundary (0% and 100%), invalid discount throws RangeError,
        free shipping at/above threshold, below threshold adds shipping.
Format: Extend orderCalculator.test.js, Arrange-Act-Assert style, test names in German.
Constraints: No npm packages, no external test libs. Do not change orderCalculator.js.
             List assumptions before generating test code.
```

## Prompt-Template aus Confluence-Kommentar (Coding-Aufgabe präzise umsetzen)

```text
Du bist ein erfahrener Senior-Softwareentwickler für [TECH-STACK].

Ziel
Ich möchte folgende Aufgabe umsetzen: [KURZE BESCHREIBUNG DES ZIELS]

Kontext
Projekt/Modul: [DATEI ODER BEREICH]
Aktueller Stand: [IST-ZUSTAND IN 2-4 STICHPUNKTEN]
Relevante Randbedingungen: [z. B. Performance, Security, Legacy-Code, Team-Standards]
Nicht ändern: [WAS UNBEDINGT STABIL BLEIBEN MUSS]

Anforderungen
[ANFORDERUNG 1]
[ANFORDERUNG 2]
[ANFORDERUNG 3]

Ausgabeformat
Bitte liefere die Antwort in dieser Struktur:
- Kurzlösung (max. 5 Bullet Points)
- Konkrete Code-Änderungen (mit Dateipfaden)
- Testfälle (Happy Path + 2 Edge Cases)
- Risiken/Offene Punkte
- Nächster sinnvoller Schritt

Qualitätskriterien
- Lösung muss produktionsnah und verständlich sein.
- Keine vagen Aussagen; bei Annahmen bitte explizit kennzeichnen.
- Wenn Infos fehlen, stelle zuerst max. 3 präzise Rückfragen.
```

## Review-Nachprompt (optional in Debrief)

```text
List assumptions, uncertainties, and missing test cases. Do not change any code.
```

## Erwartung

- Assumptions werden zuerst gelistet  
- Tests decken mindestens: leere Liste, ungültiger Rabatt, Versandlogik ab  
- Keine externen Libraries in der Antwort  
- `node --test orderCalculator.test.js` in `exercises/sample/` läuft grün nach Übernahme der Tests

## Challenge (erfahrene Teilnehmende)

„Add a constraint: property-based test idea for discountPercent bounds — describe only, no code.“
