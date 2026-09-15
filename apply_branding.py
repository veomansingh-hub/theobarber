import re

# ==========================================
# 1. UPDATE index.html
# ==========================================
with open('index.html', 'r') as f:
    html = f.read()

# Fix opening curtain
old_curtain = re.compile(r'<div class="curtain-content">.*?</div>', re.DOTALL)
new_curtain = """<div class="curtain-content">
      <a href="https://theomedia.co.uk" target="_blank" rel="noopener noreferrer" class="tm-opening-text">theomedia.co.uk</a>
    </div>"""
html = old_curtain.sub(new_curtain, html, count=1)

# Fix Wren & Crown Appointment Form Action
html = html.replace('action="https://www.theomedia.co.uk/contact"', 'action="#"')

# Fix Wren & Crown Contact Button (which had a TheoMedia link)
old_contact_btn = re.compile(r'<a href="https://www\.theomedia\.co\.uk/contact"[^>]*>\s*<span class="span">CONTACT ↗</span>\s*</a>', re.DOTALL)
new_contact_btn = """<a href="tel:+442071234567" class="btn has-before" style="margin: 0 auto; display:inline-flex;">
            <span class="span">CONTACT ↗</span>
          </a>"""
html = old_contact_btn.sub(new_contact_btn, html)

# Replace the Footer Credit section
old_credit_list = re.compile(r'<ul class="footer-list"[^>]*>\s*<li><p class="footer-list-title"[^>]*>Credit</p></li>.*?</ul>', re.DOTALL)
new_colophon = """<div class="tm-footer-colophon">
            <span class="tm-colophon-title">DIGITAL EXPERIENCE BY</span>
            <a href="https://theomedia.co.uk" target="_blank" rel="noopener noreferrer" class="tm-colophon-brand">TheoMedia &nearr;</a>
            <span class="tm-colophon-url">theomedia.co.uk</span>
            <span class="tm-colophon-loc">UK &middot; IRELAND &middot; EUROPE</span>
            <div class="tm-colophon-links">
              <a href="https://theomedia.co.uk" target="_blank" rel="noopener noreferrer" class="tm-colophon-link">Explore Studio &nearr;</a>
              <a href="https://wa.me/353852258004" target="_blank" rel="noopener noreferrer" class="tm-colophon-link">WhatsApp &nearr;</a>
            </div>
          </div>"""
html = old_credit_list.sub(new_colophon, html)

# Remove the old tm-studio widget
old_widget = re.compile(r'<!-- NEW THEOMEDIA STUDIO BRANDING -->.*?</div>\s*</div>', re.DOTALL)
html = old_widget.sub('', html)

# Add the new Studio Dock
new_dock = """
  <!-- PREMIUM STUDIO DOCK -->
  <div class="tm-studio-dock">
    <span class="tm-dock-brand">THEOMEDIA</span>
    <div class="tm-dock-actions">
      <a href="https://theomedia.co.uk" target="_blank" rel="noopener noreferrer" class="tm-dock-btn">
        <span class="tm-dock-desktop">Explore the Studio</span><span class="tm-dock-mobile">Studio</span> <span class="tm-dock-arrow">&nearr;</span>
      </a>
      <a href="https://wa.me/353852258004" target="_blank" rel="noopener noreferrer" class="tm-dock-btn">
        WhatsApp <span class="tm-dock-arrow">&nearr;</span>
      </a>
    </div>
  </div>
"""
html = html.replace('</body>', new_dock + '\n</body>')

with open('index.html', 'w') as f:
    f.write(html)

# ==========================================
# 2. UPDATE menu.html
# ==========================================
try:
    with open('menu.html', 'r') as f:
        menu_html = f.read()
    
    # Remove old widget from menu.html
    menu_html = old_widget.sub('', menu_html)
    menu_html = menu_html.replace('</body>', new_dock + '\n</body>')
    
    with open('menu.html', 'w') as f:
        f.write(menu_html)
except FileNotFoundError:
    pass


# ==========================================
# 3. UPDATE script.js
# ==========================================
with open('assets/js/script.js', 'r') as f:
    js = f.read()

# Remove old toggle function
js = re.sub(r'function toggleTmMenu\(\) \{.*?\}', '', js, flags=re.DOTALL)

with open('assets/js/script.js', 'w') as f:
    f.write(js)

print("HTML and JS updated.")
