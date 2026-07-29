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
