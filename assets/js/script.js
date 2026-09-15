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

/**
 * Advanced Marquee Scroll Lighting & Parallax
 */
document.addEventListener("DOMContentLoaded", () => {
  const marqueeSection = document.querySelector('.marquee-pricing-section');
  const marqueeContainer = document.querySelector('.marquee-rows-container');
  const marqueeRows = document.querySelectorAll('.marquee-row');
  
  if (!marqueeSection || !marqueeRows.length) return;

  function updateMarqueeScroll() {
    const secRect = marqueeSection.getBoundingClientRect();
    const viewportHeight = window.innerHeight;
    const viewportCenter = viewportHeight / 2;
    
    // 1. Parallax Translation
    // The section is 160vh, so scrollable amount is 60vh.
    const totalScroll = secRect.height - viewportHeight;
    let progress = -secRect.top / totalScroll;
    progress = Math.max(0, Math.min(1, progress));
    
    // Translate the container up by 40vh over the course of the section scroll
    if (marqueeContainer) {
      marqueeContainer.style.transform = `translateY(-${progress * 40}vh)`;
    }
    
    // 2. Lighting Effect
    marqueeRows.forEach(row => {
      const rect = row.getBoundingClientRect();
      const rowCenter = rect.top + rect.height / 2;
      const distance = Math.abs(viewportCenter - rowCenter);
      
      const maxDistance = viewportHeight * 0.4; // Fade completely out at 40% from center
      let ratio = distance / maxDistance;
      ratio = Math.max(0, Math.min(1, ratio));
      
      let opacity, brightness;
      // Maximum readability zone: middle 30% of screen (distance ratio < 0.3)
      if (ratio < 0.3) {
        opacity = 1;
        brightness = 1;
      } else {
        const fadeProgress = (ratio - 0.3) / 0.7; // 0 to 1
        opacity = 1 - (fadeProgress * 0.85); // 1 down to 0.15
        brightness = 1 - fadeProgress;
      }
      
      row.style.opacity = opacity;
      row.style.color = '#F4F1E8';
      
      // VERY subtle soft highlight, no excessive neon glow
      const shadowOpacity = brightness * 0.15;
      row.style.textShadow = `0 0 12px rgba(244, 241, 232, ${shadowOpacity})`;
    });
    
    requestAnimationFrame(updateMarqueeScroll);
  }
  
  requestAnimationFrame(updateMarqueeScroll);
});



