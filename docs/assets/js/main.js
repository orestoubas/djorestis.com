/* DJORESTIS.com — minimal enhancement layer (no dependencies) */
(function () {
  "use strict";

  // Mobile navigation
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  // Footer year
  var year = document.getElementById("year");
  if (year) year.textContent = String(new Date().getFullYear());

  // Cookie consent + GA4 (banner exists only when a GA4 ID is configured)
  var banner = document.getElementById("cookie-banner");
  if (banner) {
    var gaId = banner.getAttribute("data-ga");
    var loadGA = function () {
      var s = document.createElement("script");
      s.src = "https://www.googletagmanager.com/gtag/js?id=" + gaId;
      s.async = true;
      document.head.appendChild(s);
      window.dataLayer = window.dataLayer || [];
      window.gtag = function () { window.dataLayer.push(arguments); };
      window.gtag("js", new Date());
      window.gtag("config", gaId, { anonymize_ip: true });
    };
    var choice = null;
    try { choice = localStorage.getItem("cookie-consent"); } catch (e) {}
    if (choice === "yes") {
      loadGA();
    } else if (choice !== "no") {
      banner.hidden = false;
      banner.querySelectorAll("[data-consent]").forEach(function (btn) {
        btn.addEventListener("click", function () {
          var v = btn.getAttribute("data-consent");
          try { localStorage.setItem("cookie-consent", v); } catch (e) {}
          banner.hidden = true;
          if (v === "yes") loadGA();
        });
      });
    }
  }

  // Quote form.
  // If data-endpoint is set (e.g. a Formspree URL — see README), submit via fetch.
  // Otherwise fall back to opening the visitor's email client, pre-filled.
  var form = document.getElementById("quote-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var status = form.querySelector(".form-status");
      var endpoint = form.getAttribute("data-endpoint");
      var data = new FormData(form);

      if (endpoint) {
        fetch(endpoint, {
          method: "POST",
          body: data,
          headers: { Accept: "application/json" },
        })
          .then(function (res) {
            if (!res.ok) throw new Error("bad status");
            form.reset();
            status.textContent = form.dataset.sentMsg || "Thank you! Your request has been sent.";
          })
          .catch(function () {
            status.textContent = form.dataset.errorMsg || "Something went wrong. Please email me directly.";
          });
        return;
      }

      // mailto fallback
      var lines = [];
      data.forEach(function (value, key) {
        if (value) lines.push(key + ": " + value);
      });
      var email = form.getAttribute("data-email");
      var subject = form.dataset.mailtoSubject || "Quote request — DJORESTIS.com";
      window.location.href =
        "mailto:" + email +
        "?subject=" + encodeURIComponent(subject) +
        "&body=" + encodeURIComponent(lines.join("\n"));
    });
  }
})();
