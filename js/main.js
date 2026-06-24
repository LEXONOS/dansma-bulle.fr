/* ============================================================
   DANS MA BULLE — Interactions (vanilla JS)
   ============================================================ */
(function () {
  "use strict";

  /* ------------------------------------------------------------------
     FORMULAIRE — clé d'accès Web3Forms
     ------------------------------------------------------------------
     Pour recevoir les demandes par email (sur Vercel ET sur OVH),
     crée une clé gratuite sur https://web3forms.com (avec l'email
     contact@dansma-bulle.fr), puis colle-la ci-dessous à la place de
     "VOTRE_CLE_WEB3FORMS". Tant que la clé n'est pas renseignée, le
     formulaire ouvre simplement la messagerie avec la demande pré-remplie.
     ------------------------------------------------------------------ */
  var WEB3FORMS_KEY = "VOTRE_CLE_WEB3FORMS";
  var CONTACT_EMAIL = "contact@dansma-bulle.fr";
  var CONTACT_PHONE = "06 14 83 81 09";

  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var body = document.body;

  /* ---------- Bulles flottantes ---------- */
  (function bubbles() {
    if (reduced) return;
    var host = document.querySelector("[data-bubbles]");
    if (!host) return;
    var count = window.innerWidth < 640 ? 9 : 15;
    var frag = document.createDocumentFragment();
    for (var i = 0; i < count; i++) {
      var b = document.createElement("span");
      b.className = "bubble";
      var size = 14 + Math.random() * 72;
      var dur = 20 + Math.random() * 24;
      b.style.setProperty("--size", size.toFixed(0) + "px");
      b.style.setProperty("--left", (2 + Math.random() * 94).toFixed(1) + "%");
      b.style.setProperty("--dur", dur.toFixed(1) + "s");
      b.style.setProperty("--delay", (-Math.random() * dur).toFixed(1) + "s");
      b.style.setProperty("--drift", ((Math.random() * 80 - 40)).toFixed(0) + "px");
      b.style.setProperty("--op", (0.35 + Math.random() * 0.45).toFixed(2));
      frag.appendChild(b);
    }
    host.appendChild(frag);
  })();

  /* ---------- Header : état au scroll ---------- */
  var header = document.querySelector("[data-header]");
  var hero = document.querySelector(".hero");
  function onScroll() {
    if (!header) return;
    var threshold = hero ? Math.min(window.innerHeight * 0.62, 520) : 8;
    header.classList.toggle("is-scrolled", window.scrollY > threshold);
  }
  if (!hero && header) header.classList.add("is-scrolled");
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  /* ---------- Hero : entrée orchestrée + parallaxe ---------- */
  if (hero) {
    requestAnimationFrame(function () {
      requestAnimationFrame(function () { hero.classList.add("is-ready"); });
    });
    var heroImg = hero.querySelector(".hero__media img");
    if (heroImg && !reduced) {
      var ticking = false;
      window.addEventListener("scroll", function () {
        if (ticking) return;
        ticking = true;
        requestAnimationFrame(function () {
          var y = Math.min(window.scrollY, window.innerHeight);
          heroImg.style.transform = "scale(1.06) translateY(" + (y * 0.12).toFixed(1) + "px)";
          ticking = false;
        });
      }, { passive: true });
    }
  }

  /* ---------- Menu mobile ---------- */
  var toggle = document.querySelector("[data-menu-toggle]");
  function closeMenu() {
    body.classList.remove("menu-open");
    if (toggle) toggle.setAttribute("aria-expanded", "false");
  }
  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = body.classList.toggle("menu-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.querySelectorAll(".drawer a, [data-menu-close]").forEach(function (el) {
      el.addEventListener("click", closeMenu);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && body.classList.contains("menu-open")) closeMenu();
    });
  }

  /* ---------- Révélations au scroll ---------- */
  var revealEls = document.querySelectorAll(".reveal");
  if (revealEls.length) {
    if (reduced || !("IntersectionObserver" in window)) {
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

  /* ---------- Accordéon FAQ ---------- */
  var accItems = document.querySelectorAll(".acc");
  accItems.forEach(function (item) {
    var q = item.querySelector(".acc__q");
    var panel = item.querySelector(".acc__a");
    if (!q || !panel) return;
    q.addEventListener("click", function () {
      var willOpen = !item.classList.contains("is-open");
      accItems.forEach(function (other) {
        if (other !== item) {
          other.classList.remove("is-open");
          var oq = other.querySelector(".acc__q");
          var op = other.querySelector(".acc__a");
          if (oq) oq.setAttribute("aria-expanded", "false");
          if (op) op.style.maxHeight = null;
        }
      });
      item.classList.toggle("is-open", willOpen);
      q.setAttribute("aria-expanded", willOpen ? "true" : "false");
      panel.style.maxHeight = willOpen ? panel.scrollHeight + "px" : null;
    });
  });

  /* ---------- Présélection de la formule ---------- */
  var formuleMap = {
    "romantique": "La Romantique",
    "brunch": "Le Brunch",
    "sur-mesure": "Sur-Mesure",
    "carte cadeau": "Carte cadeau"
  };
  var select = document.querySelector("#f-formule");
  function setFormule(key) {
    if (!select || !key) return;
    var label = formuleMap[key.toLowerCase()];
    if (!label) return;
    Array.prototype.forEach.call(select.options, function (opt) {
      if (opt.text === label) opt.selected = true;
    });
  }
  document.querySelectorAll("[data-prefill]").forEach(function (el) {
    el.addEventListener("click", function () {
      setFormule(el.getAttribute("data-prefill"));
      var nameField = document.querySelector("#f-nom");
      if (nameField) setTimeout(function () { nameField.focus({ preventScroll: true }); }, 650);
    });
  });
  try {
    var params = new URLSearchParams(window.location.search);
    var wanted = params.get("formule") || params.get("objet");
    if (wanted) setFormule(wanted.replace(/-/g, " "));
  } catch (e) { /* sans incidence */ }

  /* ---------- Soumission du formulaire ---------- */
  var form = document.querySelector("#reservation");
  if (form) {
    var statusEl = form.querySelector("[data-form-status]");
    var submitBtn = form.querySelector(".form__submit");
    var defaultStatus = statusEl ? statusEl.textContent : "";

    function setStatus(msg, cls) {
      if (!statusEl) return;
      statusEl.textContent = msg;
      statusEl.classList.remove("is-success", "is-error");
      if (cls) statusEl.classList.add(cls);
    }
    function isEmail(v) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v); }

    function openMailFallback(d) {
      var sujet = "Demande de réservation · " + (d.formule || "Dans Ma Bulle");
      var corps =
        "Bonjour,\n\nJe souhaite réserver une expérience Dans Ma Bulle.\n\n" +
        "Nom : " + d.nom + "\n" +
        "Email : " + d.email + "\n" +
        "Téléphone : " + d.telephone + "\n" +
        "Formule : " + d.formule + "\n" +
        "Date souhaitée : " + d.date + "\n" +
        "Nombre de convives : " + d.convives + "\n\n" +
        "Message :\n" + d.message + "\n";
      window.location.href = "mailto:" + CONTACT_EMAIL +
        "?subject=" + encodeURIComponent(sujet) + "&body=" + encodeURIComponent(corps);
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();

      // Anti-spam (honeypot)
      if (form.querySelector(".hp") && form.querySelector(".hp").checked) return;

      var data = {
        nom: (form.nom.value || "").trim(),
        email: (form.email.value || "").trim(),
        telephone: (form.telephone.value || "").trim(),
        convives: form.convives.value || "",
        formule: form.formule.value || "",
        date: form.date.value || "",
        message: (form.message.value || "").trim()
      };

      if (!data.nom) { setStatus("Indiquez votre nom pour qu'on sache qui vous êtes.", "is-error"); form.nom.focus(); return; }
      if (!isEmail(data.email)) { setStatus("Vérifiez votre email : on en a besoin pour vous répondre.", "is-error"); form.email.focus(); return; }

      // Repli messagerie si la clé n'est pas configurée
      if (!WEB3FORMS_KEY || WEB3FORMS_KEY === "VOTRE_CLE_WEB3FORMS") {
        openMailFallback(data);
        setStatus("Votre messagerie s'ouvre avec la demande pré-remplie. Pour une réponse immédiate, appelez le " + CONTACT_PHONE + ".");
        return;
      }

      // Envoi via Web3Forms
      if (submitBtn) { submitBtn.disabled = true; }
      setStatus("Envoi en cours…");

      var payload = {
        access_key: WEB3FORMS_KEY,
        subject: "Nouvelle demande de réservation · " + (data.formule || "Dans Ma Bulle"),
        from_name: "Site Dans Ma Bulle",
        nom: data.nom,
        email: data.email,
        telephone: data.telephone || "non renseigné",
        formule: data.formule,
        convives: data.convives,
        date_souhaitee: data.date || "non précisée",
        message: data.message || "(aucun message)"
      };

      fetch("https://api.web3forms.com/submit", {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify(payload)
      })
        .then(function (r) { return r.json(); })
        .then(function (res) {
          if (res && res.success) {
            form.reset();
            setStatus("C'est envoyé. On revient vers vous sous 24h pour composer votre moment. Merci !", "is-success");
          } else {
            openMailFallback(data);
            setStatus("L'envoi automatique a échoué, votre messagerie s'ouvre avec la demande. Sinon, appelez le " + CONTACT_PHONE + ".", "is-error");
          }
        })
        .catch(function () {
          openMailFallback(data);
          setStatus("Connexion impossible. Votre messagerie s'ouvre avec la demande, ou appelez le " + CONTACT_PHONE + ".", "is-error");
        })
        .finally(function () { if (submitBtn) { submitBtn.disabled = false; } });
    });

    form.addEventListener("reset", function () {
      setTimeout(function () { setStatus(defaultStatus); }, 50);
    });
  }

  /* ---------- Année courante ---------- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
