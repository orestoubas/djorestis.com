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


  // Email addresses are published split and base64-encoded so a regex harvester
  // finds nothing to match. Reassemble them here for real visitors. Without JS
  // the link still works — it points at the contact page instead.
  function mailAddress(el) {
    var u = el.getAttribute("data-u"), h = el.getAttribute("data-h");
    if (!u || !h) return "";
    try { return atob(u) + "@" + atob(h); } catch (err) { return ""; }
  }
  Array.prototype.forEach.call(document.querySelectorAll("a.obf-mail"), function (a) {
    var addr = mailAddress(a);
    if (!addr) return;
    a.href = "mailto:" + addr;
    a.textContent = addr;
  });

  // Quote form.
  // If data-endpoint is set (e.g. a Formspree URL — see README), submit via fetch.
  // Otherwise fall back to opening the visitor's email client, pre-filled.
  var form = document.getElementById("quote-form");
  var formShownAt = Date.now();
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var status = form.querySelector(".form-status");
      var endpoint = form.getAttribute("data-endpoint");
      var data = new FormData(form);

      // Two silent checks before anything is sent.
      //
      // The honeypot is a field positioned off-screen. A person never sees it,
      // so anything in it came from a bot filling every input on the page.
      //
      // The timer catches the rest: a bot posts the moment the page parses,
      // where a person needs time to read the labels and type. Under three
      // seconds is not a human filling in a booking enquiry.
      //
      // Both fail silently and report success. Telling a bot why it was
      // rejected only teaches whoever wrote it what to change.
      var trap = form.querySelector('input[name="website"]');
      var tooFast = (Date.now() - formShownAt) < 3000;
      if ((trap && trap.value) || tooFast) {
        form.reset();
        status.textContent = form.dataset.sentMsg || "Thank you! Your request has been sent.";
        return;
      }
      data.delete("website");

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
      var email = mailAddress(form);
      if (!email) return;
      var subject = form.dataset.mailtoSubject || "Quote request — DJORESTIS.com";
      window.location.href =
        "mailto:" + email +
        "?subject=" + encodeURIComponent(subject) +
        "&body=" + encodeURIComponent(lines.join("\n"));
    });
  }
})();
