import re

with open('index.html', 'r') as f:
    html = f.read()

# Fix the Curtain
old_curtain = """<div class="curtain-content">
      <span class="made-by">MADE BY</span>
      <a href="https://www.theomedia.co.uk/" target="_blank" rel="noopener noreferrer" class="theomedia-link">THEOMEDIA.CO.UK</a>
    </div>"""

new_curtain = """<div class="curtain-content">
      <span class="made-by">WEBSITE BY</span>
      <a href="https://www.theomedia.co.uk/" target="_blank" rel="noopener noreferrer" class="theomedia-link" style="display:flex; flex-direction:column; align-items:center; gap:20px;">
        <img src="./assets/images/theomedia-logo.jpg" alt="TheoMedia Logo" style="width: 120px; height: 120px; border-radius: 50%; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
      </a>
    </div>"""

html = html.replace(old_curtain, new_curtain)

# Fix the Footer
old_footer_regex = re.compile(r'<footer class="footer.*?</header>', re.DOTALL) # wait, footer to footer
old_footer_regex = re.compile(r'<footer class="footer.*?</footer>', re.DOTALL)

new_footer = """<footer class="footer" style="background-color: var(--rich-black-fogra-39); padding-top: 80px; padding-bottom: 80px; border-top: 1px solid rgba(255,255,255,0.05);">
    <div class="container">
      <div class="footer-top" style="display:flex; justify-content:space-between; flex-wrap:wrap; gap:60px;">
        
        <div class="footer-brand" style="flex: 1; min-width: 250px;">
          <a href="#top" class="logo" style="margin-bottom: 20px;">
            WREN & CROWN
            <span class="span">BARBERS · LONDON</span>
          </a>
          <p class="section-text" style="color: var(--white); opacity: 0.7; line-height: 1.8;">
            COVENT GARDEN<br>LONDON · WC2
          </p>
        </div>
        
        <div class="footer-link-box" style="flex: 2; display: flex; justify-content: space-around; flex-wrap: wrap; gap: 40px;">
          
          <ul class="footer-list" style="padding: 0;">
            <li><p class="footer-list-title" style="color: var(--white); font-family: var(--ff-oswald); letter-spacing: 2px; margin-bottom: 20px; font-size: 1.6rem; text-transform: uppercase;">Navigation</p></li>
            <li style="margin-bottom: 10px;"><a href="menu.html" class="footer-link" style="transition: opacity 0.3s ease;">SERVICES</a></li>
            <li style="margin-bottom: 10px;"><a href="menu.html" class="footer-link" style="transition: opacity 0.3s ease;">PRICES</a></li>
            <li style="margin-bottom: 10px;"><a href="#gallery" class="footer-link" style="transition: opacity 0.3s ease;">THE CRAFT</a></li>
            <li style="margin-bottom: 10px;"><a href="#about" class="footer-link" style="transition: opacity 0.3s ease;">ABOUT</a></li>
            <li style="margin-bottom: 10px;"><a href="#appointment" class="footer-link" style="transition: opacity 0.3s ease;">BOOK</a></li>
            <li><a href="#contact" class="footer-link" style="transition: opacity 0.3s ease;">CONTACT</a></li>
          </ul>
          
          <ul class="footer-list" style="padding: 0;">
             <li><p class="footer-list-title" style="color: var(--white); font-family: var(--ff-oswald); letter-spacing: 2px; margin-bottom: 20px; font-size: 1.6rem; text-transform: uppercase;">Credit</p></li>
             
             <li style="display: flex; align-items: center; gap: 15px; margin-bottom: 30px;">
               <img src="./assets/images/theomedia-logo.jpg" alt="TheoMedia" style="width: 50px; height: 50px; border-radius: 50%;">
               <div>
                 <span style="display:block; color:var(--white); opacity:0.7; font-size: 1.2rem; margin-bottom: 2px;">WEBSITE BY</span>
                 <a href="https://www.theomedia.co.uk/" target="_blank" rel="noopener noreferrer" style="font-weight:700; color:var(--white); text-decoration:none; white-space: nowrap; font-size: 1.4rem; transition: opacity 0.3s ease;" onmouseover="this.style.opacity=0.7" onmouseout="this.style.opacity=1">THEOMEDIA.CO.UK &nearr;</a>
               </div>
             </li>
             
             <li>
               <span style="display:block; color:var(--white); opacity:0.7; font-size: 1.2rem; margin-bottom: 5px;">NEED A WEBSITE?</span>
               <a href="https://www.theomedia.co.uk/contact" target="_blank" rel="noopener noreferrer" style="font-weight:700; color:var(--white); text-decoration:none; white-space: nowrap; font-size: 1.4rem; transition: opacity 0.3s ease;" onmouseover="this.style.opacity=0.7" onmouseout="this.style.opacity=1">CONTACT THEOMEDIA &nearr;</a>
             </li>
          </ul>
          
        </div>
      </div>
    </div>
  </footer>"""

html = old_footer_regex.sub(new_footer, html)

with open('index.html', 'w') as f:
    f.write(html)
