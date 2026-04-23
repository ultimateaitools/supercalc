# -*- coding: utf-8 -*-
import os

BASE = r"d:\Datomate AI Lab\CalcWebsite"

def page(filename, title, desc, keywords, icon, grad_start, grad_end, cat_url, cat_icon, cat_label, body, script=""):
    html = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | SuperCalc - Free Online Calculator</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<link rel="canonical" href="https://supercalc.online/{filename}">
<meta property="og:title" content="{title} | SuperCalc">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://supercalc.online/{filename}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title} | SuperCalc">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
<link rel="stylesheet" href="css/style.css">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"WebPage","name":"{title}","description":"{desc}","url":"https://supercalc.online/{filename}","publisher":{{"@type":"Organization","name":"SuperCalc","url":"https://supercalc.online"}}}}
</script>
</head>
<body>
<nav class="navbar navbar-expand-lg"><div class="container"><a class="navbar-brand" href="index.html">&#9889; Super<span>Calc</span></a><button class="navbar-toggler border-0" type="button" data-bs-toggle="collapse" data-bs-target="#nav"><span></span></button><div class="collapse navbar-collapse" id="nav"><ul class="navbar-nav me-auto ms-3"><li><a class="nav-link" href="index.html#{cat_url}">{cat_icon} {cat_label}</a></li></ul><div class="d-flex gap-2"><button class="theme-toggle" id="themeToggle"><i class="bi bi-moon-fill" id="themeIcon"></i></button></div></div></div></nav>
<div class="calc-page-header" style="background:linear-gradient(135deg,{grad_start},{grad_end})">
  <div class="container"><nav class="breadcrumb-nav"><a href="index.html">Home</a> <i class="bi bi-chevron-right"></i> <a href="index.html#{cat_url}">{cat_label}</a> <i class="bi bi-chevron-right"></i><span>{title}</span></nav>
  <h1 class="calc-page-title">{icon} {title}</h1>
  <p class="calc-page-subtitle">{desc}</p></div>
</div>
<div class="container my-4">
  <div class="row g-4">
    <div class="col-lg-8">{body}</div>
    <div class="col-lg-4">
      <div class="sidebar-ad"><span style="font-size:0.7rem;color:var(--text-muted)">Advertisement [300x250]</span></div>
      <div class="calc-box mt-3" style="padding:16px">
        <h6 style="font-weight:700;margin-bottom:12px">&#128279; Related Calculators</h6>
        <ul style="list-style:none;padding:0;margin:0;font-size:0.85rem">
          <li><a href="instagram-engagement-rate-calculator.html" style="color:var(--primary);text-decoration:none">&#128247; Instagram Engagement Rate</a></li>
          <li class="mt-1"><a href="youtube-money-calculator.html" style="color:var(--primary);text-decoration:none">&#127909; YouTube Money Calculator</a></li>
          <li class="mt-1"><a href="tiktok-earnings-calculator.html" style="color:var(--primary);text-decoration:none">&#127925; TikTok Earnings</a></li>
          <li class="mt-1"><a href="influencer-earnings-per-post-calculator.html" style="color:var(--primary);text-decoration:none">&#128176; Influencer Earnings</a></li>
          <li class="mt-1"><a href="adsense-rpm-calculator.html" style="color:var(--primary);text-decoration:none">&#128200; AdSense RPM Calculator</a></li>
        </ul>
      </div>
    </div>
  </div>
</div>
<footer><div class="container"><div class="footer-bottom"><p>&copy; 2025 SuperCalc.online</p><div><a href="privacy.html">Privacy</a> &bull; <a href="terms.html">Terms</a></div></div></div></footer>
<button class="back-to-top" id="backToTop"><i class="bi bi-arrow-up"></i></button>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
<script src="js/main.js"></script>
{script}
</body>
</html>""".format(
        title=title, desc=desc, keywords=keywords, filename=filename,
        icon=icon, grad_start=grad_start, grad_end=grad_end,
        cat_url=cat_url, cat_icon=cat_icon, cat_label=cat_label,
        body=body, script=script)
    path = os.path.join(BASE, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Created: " + filename)


# ─────────────────────────────────────────────────────────
# INSTAGRAM CALCULATORS
# ─────────────────────────────────────────────────────────

page("instagram-engagement-rate-calculator.html",
"Instagram Engagement Rate Calculator",
"Calculate your Instagram engagement rate instantly. Find out if your engagement is good, average, or poor. Used by brands and influencers worldwide.",
"instagram engagement rate calculator, instagram engagement rate, how to calculate instagram engagement, instagram analytics, influencer engagement rate",
"&#128247;","#833ab4","#fd1d1d","social","&#128247;","Social Media",
"""<div class="calc-box">
<h2 class="calc-title">&#128247; Instagram Engagement Rate Calculator</h2>
<div class="row g-3">
  <div class="col-md-6">
    <label class="form-label">Total Followers</label>
    <input type="number" class="form-control" id="followers" placeholder="e.g. 10000" min="1">
  </div>
  <div class="col-md-6">
    <label class="form-label">Total Likes (per post)</label>
    <input type="number" class="form-control" id="likes" placeholder="e.g. 350" min="0">
  </div>
  <div class="col-md-6">
    <label class="form-label">Total Comments (per post)</label>
    <input type="number" class="form-control" id="comments" placeholder="e.g. 25" min="0">
  </div>
  <div class="col-md-6">
    <label class="form-label">Number of Posts Averaged</label>
    <input type="number" class="form-control" id="posts" placeholder="e.g. 10" min="1" value="1">
  </div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate Engagement Rate</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Engagement Rate</div><div class="result-value" id="engRate">-</div></div>
    <div class="col-6"><div class="result-label">Quality Rating</div><div class="result-value" id="quality">-</div></div>
    <div class="col-6"><div class="result-label">Avg Interactions/Post</div><div class="result-value" id="avgInter">-</div></div>
    <div class="col-6"><div class="result-label">Tier</div><div class="result-value" id="tier">-</div></div>
  </div>
