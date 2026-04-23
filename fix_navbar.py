# -*- coding: utf-8 -*-
"""
fix_navbar.py - Replaces minimal calculator page navbars with a full,
clean navbar showing all major category links. Removes search and theme toggle.
"""
import os, re

BASE = r"d:\Datomate AI Lab\CalcWebsite"

# The new clean, full-category navbar for ALL calculator pages
NEW_NAV = '''<nav class="navbar navbar-expand-lg">
  <div class="container">
    <a class="navbar-brand" href="index.html">&#9889; Super<span>Calc</span></a>
    <button class="navbar-toggler border-0" type="button" data-bs-toggle="collapse" data-bs-target="#nav">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="nav">
      <ul class="navbar-nav me-auto ms-3 gap-1">
        <li class="nav-item"><a class="nav-link" href="index.html#finance">&#128176; Finance</a></li>
        <li class="nav-item"><a class="nav-link" href="index.html#health">&#10084; Health</a></li>
        <li class="nav-item"><a class="nav-link" href="index.html#math">&#128290; Math</a></li>
        <li class="nav-item"><a class="nav-link" href="index.html#social">&#128247; Social</a></li>
        <li class="nav-item"><a class="nav-link" href="index.html#ai-tools">&#129302; AI Tools</a></li>
        <li class="nav-item"><a class="nav-link" href="index.html">More &#9662;</a></li>
      </ul>
      <div class="d-flex gap-2">
        <button class="theme-toggle" id="themeToggle" title="Toggle Dark Mode"><i class="bi bi-moon-fill" id="themeIcon"></i></button>
      </div>
    </div>
  </div>
</nav>'''

# Skip index and info pages - they have their own navbars
SKIP = {'index.html', 'about.html', 'privacy.html', 'terms.html',
        'emi-calculator.html', 'bmi-calculator.html', 'gst-calculator.html',
        'income-tax-calculator.html', 'sip-calculator.html',
        'compound-interest-calculator.html', 'age-calculator.html',
        'percentage-calculator.html'}

processed = 0
skipped = 0

for filename in sorted(os.listdir(BASE)):
    if not filename.endswith('.html') or filename in SKIP:
        continue
    filepath = os.path.join(BASE, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the existing navbar
    nav_start = html.find('<nav class="navbar')
    if nav_start == -1:
        skipped += 1
        continue

    nav_end = html.find('</nav>', nav_start)
    if nav_end == -1:
        skipped += 1
        continue

    old_nav = html[nav_start:nav_end + 6]  # +6 for </nav>

    # Replace old navbar with new clean navbar
    html = html[:nav_start] + NEW_NAV + html[nav_end + 6:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    processed += 1

print(f"Updated navbar: {processed} pages")
print(f"Skipped: {skipped} pages")
