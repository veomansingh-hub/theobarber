import re

with open('menu.html', 'r') as f:
    html = f.read()

# Add link to style.css and script.js if not there
if 'style.css' not in html:
    html = html.replace('</head>', '  <link rel="stylesheet" href="./assets/css/style.css">\n</head>')
if 'script.js' not in html:
    html = html.replace('</body>', '  <script src="./assets/js/script.js"></script>\n</body>')

# Remove old button
old_btn = r'<a href="https://www.theomedia.co.uk/contact" target="_blank" rel="noopener noreferrer" class="theomedia-fixed-btn" aria-label="Contact TheoMedia">\s*CONTACT THEOMEDIA ↗\s*</a>'
html = re.sub(old_btn, '', html, flags=re.DOTALL)

widget_html = """
  <!-- NEW THEOMEDIA STUDIO BRANDING -->
  <div class="tm-studio-trigger" onclick="toggleTmMenu()" aria-label="About the website creator">
    <img src="./assets/images/theomedia-logo.jpg" alt="TheoMedia" class="tm-trigger-logo">
    <span class="tm-trigger-text">Site by TheoMedia</span>
  </div>

  <div class="tm-studio-overlay" id="tmMenuOverlay" onclick="toggleTmMenu()"></div>
  
  <div class="tm-studio-sheet" id="tmMenuSheet">
    <div class="tm-sheet-header">
      <img src="./assets/images/theomedia-logo.jpg" alt="TheoMedia" class="tm-sheet-logo">
      <div class="tm-sheet-title-box">
        <h4 class="tm-sheet-title">TheoMedia Studio</h4>
        <p class="tm-sheet-subtitle">Premium Digital Experiences</p>
      </div>
      <button class="tm-sheet-close" onclick="toggleTmMenu()">&times;</button>
    </div>
    <div class="tm-sheet-actions">
      <a href="https://www.theomedia.co.uk" target="_blank" class="tm-action-btn">
        <span>Visit Studio Website</span>
      </a>
      <a href="https://wa.me/353852258004" target="_blank" class="tm-action-btn">
        <span>WhatsApp Message</span>
      </a>
      <a href="tel:+353852258004" class="tm-action-btn">
        <span>+353 85 225 8004</span>
      </a>
    </div>
  </div>
"""
# Note: I used text for close button (&times;) and removed ion-icons in menu.html 
# because menu.html might not load ionicons. But I can just add ionicons to menu.html!

if 'ionicons' not in html:
    html = html.replace('</head>', '  <script type="module" src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"></script>\n  <script nomodule src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"></script>\n</head>')

# Re-inject widget with ionicons
widget_html = """
  <!-- NEW THEOMEDIA STUDIO BRANDING -->
  <div class="tm-studio-trigger" onclick="toggleTmMenu()" aria-label="About the website creator">
    <img src="./assets/images/theomedia-logo.jpg" alt="TheoMedia" class="tm-trigger-logo">
    <span class="tm-trigger-text">Site by TheoMedia</span>
  </div>

  <div class="tm-studio-overlay" id="tmMenuOverlay" onclick="toggleTmMenu()"></div>
  
  <div class="tm-studio-sheet" id="tmMenuSheet">
    <div class="tm-sheet-header">
      <img src="./assets/images/theomedia-logo.jpg" alt="TheoMedia" class="tm-sheet-logo">
      <div class="tm-sheet-title-box">
        <h4 class="tm-sheet-title">TheoMedia Studio</h4>
        <p class="tm-sheet-subtitle">Premium Digital Experiences</p>
      </div>
      <button class="tm-sheet-close" onclick="toggleTmMenu()"><ion-icon name="close-outline"></ion-icon></button>
    </div>
    <div class="tm-sheet-actions">
      <a href="https://www.theomedia.co.uk" target="_blank" class="tm-action-btn">
        <ion-icon name="globe-outline"></ion-icon>
        <span>Visit Studio Website</span>
      </a>
      <a href="https://wa.me/353852258004" target="_blank" class="tm-action-btn">
        <ion-icon name="logo-whatsapp"></ion-icon>
        <span>WhatsApp Message</span>
      </a>
      <a href="tel:+353852258004" class="tm-action-btn">
        <ion-icon name="call-outline"></ion-icon>
        <span>+353 85 225 8004</span>
      </a>
    </div>
  </div>
"""
html = html.replace('</body>', widget_html + '\n</body>')

with open('menu.html', 'w') as f:
    f.write(html)
