const test = require('node:test');
const assert = require('node:assert/strict');
const { calculateTotal } = require('./orderCalculator');

// Minimaler Smoke-Test — Setup pruefen. In den Uebungen erweitert ihr die Suite per Prompt.
test('berechnet Summe mit Versand unter Schwellwert', () => {
  assert.equal(calculateTotal([10, 20], 0), 34.99);
});
