import re

with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Remove old branding CSS
old_branding_marker = r'/\*-----------------------------------\*\\\n\s*# THEOMEDIA STUDIO BRANDING WIDGET\n\\\*-----------------------------------\*/'
# The old block ends where? It goes to the end of the file.
match = re.search(old_branding_marker, css)
if match:
    css = css[:match.start()]

new_css = """
/*-----------------------------------*\\
  # REFINED THEOMEDIA STUDIO BRANDING
\\*-----------------------------------*/

/* 1. Opening Signature */
.tm-opening-text {
  font-family: var(--ff-rubik);
  font-size: 1.2rem;
  letter-spacing: 0.15em;
  color: var(--white);
  text-decoration: none;
  opacity: 0.7;
  position: relative;
  padding-bottom: 4px;
  transition: opacity 250ms cubic-bezier(0.25, 1, 0.5, 1), transform 250ms cubic-bezier(0.25, 1, 0.5, 1);
  display: inline-block;
}

.tm-opening-text::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0%;
  height: 1px;
  background-color: var(--white);
  transition: width 300ms cubic-bezier(0.25, 1, 0.5, 1);
}

.tm-opening-text:hover {
  opacity: 1;
  transform: translateY(-2px);
}

.tm-opening-text:hover::after {
  width: 100%;
}

/* 2. Studio Dock (Architectural, Masculine) */
.tm-studio-dock {
  position: fixed;
  bottom: calc(24px + env(safe-area-inset-bottom));
  left: 50%;
  transform: translateX(-50%);
  background: rgba(12, 12, 12, 0.8);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 6px;
  display: flex;
  align-items: center;
  gap: 24px;
  padding: 10px 16px;
  z-index: 1000;
}

.tm-dock-brand {
  font-family: var(--ff-oswald);
  font-size: 0.75rem;
  letter-spacing: 0.15em;
  color: rgba(255, 255, 255, 0.4);
  text-transform: uppercase;
  user-select: none;
}

.tm-dock-actions {
  display: flex;
  align-items: center;
  gap: 16px;
  border-left: 1px solid rgba(255, 255, 255, 0.12);
  padding-left: 16px;
}

.tm-dock-btn {
  font-family: var(--ff-rubik);
  font-size: 0.85rem;
  color: var(--white);
  text-decoration: none;
  opacity: 0.85;
  display: flex;
  align-items: center;
  gap: 4px;
  transition: opacity 250ms cubic-bezier(0.25, 1, 0.5, 1);
}

.tm-dock-arrow {
  display: inline-block;
  font-family: system-ui, sans-serif;
  font-size: 0.9rem;
  transition: transform 250ms cubic-bezier(0.25, 1, 0.5, 1);
}

.tm-dock-btn:hover {
  opacity: 1;
}

.tm-dock-btn:hover .tm-dock-arrow {
  transform: translate(2px, -2px);
}

.tm-dock-desktop { display: inline; }
.tm-dock-mobile { display: none; }

/* 3. Footer Colophon */
.tm-footer-colophon {
  display: flex;
  flex-direction: column;
  gap: 6px;
  font-family: var(--ff-rubik);
}

.tm-colophon-title {
  font-family: var(--ff-oswald);
  font-size: 0.75rem;
  letter-spacing: 0.1em;
  color: rgba(255, 255, 255, 0.4);
  margin-bottom: 4px;
}

.tm-colophon-brand {
  font-family: var(--ff-playfair);
  font-size: 1.5rem;
  color: var(--white);
  text-decoration: none;
  font-style: italic;
  display: inline-block;
  transition: opacity 250ms ease;
}

.tm-colophon-brand:hover {
  opacity: 0.7;
}

.tm-colophon-url, .tm-colophon-loc {
  font-size: 0.8rem;
  color: rgba(255, 255, 255, 0.5);
  letter-spacing: 0.05em;
}

.tm-colophon-links {
  display: flex;
  gap: 16px;
  margin-top: 12px;
}

.tm-colophon-link {
  font-size: 0.85rem;
  color: var(--white);
  text-decoration: none;
  opacity: 0.8;
  position: relative;
  transition: opacity 250ms ease;
}

.tm-colophon-link:hover {
  opacity: 1;
}

.tm-colophon-link::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 100%;
  height: 1px;
  background-color: rgba(255, 255, 255, 0.3);
  transition: background-color 250ms ease;
}

.tm-colophon-link:hover::after {
  background-color: var(--white);
}

/* Mobile Adjustments */
@media (max-width: 575px) {
  .tm-studio-dock {
    width: calc(100% - 32px);
    max-width: 400px;
    justify-content: space-between;
    padding: 12px 16px;
    gap: 12px;
  }
  
  .tm-dock-brand {
    font-size: 0.7rem;
  }
  
  .tm-dock-actions {
    gap: 12px;
    padding-left: 12px;
  }
  
  .tm-dock-desktop { display: none; }
  .tm-dock-mobile { display: inline; }
}
"""

css += new_css
with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("CSS updated.")
