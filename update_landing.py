# -*- coding: utf-8 -*-
"""
update_landing.py - Gives top preference to 43 new Social/AI calculators
on the landing page. Updates hero, adds trending section, updates nav.
"""
import os, re

BASE = r"d:\Datomate AI Lab\CalcWebsite"
INDEX = os.path.join(BASE, "index.html")

with open(INDEX, 'r', encoding='utf-8') as f:
    html = f.read()

# ── 1. Update hero badge count ─────────────────────────────────────────────
html = html.replace('250+ Tools', '292+ Tools')
html = html.replace('250+ professional calculators', '292+ professional calculators')
print("✓ Updated hero badge to 292+ Tools")

# ── 2. Update hero paragraph to mention social/AI ──────────────────────────
OLD_PARA = '<p>EMI - GST - BMI - SIP - Income Tax - Age - Percentage - 292+ professional calculators. No signup. No cost. Ever.</p>'
NEW_PARA = '<p>EMI - GST - BMI - SIP - YouTube Money - Instagram ER - TikTok Earnings - AI Token Cost - 292+ calculators. No signup. No cost. Ever.</p>'
html = html.replace(OLD_PARA, NEW_PARA)
print("✓ Updated hero paragraph")

# ── 3. Add Social/AI hero tags (quick links) ───────────────────────────────
OLD_TAGS_END = "</div>\n      </div>\n    </div>\n  </div>\n</section>"
# Find the hero-tags div and add new tags at the beginning
OLD_TAGS_START = '''<span class="hero-tag" onclick="location.href='emi-calculator.html'">'''
NEW_TAGS_INSERT = '''<span class="hero-tag" onclick="location.href='youtube-money-calculator.html'" style="background:rgba(255,0,0,0.15);border-color:rgba(255,0,0,0.4)">&#127909; YouTube Money</span>
        <span class="hero-tag" onclick="location.href='instagram-engagement-rate-calculator.html'" style="background:rgba(131,58,180,0.15);border-color:rgba(131,58,180,0.4)">&#128247; Instagram ER</span>
        <span class="hero-tag" onclick="location.href='tiktok-earnings-calculator.html'" style="background:rgba(255,0,80,0.15);border-color:rgba(255,0,80,0.4)">&#127925; TikTok Earnings</span>
        <span class="hero-tag" onclick="location.href='ai-token-cost-calculator.html'" style="background:rgba(16,185,129,0.15);border-color:rgba(16,185,129,0.4)">&#129302; AI Token Cost</span>
        <span class="hero-tag" onclick="location.href='adsense-rpm-calculator.html'" style="background:rgba(66,133,244,0.15);border-color:rgba(66,133,244,0.4)">&#128176; AdSense RPM</span>
        '''
html = html.replace(OLD_TAGS_START, NEW_TAGS_INSERT + OLD_TAGS_START)
print("✓ Added social/AI hero tags")

