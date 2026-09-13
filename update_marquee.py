import re

with open('index.html', 'r') as f:
    html = f.read()

# Generate the rows
rows_data = [
    [("CLASSIC CUT", "£32"), ("SKIN FADE", "£38"), ("SCISSOR CUT", "£40")],
    [("BEARD TRIM & SHAPE", "£20"), ("HOT TOWEL SHAVE", "£30"), ("CUT + BEARD", "£48")],
    [("SKIN FADE + BEARD", "£55"), ("BUZZ CUT", "£22"), ("CHILDREN'S CUT", "£24")],
    [("STUDENT CUT", "£27"), ("CLASSIC CUT", "£32"), ("SKIN FADE", "£38")]
]

rows_html = ""
for i, row in enumerate(rows_data):
    direction = "marquee-left" if i % 2 == 0 else "marquee-right"
    duration = "35s" if i % 2 == 0 else "40s"
    if i == 2: duration = "38s"
    if i == 3: duration = "42s"
    
    content_html = ""
    for name, price in row:
        content_html += f'<span class="marquee-text">{name} <span class="marquee-price">{price}</span></span><span class="marquee-separator">—</span>'
    
    # We duplicate the content a few times to ensure it fills the screen and wraps seamlessly
    # 4 times should be plenty to fill 100vw even on ultrawide
    full_content = f'<div class="marquee-content">{content_html * 3}</div><div class="marquee-content">{content_html * 3}</div>'
    
    rows_html += f"""
      <div class="marquee-row {direction}" style="--duration: {duration};">
        <div class="marquee-inner">
          {full_content}
        </div>
      </div>"""

new_pricing_html = f"""<section class="section marquee-pricing-section" id="pricing" style="height: 160vh; background-color: var(--bg-color, #0a0a0a); position: relative; padding: 0;">
  <div class="marquee-sticky-stage" style="position: sticky; top: 0; height: 100vh; overflow: hidden; display: flex; align-items: center; justify-content: center; mask-image: linear-gradient(to right, transparent 0%, black 10%, black 90%, transparent 100%); -webkit-mask-image: linear-gradient(to right, transparent 0%, black 5%, black 95%, transparent 100%);">
    <div class="marquee-rows-container" style="width: 100%; display: flex; flex-direction: column; gap: 8vh; will-change: transform;">
{rows_html}
    </div>
  </div>
</section>"""

old_pricing_regex = re.compile(r'<section class="section pricing".*?</section>', re.DOTALL)
if old_pricing_regex.search(html):
    html = old_pricing_regex.sub(new_pricing_html, html)
else:
    print("Could not find old pricing section.")

with open('index.html', 'w') as f:
    f.write(html)


# Update style.css
with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Remove the old typography menu CSS to keep it clean
# I'll just append the new marquee CSS. The old classes like .service-item won't hurt.

new_css = """
/*-----------------------------------*\\
  # PREMIUM SCROLLING MARQUEE
\\*-----------------------------------*/

.marquee-row {
  display: flex;
  white-space: nowrap;
  width: 100vw;
  opacity: 0.15; /* Base dark state */
  will-change: opacity, color;
}

.marquee-inner {
  display: flex;
  width: max-content;
  will-change: transform;
}

.marquee-content {
  display: flex;
  align-items: center;
}

.marquee-left .marquee-inner {
  animation: marqueeLeft var(--duration) linear infinite;
}

.marquee-right .marquee-inner {
  animation: marqueeRight var(--duration) linear infinite;
}

@keyframes marqueeLeft {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

@keyframes marqueeRight {
  0% { transform: translateX(-50%); }
  100% { transform: translateX(0); }
}

.marquee-text {
  font-family: 'Playfair Display', serif;
  font-size: clamp(27px, 6vw, 88px);
  color: inherit;
  margin: 0;
  padding: 0;
}

.marquee-price {
  font-family: 'Oswald', sans-serif;
  font-size: clamp(27px, 6vw, 88px);
  margin-left: 8px;
  opacity: 0.9;
}

.marquee-separator {
  font-family: 'Rubik', sans-serif;
  font-size: clamp(27px, 6vw, 88px);
  margin: 0 4vw;
  font-weight: 300;
  opacity: 0.3;
}

@media (prefers-reduced-motion: reduce) {
  .marquee-left .marquee-inner,
  .marquee-right .marquee-inner {
    animation-duration: 120s; /* Extremely slow instead of completely stopped */
  }
}
"""

css += new_css
with open('assets/css/style.css', 'w') as f:
    f.write(css)


# Update script.js
with open('assets/js/script.js', 'r') as f:
    js = f.read()

# Find the old scroll reveal and append the new complex marquee scroll math
new_js = """
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
"""

js += new_js
with open('assets/js/script.js', 'w') as f:
    f.write(js)

