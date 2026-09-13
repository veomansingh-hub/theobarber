with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Add white-space: nowrap to fixed button
css = css.replace('.theomedia-fixed-btn {', '.theomedia-fixed-btn {\n  white-space: nowrap;')

# Also let's fix the footer-link hover color
css += """
.footer-link {
  color: var(--white);
  opacity: 0.7;
}
.footer-link:hover {
  opacity: 1;
  color: var(--indian-yellow);
}
"""

with open('assets/css/style.css', 'w') as f:
    f.write(css)
