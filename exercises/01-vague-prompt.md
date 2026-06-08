# Übung 1 — KI-Agent instruieren: Unit Tests schreiben (GiGo)

**Aufgabe:** Den KI-Agenten anweisen, Unit Tests für `calculateTotal()` zu erstellen — erst mit vagem Prompt, dann präziser.

**Zeit:** 10 min Arbeit + 4 min Debrief  
**Modus:** Paare

## Start

1. Repo auschecken
2. `run-tests.bat` im Repo-Root ausführen — fertig

## Wo

`exercises/ex-1/` — `orderCalculator.js` + `orderCalculator.test.js`

## Ausgangs-Prompt (vage)

```text
make unit tests
```

## Schritte

1. `calculateTotal()` in `orderCalculator.js` markieren
2. **Vagen Prompt ausführen** — Agent instruieren, Unit Tests zu schreiben: Was liefert die KI? Was fehlt? Wo rät sie?
3. **Prompt präzisieren** — so umformulieren, dass der Agent gezielt Unit Tests für `calculateTotal()` liefert, **ohne zu raten**; erneut ausführen und mit Schritt 2 vergleichen
4. GiGo-Check: **Ziel?** **Scope?** Was fehlt noch?
5. Optional: Tests übernehmen, `run-tests.bat` erneut ausführen

**Noch kein CRAFT** — das kommt in Übung 2.