# ── 4. Add "🔥 TRENDING NOW" section BEFORE all other sections ──────────────
TRENDING_SECTION = '''
    <!-- TRENDING NOW - Social & AI Calculators -->
    <div class="calc-section mb-5" data-cat="Trending" id="trending">
      <h2 class="section-title reveal" style="background:linear-gradient(90deg,#FF0000,#FF6B35,#8B00FF);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text">&#128293; Trending Now — Social Media &amp; AI Calculators</h2>
      <p class="reveal" style="color:var(--text-secondary);margin-bottom:1rem;font-size:0.9rem">292 calculators · New social media, creator economy &amp; AI tools added</p>
      <div class="row g-2">
        <div class="col-md-6 col-lg-4 reveal">
          <a href="youtube-money-calculator.html" class="calc-card hot" style="border-color:rgba(255,0,0,0.3)">
            <div class="calc-icon">&#128176;</div>
            <div class="calc-info"><div class="calc-name">YouTube Money Calculator</div><div class="calc-desc">How much does your channel earn?</div></div>
            <span class="badge" style="background:#FF0000;color:#fff;font-size:0.65rem;padding:3px 7px;border-radius:20px;margin-left:auto;flex-shrink:0">NEW</span>
          </a>
        </div>
        <div class="col-md-6 col-lg-4 reveal">
          <a href="instagram-engagement-rate-calculator.html" class="calc-card hot" style="border-color:rgba(131,58,180,0.3)">
            <div class="calc-icon">&#128247;</div>
            <div class="calc-info"><div class="calc-name">Instagram Engagement Rate</div><div class="calc-desc">Check if your IG engagement is good</div></div>
            <span class="badge" style="background:#833ab4;color:#fff;font-size:0.65rem;padding:3px 7px;border-radius:20px;margin-left:auto;flex-shrink:0">HOT</span>
          </a>
        </div>
        <div class="col-md-6 col-lg-4 reveal">
          <a href="tiktok-earnings-calculator.html" class="calc-card hot" style="border-color:rgba(255,0,80,0.3)">
            <div class="calc-icon">&#127925;</div>
            <div class="calc-info"><div class="calc-name">TikTok Earnings Calculator</div><div class="calc-desc">Creator fund + brand deal income</div></div>
            <span class="badge" style="background:#ff0050;color:#fff;font-size:0.65rem;padding:3px 7px;border-radius:20px;margin-left:auto;flex-shrink:0">HOT</span>
          </a>
        </div>
        <div class="col-md-6 col-lg-4 reveal">
          <a href="ai-token-cost-calculator.html" class="calc-card" style="border-color:rgba(16,185,129,0.3)">
            <div class="calc-icon">&#129302;</div>
            <div class="calc-info"><div class="calc-name">AI Token Cost Calculator</div><div class="calc-desc">ChatGPT, Claude, Gemini API costs</div></div>
            <span class="badge" style="background:#10b981;color:#fff;font-size:0.65rem;padding:3px 7px;border-radius:20px;margin-left:auto;flex-shrink:0">NEW</span>
          </a>
        </div>
        <div class="col-md-6 col-lg-4 reveal">
          <a href="adsense-rpm-calculator.html" class="calc-card" style="border-color:rgba(66,133,244,0.3)">
            <div class="calc-icon">&#128176;</div>
            <div class="calc-info"><div class="calc-name">AdSense RPM Calculator</div><div class="calc-desc">Website earnings estimator</div></div>
            <span class="badge" style="background:#4285F4;color:#fff;font-size:0.65rem;padding:3px 7px;border-radius:20px;margin-left:auto;flex-shrink:0">HOT</span>
          </a>
        </div>
        <div class="col-md-6 col-lg-4 reveal">
          <a href="youtube-cpm-calculator.html" class="calc-card" style="border-color:rgba(255,0,0,0.25)">
            <div class="calc-icon">&#128200;</div>
            <div class="calc-info"><div class="calc-name">YouTube CPM Calculator</div><div class="calc-desc">YouTube ad rate breakdown</div></div>
            <span class="badge" style="background:#FF0000;color:#fff;font-size:0.65rem;padding:3px 7px;border-radius:20px;margin-left:auto;flex-shrink:0">NEW</span>
          </a>
        </div>
        <div class="col-md-6 col-lg-4 reveal">
          <a href="instagram-influencer-earnings-calculator.html" class="calc-card">
            <div class="calc-icon">&#128176;</div>
            <div class="calc-info"><div class="calc-name">Influencer Earnings Per Post</div><div class="calc-desc">Sponsored post rate calculator</div></div>
            <span class="badge" style="background:#fd1d1d;color:#fff;font-size:0.65rem;padding:3px 7px;border-radius:20px;margin-left:auto;flex-shrink:0">NEW</span>
          </a>
        </div>
        <div class="col-md-6 col-lg-4 reveal">
          <a href="tiktok-virality-score-calculator.html" class="calc-card">
            <div class="calc-icon">&#128293;</div>
            <div class="calc-info"><div class="calc-name">TikTok Virality Score</div><div class="calc-desc">Is your TikTok going viral?</div></div>
            <span class="badge" style="background:#ff0050;color:#fff;font-size:0.65rem;padding:3px 7px;border-radius:20px;margin-left:auto;flex-shrink:0">NEW</span>
          </a>
        </div>
        <div class="col-md-6 col-lg-4 reveal">
          <a href="saas-pricing-calculator.html" class="calc-card">
            <div class="calc-icon">&#128200;</div>
            <div class="calc-info"><div class="calc-name">SaaS Pricing Calculator</div><div class="calc-desc">MRR, ARR, LTV &amp; churn metrics</div></div>
            <span class="badge" style="background:#6366f1;color:#fff;font-size:0.65rem;padding:3px 7px;border-radius:20px;margin-left:auto;flex-shrink:0">NEW</span>
          </a>
        </div>
        <div class="col-md-6 col-lg-4 reveal">
          <a href="youtube-rpm-calculator.html" class="calc-card">
            <div class="calc-icon">&#128200;</div>
            <div class="calc-info"><div class="calc-name">YouTube RPM Calculator</div><div class="calc-desc">Revenue per 1000 views explained</div></div>
          </a>
        </div>
        <div class="col-md-6 col-lg-4 reveal">
          <a href="affiliate-earnings-calculator.html" class="calc-card">
            <div class="calc-icon">&#128200;</div>
            <div class="calc-info"><div class="calc-name">Affiliate Earnings Calculator</div><div class="calc-desc">Affiliate marketing income estimate</div></div>
          </a>
        </div>
        <div class="col-md-6 col-lg-4 reveal">
          <a href="brand-deal-rate-calculator.html" class="calc-card">
            <div class="calc-icon">&#129534;</div>
            <div class="calc-info"><div class="calc-name">Brand Deal Rate Calculator</div><div class="calc-desc">Content creator sponsorship pricing</div></div>
          </a>
        </div>
      </div>
      <div class="text-center mt-3 reveal">
        <a href="#social" class="btn-calculate" style="display:inline-block;text-decoration:none;padding:10px 24px;font-size:0.9rem">See All 43 Social &amp; AI Calculators &#8594;</a>
      </div>
    </div>

'''