</div>
</div>
<div class="calc-box mt-3">
<h3 style="font-size:1.1rem;font-weight:700;margin-bottom:12px">&#128200; Instagram Engagement Rate Benchmarks 2025</h3>
<div class="table-responsive">
<table class="table table-sm" style="font-size:0.85rem">
<thead><tr><th>Engagement Rate</th><th>Rating</th><th>Industry Standard</th></tr></thead>
<tbody>
<tr><td>&lt; 1%</td><td style="color:#ef4444">Poor</td><td>Below average, review content strategy</td></tr>
<tr><td>1% - 3%</td><td style="color:#f59e0b">Average</td><td>Typical for large accounts (100K+)</td></tr>
<tr><td>3% - 6%</td><td style="color:#10b981">Good</td><td>Strong for mid-tier influencers</td></tr>
<tr><td>6% - 10%</td><td style="color:#6366f1">Excellent</td><td>Micro-influencer sweet spot</td></tr>
<tr><td>&gt; 10%</td><td style="color:#8b5cf6">Outstanding</td><td>Nano-influencer or viral content</td></tr>
</tbody>
</table>
</div>
</div>""",
"""<script>
function calc() {
  var followers = parseFloat(document.getElementById('followers').value)||0;
  var likes = parseFloat(document.getElementById('likes').value)||0;
  var comments = parseFloat(document.getElementById('comments').value)||0;
  var posts = parseFloat(document.getElementById('posts').value)||1;
  if(!followers){alert('Enter follower count');return;}
  var totalInter = (likes + comments) / posts;
  var rate = (totalInter / followers) * 100;
  var quality = rate < 1 ? 'Poor' : rate < 3 ? 'Average' : rate < 6 ? 'Good' : rate < 10 ? 'Excellent' : 'Outstanding';
  var tier = followers < 1000 ? 'Nano' : followers < 10000 ? 'Micro' : followers < 100000 ? 'Mid-Tier' : followers < 1000000 ? 'Macro' : 'Mega';
  document.getElementById('engRate').textContent = rate.toFixed(2) + '%';
  document.getElementById('quality').textContent = quality;
  document.getElementById('avgInter').textContent = Math.round(totalInter).toLocaleString();
  document.getElementById('tier').textContent = tier;
  document.getElementById('resultBox').style.display = 'block';
}
</script>""")


page("instagram-engagement-per-post-calculator.html",
"Instagram Engagement Per Post Calculator",
"Calculate average engagement per post on Instagram. Analyze likes, comments, shares and saves per post to measure content performance.",
"instagram engagement per post, instagram post analytics, average engagement instagram, instagram post performance, content performance calculator",
"&#128247;","#c13584","#833ab4","social","&#128247;","Social Media",
"""<div class="calc-box">
<h2 class="calc-title">&#128247; Instagram Engagement Per Post Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Total Likes (sum of all posts)</label><input type="number" class="form-control" id="totalLikes" placeholder="e.g. 5000" min="0"></div>
  <div class="col-md-6"><label class="form-label">Total Comments</label><input type="number" class="form-control" id="totalComments" placeholder="e.g. 300" min="0"></div>
  <div class="col-md-6"><label class="form-label">Total Saves</label><input type="number" class="form-control" id="totalSaves" placeholder="e.g. 150" min="0" value="0"></div>
  <div class="col-md-6"><label class="form-label">Total Shares</label><input type="number" class="form-control" id="totalShares" placeholder="e.g. 80" min="0" value="0"></div>
  <div class="col-md-6"><label class="form-label">Number of Posts</label><input type="number" class="form-control" id="numPosts" placeholder="e.g. 20" min="1"></div>
  <div class="col-md-6"><label class="form-label">Total Followers</label><input type="number" class="form-control" id="followers" placeholder="e.g. 10000" min="1"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Avg Engagement/Post</div><div class="result-value" id="avgEng">-</div></div>
    <div class="col-6"><div class="result-label">Avg Engagement Rate</div><div class="result-value" id="avgRate">-</div></div>
    <div class="col-6"><div class="result-label">Avg Likes/Post</div><div class="result-value" id="avgLikes">-</div></div>
    <div class="col-6"><div class="result-label">Avg Comments/Post</div><div class="result-value" id="avgComments">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var tl=parseFloat(document.getElementById('totalLikes').value)||0;
  var tc=parseFloat(document.getElementById('totalComments').value)||0;
  var ts=parseFloat(document.getElementById('totalSaves').value)||0;
  var th=parseFloat(document.getElementById('totalShares').value)||0;
  var np=parseFloat(document.getElementById('numPosts').value)||1;
  var fl=parseFloat(document.getElementById('followers').value)||1;
  var total=tl+tc+ts+th;
  var avgEng=total/np;
  var avgRate=(avgEng/fl)*100;
  document.getElementById('avgEng').textContent=Math.round(avgEng).toLocaleString();
  document.getElementById('avgRate').textContent=avgRate.toFixed(2)+'%';
  document.getElementById('avgLikes').textContent=Math.round(tl/np).toLocaleString();
  document.getElementById('avgComments').textContent=Math.round(tc/np).toLocaleString();
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("instagram-reach-rate-calculator.html",
"Instagram Reach Rate Calculator",
"Calculate your Instagram reach rate percentage. Find what percentage of your followers are actually seeing your posts.",
"instagram reach rate calculator, instagram reach percentage, post reach instagram, organic reach instagram, impressions vs reach",
"&#128247;","#fd1d1d","#fcb045","social","&#128247;","Social Media",
"""<div class="calc-box">
<h2 class="calc-title">&#128247; Instagram Reach Rate Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Post Reach (Unique Accounts)</label><input type="number" class="form-control" id="reach" placeholder="e.g. 3500"></div>
  <div class="col-md-6"><label class="form-label">Total Followers</label><input type="number" class="form-control" id="followers" placeholder="e.g. 10000"></div>
  <div class="col-md-12"><label class="form-label">Post Impressions (optional)</label><input type="number" class="form-control" id="impressions" placeholder="e.g. 5000" value="0"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate Reach Rate</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Reach Rate</div><div class="result-value" id="reachRate">-</div></div>
    <div class="col-6"><div class="result-label">Rating</div><div class="result-value" id="rating">-</div></div>
    <div class="col-6"><div class="result-label">Impressions/Reach</div><div class="result-value" id="impRatio">-</div></div>
    <div class="col-6"><div class="result-label">Non-Reached Followers</div><div class="result-value" id="missed">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var reach=parseFloat(document.getElementById('reach').value)||0;
  var followers=parseFloat(document.getElementById('followers').value)||1;
  var impressions=parseFloat(document.getElementById('impressions').value)||0;
  var reachRate=(reach/followers)*100;
  var rating=reachRate<10?'Low':reachRate<25?'Average':reachRate<50?'Good':'Excellent';
  var impRatio=impressions&&reach?(impressions/reach).toFixed(2):'N/A';
  var missed=Math.max(0,followers-reach);
  document.getElementById('reachRate').textContent=reachRate.toFixed(2)+'%';
  document.getElementById('rating').textContent=rating;
  document.getElementById('impRatio').textContent=impRatio;
  document.getElementById('missed').textContent=Math.round(missed).toLocaleString();
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("instagram-growth-rate-calculator.html",
"Instagram Growth Rate Calculator",
"Track your Instagram follower growth rate month over month. See if your account is growing fast enough to reach your goals.",
"instagram growth rate calculator, instagram follower growth, monthly growth rate instagram, instagram account growth, follower increase percentage",
"&#128200;","#405de6","#5851db","social","&#128247;","Social Media",
"""<div class="calc-box">
<h2 class="calc-title">&#128200; Instagram Growth Rate Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Followers at Start of Period</label><input type="number" class="form-control" id="startFollowers" placeholder="e.g. 8500"></div>
  <div class="col-md-6"><label class="form-label">Followers at End of Period</label><input type="number" class="form-control" id="endFollowers" placeholder="e.g. 10000"></div>
  <div class="col-md-6"><label class="form-label">Period (Days)</label><input type="number" class="form-control" id="days" placeholder="e.g. 30" value="30"></div>
  <div class="col-md-6"><label class="form-label">New Followers Gained</label><input type="number" class="form-control" id="newFollowers" placeholder="Auto-calculated" id="newF" value="0"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate Growth</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Growth Rate</div><div class="result-value" id="growthRate">-</div></div>
    <div class="col-6"><div class="result-label">Daily Growth</div><div class="result-value" id="dailyGrowth">-</div></div>
    <div class="col-6"><div class="result-label">Monthly Projection</div><div class="result-value" id="monthly">-</div></div>
    <div class="col-6"><div class="result-label">Days to 100K</div><div class="result-value" id="to100k">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var s=parseFloat(document.getElementById('startFollowers').value)||0;
  var e=parseFloat(document.getElementById('endFollowers').value)||0;
  var d=parseFloat(document.getElementById('days').value)||30;
  if(!s||!e){alert('Enter start and end followers');return;}
  var gained=e-s;
  var rate=(gained/s)*100;
  var daily=gained/d;
  var monthly=daily*30;
  var remaining=Math.max(0,100000-e);
  var days100k=daily>0?Math.ceil(remaining/daily):999999;
  document.getElementById('growthRate').textContent=rate.toFixed(2)+'%';
  document.getElementById('dailyGrowth').textContent='+'+daily.toFixed(1)+'/day';
  document.getElementById('monthly').textContent='+'+Math.round(monthly).toLocaleString();
  document.getElementById('to100k').textContent=days100k>9999?'10+ yrs':days100k+' days';
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("instagram-influencer-earnings-calculator.html",
"Instagram Influencer Earnings Calculator",
"Estimate how much money you can earn per sponsored post on Instagram based on your follower count, engagement rate, and niche.",
"instagram influencer earnings calculator, instagram sponsored post price, how much do influencers make, instagram monetization, influencer rate card",
"&#128176;","#833ab4","#fd1d1d","social","&#128247;","Social Media",
"""<div class="calc-box">
<h2 class="calc-title">&#128176; Instagram Influencer Earnings Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Total Followers</label><input type="number" class="form-control" id="followers" placeholder="e.g. 50000"></div>
  <div class="col-md-6"><label class="form-label">Engagement Rate (%)</label><input type="number" class="form-control" id="engRate" placeholder="e.g. 3.5" step="0.1"></div>
  <div class="col-md-6"><label class="form-label">Niche / Industry</label>
    <select class="form-control" id="niche">
      <option value="1.0">General / Lifestyle</option>
      <option value="1.5">Fashion / Beauty</option>
      <option value="1.8">Fitness / Health</option>
      <option value="2.0">Finance / Business</option>
      <option value="1.3">Food / Travel</option>
      <option value="2.2">Technology / SaaS</option>
      <option value="1.6">Parenting / Family</option>
      <option value="1.4">Entertainment</option>
    </select>
  </div>
  <div class="col-md-6"><label class="form-label">Content Type</label>
    <select class="form-control" id="contentType">
      <option value="1.0">Feed Post</option>
      <option value="0.7">Story (24hr)</option>
      <option value="1.3">Reel / Video</option>
      <option value="0.5">Story Swipe-up</option>
    </select>
  </div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate Earnings</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Estimated Per Post</div><div class="result-value" id="perPost">-</div></div>
    <div class="col-6"><div class="result-label">Monthly (10 posts)</div><div class="result-value" id="monthly">-</div></div>
    <div class="col-6"><div class="result-label">Influencer Tier</div><div class="result-value" id="tier">-</div></div>
    <div class="col-6"><div class="result-label">Rate Range</div><div class="result-value" id="range">-</div></div>
  </div>
</div>
</div>
<div class="calc-box mt-3">
<h3 style="font-size:1rem;font-weight:700;margin-bottom:10px">&#127981; Industry Rate Benchmarks (USD)</h3>
<div class="table-responsive"><table class="table table-sm" style="font-size:0.82rem">
<thead><tr><th>Tier</th><th>Followers</th><th>Per Post Rate</th><th>Engagement Avg</th></tr></thead>
<tbody>
<tr><td>Nano</td><td>1K - 10K</td><td>$10 - $100</td><td>5-8%</td></tr>
<tr><td>Micro</td><td>10K - 100K</td><td>$100 - $1,000</td><td>3-6%</td></tr>
<tr><td>Mid-Tier</td><td>100K - 500K</td><td>$1,000 - $5,000</td><td>2-4%</td></tr>
<tr><td>Macro</td><td>500K - 1M</td><td>$5,000 - $20,000</td><td>1.5-3%</td></tr>
<tr><td>Mega</td><td>1M+</td><td>$20,000+</td><td>1-2%</td></tr>
</tbody>
</table></div>
</div>""",
"""<script>
function calc(){
  var f=parseFloat(document.getElementById('followers').value)||0;
  var e=parseFloat(document.getElementById('engRate').value)||1;
  var n=parseFloat(document.getElementById('niche').value)||1;
  var c=parseFloat(document.getElementById('contentType').value)||1;
  if(!f){alert('Enter follower count');return;}
  var base=f/1000*10;
  var engMult=1+(e-1)*0.1;
  var estimated=base*n*c*engMult;
  var low=Math.round(estimated*0.7);
  var high=Math.round(estimated*1.4);
  var tier=f<1000?'Nano':f<10000?'Micro':f<100000?'Mid-Tier':f<500000?'Macro':'Mega';
  document.getElementById('perPost').textContent='$'+Math.round(estimated).toLocaleString();
  document.getElementById('monthly').textContent='$'+(Math.round(estimated)*10).toLocaleString();
  document.getElementById('tier').textContent=tier;
  document.getElementById('range').textContent='$'+low.toLocaleString()+' - $'+high.toLocaleString();
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("instagram-reels-earnings-calculator.html",
"Instagram Reels Earnings Calculator",
"Calculate how much you can earn from Instagram Reels. Estimate Reels Play Bonus and brand deal rates based on views and engagement.",
"instagram reels earnings calculator, instagram reels monetization, reels play bonus, how much instagram reels pay, reels views to money",
"&#127909;","#c13584","#833ab4","social","&#128247;","Social Media",
"""<div class="calc-box">
<h2 class="calc-title">&#127909; Instagram Reels Earnings Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Average Reel Views</label><input type="number" class="form-control" id="views" placeholder="e.g. 50000"></div>
  <div class="col-md-6"><label class="form-label">Total Followers</label><input type="number" class="form-control" id="followers" placeholder="e.g. 25000"></div>
  <div class="col-md-6"><label class="form-label">Engagement Rate (%)</label><input type="number" class="form-control" id="engRate" placeholder="e.g. 4.5" step="0.1" value="4"></div>
  <div class="col-md-6"><label class="form-label">Reels Per Month</label><input type="number" class="form-control" id="reelsPerMonth" placeholder="e.g. 12" value="10"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate Earnings</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Est. Brand Deal/Reel</div><div class="result-value" id="brandDeal">-</div></div>
    <div class="col-6"><div class="result-label">Monthly Brand Income</div><div class="result-value" id="monthly">-</div></div>
    <div class="col-6"><div class="result-label">Reels Play Bonus Est.</div><div class="result-value" id="bonus">-</div></div>
    <div class="col-6"><div class="result-label">Views/Follower Ratio</div><div class="result-value" id="vfRatio">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var views=parseFloat(document.getElementById('views').value)||0;
  var followers=parseFloat(document.getElementById('followers').value)||1;
  var eng=parseFloat(document.getElementById('engRate').value)||1;
  var rpm=parseFloat(document.getElementById('reelsPerMonth').value)||10;
  var base=followers/1000*12*(1+(eng-1)*0.08);
  var bonus=(views/1000)*0.015;
  var monthly=base*rpm;
  var vfr=(views/followers*100).toFixed(1);
  document.getElementById('brandDeal').textContent='$'+Math.round(base).toLocaleString();
  document.getElementById('monthly').textContent='$'+Math.round(monthly).toLocaleString();
  document.getElementById('bonus').textContent='$'+bonus.toFixed(2)+'/1K views';
  document.getElementById('vfRatio').textContent=vfr+'%';
  document.getElementById('resultBox').style.display='block';
}
</script>""")


# ─────────────────────────────────────────────────────────
# YOUTUBE CALCULATORS
# ─────────────────────────────────────────────────────────

page("youtube-engagement-rate-calculator.html",
"YouTube Engagement Rate Calculator",
"Calculate your YouTube engagement rate from likes, comments, and views. See how your channel compares to industry benchmarks.",
"youtube engagement rate calculator, youtube engagement rate, youtube likes comments ratio, youtube channel analytics, youtube metrics",
"&#127909;","#FF0000","#cc0000","social","&#127909;","YouTube",
"""<div class="calc-box">
<h2 class="calc-title">&#127909; YouTube Engagement Rate Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Total Views</label><input type="number" class="form-control" id="views" placeholder="e.g. 100000"></div>
  <div class="col-md-6"><label class="form-label">Total Likes</label><input type="number" class="form-control" id="likes" placeholder="e.g. 5000"></div>
  <div class="col-md-6"><label class="form-label">Total Comments</label><input type="number" class="form-control" id="comments" placeholder="e.g. 300"></div>
  <div class="col-md-6"><label class="form-label">Subscribers</label><input type="number" class="form-control" id="subs" placeholder="e.g. 50000"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Engagement Rate</div><div class="result-value" id="eng">-</div></div>
    <div class="col-6"><div class="result-label">Like Rate</div><div class="result-value" id="likeRate">-</div></div>
    <div class="col-6"><div class="result-label">Comment Rate</div><div class="result-value" id="commRate">-</div></div>
    <div class="col-6"><div class="result-label">Rating</div><div class="result-value" id="rating">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var v=parseFloat(document.getElementById('views').value)||1;
  var l=parseFloat(document.getElementById('likes').value)||0;
  var c=parseFloat(document.getElementById('comments').value)||0;
  var s=parseFloat(document.getElementById('subs').value)||1;
  var eng=((l+c)/v)*100;
  var lr=(l/v)*100;
  var cr=(c/v)*100;
  var rating=eng<1?'Poor':eng<3?'Average':eng<6?'Good':'Excellent';
  document.getElementById('eng').textContent=eng.toFixed(2)+'%';
  document.getElementById('likeRate').textContent=lr.toFixed(2)+'%';
  document.getElementById('commRate').textContent=cr.toFixed(3)+'%';
  document.getElementById('rating').textContent=rating;
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("youtube-money-calculator.html",
"YouTube Money Calculator",
"Calculate how much money a YouTube channel makes based on views, CPM, and RPM. Estimate monthly and yearly YouTube earnings.",
"youtube money calculator, youtube earnings calculator, how much does youtube pay, youtube revenue estimator, youtube income calculator, youtube salary",
"&#128176;","#FF0000","#ff6b35","social","&#127909;","YouTube",
"""<div class="calc-box">
<h2 class="calc-title">&#128176; YouTube Money Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Daily Video Views</label><input type="number" class="form-control" id="dailyViews" placeholder="e.g. 10000"></div>
  <div class="col-md-6"><label class="form-label">CPM Rate ($ per 1000 views)</label><input type="number" class="form-control" id="cpm" placeholder="e.g. 4.00" value="4" step="0.1"></div>
  <div class="col-md-6"><label class="form-label">Click-Through Rate (%)</label><input type="number" class="form-control" id="ctr" placeholder="e.g. 45" value="45" step="1">
    <small class="text-muted">% of views that are monetized (typically 40-60%)</small>
  </div>
  <div class="col-md-6"><label class="form-label">Content Niche</label>
    <select class="form-control" id="niche">
      <option value="2">Finance / Business ($6-15 CPM)</option>
      <option value="1.5">Technology ($4-10 CPM)</option>
      <option value="1.2" selected>General / Entertainment ($2-5 CPM)</option>
      <option value="1">Gaming ($1-4 CPM)</option>
      <option value="1.3">Health / Fitness ($3-7 CPM)</option>
      <option value="1.8">Education ($5-12 CPM)</option>
    </select>
  </div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate YouTube Income</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Daily Earnings</div><div class="result-value" id="daily">-</div></div>
    <div class="col-6"><div class="result-label">Monthly Earnings</div><div class="result-value" id="monthly">-</div></div>
    <div class="col-6"><div class="result-label">Yearly Earnings</div><div class="result-value" id="yearly">-</div></div>
    <div class="col-6"><div class="result-label">Effective RPM</div><div class="result-value" id="rpm">-</div></div>
  </div>
</div>
</div>
<div class="calc-box mt-3">
<h3 style="font-size:1rem;font-weight:700">&#128161; YouTube Earning Tips</h3>
<ul style="font-size:0.85rem;color:var(--text-secondary)">
<li>Finance and business niches earn 3-5x more than entertainment</li>
<li>US/UK/AU traffic earns significantly more than Asian/South American traffic</li>
<li>Long-form videos (8+ min) allow mid-roll ads boosting RPM by 30-50%</li>
<li>YouTube pays ~55% of ad revenue to creators (45% kept by YouTube)</li>
</ul>
</div>""",
"""<script>
function calc(){
  var dv=parseFloat(document.getElementById('dailyViews').value)||0;
  var cpm=parseFloat(document.getElementById('cpm').value)||4;
  var ctr=parseFloat(document.getElementById('ctr').value)||45;
  var n=parseFloat(document.getElementById('niche').value)||1;
  if(!dv){alert('Enter daily views');return;}
  var monetized=dv*(ctr/100);
  var effectiveCPM=cpm*n;
  var daily=(monetized/1000)*effectiveCPM*0.55;
  var monthly=daily*30;
  var yearly=daily*365;
  var rpm=(daily/dv*1000).toFixed(2);
  document.getElementById('daily').textContent='$'+daily.toFixed(2);
  document.getElementById('monthly').textContent='$'+monthly.toFixed(0).replace(/\B(?=(\d{3})+(?!\d))/g,',');
  document.getElementById('yearly').textContent='$'+yearly.toFixed(0).replace(/\B(?=(\d{3})+(?!\d))/g,',');
  document.getElementById('rpm').textContent='$'+rpm;
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("youtube-cpm-calculator.html",
"YouTube CPM Calculator",
"Calculate YouTube CPM (Cost Per Mille) to understand your channel's ad rate. Convert between CPM, RPM, and total revenue.",
"youtube CPM calculator, what is youtube CPM, youtube ad rate, CPM to revenue, youtube advertising cost, CPM by niche",
"&#128200;","#cc0000","#FF0000","social","&#127909;","YouTube",
"""<div class="calc-box">
<h2 class="calc-title">&#128200; YouTube CPM Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Total Ad Revenue ($)</label><input type="number" class="form-control" id="revenue" placeholder="e.g. 500" step="0.01"></div>
  <div class="col-md-6"><label class="form-label">Total Ad Impressions</label><input type="number" class="form-control" id="impressions" placeholder="e.g. 100000"></div>
  <div class="col-md-6"><label class="form-label">Total Views</label><input type="number" class="form-control" id="views" placeholder="e.g. 200000"></div>
  <div class="col-md-6"><label class="form-label">Monetized Views (%)</label><input type="number" class="form-control" id="monPct" placeholder="e.g. 45" value="45"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate CPM</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Your CPM</div><div class="result-value" id="cpm">-</div></div>
    <div class="col-6"><div class="result-label">Your RPM</div><div class="result-value" id="rpm">-</div></div>
    <div class="col-6"><div class="result-label">Revenue per View</div><div class="result-value" id="rpv">-</div></div>
    <div class="col-6"><div class="result-label">Monetization Rate</div><div class="result-value" id="monRate">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var rev=parseFloat(document.getElementById('revenue').value)||0;
  var imp=parseFloat(document.getElementById('impressions').value)||1;
  var views=parseFloat(document.getElementById('views').value)||1;
  var monPct=parseFloat(document.getElementById('monPct').value)||45;
  var cpm=(rev/imp)*1000;
  var rpm=(rev/views)*1000;
  var rpv=rev/views;
  var monRate=((imp/(views*(monPct/100)))*100).toFixed(1);
  document.getElementById('cpm').textContent='$'+cpm.toFixed(2);
  document.getElementById('rpm').textContent='$'+rpm.toFixed(2);
  document.getElementById('rpv').textContent='$'+rpv.toFixed(4);
  document.getElementById('monRate').textContent=monPct+'%';
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("youtube-rpm-calculator.html",
"YouTube RPM Calculator",
"Calculate YouTube RPM (Revenue Per Mille). Understand the difference between CPM and RPM and how much you earn per 1000 views.",
"youtube RPM calculator, youtube revenue per mille, RPM vs CPM youtube, youtube income per 1000 views, youtube monetization RPM",
"&#128200;","#FF0000","#ff4500","social","&#127909;","YouTube",
"""<div class="calc-box">
<h2 class="calc-title">&#128200; YouTube RPM Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Total Revenue ($) - 30 days</label><input type="number" class="form-control" id="revenue" placeholder="e.g. 1200" step="0.01"></div>
  <div class="col-md-6"><label class="form-label">Total Views - 30 days</label><input type="number" class="form-control" id="views" placeholder="e.g. 500000"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate RPM</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Your RPM</div><div class="result-value" id="rpm">-</div></div>
    <div class="col-6"><div class="result-label">Est. CPM</div><div class="result-value" id="cpm">-</div></div>
    <div class="col-6"><div class="result-label">Revenue per View</div><div class="result-value" id="rpv">-</div></div>
    <div class="col-6"><div class="result-label">Yearly Projection</div><div class="result-value" id="yearly">-</div></div>
  </div>
</div>
</div>
<div class="calc-box mt-3">
<h3 style="font-size:1rem;font-weight:700">RPM vs CPM Explained</h3>
<p style="font-size:0.85rem;color:var(--text-secondary)"><strong>CPM</strong> = What advertisers pay per 1,000 ad impressions (higher number)<br>
<strong>RPM</strong> = What YOU earn per 1,000 total views (lower number, ~45-55% of CPM)<br>
Average YouTube RPM globally: $1-$5. Finance/Business: $10-$30. Gaming: $1-$3.</p>
</div>""",
"""<script>
function calc(){
  var rev=parseFloat(document.getElementById('revenue').value)||0;
  var views=parseFloat(document.getElementById('views').value)||1;
  var rpm=(rev/views)*1000;
  var cpm=rpm/0.55;
  var rpv=rev/views;
  var yearly=rev*12;
  document.getElementById('rpm').textContent='$'+rpm.toFixed(2);
  document.getElementById('cpm').textContent='$'+cpm.toFixed(2);
  document.getElementById('rpv').textContent='$'+rpv.toFixed(4);
  document.getElementById('yearly').textContent='$'+yearly.toFixed(0).replace(/\B(?=(\d{3})+(?!\d))/g,',');
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("youtube-growth-rate-calculator.html",
"YouTube Channel Growth Rate Calculator",
"Track your YouTube subscriber growth rate. Calculate daily subscriber gains, project future subscriber milestones, and compare to industry benchmarks.",
"youtube growth rate calculator, youtube subscriber growth, youtube channel growth, youtube subscriber increase, youtube growth tracker",
"&#128200;","#cc0000","#b71c1c","social","&#127909;","YouTube",
"""<div class="calc-box">
<h2 class="calc-title">&#128200; YouTube Growth Rate Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Subscribers (Start of Period)</label><input type="number" class="form-control" id="startSubs" placeholder="e.g. 45000"></div>
  <div class="col-md-6"><label class="form-label">Subscribers (End of Period)</label><input type="number" class="form-control" id="endSubs" placeholder="e.g. 52000"></div>
  <div class="col-md-6"><label class="form-label">Period (Days)</label><input type="number" class="form-control" id="days" value="30"></div>
  <div class="col-md-6"><label class="form-label">Videos Published in Period</label><input type="number" class="form-control" id="videos" placeholder="e.g. 8" value="4"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate Growth</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Growth Rate</div><div class="result-value" id="rate">-</div></div>
    <div class="col-6"><div class="result-label">Subs/Day</div><div class="result-value" id="perDay">-</div></div>
    <div class="col-6"><div class="result-label">Subs/Video</div><div class="result-value" id="perVideo">-</div></div>
    <div class="col-6"><div class="result-label">Days to 100K</div><div class="result-value" id="to100k">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var s=parseFloat(document.getElementById('startSubs').value)||0;
  var e=parseFloat(document.getElementById('endSubs').value)||0;
  var d=parseFloat(document.getElementById('days').value)||30;
  var v=parseFloat(document.getElementById('videos').value)||1;
  var gained=e-s;
  var rate=((gained/s)*100).toFixed(2);
  var perDay=(gained/d).toFixed(1);
  var perVideo=(gained/v).toFixed(0);
  var remaining=Math.max(0,100000-e);
  var days100k=gained/d>0?Math.ceil(remaining/(gained/d)):'N/A';
  document.getElementById('rate').textContent=rate+'%';
  document.getElementById('perDay').textContent='+'+perDay+'/day';
  document.getElementById('perVideo').textContent='+'+perVideo+'/video';
  document.getElementById('to100k').textContent=typeof days100k==='number'&&days100k>3650?'10+ yrs':days100k+' days';
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("youtube-shorts-earnings-calculator.html",
"YouTube Shorts Earnings Calculator",
"Calculate YouTube Shorts earnings and monetization. Estimate revenue from Shorts views, Shorts Fund, and brand partnerships.",
"youtube shorts earnings calculator, youtube shorts monetization, how much youtube shorts pay, youtube shorts revenue, shorts views to money",
"&#127909;","#FF0000","#ff6b35","social","&#127909;","YouTube",
"""<div class="calc-box">
<h2 class="calc-title">&#127909; YouTube Shorts Earnings Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Average Views per Short</label><input type="number" class="form-control" id="views" placeholder="e.g. 100000"></div>
  <div class="col-md-6"><label class="form-label">Shorts Published per Month</label><input type="number" class="form-control" id="shorts" placeholder="e.g. 20" value="15"></div>
  <div class="col-md-6"><label class="form-label">Subscribers</label><input type="number" class="form-control" id="subs" placeholder="e.g. 50000"></div>
  <div class="col-md-6"><label class="form-label">Niche</label>
    <select class="form-control" id="niche">
      <option value="1.0">Entertainment / Viral</option>
      <option value="1.5">Education / How-to</option>
      <option value="2.0">Finance / Business</option>
      <option value="1.2">Gaming</option>
      <option value="1.3">Fitness / Health</option>
    </select>
  </div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate Earnings</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Monthly Ad Revenue</div><div class="result-value" id="adRev">-</div></div>
    <div class="col-6"><div class="result-label">Per Short Earnings</div><div class="result-value" id="perShort">-</div></div>
    <div class="col-6"><div class="result-label">Total Monthly Views</div><div class="result-value" id="totalViews">-</div></div>
    <div class="col-6"><div class="result-label">Effective RPM</div><div class="result-value" id="rpm">-</div></div>
  </div>
</div>
</div>
<p style="font-size:0.8rem;color:var(--text-muted);margin-top:8px">Note: YouTube Shorts RPM is typically $0.03-$0.06 per 1000 views (lower than long-form). Results are estimates.</p>""",
"""<script>
function calc(){
  var views=parseFloat(document.getElementById('views').value)||0;
  var shorts=parseFloat(document.getElementById('shorts').value)||15;
  var n=parseFloat(document.getElementById('niche').value)||1;
  var totalViews=views*shorts;
  var rpm=0.04*n;
  var adRev=(totalViews/1000)*rpm;
  var perShort=adRev/shorts;
  document.getElementById('adRev').textContent='$'+adRev.toFixed(2);
  document.getElementById('perShort').textContent='$'+perShort.toFixed(2);
  document.getElementById('totalViews').textContent=totalViews.toLocaleString();
  document.getElementById('rpm').textContent='$'+(rpm).toFixed(3)+'/1K';
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("youtube-watch-time-calculator.html",
"YouTube Watch Time Calculator",
"Calculate total YouTube watch time hours for monetization eligibility. Find how many more hours you need to reach 4000 hours.",
"youtube watch time calculator, 4000 watch hours youtube, youtube monetization watch hours, how to reach 4000 hours youtube, watch time tracker",
"&#9201;","#FF0000","#cc0000","social","&#127909;","YouTube",
"""<div class="calc-box">
<h2 class="calc-title">&#9201; YouTube Watch Time Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Average Views per Video</label><input type="number" class="form-control" id="views" placeholder="e.g. 500"></div>
  <div class="col-md-6"><label class="form-label">Average Video Length (minutes)</label><input type="number" class="form-control" id="videoLen" placeholder="e.g. 8" step="0.5"></div>
  <div class="col-md-6"><label class="form-label">Average Watch Duration (%)</label><input type="number" class="form-control" id="retention" placeholder="e.g. 45" value="45"></div>
  <div class="col-md-6"><label class="form-label">Videos Published per Month</label><input type="number" class="form-control" id="videosPerMonth" placeholder="e.g. 8" value="4"></div>
  <div class="col-md-12"><label class="form-label">Current Watch Hours (past 12 months)</label><input type="number" class="form-control" id="currentHours" placeholder="e.g. 1200" value="0"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate Watch Time</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Watch Hours/Month</div><div class="result-value" id="monthly">-</div></div>
    <div class="col-6"><div class="result-label">Hours Still Needed</div><div class="result-value" id="needed">-</div></div>
    <div class="col-6"><div class="result-label">Months to Monetize</div><div class="result-value" id="months">-</div></div>
    <div class="col-6"><div class="result-label">Watch Hours/Video</div><div class="result-value" id="perVideo">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var views=parseFloat(document.getElementById('views').value)||0;
  var len=parseFloat(document.getElementById('videoLen').value)||0;
  var ret=parseFloat(document.getElementById('retention').value)||45;
  var vpm=parseFloat(document.getElementById('videosPerMonth').value)||4;
  var current=parseFloat(document.getElementById('currentHours').value)||0;
  var watchMins=views*len*(ret/100);
  var watchHoursPerVideo=watchMins/60;
  var monthly=watchHoursPerVideo*vpm;
  var needed=Math.max(0,4000-current);
  var months=monthly>0?(needed/monthly).toFixed(1):'N/A';
  document.getElementById('monthly').textContent=monthly.toFixed(1)+' hrs';
  document.getElementById('needed').textContent=needed.toLocaleString()+' hrs';
  document.getElementById('months').textContent=months+' months';
  document.getElementById('perVideo').textContent=watchHoursPerVideo.toFixed(2)+' hrs';
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("youtube-retention-rate-calculator.html",
"YouTube Retention Rate Calculator",
"Calculate your YouTube audience retention rate. Understand what percentage of viewers watch your entire video and how to improve it.",
"youtube retention rate calculator, audience retention youtube, youtube watch percentage, average view duration, youtube analytics retention",
"&#128200;","#b71c1c","#FF0000","social","&#127909;","YouTube",
"""<div class="calc-box">
<h2 class="calc-title">&#128200; YouTube Retention Rate Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Average View Duration (minutes)</label><input type="number" class="form-control" id="avgDuration" placeholder="e.g. 4.5" step="0.1"></div>
  <div class="col-md-6"><label class="form-label">Total Video Length (minutes)</label><input type="number" class="form-control" id="videoLength" placeholder="e.g. 10" step="0.5"></div>
  <div class="col-md-6"><label class="form-label">Total Views</label><input type="number" class="form-control" id="views" placeholder="e.g. 5000"></div>
  <div class="col-md-6"><label class="form-label">Impressions Click-Through Rate (%)</label><input type="number" class="form-control" id="ctr" placeholder="e.g. 4.5" step="0.1"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate Retention</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Retention Rate</div><div class="result-value" id="retention">-</div></div>
    <div class="col-6"><div class="result-label">Rating</div><div class="result-value" id="rating">-</div></div>
    <div class="col-6"><div class="result-label">Total Watch Time</div><div class="result-value" id="totalWatch">-</div></div>
    <div class="col-6"><div class="result-label">Benchmark</div><div class="result-value" id="bench">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var avg=parseFloat(document.getElementById('avgDuration').value)||0;
  var total=parseFloat(document.getElementById('videoLength').value)||1;
  var views=parseFloat(document.getElementById('views').value)||0;
  var retention=(avg/total)*100;
  var rating=retention<30?'Poor':retention<50?'Average':retention<70?'Good':'Excellent';
  var bench=total<5?'50%+ ideal':total<10?'40-50% good':total<20?'35-45% good':'30%+ good';
  var totalWatch=(views*avg/60).toFixed(1);
  document.getElementById('retention').textContent=retention.toFixed(1)+'%';
  document.getElementById('rating').textContent=rating;
  document.getElementById('totalWatch').textContent=totalWatch+' hrs';
  document.getElementById('bench').textContent=bench;
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("youtube-channel-growth-projection-calculator.html",
"YouTube Channel Growth Projection Calculator",
"Project your YouTube channel's future subscriber count. Set growth targets and see when you'll reach 1K, 10K, 100K, and 1M subscribers.",
"youtube channel growth projection, youtube subscriber projection calculator, when will i reach 1000 subscribers, youtube growth forecast, subscriber milestone calculator",
"&#128200;","#cc0000","#FF0000","social","&#127909;","YouTube",
"""<div class="calc-box">
<h2 class="calc-title">&#128200; YouTube Channel Growth Projection</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Current Subscribers</label><input type="number" class="form-control" id="current" placeholder="e.g. 2500"></div>
  <div class="col-md-6"><label class="form-label">Monthly Growth Rate (%)</label><input type="number" class="form-control" id="growthRate" placeholder="e.g. 15" step="0.5"></div>
  <div class="col-md-6"><label class="form-label">New Subs Per Month (Alternative)</label><input type="number" class="form-control" id="newPerMonth" placeholder="e.g. 500 (uses if rate=0)" value="0"></div>
  <div class="col-md-6"><label class="form-label">Projection Period (Months)</label><input type="number" class="form-control" id="months" placeholder="e.g. 12" value="12"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Project Growth</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Subs in 6 Months</div><div class="result-value" id="m6">-</div></div>
    <div class="col-6"><div class="result-label">Subs in 12 Months</div><div class="result-value" id="m12">-</div></div>
    <div class="col-6"><div class="result-label">Days to 1K</div><div class="result-value" id="to1k">-</div></div>
    <div class="col-6"><div class="result-label">Days to 10K</div><div class="result-value" id="to10k">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var c=parseFloat(document.getElementById('current').value)||0;
  var gr=parseFloat(document.getElementById('growthRate').value)||0;
  var npm=parseFloat(document.getElementById('newPerMonth').value)||0;
  function project(months){
    var subs=c;
    for(var i=0;i<months;i++){
      if(gr>0) subs=subs*(1+gr/100);
      else subs+=npm;
    }
    return Math.round(subs);
  }
  function monthsTo(target){
    var subs=c;
    if(subs>=target) return 0;
    for(var i=1;i<=1200;i++){
      if(gr>0) subs=subs*(1+gr/100);
      else subs+=npm;
      if(subs>=target) return i;
    }
    return 'N/A';
  }
  document.getElementById('m6').textContent=project(6).toLocaleString();
  document.getElementById('m12').textContent=project(12).toLocaleString();
  var t1=monthsTo(1000);
  var t10=monthsTo(10000);
  document.getElementById('to1k').textContent=c>=1000?'Reached!':(t1==='N/A'?'N/A':t1+' months');
  document.getElementById('to10k').textContent=c>=10000?'Reached!':(t10==='N/A'?'N/A':t10+' months');
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("views-to-subscribers-ratio-calculator.html",
"Views to Subscribers Ratio Calculator",
"Calculate your YouTube views to subscribers ratio. Understand what percentage of viewers subscribe and how to improve conversion.",
"views to subscribers ratio, youtube conversion rate, subscriber conversion calculator, views per subscriber, youtube subscriber rate",
"&#127909;","#FF0000","#cc0000","social","&#127909;","YouTube",
"""<div class="calc-box">
<h2 class="calc-title">&#127909; Views to Subscribers Ratio Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Total Channel Views</label><input type="number" class="form-control" id="totalViews" placeholder="e.g. 500000"></div>
  <div class="col-md-6"><label class="form-label">Total Subscribers</label><input type="number" class="form-control" id="subs" placeholder="e.g. 5000"></div>
  <div class="col-md-6"><label class="form-label">Views Per Video (Average)</label><input type="number" class="form-control" id="avgViews" placeholder="e.g. 2000"></div>
  <div class="col-md-6"><label class="form-label">New Subs Per Video (Average)</label><input type="number" class="form-control" id="newSubs" placeholder="e.g. 50"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate Ratio</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Views/Subscriber</div><div class="result-value" id="ratio">-</div></div>
    <div class="col-6"><div class="result-label">Sub Conversion Rate</div><div class="result-value" id="convRate">-</div></div>
    <div class="col-6"><div class="result-label">Per-Video Sub Rate</div><div class="result-value" id="perVideoRate">-</div></div>
    <div class="col-6"><div class="result-label">Rating</div><div class="result-value" id="rating">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var tv=parseFloat(document.getElementById('totalViews').value)||1;
  var s=parseFloat(document.getElementById('subs').value)||0;
  var av=parseFloat(document.getElementById('avgViews').value)||0;
  var ns=parseFloat(document.getElementById('newSubs').value)||0;
  var ratio=(tv/s).toFixed(1);
  var convRate=(s/tv*100).toFixed(3);
  var perVideoRate=av>0?(ns/av*100).toFixed(2)+'%':'N/A';
  var rating=parseFloat(convRate)>1?'Excellent':parseFloat(convRate)>0.5?'Good':parseFloat(convRate)>0.2?'Average':'Poor';
  document.getElementById('ratio').textContent=ratio+' views/sub';
  document.getElementById('convRate').textContent=convRate+'%';
  document.getElementById('perVideoRate').textContent=perVideoRate;
  document.getElementById('rating').textContent=rating;
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("youtube-thumbnail-ctr-calculator.html",
"YouTube Thumbnail CTR Calculator",
"Calculate your YouTube thumbnail click-through rate. Understand if your CTR is good and how it affects your channel growth.",
"youtube thumbnail CTR calculator, click through rate youtube, improve youtube CTR, youtube impressions CTR, thumbnail performance",
"&#128249;","#FF0000","#cc0000","social","&#127909;","YouTube",
"""<div class="calc-box">
<h2 class="calc-title">&#128249; YouTube Thumbnail CTR Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Total Impressions</label><input type="number" class="form-control" id="impressions" placeholder="e.g. 50000"></div>
  <div class="col-md-6"><label class="form-label">Total Clicks (Views)</label><input type="number" class="form-control" id="clicks" placeholder="e.g. 2500"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate CTR</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Your CTR</div><div class="result-value" id="ctr">-</div></div>
    <div class="col-6"><div class="result-label">Rating</div><div class="result-value" id="rating">-</div></div>
    <div class="col-6"><div class="result-label">Missed Views</div><div class="result-value" id="missed">-</div></div>
    <div class="col-6"><div class="result-label">CTR Benchmark</div><div class="result-value" id="bench">-</div></div>
  </div>
</div>
</div>
<div class="calc-box mt-3">
<h3 style="font-size:1rem;font-weight:700">YouTube CTR Benchmarks</h3>
<ul style="font-size:0.85rem;color:var(--text-secondary)">
<li><strong>Below 2%</strong> - Poor: Thumbnail/title needs major rework</li>
<li><strong>2-5%</strong> - Average: Room for improvement</li>
<li><strong>5-10%</strong> - Good: Above YouTube average</li>
<li><strong>10%+</strong> - Excellent: Top-performing content</li>
</ul>
</div>""",
"""<script>
function calc(){
  var imp=parseFloat(document.getElementById('impressions').value)||1;
  var clicks=parseFloat(document.getElementById('clicks').value)||0;
  var ctr=(clicks/imp)*100;
  var rating=ctr<2?'Poor':ctr<5?'Average':ctr<10?'Good':'Excellent';
  var missed=imp-clicks;
  document.getElementById('ctr').textContent=ctr.toFixed(2)+'%';
  document.getElementById('rating').textContent=rating;
  document.getElementById('missed').textContent=missed.toLocaleString()+' missed';
  document.getElementById('bench').textContent='Avg: 4-5%';
  document.getElementById('resultBox').style.display='block';
}
</script>""")


# ─────────────────────────────────────────────────────────
# TIKTOK CALCULATORS
# ─────────────────────────────────────────────────────────

page("tiktok-engagement-rate-calculator.html",
"TikTok Engagement Rate Calculator",
"Calculate your TikTok engagement rate from likes, comments, shares, and views. See if your engagement is above average for TikTok creators.",
"tiktok engagement rate calculator, tiktok engagement rate, how to calculate tiktok engagement, tiktok analytics, tiktok creator metrics",
"&#127925;","#010101","#ff0050","social","&#127925;","TikTok",
"""<div class="calc-box">
<h2 class="calc-title">&#127925; TikTok Engagement Rate Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Total Views</label><input type="number" class="form-control" id="views" placeholder="e.g. 100000"></div>
  <div class="col-md-6"><label class="form-label">Total Likes</label><input type="number" class="form-control" id="likes" placeholder="e.g. 8000"></div>
  <div class="col-md-6"><label class="form-label">Total Comments</label><input type="number" class="form-control" id="comments" placeholder="e.g. 300"></div>
  <div class="col-md-6"><label class="form-label">Total Shares</label><input type="number" class="form-control" id="shares" placeholder="e.g. 500"></div>
  <div class="col-md-6"><label class="form-label">Followers</label><input type="number" class="form-control" id="followers" placeholder="e.g. 25000"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate TikTok Engagement</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">View-Based ER</div><div class="result-value" id="viewER">-</div></div>
    <div class="col-6"><div class="result-label">Follower-Based ER</div><div class="result-value" id="follER">-</div></div>
    <div class="col-6"><div class="result-label">Viral Score</div><div class="result-value" id="viral">-</div></div>
    <div class="col-6"><div class="result-label">Rating</div><div class="result-value" id="rating">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var v=parseFloat(document.getElementById('views').value)||1;
  var l=parseFloat(document.getElementById('likes').value)||0;
  var c=parseFloat(document.getElementById('comments').value)||0;
  var s=parseFloat(document.getElementById('shares').value)||0;
  var f=parseFloat(document.getElementById('followers').value)||1;
  var total=l+c+s;
  var viewER=(total/v)*100;
  var follER=(total/f)*100;
  var viralScore=(v/f*100).toFixed(1);
  var rating=viewER<3?'Below Avg':viewER<6?'Average':viewER<10?'Good':'Viral';
  document.getElementById('viewER').textContent=viewER.toFixed(2)+'%';
  document.getElementById('follER').textContent=follER.toFixed(2)+'%';
  document.getElementById('viral').textContent=viralScore+'%';
  document.getElementById('rating').textContent=rating;
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("tiktok-earnings-calculator.html",
"TikTok Earnings Calculator",
"Calculate how much money you can earn from TikTok. Estimate TikTok Creator Fund payments, brand deals, and total monthly income.",
"tiktok earnings calculator, how much does tiktok pay, tiktok creator fund, tiktok money calculator, tiktok income estimator, tiktok monetization",
"&#128176;","#ff0050","#00f2ea","social","&#127925;","TikTok",
"""<div class="calc-box">
<h2 class="calc-title">&#128176; TikTok Earnings Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Average Views per Video</label><input type="number" class="form-control" id="views" placeholder="e.g. 50000"></div>
  <div class="col-md-6"><label class="form-label">Videos per Month</label><input type="number" class="form-control" id="videos" placeholder="e.g. 20" value="15"></div>
  <div class="col-md-6"><label class="form-label">Total Followers</label><input type="number" class="form-control" id="followers" placeholder="e.g. 100000"></div>
  <div class="col-md-6"><label class="form-label">Engagement Rate (%)</label><input type="number" class="form-control" id="engRate" placeholder="e.g. 5" step="0.1" value="5"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate TikTok Income</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Creator Fund/Month</div><div class="result-value" id="fund">-</div></div>
    <div class="col-6"><div class="result-label">Brand Deal/Post</div><div class="result-value" id="brand">-</div></div>
    <div class="col-6"><div class="result-label">Total Monthly Income</div><div class="result-value" id="total">-</div></div>
    <div class="col-6"><div class="result-label">Annual Projection</div><div class="result-value" id="annual">-</div></div>
  </div>
</div>
</div>
<p style="font-size:0.8rem;color:var(--text-muted);margin-top:8px">TikTok Creator Fund pays approximately $0.02-$0.04 per 1,000 views. Brand deals are estimates based on follower count and engagement.</p>""",
"""<script>
function calc(){
  var views=parseFloat(document.getElementById('views').value)||0;
  var videos=parseFloat(document.getElementById('videos').value)||15;
  var followers=parseFloat(document.getElementById('followers').value)||1;
  var eng=parseFloat(document.getElementById('engRate').value)||5;
  var monthlyViews=views*videos;
  var fund=(monthlyViews/1000)*0.03;
  var brandDeal=(followers/1000)*8*(1+(eng-3)*0.05);
  var brandDeals=Math.floor(videos/10);
  var total=fund+(brandDeal*brandDeals);
  document.getElementById('fund').textContent='$'+fund.toFixed(2);
  document.getElementById('brand').textContent='$'+brandDeal.toFixed(0);
  document.getElementById('total').textContent='$'+total.toFixed(0);
  document.getElementById('annual').textContent='$'+(total*12).toFixed(0).replace(/\B(?=(\d{3})+(?!\d))/g,',');
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("tiktok-virality-score-calculator.html",
"TikTok Virality Score Calculator",
"Calculate your TikTok virality score. Find out if your video is going viral based on views-to-follower ratio and engagement metrics.",
"tiktok virality score, how to go viral on tiktok, tiktok viral calculator, tiktok views ratio, tiktok for you page algorithm",
"&#128293;","#010101","#ff0050","social","&#127925;","TikTok",
"""<div class="calc-box">
<h2 class="calc-title">&#128293; TikTok Virality Score Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Video Views</label><input type="number" class="form-control" id="views" placeholder="e.g. 500000"></div>
  <div class="col-md-6"><label class="form-label">Followers at Time of Post</label><input type="number" class="form-control" id="followers" placeholder="e.g. 5000"></div>
  <div class="col-md-6"><label class="form-label">Likes</label><input type="number" class="form-control" id="likes" placeholder="e.g. 50000"></div>
  <div class="col-md-6"><label class="form-label">Shares</label><input type="number" class="form-control" id="shares" placeholder="e.g. 5000"></div>
  <div class="col-md-6"><label class="form-label">Comments</label><input type="number" class="form-control" id="comments" placeholder="e.g. 1000"></div>
  <div class="col-md-6"><label class="form-label">Hours Since Posted</label><input type="number" class="form-control" id="hours" placeholder="e.g. 24" value="24"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate Virality</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Virality Score</div><div class="result-value" id="score">-</div></div>
    <div class="col-6"><div class="result-label">Status</div><div class="result-value" id="status">-</div></div>
    <div class="col-6"><div class="result-label">Views/Follower Ratio</div><div class="result-value" id="ratio">-</div></div>
    <div class="col-6"><div class="result-label">Hourly View Rate</div><div class="result-value" id="hourly">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var v=parseFloat(document.getElementById('views').value)||0;
  var f=parseFloat(document.getElementById('followers').value)||1;
  var l=parseFloat(document.getElementById('likes').value)||0;
  var s=parseFloat(document.getElementById('shares').value)||0;
  var c=parseFloat(document.getElementById('comments').value)||0;
  var h=parseFloat(document.getElementById('hours').value)||24;
  var vfr=v/f;
  var engRate=((l+s+c)/v)*100;
  var hourly=Math.round(v/h);
  var raw=Math.min(100,(vfr*0.3+engRate*0.7));
  var score=Math.min(100,Math.round(raw));
  var status=score<20?'Normal':score<40?'Trending':score<70?'Going Viral':'Mega Viral!';
  document.getElementById('score').textContent=score+'/100';
  document.getElementById('status').textContent=status;
  document.getElementById('ratio').textContent=vfr.toFixed(1)+'x';
  document.getElementById('hourly').textContent=hourly.toLocaleString()+'/hr';
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("tiktok-growth-rate-calculator.html",
"TikTok Growth Rate Calculator",
"Track your TikTok follower growth rate and project when you'll reach your next milestone. Calculate daily gain and monthly growth percentage.",
"tiktok growth rate calculator, tiktok follower growth, tiktok growth tracker, how to grow on tiktok, tiktok followers increase",
"&#128200;","#ff0050","#010101","social","&#127925;","TikTok",
"""<div class="calc-box">
<h2 class="calc-title">&#128200; TikTok Growth Rate Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Followers at Start</label><input type="number" class="form-control" id="start" placeholder="e.g. 8000"></div>
  <div class="col-md-6"><label class="form-label">Followers Now</label><input type="number" class="form-control" id="end" placeholder="e.g. 12000"></div>
  <div class="col-md-6"><label class="form-label">Days in Period</label><input type="number" class="form-control" id="days" value="30"></div>
  <div class="col-md-6"><label class="form-label">Videos Posted</label><input type="number" class="form-control" id="videos" placeholder="e.g. 25" value="20"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate TikTok Growth</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Monthly Growth Rate</div><div class="result-value" id="rate">-</div></div>
    <div class="col-6"><div class="result-label">Daily Follower Gain</div><div class="result-value" id="daily">-</div></div>
    <div class="col-6"><div class="result-label">Followers per Video</div><div class="result-value" id="perVideo">-</div></div>
    <div class="col-6"><div class="result-label">Months to 100K</div><div class="result-value" id="to100k">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var s=parseFloat(document.getElementById('start').value)||1;
  var e=parseFloat(document.getElementById('end').value)||0;
  var d=parseFloat(document.getElementById('days').value)||30;
  var v=parseFloat(document.getElementById('videos').value)||1;
  var gained=e-s;
  var rate=((gained/s)*100*(30/d)).toFixed(2);
  var daily=(gained/d).toFixed(1);
  var perVideo=(gained/v).toFixed(0);
  var monthlyGain=gained/d*30;
  var remaining=Math.max(0,100000-e);
  var to100k=monthlyGain>0?Math.ceil(remaining/monthlyGain):'N/A';
  document.getElementById('rate').textContent=rate+'%/month';
  document.getElementById('daily').textContent='+'+daily+'/day';
  document.getElementById('perVideo').textContent='+'+perVideo+'/video';
  document.getElementById('to100k').textContent=to100k==='N/A'?'N/A':to100k+' months';
  document.getElementById('resultBox').style.display='block';
}
</script>""")


# ─────────────────────────────────────────────────────────
# TWITTER / X CALCULATORS
# ─────────────────────────────────────────────────────────

page("twitter-engagement-rate-calculator.html",
"Twitter (X) Engagement Rate Calculator",
"Calculate your Twitter/X engagement rate from likes, retweets, replies, and impressions. See how your tweets perform compared to benchmarks.",
"twitter engagement rate calculator, X engagement rate, tweet performance calculator, twitter analytics, twitter impressions engagement",
"&#128038;","#1DA1F2","#0d8bd9","social","&#128038;","Twitter / X",
"""<div class="calc-box">
<h2 class="calc-title">&#128038; Twitter (X) Engagement Rate Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Tweet Impressions</label><input type="number" class="form-control" id="impressions" placeholder="e.g. 10000"></div>
  <div class="col-md-6"><label class="form-label">Likes</label><input type="number" class="form-control" id="likes" placeholder="e.g. 150"></div>
  <div class="col-md-6"><label class="form-label">Retweets</label><input type="number" class="form-control" id="retweets" placeholder="e.g. 30"></div>
  <div class="col-md-6"><label class="form-label">Replies</label><input type="number" class="form-control" id="replies" placeholder="e.g. 20"></div>
  <div class="col-md-6"><label class="form-label">Followers</label><input type="number" class="form-control" id="followers" placeholder="e.g. 5000"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate X Engagement</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Impression-Based ER</div><div class="result-value" id="impER">-</div></div>
    <div class="col-6"><div class="result-label">Follower-Based ER</div><div class="result-value" id="follER">-</div></div>
    <div class="col-6"><div class="result-label">Total Engagements</div><div class="result-value" id="total">-</div></div>
    <div class="col-6"><div class="result-label">Rating</div><div class="result-value" id="rating">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var imp=parseFloat(document.getElementById('impressions').value)||1;
  var l=parseFloat(document.getElementById('likes').value)||0;
  var r=parseFloat(document.getElementById('retweets').value)||0;
  var rep=parseFloat(document.getElementById('replies').value)||0;
  var f=parseFloat(document.getElementById('followers').value)||1;
  var total=l+r+rep;
  var impER=(total/imp)*100;
  var follER=(total/f)*100;
  var rating=impER<0.5?'Poor':impER<1?'Average':impER<2?'Good':'Excellent';
  document.getElementById('impER').textContent=impER.toFixed(2)+'%';
  document.getElementById('follER').textContent=follER.toFixed(2)+'%';
  document.getElementById('total').textContent=total.toLocaleString();
  document.getElementById('rating').textContent=rating;
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("tweet-engagement-calculator.html",
"Tweet Engagement Calculator",
"Calculate individual tweet engagement metrics including likes ratio, retweet rate, and reply rate for any tweet or thread.",
"tweet engagement calculator, single tweet analytics, twitter post performance, tweet likes retweet ratio, tweet reach calculator",
"&#128038;","#0d8bd9","#1DA1F2","social","&#128038;","Twitter / X",
"""<div class="calc-box">
<h2 class="calc-title">&#128038; Tweet Engagement Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Likes</label><input type="number" class="form-control" id="likes" placeholder="e.g. 250"></div>
  <div class="col-md-6"><label class="form-label">Retweets</label><input type="number" class="form-control" id="rt" placeholder="e.g. 80"></div>
  <div class="col-md-6"><label class="form-label">Quote Tweets</label><input type="number" class="form-control" id="qt" placeholder="e.g. 15" value="0"></div>
  <div class="col-md-6"><label class="form-label">Replies</label><input type="number" class="form-control" id="replies" placeholder="e.g. 40"></div>
  <div class="col-md-6"><label class="form-label">Bookmarks</label><input type="number" class="form-control" id="bookmarks" placeholder="e.g. 30" value="0"></div>
  <div class="col-md-6"><label class="form-label">Impressions</label><input type="number" class="form-control" id="imp" placeholder="e.g. 15000"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Analyze Tweet</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Engagement Rate</div><div class="result-value" id="er">-</div></div>
    <div class="col-6"><div class="result-label">Amplification Rate</div><div class="result-value" id="amp">-</div></div>
    <div class="col-6"><div class="result-label">Applause Rate</div><div class="result-value" id="applause">-</div></div>
    <div class="col-6"><div class="result-label">Conversation Rate</div><div class="result-value" id="conv">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var l=parseFloat(document.getElementById('likes').value)||0;
  var rt=parseFloat(document.getElementById('rt').value)||0;
  var qt=parseFloat(document.getElementById('qt').value)||0;
  var rep=parseFloat(document.getElementById('replies').value)||0;
  var bm=parseFloat(document.getElementById('bookmarks').value)||0;
  var imp=parseFloat(document.getElementById('imp').value)||1;
  var total=l+rt+qt+rep+bm;
  var er=(total/imp)*100;
  var amp=((rt+qt)/imp)*100;
  var applause=(l/imp)*100;
  var conv=(rep/imp)*100;
  document.getElementById('er').textContent=er.toFixed(2)+'%';
  document.getElementById('amp').textContent=amp.toFixed(2)+'%';
  document.getElementById('applause').textContent=applause.toFixed(2)+'%';
  document.getElementById('conv').textContent=conv.toFixed(3)+'%';
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("twitter-growth-rate-calculator.html",
"Twitter (X) Growth Rate Calculator",
"Calculate your Twitter/X account follower growth rate. Track monthly growth and project when you'll reach your follower milestones.",
"twitter growth rate calculator, X follower growth, twitter followers increase, twitter growth tracker, how to grow twitter",
"&#128200;","#1DA1F2","#0d8bd9","social","&#128038;","Twitter / X",
"""<div class="calc-box">
<h2 class="calc-title">&#128200; Twitter (X) Growth Rate Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Followers at Start</label><input type="number" class="form-control" id="start" placeholder="e.g. 2000"></div>
  <div class="col-md-6"><label class="form-label">Followers Now</label><input type="number" class="form-control" id="end" placeholder="e.g. 2500"></div>
  <div class="col-md-6"><label class="form-label">Days in Period</label><input type="number" class="form-control" id="days" value="30"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate Growth</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Growth Rate</div><div class="result-value" id="rate">-</div></div>
    <div class="col-6"><div class="result-label">Daily Gain</div><div class="result-value" id="daily">-</div></div>
    <div class="col-6"><div class="result-label">Months to 10K</div><div class="result-value" id="to10k">-</div></div>
    <div class="col-6"><div class="result-label">Annual Projection</div><div class="result-value" id="annual">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var s=parseFloat(document.getElementById('start').value)||1;
  var e=parseFloat(document.getElementById('end').value)||0;
  var d=parseFloat(document.getElementById('days').value)||30;
  var gained=e-s;
  var rate=((gained/s)*100).toFixed(2);
  var daily=(gained/d).toFixed(1);
  var monthlyGain=gained/d*30;
  var remaining=Math.max(0,10000-e);
  var to10k=monthlyGain>0?Math.ceil(remaining/monthlyGain):'N/A';
  var annual=Math.round(e+monthlyGain*12);
  document.getElementById('rate').textContent=rate+'%';
  document.getElementById('daily').textContent='+'+daily+'/day';
  document.getElementById('to10k').textContent=e>=10000?'Reached!':to10k+' months';
  document.getElementById('annual').textContent=annual.toLocaleString();
  document.getElementById('resultBox').style.display='block';
}
</script>""")


# ─────────────────────────────────────────────────────────
# LINKEDIN CALCULATORS
# ─────────────────────────────────────────────────────────

page("linkedin-engagement-rate-calculator.html",
"LinkedIn Engagement Rate Calculator",
"Calculate your LinkedIn post and profile engagement rate. See how your content performs against LinkedIn's average benchmarks.",
"linkedin engagement rate calculator, linkedin post analytics, linkedin engagement, how to calculate linkedin engagement, linkedin metrics",
"&#128188;","#0077B5","#005885","social","&#128188;","LinkedIn",
"""<div class="calc-box">
<h2 class="calc-title">&#128188; LinkedIn Engagement Rate Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Post Impressions</label><input type="number" class="form-control" id="impressions" placeholder="e.g. 5000"></div>
  <div class="col-md-6"><label class="form-label">Reactions (Likes)</label><input type="number" class="form-control" id="reactions" placeholder="e.g. 120"></div>
  <div class="col-md-6"><label class="form-label">Comments</label><input type="number" class="form-control" id="comments" placeholder="e.g. 25"></div>
  <div class="col-md-6"><label class="form-label">Reposts / Shares</label><input type="number" class="form-control" id="shares" placeholder="e.g. 15" value="0"></div>
  <div class="col-md-6"><label class="form-label">Clicks</label><input type="number" class="form-control" id="clicks" placeholder="e.g. 80" value="0"></div>
  <div class="col-md-6"><label class="form-label">Connections / Followers</label><input type="number" class="form-control" id="followers" placeholder="e.g. 3000"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate LinkedIn ER</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Engagement Rate</div><div class="result-value" id="er">-</div></div>
    <div class="col-6"><div class="result-label">Rating</div><div class="result-value" id="rating">-</div></div>
    <div class="col-6"><div class="result-label">Click-Through Rate</div><div class="result-value" id="ctr">-</div></div>
    <div class="col-6"><div class="result-label">Reach Rate</div><div class="result-value" id="reach">-</div></div>
  </div>
</div>
</div>
<div class="calc-box mt-3">
<h3 style="font-size:1rem;font-weight:700">LinkedIn Engagement Benchmarks</h3>
<ul style="font-size:0.85rem;color:var(--text-secondary)">
<li><strong>Below 1%</strong> - Poor performance, review posting strategy</li>
<li><strong>1-2%</strong> - Average for LinkedIn (typical B2B benchmark)</li>
<li><strong>2-5%</strong> - Good: Above average LinkedIn performance</li>
<li><strong>5%+</strong> - Excellent: High-performing LinkedIn content</li>
</ul>
</div>""",
"""<script>
function calc(){
  var imp=parseFloat(document.getElementById('impressions').value)||1;
  var r=parseFloat(document.getElementById('reactions').value)||0;
  var c=parseFloat(document.getElementById('comments').value)||0;
  var s=parseFloat(document.getElementById('shares').value)||0;
  var cl=parseFloat(document.getElementById('clicks').value)||0;
  var f=parseFloat(document.getElementById('followers').value)||1;
  var total=r+c+s+cl;
  var er=(total/imp)*100;
  var ctr=(cl/imp)*100;
  var reach=(imp/f)*100;
  var rating=er<1?'Poor':er<2?'Average':er<5?'Good':'Excellent';
  document.getElementById('er').textContent=er.toFixed(2)+'%';
  document.getElementById('rating').textContent=rating;
  document.getElementById('ctr').textContent=ctr.toFixed(2)+'%';
  document.getElementById('reach').textContent=reach.toFixed(1)+'%';
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("linkedin-post-performance-calculator.html",
"LinkedIn Post Performance Calculator",
"Analyze the performance of your LinkedIn posts. Calculate reach, engagement, virality, and overall post score to optimize your content strategy.",
"linkedin post performance calculator, linkedin analytics, linkedin post reach, linkedin content score, linkedin post analyzer",
"&#128202;","#005885","#0077B5","social","&#128188;","LinkedIn",
"""<div class="calc-box">
<h2 class="calc-title">&#128202; LinkedIn Post Performance Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Impressions</label><input type="number" class="form-control" id="imp" placeholder="e.g. 8000"></div>
  <div class="col-md-6"><label class="form-label">Unique Views</label><input type="number" class="form-control" id="views" placeholder="e.g. 5000"></div>
  <div class="col-md-6"><label class="form-label">Reactions</label><input type="number" class="form-control" id="react" placeholder="e.g. 200"></div>
  <div class="col-md-6"><label class="form-label">Comments</label><input type="number" class="form-control" id="comments" placeholder="e.g. 35"></div>
  <div class="col-md-6"><label class="form-label">Reposts</label><input type="number" class="form-control" id="reposts" placeholder="e.g. 20"></div>
  <div class="col-md-6"><label class="form-label">Profile Visits from Post</label><input type="number" class="form-control" id="profileVisits" placeholder="e.g. 80" value="0"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Analyze Performance</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Performance Score</div><div class="result-value" id="score">-</div></div>
    <div class="col-6"><div class="result-label">Engagement Rate</div><div class="result-value" id="er">-</div></div>
    <div class="col-6"><div class="result-label">Virality Rate</div><div class="result-value" id="viral">-</div></div>
    <div class="col-6"><div class="result-label">Overall Grade</div><div class="result-value" id="grade">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var imp=parseFloat(document.getElementById('imp').value)||1;
  var views=parseFloat(document.getElementById('views').value)||1;
  var r=parseFloat(document.getElementById('react').value)||0;
  var c=parseFloat(document.getElementById('comments').value)||0;
  var re=parseFloat(document.getElementById('reposts').value)||0;
  var pv=parseFloat(document.getElementById('profileVisits').value)||0;
  var er=((r+c+re)/imp)*100;
  var viral=(re/imp)*100;
  var pvRate=(pv/views)*100;
  var score=Math.min(100,Math.round(er*10+viral*50+pvRate*2));
  var grade=score>=80?'A':score>=60?'B':score>=40?'C':score>=20?'D':'F';
  document.getElementById('score').textContent=score+'/100';
  document.getElementById('er').textContent=er.toFixed(2)+'%';
  document.getElementById('viral').textContent=viral.toFixed(3)+'%';
  document.getElementById('grade').textContent=grade;
  document.getElementById('resultBox').style.display='block';
}
</script>""")


# ─────────────────────────────────────────────────────────
# ADVANCED / EARNING CALCULATORS
# ─────────────────────────────────────────────────────────

page("influencer-earnings-per-post-calculator.html",
"Influencer Earnings Per Post Calculator",
"Calculate how much to charge per sponsored post as an influencer. Get your rate card based on followers, engagement rate, and platform.",
"influencer earnings per post calculator, how much to charge for sponsored post, influencer rate card, sponsored content pricing, influencer fee calculator",
"&#128176;","#ff6b35","#f7c59f","social","&#128247;","Social Media",
"""<div class="calc-box">
<h2 class="calc-title">&#128176; Influencer Earnings Per Post Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Platform</label>
    <select class="form-control" id="platform">
      <option value="1.0">Instagram Feed Post</option>
      <option value="1.3">Instagram Reel</option>
      <option value="0.6">Instagram Story</option>
      <option value="1.2">YouTube Integration</option>
      <option value="0.8">TikTok Video</option>
      <option value="0.7">Twitter/X Tweet</option>
      <option value="0.9">LinkedIn Post</option>
    </select>
  </div>
  <div class="col-md-6"><label class="form-label">Followers</label><input type="number" class="form-control" id="followers" placeholder="e.g. 50000"></div>
  <div class="col-md-6"><label class="form-label">Engagement Rate (%)</label><input type="number" class="form-control" id="eng" placeholder="e.g. 4" step="0.1"></div>
  <div class="col-md-6"><label class="form-label">Niche</label>
    <select class="form-control" id="niche">
      <option value="2.5">Finance / Business</option>
      <option value="2.0">Technology</option>
      <option value="1.8">Health / Fitness</option>
      <option value="1.5">Fashion / Beauty</option>
      <option value="1.3">Food / Travel</option>
      <option value="1.0">Entertainment</option>
      <option value="1.2">Parenting / Family</option>
    </select>
  </div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Get My Rate</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Suggested Rate</div><div class="result-value" id="rate">-</div></div>
    <div class="col-6"><div class="result-label">Rate Range</div><div class="result-value" id="range">-</div></div>
    <div class="col-6"><div class="result-label">Monthly Potential</div><div class="result-value" id="monthly">-</div></div>
    <div class="col-6"><div class="result-label">Influencer Tier</div><div class="result-value" id="tier">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var platform=parseFloat(document.getElementById('platform').value)||1;
  var f=parseFloat(document.getElementById('followers').value)||0;
  var eng=parseFloat(document.getElementById('eng').value)||1;
  var niche=parseFloat(document.getElementById('niche').value)||1;
  if(!f){alert('Enter follower count');return;}
  var base=(f/1000)*10*niche*platform*(1+(eng-1)*0.08);
  var low=Math.round(base*0.65);
  var high=Math.round(base*1.5);
  var monthly=Math.round(base*4);
  var tier=f<1000?'Nano':f<10000?'Micro':f<100000?'Mid-Tier':f<500000?'Macro':'Mega';
  document.getElementById('rate').textContent='$'+Math.round(base).toLocaleString();
  document.getElementById('range').textContent='$'+low.toLocaleString()+'-$'+high.toLocaleString();
  document.getElementById('monthly').textContent='$'+monthly.toLocaleString();
  document.getElementById('tier').textContent=tier;
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("brand-deal-rate-calculator.html",
"Brand Deal Rate Calculator",
"Calculate your brand deal rate as a content creator. Get the right price for sponsored content, product reviews, and long-term brand partnerships.",
"brand deal rate calculator, sponsored content pricing, brand partnership rate, content creator brand deals, how much to charge brands",
"&#129534;","#6366f1","#8b5cf6","social","&#128247;","Social Media",
"""<div class="calc-box">
<h2 class="calc-title">&#129534; Brand Deal Rate Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Total Followers (all platforms)</label><input type="number" class="form-control" id="followers" placeholder="e.g. 75000"></div>
  <div class="col-md-6"><label class="form-label">Average Engagement Rate (%)</label><input type="number" class="form-control" id="eng" placeholder="e.g. 3.5" step="0.1"></div>
  <div class="col-md-6"><label class="form-label">Deal Type</label>
    <select class="form-control" id="dealType">
      <option value="1.0">Single Sponsored Post</option>
      <option value="2.5">Dedicated Video Review</option>
      <option value="1.5">Story/Short Mention</option>
      <option value="4.0">Monthly Ambassador</option>
      <option value="3.0">Exclusive Campaign</option>
    </select>
  </div>
  <div class="col-md-6"><label class="form-label">Your Niche CPM Value</label>
    <select class="form-control" id="cpm">
      <option value="15">Finance ($15+ CPM)</option>
      <option value="10">Technology ($10 CPM)</option>
      <option value="8">Health & Fitness ($8 CPM)</option>
      <option value="5" selected>Lifestyle ($5 CPM)</option>
      <option value="3">Entertainment ($3 CPM)</option>
    </select>
  </div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate Brand Deal Rate</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Minimum Rate</div><div class="result-value" id="min">-</div></div>
    <div class="col-6"><div class="result-label">Recommended Rate</div><div class="result-value" id="rec">-</div></div>
    <div class="col-6"><div class="result-label">Premium Rate</div><div class="result-value" id="prem">-</div></div>
    <div class="col-6"><div class="result-label">Monthly Deal Revenue</div><div class="result-value" id="monthly">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var f=parseFloat(document.getElementById('followers').value)||0;
  var eng=parseFloat(document.getElementById('eng').value)||1;
  var dt=parseFloat(document.getElementById('dealType').value)||1;
  var cpm=parseFloat(document.getElementById('cpm').value)||5;
  var base=(f/1000)*cpm*dt*(1+(eng-1)*0.05);
  document.getElementById('min').textContent='$'+Math.round(base*0.6).toLocaleString();
  document.getElementById('rec').textContent='$'+Math.round(base).toLocaleString();
  document.getElementById('prem').textContent='$'+Math.round(base*1.8).toLocaleString();
  document.getElementById('monthly').textContent='$'+Math.round(base*3).toLocaleString();
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("adsense-rpm-calculator.html",
"AdSense RPM Calculator",
"Calculate your Google AdSense RPM (Revenue Per Mille) and estimate monthly earnings from your website traffic. Optimize your AdSense strategy.",
"adsense RPM calculator, google adsense earnings calculator, website adsense income, adsense revenue estimator, adsense CPM calculator, blog earnings",
"&#128176;","#4285F4","#34A853","social","&#128176;","Monetization",
"""<div class="calc-box">
<h2 class="calc-title">&#128176; AdSense RPM Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Monthly Page Views</label><input type="number" class="form-control" id="pageviews" placeholder="e.g. 100000"></div>
  <div class="col-md-6"><label class="form-label">AdSense Revenue Last Month ($)</label><input type="number" class="form-control" id="revenue" placeholder="e.g. 250" step="0.01"></div>
  <div class="col-md-6"><label class="form-label">Ad Impressions per Page</label><input type="number" class="form-control" id="adsPerPage" placeholder="e.g. 3" value="3"></div>
  <div class="col-md-6"><label class="form-label">Website Niche</label>
    <select class="form-control" id="niche">
      <option value="15">Finance / Insurance</option>
      <option value="10">Legal / Law</option>
      <option value="8">Technology / Software</option>
      <option value="6">Health / Medical</option>
      <option value="4" selected>General / Lifestyle</option>
      <option value="3">Entertainment / Gaming</option>
      <option value="2">News / Blog</option>
    </select>
  </div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate AdSense RPM</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Your RPM</div><div class="result-value" id="rpm">-</div></div>
    <div class="col-6"><div class="result-label">Estimated CPM</div><div class="result-value" id="cpm">-</div></div>
    <div class="col-6"><div class="result-label">Monthly Earnings</div><div class="result-value" id="monthly">-</div></div>
    <div class="col-6"><div class="result-label">Yearly Projection</div><div class="result-value" id="yearly">-</div></div>
  </div>
</div>
</div>
<div class="calc-box mt-3">
<h3 style="font-size:1rem;font-weight:700">&#128200; AdSense RPM by Niche (2025)</h3>
<div class="table-responsive"><table class="table table-sm" style="font-size:0.82rem">
<thead><tr><th>Niche</th><th>Avg RPM</th><th>Avg CPM</th></tr></thead>
<tbody>
<tr><td>Finance/Insurance</td><td>$10-$25</td><td>$15-$50</td></tr>
<tr><td>Technology</td><td>$5-$15</td><td>$8-$25</td></tr>
<tr><td>Health/Medical</td><td>$4-$10</td><td>$6-$18</td></tr>
<tr><td>General/Blog</td><td>$2-$6</td><td>$3-$10</td></tr>
<tr><td>Entertainment</td><td>$1-$4</td><td>$2-$6</td></tr>
</tbody>
</table></div>
</div>""",
"""<script>
function calc(){
  var pv=parseFloat(document.getElementById('pageviews').value)||0;
  var rev=parseFloat(document.getElementById('revenue').value)||0;
  var adsPP=parseFloat(document.getElementById('adsPerPage').value)||3;
  var nicheRPM=parseFloat(document.getElementById('niche').value)||4;
  var rpm, monthly;
  if(rev&&pv){
    rpm=(rev/pv)*1000;
    monthly=rev;
  } else {
    rpm=nicheRPM*(adsPP/3);
    monthly=(pv/1000)*rpm;
  }
  var cpm=rpm/0.68;
  var yearly=monthly*12;
  document.getElementById('rpm').textContent='$'+rpm.toFixed(2);
  document.getElementById('cpm').textContent='$'+cpm.toFixed(2);
  document.getElementById('monthly').textContent='$'+monthly.toFixed(2);
  document.getElementById('yearly').textContent='$'+yearly.toFixed(0).replace(/\B(?=(\d{3})+(?!\d))/g,',');
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("affiliate-earnings-calculator.html",
"Affiliate Earnings Calculator",
"Calculate your potential affiliate marketing income. Estimate commissions from traffic, conversion rates, and average order values.",
"affiliate earnings calculator, affiliate marketing income calculator, affiliate commission calculator, how much can i make with affiliate marketing",
"&#128200;","#10b981","#059669","social","&#128176;","Monetization",
"""<div class="calc-box">
<h2 class="calc-title">&#128200; Affiliate Earnings Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Monthly Website/Social Traffic</label><input type="number" class="form-control" id="traffic" placeholder="e.g. 10000"></div>
  <div class="col-md-6"><label class="form-label">Click-Through Rate to Affiliate (%)</label><input type="number" class="form-control" id="ctr" placeholder="e.g. 5" step="0.1" value="5"></div>
  <div class="col-md-6"><label class="form-label">Affiliate Conversion Rate (%)</label><input type="number" class="form-control" id="convRate" placeholder="e.g. 2" step="0.1" value="2"></div>
  <div class="col-md-6"><label class="form-label">Average Order Value ($)</label><input type="number" class="form-control" id="aov" placeholder="e.g. 100" value="100"></div>
  <div class="col-md-6"><label class="form-label">Commission Rate (%)</label><input type="number" class="form-control" id="commission" placeholder="e.g. 10" step="0.5" value="10"></div>
  <div class="col-md-6"><label class="form-label">Number of Affiliate Products</label><input type="number" class="form-control" id="products" placeholder="e.g. 3" value="1"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate Affiliate Income</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Monthly Sales</div><div class="result-value" id="sales">-</div></div>
    <div class="col-6"><div class="result-label">Monthly Commission</div><div class="result-value" id="monthly">-</div></div>
    <div class="col-6"><div class="result-label">Yearly Projection</div><div class="result-value" id="yearly">-</div></div>
    <div class="col-6"><div class="result-label">EPC (Earnings/Click)</div><div class="result-value" id="epc">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var t=parseFloat(document.getElementById('traffic').value)||0;
  var ctr=parseFloat(document.getElementById('ctr').value)||5;
  var conv=parseFloat(document.getElementById('convRate').value)||2;
  var aov=parseFloat(document.getElementById('aov').value)||100;
  var comm=parseFloat(document.getElementById('commission').value)||10;
  var prod=parseFloat(document.getElementById('products').value)||1;
  var clicks=t*(ctr/100);
  var sales=clicks*(conv/100)*prod;
  var monthly=sales*aov*(comm/100);
  var yearly=monthly*12;
  var epc=clicks>0?(monthly/clicks).toFixed(3):'0';
  document.getElementById('sales').textContent=Math.round(sales).toLocaleString();
  document.getElementById('monthly').textContent='$'+monthly.toFixed(2);
  document.getElementById('yearly').textContent='$'+yearly.toFixed(0).replace(/\B(?=(\d{3})+(?!\d))/g,',');
  document.getElementById('epc').textContent='$'+epc;
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("social-media-roi-calculator.html",
"Social Media ROI Calculator",
"Calculate your social media marketing ROI. Measure returns from organic content, paid ads, and influencer campaigns against total spend.",
"social media ROI calculator, social media return on investment, marketing ROI calculator, social media campaign ROI, digital marketing ROI",
"&#128200;","#6366f1","#8b5cf6","social","&#128200;","Social Media",
"""<div class="calc-box">
<h2 class="calc-title">&#128200; Social Media ROI Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Total Social Media Spend ($)</label><input type="number" class="form-control" id="spend" placeholder="e.g. 2000"></div>
  <div class="col-md-6"><label class="form-label">Revenue Generated ($)</label><input type="number" class="form-control" id="revenue" placeholder="e.g. 8000"></div>
  <div class="col-md-6"><label class="form-label">Leads Generated</label><input type="number" class="form-control" id="leads" placeholder="e.g. 150" value="0"></div>
  <div class="col-md-6"><label class="form-label">Average Lead Value ($)</label><input type="number" class="form-control" id="leadValue" placeholder="e.g. 50" value="0"></div>
  <div class="col-md-6"><label class="form-label">Cost per Lead Goal ($)</label><input type="number" class="form-control" id="cplGoal" placeholder="e.g. 20" value="20"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate ROI</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Social Media ROI</div><div class="result-value" id="roi">-</div></div>
    <div class="col-6"><div class="result-label">Net Profit</div><div class="result-value" id="profit">-</div></div>
    <div class="col-6"><div class="result-label">Cost Per Lead</div><div class="result-value" id="cpl">-</div></div>
    <div class="col-6"><div class="result-label">ROAS</div><div class="result-value" id="roas">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var spend=parseFloat(document.getElementById('spend').value)||1;
  var rev=parseFloat(document.getElementById('revenue').value)||0;
  var leads=parseFloat(document.getElementById('leads').value)||0;
  var lv=parseFloat(document.getElementById('leadValue').value)||0;
  var totalRevenue=rev+(leads*lv);
  var profit=totalRevenue-spend;
  var roi=((profit/spend)*100).toFixed(1);
  var cpl=leads>0?(spend/leads).toFixed(2):'N/A';
  var roas=(totalRevenue/spend).toFixed(2);
  document.getElementById('roi').textContent=roi+'%';
  document.getElementById('profit').textContent='$'+profit.toLocaleString();
  document.getElementById('cpl').textContent=cpl==='N/A'?'N/A':'$'+cpl;
  document.getElementById('roas').textContent=roas+'x';
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("website-traffic-to-revenue-calculator.html",
"Website Traffic to Revenue Calculator",
"Calculate how much revenue your website traffic can generate. Estimate income from AdSense, affiliate links, products, and leads.",
"website traffic to revenue calculator, blog income calculator, website monetization calculator, how much does a website make, traffic to money calculator",
"&#128200;","#10b981","#3b82f6","social","&#128200;","Monetization",
"""<div class="calc-box">
<h2 class="calc-title">&#128200; Website Traffic to Revenue Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Monthly Page Views</label><input type="number" class="form-control" id="pv" placeholder="e.g. 50000"></div>
  <div class="col-md-6"><label class="form-label">AdSense RPM ($)</label><input type="number" class="form-control" id="rpm" placeholder="e.g. 3" value="3" step="0.5"></div>
  <div class="col-md-6"><label class="form-label">Affiliate CTR (%)</label><input type="number" class="form-control" id="affCTR" placeholder="e.g. 3" value="3" step="0.1"></div>
  <div class="col-md-6"><label class="form-label">Affiliate Monthly Income ($)</label><input type="number" class="form-control" id="affIncome" placeholder="e.g. 200" value="0"></div>
  <div class="col-md-6"><label class="form-label">Product/Service Sales/Month</label><input type="number" class="form-control" id="sales" placeholder="e.g. 5" value="0"></div>
  <div class="col-md-6"><label class="form-label">Average Product Price ($)</label><input type="number" class="form-control" id="price" placeholder="e.g. 50" value="0"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate Revenue</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">AdSense Income</div><div class="result-value" id="adsense">-</div></div>
    <div class="col-6"><div class="result-label">Affiliate Income</div><div class="result-value" id="affiliate">-</div></div>
    <div class="col-6"><div class="result-label">Product Income</div><div class="result-value" id="product">-</div></div>
    <div class="col-6"><div class="result-label">Total Monthly Revenue</div><div class="result-value" id="total">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var pv=parseFloat(document.getElementById('pv').value)||0;
  var rpm=parseFloat(document.getElementById('rpm').value)||3;
  var affInc=parseFloat(document.getElementById('affIncome').value)||0;
  var sales=parseFloat(document.getElementById('sales').value)||0;
  var price=parseFloat(document.getElementById('price').value)||0;
  var adsense=(pv/1000)*rpm;
  var product=sales*price;
  var total=adsense+affInc+product;
  document.getElementById('adsense').textContent='$'+adsense.toFixed(2);
  document.getElementById('affiliate').textContent='$'+affInc.toFixed(2);
  document.getElementById('product').textContent='$'+product.toFixed(2);
  document.getElementById('total').textContent='$'+total.toFixed(2);
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("follower-to-income-calculator.html",
"Follower to Income Calculator",
"Convert your social media followers to estimated income potential. Calculate how much your follower count is worth across all platforms.",
"follower to income calculator, how much is my instagram worth, social media followers money, follower count value calculator, influencer income calculator",
"&#128176;","#f59e0b","#ef4444","social","&#128176;","Monetization",
"""<div class="calc-box">
<h2 class="calc-title">&#128176; Follower to Income Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Instagram Followers</label><input type="number" class="form-control" id="igFollowers" placeholder="e.g. 25000" value="0"></div>
  <div class="col-md-6"><label class="form-label">YouTube Subscribers</label><input type="number" class="form-control" id="ytSubs" placeholder="e.g. 10000" value="0"></div>
  <div class="col-md-6"><label class="form-label">TikTok Followers</label><input type="number" class="form-control" id="ttFollowers" placeholder="e.g. 50000" value="0"></div>
  <div class="col-md-6"><label class="form-label">Twitter/X Followers</label><input type="number" class="form-control" id="twFollowers" placeholder="e.g. 5000" value="0"></div>
  <div class="col-md-6"><label class="form-label">Average Engagement Rate (%)</label><input type="number" class="form-control" id="eng" placeholder="e.g. 4" step="0.1" value="4"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate Income Potential</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Instagram Value</div><div class="result-value" id="igVal">-</div></div>
    <div class="col-6"><div class="result-label">YouTube Value</div><div class="result-value" id="ytVal">-</div></div>
    <div class="col-6"><div class="result-label">TikTok Value</div><div class="result-value" id="ttVal">-</div></div>
    <div class="col-6"><div class="result-label">Total Monthly Potential</div><div class="result-value" id="total">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var ig=parseFloat(document.getElementById('igFollowers').value)||0;
  var yt=parseFloat(document.getElementById('ytSubs').value)||0;
  var tt=parseFloat(document.getElementById('ttFollowers').value)||0;
  var tw=parseFloat(document.getElementById('twFollowers').value)||0;
  var eng=parseFloat(document.getElementById('eng').value)||4;
  var engMult=1+(eng-3)*0.05;
  var igVal=(ig/1000)*12*engMult;
  var ytVal=(yt/1000)*25*engMult;
  var ttVal=(tt/1000)*8*engMult;
  var twVal=(tw/1000)*3*engMult;
  var total=igVal+ytVal+ttVal+twVal;
  document.getElementById('igVal').textContent='$'+Math.round(igVal).toLocaleString();
  document.getElementById('ytVal').textContent='$'+Math.round(ytVal).toLocaleString();
  document.getElementById('ttVal').textContent='$'+Math.round(ttVal).toLocaleString();
  document.getElementById('total').textContent='$'+Math.round(total).toLocaleString()+'/mo';
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("micro-influencer-rate-calculator.html",
"Micro Influencer Rate Calculator",
"Calculate the right rate for micro-influencers (1K-100K followers). Get fair pricing for sponsored posts based on engagement and niche.",
"micro influencer rate calculator, nano influencer pricing, small influencer rates, how much micro influencer charge, influencer pricing 1000 followers",
"&#128247;","#ec4899","#f43f5e","social","&#128247;","Social Media",
"""<div class="calc-box">
<h2 class="calc-title">&#128247; Micro Influencer Rate Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Followers (1K - 100K)</label><input type="number" class="form-control" id="followers" placeholder="e.g. 15000" min="100" max="100000"></div>
  <div class="col-md-6"><label class="form-label">Engagement Rate (%)</label><input type="number" class="form-control" id="eng" placeholder="e.g. 6" step="0.1"></div>
  <div class="col-md-6"><label class="form-label">Audience Quality</label>
    <select class="form-control" id="quality">
      <option value="1.5">Highly targeted niche audience</option>
      <option value="1.2" selected>Mixed engaged audience</option>
      <option value="0.8">General audience</option>
    </select>
  </div>
  <div class="col-md-6"><label class="form-label">Content Format</label>
    <select class="form-control" id="format">
      <option value="1.0">Static Feed Post</option>
      <option value="1.4">Reel / Short Video</option>
      <option value="0.5">Story (24 hrs)</option>
      <option value="2.0">YouTube Dedicated Video</option>
    </select>
  </div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Get Micro Influencer Rate</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Your Rate Per Post</div><div class="result-value" id="rate">-</div></div>
    <div class="col-6"><div class="result-label">Range</div><div class="result-value" id="range">-</div></div>
    <div class="col-6"><div class="result-label">Per 1000 Followers</div><div class="result-value" id="per1k">-</div></div>
    <div class="col-6"><div class="result-label">Why You're Valuable</div><div class="result-value" id="why">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var f=parseFloat(document.getElementById('followers').value)||0;
  var eng=parseFloat(document.getElementById('eng').value)||3;
  var q=parseFloat(document.getElementById('quality').value)||1;
  var fmt=parseFloat(document.getElementById('format').value)||1;
  var base=(f/1000)*10*q*fmt*(1+(eng-2)*0.07);
  var per1k=((base/f)*1000).toFixed(2);
  var why=eng>6?'High engagement!':eng>4?'Above avg eng.':'Solid reach';
  document.getElementById('rate').textContent='$'+Math.round(base).toLocaleString();
  document.getElementById('range').textContent='$'+Math.round(base*0.7)+'-$'+Math.round(base*1.5);
  document.getElementById('per1k').textContent='$'+per1k;
  document.getElementById('why').textContent=why;
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("virality-score-calculator.html",
"Virality Score Calculator",
"Calculate the virality score of any social media post. Measure viral coefficient, sharing rate, and overall viral potential across platforms.",
"virality score calculator, viral coefficient calculator, social media viral score, how to measure virality, viral potential calculator",
"&#128293;","#ff6b35","#ff0050","social","&#128247;","Social Media",
"""<div class="calc-box">
<h2 class="calc-title">&#128293; Virality Score Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Total Views / Reach</label><input type="number" class="form-control" id="reach" placeholder="e.g. 100000"></div>
  <div class="col-md-6"><label class="form-label">Total Shares / Retweets</label><input type="number" class="form-control" id="shares" placeholder="e.g. 5000"></div>
  <div class="col-md-6"><label class="form-label">Total Likes</label><input type="number" class="form-control" id="likes" placeholder="e.g. 15000"></div>
  <div class="col-md-6"><label class="form-label">Total Comments</label><input type="number" class="form-control" id="comments" placeholder="e.g. 800"></div>
  <div class="col-md-6"><label class="form-label">Your Followers at Posting</label><input type="number" class="form-control" id="followers" placeholder="e.g. 10000"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate Virality Score</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Virality Score</div><div class="result-value" id="score">-</div></div>
    <div class="col-6"><div class="result-label">Viral Status</div><div class="result-value" id="status">-</div></div>
    <div class="col-6"><div class="result-label">Viral Coefficient</div><div class="result-value" id="vc">-</div></div>
    <div class="col-6"><div class="result-label">Share Rate</div><div class="result-value" id="shareRate">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var reach=parseFloat(document.getElementById('reach').value)||1;
  var shares=parseFloat(document.getElementById('shares').value)||0;
  var likes=parseFloat(document.getElementById('likes').value)||0;
  var comments=parseFloat(document.getElementById('comments').value)||0;
  var followers=parseFloat(document.getElementById('followers').value)||1;
  var shareRate=(shares/reach)*100;
  var engRate=((likes+comments+shares)/reach)*100;
  var vfRatio=reach/followers;
  var vc=(shares*2/reach).toFixed(3);
  var score=Math.min(100,Math.round(shareRate*3+engRate*1.5+(vfRatio>1?(vfRatio*5):0)));
  var status=score<15?'Normal':score<30?'Trending':score<60?'Viral':'Mega Viral';
  document.getElementById('score').textContent=score+'/100';
  document.getElementById('status').textContent=status;
  document.getElementById('vc').textContent=vc;
  document.getElementById('shareRate').textContent=shareRate.toFixed(2)+'%';
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("follower-to-engagement-ratio-calculator.html",
"Follower to Engagement Ratio Calculator",
"Calculate your follower-to-engagement ratio across social media platforms. Identify ghost followers and measure true audience quality.",
"follower engagement ratio calculator, ghost followers detector, real engagement calculator, follower quality score, authentic engagement rate",
"&#128290;","#6366f1","#4f46e5","social","&#128247;","Social Media",
"""<div class="calc-box">
<h2 class="calc-title">&#128290; Follower to Engagement Ratio Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Total Followers</label><input type="number" class="form-control" id="followers" placeholder="e.g. 10000"></div>
  <div class="col-md-6"><label class="form-label">Avg Likes per Post</label><input type="number" class="form-control" id="likes" placeholder="e.g. 300"></div>
  <div class="col-md-6"><label class="form-label">Avg Comments per Post</label><input type="number" class="form-control" id="comments" placeholder="e.g. 25"></div>
  <div class="col-md-6"><label class="form-label">Platform</label>
    <select class="form-control" id="platform">
      <option value="4">Instagram (avg 3-6%)</option>
      <option value="2">Twitter/X (avg 0.5-2%)</option>
      <option value="6">TikTok (avg 5-8%)</option>
      <option value="1.5">LinkedIn (avg 1-2%)</option>
      <option value="3">Facebook (avg 1-4%)</option>
    </select>
  </div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Analyze Ratio</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Engagement Ratio</div><div class="result-value" id="ratio">-</div></div>
    <div class="col-6"><div class="result-label">Audience Quality</div><div class="result-value" id="quality">-</div></div>
    <div class="col-6"><div class="result-label">Est. Ghost Followers</div><div class="result-value" id="ghost">-</div></div>
    <div class="col-6"><div class="result-label">vs Platform Avg</div><div class="result-value" id="vsPlatform">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var f=parseFloat(document.getElementById('followers').value)||1;
  var l=parseFloat(document.getElementById('likes').value)||0;
  var c=parseFloat(document.getElementById('comments').value)||0;
  var avg=parseFloat(document.getElementById('platform').value)||4;
  var er=((l+c)/f)*100;
  var quality=er>=avg*1.5?'Excellent':er>=avg?'Good':er>=avg*0.5?'Average':'Poor (ghost followers suspected)';
  var ghost=er<avg*0.5?Math.round(f*(1-er/(avg*0.5))*.5):0;
  var comp=er>=avg?'+'+(er-avg).toFixed(1)+'% above avg':(avg-er).toFixed(1)+'% below avg';
  document.getElementById('ratio').textContent=er.toFixed(2)+'%';
  document.getElementById('quality').textContent=quality;
  document.getElementById('ghost').textContent=ghost>0?'~'+ghost.toLocaleString():'Low risk';
  document.getElementById('vsPlatform').textContent=comp;
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("content-performance-score-calculator.html",
"Content Performance Score Calculator",
"Calculate an overall performance score for any piece of content. Score posts based on reach, engagement, conversions, and audience sentiment.",
"content performance score calculator, content analytics score, social media post score, content marketing KPIs, post performance analyzer",
"&#128202;","#8b5cf6","#6366f1","social","&#128247;","Social Media",
"""<div class="calc-box">
<h2 class="calc-title">&#128202; Content Performance Score Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Reach / Views</label><input type="number" class="form-control" id="reach" placeholder="e.g. 25000"></div>
  <div class="col-md-6"><label class="form-label">Target Reach Goal</label><input type="number" class="form-control" id="goal" placeholder="e.g. 20000"></div>
  <div class="col-md-6"><label class="form-label">Engagement Rate (%)</label><input type="number" class="form-control" id="er" placeholder="e.g. 4.5" step="0.1"></div>
  <div class="col-md-6"><label class="form-label">Conversions / Clicks</label><input type="number" class="form-control" id="conv" placeholder="e.g. 150" value="0"></div>
  <div class="col-md-6"><label class="form-label">Shares</label><input type="number" class="form-control" id="shares" placeholder="e.g. 200" value="0"></div>
  <div class="col-md-6"><label class="form-label">Positive Comments (%)</label><input type="number" class="form-control" id="sentiment" placeholder="e.g. 85" value="80"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Score Content</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Performance Score</div><div class="result-value" id="score">-</div></div>
    <div class="col-6"><div class="result-label">Grade</div><div class="result-value" id="grade">-</div></div>
    <div class="col-6"><div class="result-label">Reach vs Goal</div><div class="result-value" id="reachVsGoal">-</div></div>
    <div class="col-6"><div class="result-label">Content Health</div><div class="result-value" id="health">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var reach=parseFloat(document.getElementById('reach').value)||0;
  var goal=parseFloat(document.getElementById('goal').value)||1;
  var er=parseFloat(document.getElementById('er').value)||0;
  var conv=parseFloat(document.getElementById('conv').value)||0;
  var shares=parseFloat(document.getElementById('shares').value)||0;
  var sent=parseFloat(document.getElementById('sentiment').value)||80;
  var reachScore=Math.min(25,(reach/goal)*25);
  var erScore=Math.min(25,(er/5)*25);
  var convScore=Math.min(25,(conv/100)*25);
  var shareScore=Math.min(15,(shares/500)*15);
  var sentScore=(sent/100)*10;
  var total=Math.round(reachScore+erScore+convScore+shareScore+sentScore);
  var grade=total>=85?'A+':total>=75?'A':total>=65?'B':total>=50?'C':'D';
  var rvg=reach>=goal?'Goal Met!':((reach/goal)*100).toFixed(0)+'% of goal';
  var health=total>=70?'Healthy':'Needs Work';
  document.getElementById('score').textContent=total+'/100';
  document.getElementById('grade').textContent=grade;
  document.getElementById('reachVsGoal').textContent=rvg;
  document.getElementById('health').textContent=health;
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("post-frequency-impact-calculator.html",
"Post Frequency Impact Calculator",
"Calculate the optimal posting frequency for your social media accounts. Find how post frequency affects reach, engagement, and follower growth.",
"post frequency calculator, how often to post on instagram, optimal posting frequency, social media posting schedule, content frequency impact",
"&#128197;","#f59e0b","#ef4444","social","&#128247;","Social Media",
"""<div class="calc-box">
<h2 class="calc-title">&#128197; Post Frequency Impact Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Current Posts per Week</label><input type="number" class="form-control" id="curFreq" placeholder="e.g. 3" step="0.5"></div>
  <div class="col-md-6"><label class="form-label">Current Monthly Follower Growth</label><input type="number" class="form-control" id="curGrowth" placeholder="e.g. 500"></div>
  <div class="col-md-6"><label class="form-label">Planned Posts per Week</label><input type="number" class="form-control" id="newFreq" placeholder="e.g. 7" step="0.5"></div>
  <div class="col-md-6"><label class="form-label">Current Followers</label><input type="number" class="form-control" id="followers" placeholder="e.g. 5000"></div>
  <div class="col-md-6"><label class="form-label">Platform</label>
    <select class="form-control" id="platform">
      <option value="1.1">Instagram (3-7 posts/week ideal)</option>
      <option value="1.3">TikTok (1-3 posts/day ideal)</option>
      <option value="1.2">YouTube (1-3 videos/week ideal)</option>
      <option value="1.4">Twitter/X (3-10 tweets/day)</option>
      <option value="1.0">LinkedIn (3-5 posts/week ideal)</option>
    </select>
  </div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate Impact</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Projected Growth Increase</div><div class="result-value" id="growthInc">-</div></div>
    <div class="col-6"><div class="result-label">New Monthly Growth</div><div class="result-value" id="newGrowth">-</div></div>
    <div class="col-6"><div class="result-label">Content Needed/Month</div><div class="result-value" id="content">-</div></div>
    <div class="col-6"><div class="result-label">6-Month Projection</div><div class="result-value" id="sixMonth">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var cf=parseFloat(document.getElementById('curFreq').value)||1;
  var cg=parseFloat(document.getElementById('curGrowth').value)||0;
  var nf=parseFloat(document.getElementById('newFreq').value)||1;
  var followers=parseFloat(document.getElementById('followers').value)||0;
  var platform=parseFloat(document.getElementById('platform').value)||1;
  var freqRatio=nf/cf;
  var newGrowth=Math.round(cg*Math.pow(freqRatio,0.6)*platform);
  var growthInc=((newGrowth-cg)/cg*100).toFixed(0);
  var content=Math.round(nf*4.3);
  var sixMonth=Math.round(followers+newGrowth*6);
  document.getElementById('growthInc').textContent=(growthInc>0?'+':'')+growthInc+'%';
  document.getElementById('newGrowth').textContent='+'+newGrowth.toLocaleString()+'/mo';
  document.getElementById('content').textContent=content+' posts';
  document.getElementById('sixMonth').textContent=sixMonth.toLocaleString();
  document.getElementById('resultBox').style.display='block';
}
</script>""")


# ─────────────────────────────────────────────────────────
# AI / MODERN CALCULATORS
# ─────────────────────────────────────────────────────────

page("ai-token-cost-calculator.html",
"AI Token Cost Calculator",
"Calculate the cost of AI API tokens for ChatGPT, Claude, Gemini, and other LLMs. Estimate monthly AI spending based on usage.",
"AI token cost calculator, ChatGPT API cost calculator, OpenAI token price, Claude API cost, LLM token calculator, AI API pricing 2025",
"&#129302;","#10b981","#3b82f6","social","&#129302;","AI Tools",
"""<div class="calc-box">
<h2 class="calc-title">&#129302; AI Token Cost Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">AI Model</label>
    <select class="form-control" id="model" onchange="updatePrices()">
      <option value="0.005,0.015">GPT-4o ($5/M input, $15/M output)</option>
      <option value="0.00015,0.0006">GPT-4o mini ($0.15/M input, $0.6/M output)</option>
      <option value="0.003,0.015">Claude 3.5 Sonnet ($3/M input, $15/M output)</option>
      <option value="0.00025,0.00125">Claude 3 Haiku ($0.25/M in, $1.25/M out)</option>
      <option value="0.00035,0.00105">Gemini 1.5 Flash ($0.35/M in, $1.05/M out)</option>
      <option value="0.0035,0.0105">Gemini 1.5 Pro ($3.5/M in, $10.5/M out)</option>
      <option value="custom,custom">Custom pricing</option>
    </select>
  </div>
  <div class="col-md-6"><label class="form-label">Daily API Requests</label><input type="number" class="form-control" id="requests" placeholder="e.g. 1000"></div>
  <div class="col-md-6"><label class="form-label">Avg Input Tokens per Request</label><input type="number" class="form-control" id="inputTokens" placeholder="e.g. 500" value="500"></div>
  <div class="col-md-6"><label class="form-label">Avg Output Tokens per Request</label><input type="number" class="form-control" id="outputTokens" placeholder="e.g. 200" value="200"></div>
  <div class="col-md-6"><label class="form-label">Custom Input Price (per 1M tokens $)</label><input type="number" class="form-control" id="customInput" placeholder="e.g. 5.00" step="0.001" value="0"></div>
  <div class="col-md-6"><label class="form-label">Custom Output Price (per 1M tokens $)</label><input type="number" class="form-control" id="customOutput" placeholder="e.g. 15.00" step="0.001" value="0"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate AI Cost</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">Daily Cost</div><div class="result-value" id="daily">-</div></div>
    <div class="col-6"><div class="result-label">Monthly Cost</div><div class="result-value" id="monthly">-</div></div>
    <div class="col-6"><div class="result-label">Cost per Request</div><div class="result-value" id="perReq">-</div></div>
    <div class="col-6"><div class="result-label">Annual Cost</div><div class="result-value" id="annual">-</div></div>
  </div>
</div>
</div>
<div class="calc-box mt-3">
<h3 style="font-size:1rem;font-weight:700">&#128161; Token Usage Tips</h3>
<ul style="font-size:0.85rem;color:var(--text-secondary)">
<li>1 token &#8776; 4 characters or 0.75 words in English</li>
<li>1,000 tokens &#8776; 750 words or ~1.5 pages of text</li>
<li>Use smaller models for simple tasks to reduce costs by 90%+</li>
<li>Implement caching for repeated prompts to save significantly</li>
</ul>
</div>""",
"""<script>
function updatePrices(){
  var val=document.getElementById('model').value;
  var parts=val.split(',');
  if(parts[0]!='custom'){
    document.getElementById('customInput').value=parts[0];
    document.getElementById('customOutput').value=parts[1];
  }
}
updatePrices();
function calc(){
  var req=parseFloat(document.getElementById('requests').value)||0;
  var inp=parseFloat(document.getElementById('inputTokens').value)||500;
  var out=parseFloat(document.getElementById('outputTokens').value)||200;
  var inPrice=parseFloat(document.getElementById('customInput').value)||0;
  var outPrice=parseFloat(document.getElementById('customOutput').value)||0;
  var dailyInput=(req*inp/1000000)*inPrice;
  var dailyOutput=(req*out/1000000)*outPrice;
  var daily=dailyInput+dailyOutput;
  var perReq=req>0?(daily/req).toFixed(5):0;
  document.getElementById('daily').textContent='$'+daily.toFixed(4);
  document.getElementById('monthly').textContent='$'+(daily*30).toFixed(2);
  document.getElementById('perReq').textContent='$'+perReq;
  document.getElementById('annual').textContent='$'+(daily*365).toFixed(0).replace(/\B(?=(\d{3})+(?!\d))/g,',');
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("api-cost-calculator.html",
"API Cost Calculator",
"Calculate the total monthly cost of API calls for your application. Compare API pricing tiers and estimate costs as you scale.",
"API cost calculator, API pricing calculator, monthly API cost, REST API cost estimator, API usage cost, SaaS API pricing",
"&#128187;","#3b82f6","#1d4ed8","social","&#129302;","AI Tools",
"""<div class="calc-box">
<h2 class="calc-title">&#128187; API Cost Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">API Service</label>
    <select class="form-control" id="service">
      <option value="custom">Custom API</option>
      <option value="openai">OpenAI API</option>
      <option value="google">Google Maps/Cloud API</option>
      <option value="twilio">Twilio SMS/Voice API</option>
      <option value="stripe">Stripe Payments API</option>
    </select>
  </div>
  <div class="col-md-6"><label class="form-label">Monthly API Calls</label><input type="number" class="form-control" id="calls" placeholder="e.g. 100000"></div>
  <div class="col-md-6"><label class="form-label">Cost per 1000 API Calls ($)</label><input type="number" class="form-control" id="costPer1k" placeholder="e.g. 2.00" step="0.001" value="2"></div>
  <div class="col-md-6"><label class="form-label">Free Tier Calls/Month</label><input type="number" class="form-control" id="freeTier" placeholder="e.g. 10000" value="0"></div>
  <div class="col-md-6"><label class="form-label">Data Transfer per Call (KB)</label><input type="number" class="form-control" id="dataKB" placeholder="e.g. 5" value="1" step="0.1"></div>
  <div class="col-md-6"><label class="form-label">Data Cost per GB ($)</label><input type="number" class="form-control" id="dataCost" placeholder="e.g. 0.09" value="0.09" step="0.01"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate API Cost</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">API Call Cost</div><div class="result-value" id="callCost">-</div></div>
    <div class="col-6"><div class="result-label">Data Transfer Cost</div><div class="result-value" id="dataCostTotal">-</div></div>
    <div class="col-6"><div class="result-label">Total Monthly Cost</div><div class="result-value" id="total">-</div></div>
    <div class="col-6"><div class="result-label">Annual Cost</div><div class="result-value" id="annual">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var calls=parseFloat(document.getElementById('calls').value)||0;
  var costPer1k=parseFloat(document.getElementById('costPer1k').value)||0;
  var free=parseFloat(document.getElementById('freeTier').value)||0;
  var dataKB=parseFloat(document.getElementById('dataKB').value)||1;
  var dataCostPerGB=parseFloat(document.getElementById('dataCost').value)||0.09;
  var billableCalls=Math.max(0,calls-free);
  var callCost=(billableCalls/1000)*costPer1k;
  var totalDataGB=(calls*dataKB)/(1024*1024);
  var dataTotal=totalDataGB*dataCostPerGB;
  var total=callCost+dataTotal;
  document.getElementById('callCost').textContent='$'+callCost.toFixed(2);
  document.getElementById('dataCostTotal').textContent='$'+dataTotal.toFixed(4);
  document.getElementById('total').textContent='$'+total.toFixed(2);
  document.getElementById('annual').textContent='$'+(total*12).toFixed(0).replace(/\B(?=(\d{3})+(?!\d))/g,',');
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("saas-pricing-calculator.html",
"SaaS Pricing Calculator",
"Calculate the right pricing for your SaaS product. Determine MRR, ARR, customer acquisition costs, and optimal subscription tiers.",
"SaaS pricing calculator, subscription pricing model, MRR ARR calculator, SaaS revenue calculator, software pricing strategy, SaaS metrics",
"&#128200;","#6366f1","#8b5cf6","social","&#129302;","AI Tools",
"""<div class="calc-box">
<h2 class="calc-title">&#128200; SaaS Pricing Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Monthly Subscription Price ($)</label><input type="number" class="form-control" id="price" placeholder="e.g. 49" step="0.01"></div>
  <div class="col-md-6"><label class="form-label">Current Paying Customers</label><input type="number" class="form-control" id="customers" placeholder="e.g. 200"></div>
  <div class="col-md-6"><label class="form-label">Monthly Churn Rate (%)</label><input type="number" class="form-control" id="churn" placeholder="e.g. 3" step="0.1" value="3"></div>
  <div class="col-md-6"><label class="form-label">New Customers per Month</label><input type="number" class="form-control" id="newCust" placeholder="e.g. 20"></div>
  <div class="col-md-6"><label class="form-label">Customer Acquisition Cost ($)</label><input type="number" class="form-control" id="cac" placeholder="e.g. 150" value="0"></div>
  <div class="col-md-6"><label class="form-label">Monthly Operational Cost ($)</label><input type="number" class="form-control" id="opCost" placeholder="e.g. 2000" value="0"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate SaaS Metrics</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">MRR (Monthly Recurring Revenue)</div><div class="result-value" id="mrr">-</div></div>
    <div class="col-6"><div class="result-label">ARR (Annual Recurring Revenue)</div><div class="result-value" id="arr">-</div></div>
    <div class="col-6"><div class="result-label">Customer LTV</div><div class="result-value" id="ltv">-</div></div>
    <div class="col-6"><div class="result-label">LTV:CAC Ratio</div><div class="result-value" id="ltvCac">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var price=parseFloat(document.getElementById('price').value)||0;
  var customers=parseFloat(document.getElementById('customers').value)||0;
  var churn=parseFloat(document.getElementById('churn').value)||3;
  var newCust=parseFloat(document.getElementById('newCust').value)||0;
  var cac=parseFloat(document.getElementById('cac').value)||0;
  var opCost=parseFloat(document.getElementById('opCost').value)||0;
  var mrr=price*customers;
  var arr=mrr*12;
  var ltv=churn>0?(price/(churn/100)).toFixed(0):0;
  var ltvCac=cac>0?(ltv/cac).toFixed(1):'N/A';
  document.getElementById('mrr').textContent='$'+mrr.toLocaleString();
  document.getElementById('arr').textContent='$'+arr.toLocaleString();
  document.getElementById('ltv').textContent='$'+parseFloat(ltv).toLocaleString();
  document.getElementById('ltvCac').textContent=ltvCac+(ltvCac!=='N/A'?'x':'');
  document.getElementById('resultBox').style.display='block';
}
</script>""")


page("content-generation-cost-calculator.html",
"Content Generation Cost Calculator",
"Calculate the cost of AI-generated content vs human writers. Compare costs for blog posts, social media, scripts, and SEO content.",
"content generation cost calculator, AI content cost vs human, content writing cost, blog post cost calculator, AI vs human writer cost, content marketing budget",
"&#128221;","#10b981","#059669","social","&#129302;","AI Tools",
"""<div class="calc-box">
<h2 class="calc-title">&#128221; Content Generation Cost Calculator</h2>
<div class="row g-3">
  <div class="col-md-6"><label class="form-label">Content Type</label>
    <select class="form-control" id="contentType">
      <option value="1000,0.02,50">Blog Post (1000 words)</option>
      <option value="2500,0.04,150">Long-form Article (2500 words)</option>
      <option value="200,0.004,15">Social Media Post</option>
      <option value="500,0.01,35">Email Newsletter</option>
      <option value="800,0.015,60">Product Description (10 items)</option>
      <option value="1500,0.03,80">Landing Page Copy</option>
    </select>
  </div>
  <div class="col-md-6"><label class="form-label">Pieces per Month</label><input type="number" class="form-control" id="pieces" placeholder="e.g. 10" value="10"></div>
  <div class="col-md-6"><label class="form-label">AI Model Used</label>
    <select class="form-control" id="aiModel">
      <option value="0.00015">GPT-4o mini (budget)</option>
      <option value="0.005" selected>GPT-4o (standard)</option>
      <option value="0.003">Claude 3.5 Sonnet</option>
      <option value="0.00035">Gemini 1.5 Flash</option>
    </select>
  </div>
  <div class="col-md-6"><label class="form-label">Human Writer Rate ($/word)</label><input type="number" class="form-control" id="humanRate" placeholder="e.g. 0.10" value="0.1" step="0.01"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Compare Costs</button>
<div class="result-box" id="resultBox">
  <div class="row g-3 text-center">
    <div class="col-6"><div class="result-label">AI Content Cost/Month</div><div class="result-value" id="aiCost">-</div></div>
    <div class="col-6"><div class="result-label">Human Writer Cost/Month</div><div class="result-value" id="humanCost">-</div></div>
    <div class="col-6"><div class="result-label">Monthly Savings with AI</div><div class="result-value" id="savings">-</div></div>
    <div class="col-6"><div class="result-label">Savings Percentage</div><div class="result-value" id="savingsPct">-</div></div>
  </div>
</div>
</div>""",
"""<script>
function calc(){
  var ct=document.getElementById('contentType').value.split(',');
  var words=parseFloat(ct[0]);
  var pieces=parseFloat(document.getElementById('pieces').value)||10;
  var aiPrice=parseFloat(document.getElementById('aiModel').value)||0.005;
  var humanRate=parseFloat(document.getElementById('humanRate').value)||0.1;
  var totalWords=words*pieces;
  var aiCost=(totalWords/1000)*aiPrice*1.3;
  var humanCost=totalWords*humanRate;
  var savings=humanCost-aiCost;
  var savingsPct=((savings/humanCost)*100).toFixed(1);
  document.getElementById('aiCost').textContent='$'+aiCost.toFixed(2);
  document.getElementById('humanCost').textContent='$'+humanCost.toFixed(2);
  document.getElementById('savings').textContent='$'+savings.toFixed(2);
  document.getElementById('savingsPct').textContent=savingsPct+'%';
  document.getElementById('resultBox').style.display='block';
}
</script>""")


print("\n=== All Social/Creator/AI Calculators Generated! ===")
