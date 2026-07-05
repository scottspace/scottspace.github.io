/* live.js — single source of truth renderers for scott.ai
 *
 * Two self-updating, never-hand-edited values:
 *   1. Live deployment count — read from /count.json (see below).
 *   2. Day counter — computed from DAY_ONE.
 *
 * COUNT: /count.json shape -> {"deployments": 5162, "companies": 3338, "updated": "2026-07-05"}
 *   TODO(scott): add a one-line export step to the scanner pipeline that overwrites
 *   /count.json on each run, e.g. `echo "{\"deployments\":$N,\"companies\":$C,\"updated\":\"$(date +%F)\"}" > count.json`.
 *   Nothing else needs touching — every page reads this file at load.
 *
 * Markup contract (progressive enhancement — static fallbacks live in the HTML):
 *   <span data-count="verified">5,000+</span>        -> "5,162 verified, and counting"
 *   <span data-count="plain">5,000+</span>           -> "5,162"
 *   <span data-count="companies">3,300+</span>       -> "3,338"
 *   <span data-count-updated></span>                 -> "as of 2026-07-05"
 *   <span data-day-counter></span>                   -> "Day 247 of documenting the Approximation Era."
 *   <span data-day-num></span>                       -> "247"
 *   <span data-day-of="2026-05-01"></span>           -> "Day 182" (per-entry badge; hidden if before DAY_ONE)
 * If JS is disabled or the fetch fails, the hardcoded fallback text is left untouched.
 */
(function () {
  "use strict";

  /* ---- Day counter (self-computing, never hand-edited) ---- */
  // TODO(scott): set DAY_ONE to the date your Day 1 video posted (YYYY-MM-DD, UTC).
  var DAY_ONE = new Date("2025-11-01T00:00:00Z"); // PLACEHOLDER

  var msPerDay = 86400000;
  var today = new Date();
  var day = Math.floor((today - DAY_ONE) / msPerDay) + 1;
  if (day < 1) { day = 1; }

  each("[data-day-counter]", function (el) {
    el.textContent = "Day " + day + " of documenting the Approximation Era.";
  });
  each("[data-day-num]", function (el) {
    el.textContent = String(day);
  });

  // Per-entry Day badges (The Ledger). Hidden when the entry predates DAY_ONE.
  each("[data-day-of]", function (el) {
    var d = new Date(el.getAttribute("data-day-of") + "T00:00:00Z");
    if (isNaN(d)) { return; }
    var n = Math.floor((d - DAY_ONE) / msPerDay) + 1;
    if (n >= 1) {
      el.textContent = "Day " + n;
      el.hidden = false;
    } else {
      el.hidden = true; // no day number available for pre-log entries
    }
  });

  /* ---- Live deployment count (scanner-driven, never hand-edited) ---- */
  fetch("/count.json", { cache: "no-store" })
    .then(function (r) { return r.json(); })
    .then(function (d) {
      var deployments = fmt(d.deployments);
      var companies = fmt(d.companies);

      each("[data-count]", function (el) {
        var mode = el.getAttribute("data-count");
        if (mode === "verified") {
          el.textContent = deployments + " verified, and counting";
        } else if (mode === "companies") {
          el.textContent = companies;
        } else {
          el.textContent = deployments; // "plain"
        }
      });

      each("[data-count-updated]", function (el) {
        el.textContent = "as of " + d.updated;
      });
    })
    .catch(function () {
      /* Leave the static "5,000+" fallback in place. */
    });

  /* ---- helpers ---- */
  function each(sel, fn) {
    var nodes = document.querySelectorAll(sel);
    for (var i = 0; i < nodes.length; i++) { fn(nodes[i]); }
  }
  function fmt(n) {
    try { return Number(n).toLocaleString("en-US"); }
    catch (e) { return String(n); }
  }
})();
