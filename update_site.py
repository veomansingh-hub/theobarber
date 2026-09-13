import re

# 1. Update index.html
with open('index.html', 'r') as f:
    html = f.read()

# Replace the pricing section
old_pricing_regex = re.compile(r'<section class="section pricing.*?</section>', re.DOTALL)

new_pricing_html = """<section class="section pricing" id="pricing" aria-label="pricing" style="padding-top:100px; padding-bottom:100px; background-color: var(--bg-color, #0a0a0a); overflow: hidden;">
        <div class="container" style="max-width: 1400px; text-align: justify; text-align-last: center; line-height: 2;">
          <h2 class="h2 section-title text-center scroll-reveal" style="margin-bottom:60px;">THE SERVICE MENU</h2>
          
          <div class="menu-text-block">
            <span class="service-item scroll-reveal">CLASSIC CUT <span class="price">£32</span></span>
            <span class="separator scroll-reveal">—</span>
            <span class="service-item scroll-reveal">SKIN FADE <span class="price">£38</span></span>
            <span class="separator scroll-reveal">—</span>
            <span class="service-item scroll-reveal">SCISSOR CUT <span class="price">£40</span></span>
            <span class="separator scroll-reveal">—</span>
            <span class="service-item scroll-reveal">BEARD TRIM & SHAPE <span class="price">£20</span></span>
            <span class="separator scroll-reveal">—</span>
            <span class="service-item scroll-reveal">HOT TOWEL SHAVE <span class="price">£30</span></span>
            <span class="separator scroll-reveal">—</span>
            <span class="service-item scroll-reveal">CUT & BEARD <span class="price">£48</span></span>
            <span class="separator scroll-reveal">—</span>
            <span class="service-item scroll-reveal">SKIN FADE & BEARD <span class="price">£55</span></span>
            <span class="separator scroll-reveal">—</span>
            <span class="service-item scroll-reveal">BUZZ CUT <span class="price">£22</span></span>
            <span class="separator scroll-reveal">—</span>
            <span class="service-item scroll-reveal">CHILDREN'S CUT <span class="price">£24</span></span>
            <span class="separator scroll-reveal">—</span>
            <span class="service-item scroll-reveal">STUDENT CUT <span class="price">£27</span></span>
          </div>
        </div>
      </section>"""

html = old_pricing_regex.sub(new_pricing_html, html)

# Fix team section title color by adding inline style just to be sure, and adding scroll-reveal
html = html.replace('class="service-card"', 'class="service-card scroll-reveal"')
html = html.replace('<h3 class="h3 card-title"', '<h3 class="h3 card-title" style="color: #ffffff;"')
html = html.replace('<h2 class="h2 section-title text-center">OUR BARBERS</h2>', '<h2 class="h2 section-title text-center scroll-reveal" style="color: #ffffff;">OUR BARBERS</h2>')

with open('index.html', 'w') as f:
    f.write(html)

# 2. Update style.css
with open('assets/css/style.css', 'r') as f:
    css = f.read()

new_css = """
/*-----------------------------------*\\
  # TYPOGRAPHY MENU & SCROLL REVEAL
\\*-----------------------------------*/

.menu-text-block {
  font-family: 'Playfair Display', serif;
}

.service-item {
  font-size: clamp(2rem, 5vw, 4.5rem);
  display: inline;
  color: rgba(255, 255, 255, 0.2);
  transition: color 0.6s ease, text-shadow 0.6s ease;
  white-space: nowrap;
  font-family: 'Playfair Display', serif;
}

.separator {
  font-size: clamp(2rem, 5vw, 4.5rem);
  color: rgba(255, 255, 255, 0.1);
  margin: 0 2vw;
  display: inline-block;
  vertical-align: middle;
  font-family: 'Rubik', sans-serif;
  font-weight: 300;
  transition: color 0.6s ease;
}

.price {
  font-family: 'Oswald', sans-serif;
  font-size: clamp(1rem, 2.5vw, 2.2rem);
  vertical-align: super;
  margin-left: 5px;
  opacity: 0.8;
}

/* Scroll Animation Classes */
.scroll-reveal {
  opacity: 0.2;
  transform: translateY(20px);
  transition: opacity 0.8s ease-out, transform 0.8s ease-out, color 0.8s ease-out, text-shadow 0.8s ease-out;
}

span.scroll-reveal {
  transform: none; /* Inline elements shouldn't translate usually */
}

.scroll-reveal.in-view {
  opacity: 1;
  transform: translateY(0);
}

span.service-item.scroll-reveal.in-view {
  color: rgba(255, 255, 255, 1);
  text-shadow: 0 0 15px rgba(255, 255, 255, 0.4);
}

span.separator.scroll-reveal.in-view {
  color: rgba(255, 255, 255, 0.3);
}

"""
css += new_css

with open('assets/css/style.css', 'w') as f:
    f.write(css)

# 3. Update script.js
with open('assets/js/script.js', 'r') as f:
    js = f.read()

new_js = """
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
"""

js += new_js

with open('assets/js/script.js', 'w') as f:
    f.write(js)

