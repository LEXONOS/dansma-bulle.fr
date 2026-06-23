/* ============================================================
   DANS MA BULLE · Interactions (vanilla JS, non bloquant)
   ============================================================ */
(function () {
  "use strict";

  var prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ----- Hero : entrée orchestrée ----- */
  var hero = document.querySelector(".hero");
  if (hero) {
    requestAnimationFrame(function () {
      requestAnimationFrame(function () { hero.classList.add("is-ready"); });
    });
  }

  /* ----- Header : état au scroll ----- */
  var header = document.querySelector(".site-header");
  var heroEl = document.querySelector(".hero");

  function onScroll() {
    if (!header) return;
    // Si une page n'a pas de hero plein écran, l'en-tête est solide d'emblée.
    var threshold = heroEl ? Math.min(window.innerHeight * 0.6, 480) : 10;
    header.classList.toggle("is-scrolled", window.scrollY > threshold);
  }
  if (!heroEl && header) header.classList.add("is-scrolled");
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  /* ----- Menu mobile ----- */
  var toggle = document.querySelector("[data-menu-toggle]");
  var body = document.body;

  function closeMenu() {
    body.classList.remove("menu-open");
    if (toggle) toggle.setAttribute("aria-expanded", "false");
  }
  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = body.classList.toggle("menu-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.querySelectorAll(".mobile-menu a").forEach(function (a) {
      a.addEventListener("click", closeMenu);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && body.classList.contains("menu-open")) closeMenu();
    });
  }

  /* ----- Révélations au scroll ----- */
  var revealEls = document.querySelectorAll(".reveal");
  if (revealEls.length) {
    if (prefersReduced || !("IntersectionObserver" in window)) {
      revealEls.forEach(function (el) { el.classList.add("is-visible"); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            io.unobserve(entry.target);
          }
        });
      }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
      revealEls.forEach(function (el) { io.observe(el); });
    }
  }

  /* ----- Parallaxe douce du hero (désactivée si mouvement réduit) ----- */
  var heroImg = document.querySelector(".hero__media img");
  if (heroImg && !prefersReduced) {
    var ticking = false;
    window.addEventListener("scroll", function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () {
        var y = Math.min(window.scrollY, window.innerHeight);
        heroImg.style.transform = "scale(1.04) translateY(" + y * 0.12 + "px)";
        ticking = false;
      });
    }, { passive: true });
  }

  /* ----- Accordéon FAQ ----- */
  document.querySelectorAll(".faq__q").forEach(function (q) {
    q.addEventListener("click", function () {
      var item = q.closest(".faq__item");
      var panel = item.querySelector(".faq__a");
      var open = item.classList.toggle("is-open");
      q.setAttribute("aria-expanded", open ? "true" : "false");
      panel.style.maxHeight = open ? panel.scrollHeight + "px" : null;
    });
  });

  /* ----- Formulaire de réservation : composition d'un e-mail ----- */
  var form = document.querySelector("[data-reservation-form]");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var data = new FormData(form);
      var nom = (data.get("nom") || "").toString().trim();
      var email = (data.get("email") || "").toString().trim();
      var tel = (data.get("tel") || "").toString().trim();
      var formule = (data.get("formule") || "").toString();
      var date = (data.get("date") || "").toString();
      var convives = (data.get("convives") || "").toString();
      var message = (data.get("message") || "").toString().trim();

      var sujet = "Demande de réservation · " + (formule || "Dans Ma Bulle");
      var corps =
        "Bonjour,\n\nJe souhaite réserver une expérience Dans Ma Bulle.\n\n" +
        "Nom : " + nom + "\n" +
        "Email : " + email + "\n" +
        "Téléphone : " + tel + "\n" +
        "Formule : " + formule + "\n" +
        "Date souhaitée : " + date + "\n" +
        "Nombre de convives : " + convives + "\n\n" +
        "Message :\n" + message + "\n";

      var href = "mailto:contact@dansma-bulle.fr?subject=" +
        encodeURIComponent(sujet) + "&body=" + encodeURIComponent(corps);
      window.location.href = href;

      var status = form.querySelector("[data-form-status]");
      if (status) {
        status.textContent = "Votre messagerie s'ouvre avec la demande pré-remplie. Pour une réponse immédiate, appelez le 06 14 83 81 09.";
      }
    });
  }

  /* ----- Présélection de la formule via l'URL (?formule= / ?objet=) ----- */
  if (form) {
    try {
      var params = new URLSearchParams(window.location.search);
      var wanted = (params.get("formule") || params.get("objet") || "").toLowerCase();
      if (wanted) {
        var map = {
          "romantique": "La Bulle Romantique",
          "anniversaire": "La Bulle Anniversaire",
          "brunch": "La Bulle Brunch",
          "sur-mesure": "La Bulle Sur-Mesure",
          "carte-cadeau": "Carte cadeau"
        };
        var label = map[wanted];
        var sel = form.querySelector("#formule");
        if (label && sel) {
          Array.prototype.forEach.call(sel.options, function (opt) {
            if (opt.text === label) opt.selected = true;
          });
        }
      }
    } catch (err) { /* sans incidence */ }
  }

  /* ----- Année courante ----- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
