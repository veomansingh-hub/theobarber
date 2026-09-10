'use strict';

/**
 * add event on element
 */
const addEventOnElem = function (elem, type, callback) {
  if (elem.length > 1) {
    for (let i = 0; i < elem.length; i++) {
      elem[i].addEventListener(type, callback);
    }
  } else {
    elem.addEventListener(type, callback);
  }
}

/**
 * navbar toggle
 */
const navbar = document.querySelector("[data-navbar]");
const navToggler = document.querySelector("[data-nav-toggler]");
const navLinks = document.querySelectorAll("[data-nav-link]");

const toggleNavbar = () => navbar.classList.toggle("active");
addEventOnElem(navToggler, "click", toggleNavbar);

const closeNavbar = () => navbar.classList.remove("active");
addEventOnElem(navLinks, "click", closeNavbar);

/**
 * header & back top btn active when scroll down to 100px
 */
const header = document.querySelector("[data-header]");
const backTopBtn = document.querySelector("[data-back-top-btn]");

const headerActive = function () {
  if (window.scrollY > 100) {
    header.classList.add("active");
    backTopBtn.classList.add("active");
  } else {
    header.classList.remove("active");
    backTopBtn.classList.remove("active");
  }
}
addEventOnElem(window, "scroll", headerActive);

/**
 * filter function
 */
const filterBtns = document.querySelectorAll("[data-filter-btn]");
const filterItems = document.querySelectorAll("[data-filter]");

if (filterBtns.length > 0) {
  let lastClickedFilterBtn = filterBtns[0];

  const filter = function () {
    lastClickedFilterBtn.classList.remove("active");
    this.classList.add("active");
    lastClickedFilterBtn = this;

    for (let i = 0; i < filterItems.length; i++) {
      if (this.dataset.filterBtn === filterItems[i].dataset.filter ||
        this.dataset.filterBtn === "all") {
        filterItems[i].style.display = "block";
        filterItems[i].classList.add("active");
      } else {
        filterItems[i].style.display = "none";
        filterItems[i].classList.remove("active");
      }
    }
  }
  addEventOnElem(filterBtns, "click", filter);
}

/**
 * TheoMedia Curtain Logic
 */
document.addEventListener("DOMContentLoaded", () => {
  const curtain = document.getElementById('theomediaCurtain');
  if (curtain) {
    const hasSeenCurtain = sessionStorage.getItem('theomediaCurtainShown');
    
    if (!hasSeenCurtain) {
      document.body.style.overflow = 'hidden';
      
      // The animation handles the visual split, but we need to remove it from DOM
      setTimeout(() => {
        curtain.remove();
        document.body.style.overflow = '';
        sessionStorage.setItem('theomediaCurtainShown', 'true');
      }, 2200); // 2.2 seconds total duration
      
    } else {
      curtain.style.display = 'none';
      curtain.remove();
    }
  }
});

/**
 * Scroll Reveal Animation
 */
document.addEventListener("DOMContentLoaded", () => {
  const revealElements = document.querySelectorAll('.scroll-reveal');
  
  const revealOptions = {
    root: null,
    rootMargin: '-15% 0px -15% 0px', /* Trigger when element is well within viewport */
    threshold: 0.1
  };
  
  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
      } else {
        // Remove class when scrolling out to trigger 'disappear' effect again
        entry.target.classList.remove('in-view');
      }
    });
  }, revealOptions);
  
  revealElements.forEach(el => {
    revealObserver.observe(el);
  });
});