# Insert BEFORE the first existing section (which starts with Finance)
FIRST_SECTION_MARKER = 'class="calc-section mb-5" data-cat="Finance">'
html = html.replace(FIRST_SECTION_MARKER, TRENDING_SECTION.strip() + '\n\n    <div ' + FIRST_SECTION_MARKER)
print("✓ Added Trending Now section before Finance")

# ── 5. Update navbar in index.html to add Trending ────────────────────────
OLD_NAV_ITEMS = '<li class="nav-item"><a class="nav-link" href="#social">&#128247; Social</a></li>'
NEW_NAV_ITEMS = '<li class="nav-item"><a class="nav-link" href="#trending" style="color:#FF6B35;font-weight:600">&#128293; Trending</a></li>\n        <li class="nav-item"><a class="nav-link" href="#social">&#128247; Social</a></li>'
html = html.replace(OLD_NAV_ITEMS, NEW_NAV_ITEMS)
print("✓ Added Trending nav link")

# ── 6. Update the Social section to show more social calculators ───────────
# The social section already exists, but let's add more items if missing
OLD_SOCIAL_END = '''        <li class="mt-1"><a href="adsense-rpm-calculator.html" style="color:var(--primary);text-decoration:none">&#128200; AdSense RPM Calculator</a></li>'''
# Just verify it exists
if 'adsense-rpm-calculator.html' in html:
    print("✓ Social section already has AdSense RPM")

# ── 7. Update meta tags for landing page ──────────────────────────────────
OLD_META_DESC = html[html.find('<meta name="description"'):html.find('<meta name="description"')+300]
old_desc_content_start = OLD_META_DESC.find('content="') + 9
old_desc_content_end = OLD_META_DESC.find('"', old_desc_content_start)

new_desc = 'SuperCalc - Free online calculators for finance, health, math, social media & AI. YouTube money calculator, Instagram engagement rate, TikTok earnings, EMI, BMI, GST, SIP & 292+ more. No signup required.'
html = re.sub(
    r'(<meta name="description" content=")[^"]*(")',
    r'\g<1>' + new_desc + r'\g<2>',
    html, count=1
)
print("✓ Updated landing page meta description")

# Match full tag including closing > so we do not duplicate > when replacing
OLD_META_KW = re.search(r'<meta name="keywords" content="[^"]*">', html)
if OLD_META_KW:
    new_kw_tag = '<meta name="keywords" content="free calculator, youtube money calculator, instagram engagement rate calculator, tiktok earnings calculator, ai token cost calculator, adsense rpm calculator, emi calculator, gst calculator, bmi calculator, sip calculator, income tax calculator, age calculator, percentage calculator, online calculator, financial calculator, health calculator">'
    html = html[:OLD_META_KW.start()] + new_kw_tag + html[OLD_META_KW.end():]
    print("✓ Updated landing page meta keywords")

# ── 8. Update page title ───────────────────────────────────────────────────
html = re.sub(
    r'<title>[^<]+</title>',
    '<title>SuperCalc - Free Online Calculator | YouTube Money, Instagram ER, EMI, BMI, GST & 292+ Calculators</title>',
    html, count=1
)
print("✓ Updated page title")

# ── Save ──────────────────────────────────────────────────────────────────
with open(INDEX, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"\n✓ index.html saved! New size: {len(html)} chars")
