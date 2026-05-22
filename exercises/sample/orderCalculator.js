// Lernwoche 2026 — Demo-Snippet (fiktiv, kein Kundencode)
// Für Übung 1, Live-Demo und Deep Dive Unit-Tests

const FREE_SHIPPING_THRESHOLD = 50;
const STANDARD_SHIPPING = 4.99;

/**
 * Berechnet die Gesamtsumme für eine Bestellung.
 * @param {number[]} lineItems Einzelpreise pro Position (Menge bereits eingerechnet).
 * @param {number} discountPercent Rabatt 0–100.
 * @param {string|null} [customerId] Kunden-ID für Logging (optional).
 * @returns {number} Endbetrag in EUR.
 */
function calculateTotal(lineItems, discountPercent, customerId = null) {
  if (!lineItems || lineItems.length === 0) {
    return STANDARD_SHIPPING;
  }

  if (discountPercent < 0 || discountPercent > 100) {
    throw new RangeError('discountPercent must be between 0 and 100');
  }

  const subtotal = lineItems.reduce((sum, price) => sum + price, 0);
  const discount = subtotal * (discountPercent / 100);
  let afterDiscount = subtotal - discount;

  if (afterDiscount < 0) {
    afterDiscount = 0;
  }

  const shipping = afterDiscount >= FREE_SHIPPING_THRESHOLD ? 0 : STANDARD_SHIPPING;
  return Math.round((afterDiscount + shipping) * 100) / 100;
}

module.exports = {
  calculateTotal,
  FREE_SHIPPING_THRESHOLD,
  STANDARD_SHIPPING,
};
