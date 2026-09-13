import re

# 1. Update index.html
try:
    with open('index.html', 'r') as f:
        html = f.read()

    # Make the hero title bigger and italicize part of it
    html = html.replace('LONDON BARBERING,<br>DONE PROPERLY.', 'LONDON BARBERING,<br><span class="hero-italic">DONE PROPERLY.</span>')

    # Hide the header-top by adding a class 'hide-on-premium'
    html = html.replace('class="header-top"', 'class="header-top hide-on-premium"')

    # Wrap the gallery images to allow asymmetrical layout
    html = html.replace('<div class="gallery-card">', '<div class="gallery-card premium-lookbook">')

    # Modify the about section title to be massive
    html = html.replace('<h2 class="h2 section-title text-center scroll-reveal" style="margin-bottom:10px; font-size:1.8rem; letter-spacing:2px; font-weight:500;">OUR APPROACH</h2>', '<h2 class="h2 section-title text-center premium-huge-title scroll-reveal">OUR APPROACH</h2>')

    # Fix team title too
    html = html.replace('<h2 class="h2 section-title text-center scroll-reveal" style="color: #ffffff;">OUR BARBERS</h2>', '<h2 class="h2 section-title text-center premium-huge-title scroll-reveal" style="color: #ffffff;">OUR BARBERS</h2>')

    with open('index.html', 'w') as f:
        f.write(html)
except Exception as e:
    print(f"Error modifying HTML: {e}")

# 2. Update style.css
try:
    with open('assets/css/style.css', 'r') as f:
        css = f.read()

    premium_css = """
/*-----------------------------------*\\
  # PREMIUM LEAD ENGINEER REDESIGN
\\*-----------------------------------*/

:root {
  --bg-color: #060606;
  --rich-black-fogra-39: #060606;
  --eerie-black-1: #0a0a0a;
  --eerie-black-2: #0f0f0f;
  --indian-yellow: #C1A377;
  --harvest-gold: #C1A377;
  --white: #F4F1E8;
  --platinum: #e0ddd5;
  --ff-playfair: 'Playfair Display', serif;
  --ff-oswald: 'Oswald', sans-serif;
  --ff-rubik: 'Rubik', sans-serif;
}

html {
  scroll-behavior: smooth;
}

body {
  background-color: var(--bg-color);
  color: var(--platinum);
  /* Subtle film grain/noise overlay using base64 SVG */
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 400 400' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.04'/%3E%3C/svg%3E");
  background-attachment: fixed;
}

.hide-on-premium {
  display: none !important;
}

/* Header & Logo */
.header {
  background-color: transparent !important;
  border-bottom: 1px solid rgba(255,255,255,0.05);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
}
.header.active {
  background-color: rgba(6, 6, 6, 0.9) !important;
}

.logo {
  font-family: var(--ff-playfair);
  font-size: 2.2rem;
  letter-spacing: 2px;
  font-weight: 400;
}
.logo .span {
  font-family: var(--ff-oswald);
  letter-spacing: 4px;
  font-size: 0.8rem;
  opacity: 0.6;
  margin-top: 5px;
}

/* Button Overrides */
.btn {
  background-color: transparent !important;
  border: 1px solid rgba(255,255,255,0.2) !important;
  color: var(--white) !important;
  border-radius: 0 !important;
  padding: 15px 30px !important;
  transition: all 0.4s ease !important;
  font-family: var(--ff-oswald);
  letter-spacing: 2px;
}
.btn::before {
  display: none !important;
}
.btn:hover {
  background-color: var(--white) !important;
  color: var(--bg-color) !important;
  border-color: var(--white) !important;
}

/* Hero Section */
.hero {
  padding-top: 25vh !important;
  padding-bottom: 15vh !important;
  background-attachment: fixed;
  background-position: center;
  position: relative;
}
.hero::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(to bottom, rgba(6,6,6,0.2) 0%, rgba(6,6,6,1) 100%);
  pointer-events: none;
}
.hero .container {
  position: relative;
  z-index: 2;
}

.hero-title {
  font-family: var(--ff-playfair);
  font-size: clamp(4rem, 8vw, 10rem);
  line-height: 1;
  font-weight: 400;
  text-transform: uppercase;
  color: var(--white);
}
.hero-italic {
  font-style: italic;
  text-transform: lowercase;
  color: var(--indian-yellow);
}

.hero-text {
  font-size: 1.2rem;
  max-width: 500px;
  opacity: 0.8;
  font-family: var(--ff-rubik);
  line-height: 1.6;
}

/* Global Sections */
.section {
  padding-block: 15vh !important;
}

/* Premium Huge Titles */
.premium-huge-title {
  font-family: var(--ff-playfair) !important;
  font-size: clamp(3rem, 6vw, 7rem) !important;
  font-weight: 400 !important;
  letter-spacing: 0 !important;
  text-transform: none !important;
  color: var(--white) !important;
  margin-bottom: 40px !important;
}

/* Editorial Lookbook Gallery */
.gallery .grid-list {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 30px;
}
.gallery .grid-list li:nth-child(1) { grid-column: 1 / 8; }
.gallery .grid-list li:nth-child(2) { grid-column: 8 / 13; margin-top: 100px; }
.gallery .grid-list li:nth-child(3) { grid-column: 1 / 6; margin-top: -50px; }
.gallery .grid-list li:nth-child(4) { grid-column: 6 / 13; }

.premium-lookbook {
  position: relative;
  overflow: hidden;
  aspect-ratio: 4/5;
}
.premium-lookbook img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 1.5s cubic-bezier(0.2, 1, 0.2, 1), filter 0.8s ease;
  filter: grayscale(80%) contrast(1.2);
}
.premium-lookbook:hover img {
  transform: scale(1.05);
  filter: grayscale(0%) contrast(1);
}

@media (max-width: 768px) {
  .gallery .grid-list {
    display: flex;
    flex-direction: column;
  }
  .gallery .grid-list li { margin-top: 0 !important; }
}

/* Booking Form Minimalist Overrides */
.appoin-form {
  background: transparent !important;
  border: 1px solid rgba(255,255,255,0.1);
  padding: 50px !important;
}
.input-field {
  background: transparent !important;
  border: none !important;
  border-bottom: 1px solid rgba(255,255,255,0.2) !important;
  border-radius: 0 !important;
  padding-inline: 0 !important;
  color: var(--white) !important;
  font-family: var(--ff-rubik);
}
.input-field:focus {
  border-bottom-color: var(--white) !important;
  outline: none !important;
}

/* Clean up other sections */
.title-wrapper {
  margin-bottom: 60px;
}
.section-text {
  font-size: 1.1rem;
  line-height: 1.8;
  opacity: 0.8;
}
"""

    css += premium_css
    with open('assets/css/style.css', 'w') as f:
        f.write(css)
except Exception as e:
    print(f"Error modifying CSS: {e}")

