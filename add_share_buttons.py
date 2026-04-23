# -*- coding: utf-8 -*-
"""
add_share_buttons.py - Adds Copy and WhatsApp Share buttons
to the result boxes of generated calculator pages.
"""
import os, re

BASE = r"d:\Datomate AI Lab\CalcWebsite"

# Button HTML to inject after the result row in the result-box
SHARE_BUTTONS = '''
<div class="action-btns mt-3">
  <button class="btn-action" onclick="copyResult(document.getElementById('resultBox').innerText)"><i class="bi bi-clipboard"></i> Copy Result</button>
  <button class="btn-action whatsapp" onclick="shareWhatsApp(document.getElementById('resultBox').innerText)"><i class="bi bi-whatsapp"></i> Share</button>
</div>'''

skip_files = {'about.html', 'privacy.html', 'terms.html', 'index.html', 'emi-calculator.html',
              'bmi-calculator.html', 'gst-calculator.html', 'income-tax-calculator.html',
              'sip-calculator.html', 'compound-interest-calculator.html', 'age-calculator.html',
              'percentage-calculator.html'}

processed = 0
skipped = 0

for filename in sorted(os.listdir(BASE)):
    if not filename.endswith('.html') or filename in skip_files:
        continue
    filepath = os.path.join(BASE, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Skip if already has action-btns (already has copy/share)
    if 'action-btns' in html or 'btn-action' in html:
        skipped += 1
        continue

    # Find result-box closing </div> and inject before it
    # Pattern: </div>\n</div>\n<div class="info-box"  OR  </div>\n</div>\n<script
    # The result-box div ends before the info-box starts

    # Look for the result-box id
    if 'id="resultBox"' not in html:
        skipped += 1
        continue

    # Find the closing of resultBox's row div and inject share buttons
    # Pattern: the row g-3 text-center contains result values, followed by closing divs
    # Inject after the last result-value div, before result-box closes
    
    # Strategy: find </div>\n</div> that closes the result-box
    # The result-box structure is: <div class="result-box" id="resultBox"><div class="row g-3 text-center">{results}</div></div>
    
    # Find the row closing </div> inside resultBox
    rb_idx = html.find('id="resultBox"')
    if rb_idx == -1:
        skipped += 1
        continue
    
    # Find the closing of the row div inside result-box (after all col-6 divs)
    # Look for the pattern: </div></div> after resultBox (closes row then result-box)
    search_start = rb_idx
    pattern = '</div></div>'
    close_idx = html.find(pattern, search_start)
    
    if close_idx == -1:
        skipped += 1
        continue

    # Inject share buttons before the second </div> (which closes result-box)
    # Insert after </div> (closes row) but before </div> (closes result-box)
    insert_pos = close_idx + 6  # After first </div>, before second </div>
    html = html[:insert_pos] + SHARE_BUTTONS + html[insert_pos:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    processed += 1

print(f"Added share buttons to: {processed} pages")
print(f"Skipped: {skipped} pages (already have buttons or no result box)")
