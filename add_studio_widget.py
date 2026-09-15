import re

# 1. UPDATE HTML
with open('index.html', 'r') as f:
    html = f.read()

# Remove old fixed button
old_btn = r'<a href="https://www.theomedia.co.uk/contact" target="_blank" rel="noopener noreferrer" class="theomedia-fixed-btn" aria-label="Contact TheoMedia">[^<]*CONTACT THEOMEDIA ↗[^<]*</a>'
html = re.sub(old_btn, '', html, flags=re.DOTALL)

# Add new widget HTML before </body>
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

</body>
"""
html = html.replace('</body>', widget_html)

with open('index.html', 'w') as f:
    f.write(html)

# 2. UPDATE CSS
with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Add CSS for widget
widget_css = """
/*-----------------------------------*\\
  # THEOMEDIA STUDIO BRANDING WIDGET
\\*-----------------------------------*/

.tm-studio-trigger {
  position: fixed;
  bottom: calc(20px + env(safe-area-inset-bottom));
  right: 20px;
  background: rgba(10, 10, 10, 0.85);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 40px;
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 6px 16px 6px 6px;
  cursor: pointer;
  z-index: 1000;
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
}

.tm-studio-trigger:hover {
  background: rgba(255, 255, 255, 0.05);
  border-color: rgba(255, 255, 255, 0.3);
  transform: translateY(-2px);
}

.tm-trigger-logo {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  object-fit: cover;
}

.tm-trigger-text {
  font-family: var(--ff-rubik);
  font-size: 0.85rem;
  font-weight: 400;
  color: var(--white);
  letter-spacing: 0.5px;
}

.tm-studio-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(5px);
  -webkit-backdrop-filter: blur(5px);
  z-index: 9999;
  opacity: 0;
  visibility: hidden;
  transition: all 0.4s ease;
}

.tm-studio-sheet {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background: #080808;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
  z-index: 10000;
  padding: 30px 20px calc(30px + env(safe-area-inset-bottom));
  transform: translateY(100%);
  transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 -10px 40px rgba(0, 0, 0, 0.8);
}

.tm-studio-overlay.active {
  opacity: 1;
  visibility: visible;
}

.tm-studio-sheet.active {
  transform: translateY(0);
}

.tm-sheet-header {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 30px;
  position: relative;
}

.tm-sheet-logo {
  width: 44px;
  height: 44px;
  border-radius: 50%;
}

.tm-sheet-title-box {
  flex: 1;
}

.tm-sheet-title {
  font-family: var(--ff-playfair);
  font-size: 1.4rem;
  color: var(--white);
  margin-bottom: 2px;
  font-weight: 400;
}

.tm-sheet-subtitle {
  font-family: var(--ff-rubik);
  font-size: 0.85rem;
  color: var(--indian-yellow);
  text-transform: uppercase;
  letter-spacing: 1px;
}

.tm-sheet-close {
  background: transparent;
  color: var(--white);
  font-size: 1.8rem;
  border: none;
  cursor: pointer;
  opacity: 0.6;
  transition: opacity 0.3s;
}

.tm-sheet-close:hover {
  opacity: 1;
}

.tm-sheet-actions {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.tm-action-btn {
  display: flex;
  align-items: center;
  gap: 15px;
  padding: 16px 20px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  color: var(--white);
  text-decoration: none;
  font-family: var(--ff-rubik);
  font-size: 1rem;
  transition: all 0.3s ease;
}

.tm-action-btn ion-icon {
  font-size: 1.4rem;
  color: var(--indian-yellow);
}

.tm-action-btn:hover {
  background: rgba(255, 255, 255, 0.08);
  border-color: rgba(255, 255, 255, 0.2);
  transform: translateX(5px);
}

@media (min-width: 768px) {
  .tm-studio-trigger {
    bottom: 30px;
    right: 30px;
  }
  
  .tm-studio-sheet {
    bottom: 90px;
    right: 30px;
    left: auto;
    width: 360px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    padding: 25px;
    transform: translateY(20px) scale(0.95);
    opacity: 0;
    visibility: hidden;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  }
  
  .tm-studio-sheet.active {
    transform: translateY(0) scale(1);
    opacity: 1;
    visibility: visible;
  }
}
"""

css += widget_css
with open('assets/css/style.css', 'w') as f:
    f.write(css)

# 3. UPDATE JS
with open('assets/js/script.js', 'r') as f:
    js = f.read()

js += "\n\nfunction toggleTmMenu() {\n  document.getElementById('tmMenuOverlay').classList.toggle('active');\n  document.getElementById('tmMenuSheet').classList.toggle('active');\n}\n"

with open('assets/js/script.js', 'w') as f:
    f.write(js)

print("Widget added successfully")
