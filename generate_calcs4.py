# -*- coding: utf-8 -*-
import os

BASE = r"d:\Datomate AI Lab\CalcWebsite"

def page(filename, title, desc, keywords, icon, grad_start, grad_end, cat_url, cat_icon, cat_label, body, script=""):
    html = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | SuperCalc</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<link rel="canonical" href="https://supercalc.online/{filename}">
<meta property="og:title" content="{title} | SuperCalc">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<nav class="navbar navbar-expand-lg"><div class="container"><a class="navbar-brand" href="index.html">&#9889; Super<span>Calc</span></a><button class="navbar-toggler border-0" type="button" data-bs-toggle="collapse" data-bs-target="#nav"><span></span></button><div class="collapse navbar-collapse" id="nav"><ul class="navbar-nav me-auto ms-3"><li><a class="nav-link" href="index.html#{cat_url}">{cat_icon} {cat_label}</a></li></ul><div class="d-flex gap-2"><button class="theme-toggle" id="themeToggle"><i class="bi bi-moon-fill" id="themeIcon"></i></button></div></div></div></nav>
<div class="calc-page-header" style="background:linear-gradient(135deg,{grad_start},{grad_end})">
  <div class="container"><nav class="breadcrumb-nav"><a href="index.html">Home</a> <i class="bi bi-chevron-right"></i><span>{title}</span></nav>
  <h1 class="calc-page-title">{icon} {title}</h1>
  <p class="calc-page-subtitle">{desc}</p></div>
</div>
<div class="container my-4">
  <div class="row g-4">
    <div class="col-lg-8">{body}</div>
    <div class="col-lg-4"><div class="sidebar-ad"><span style="font-size:0.7rem;color:var(--text-muted)">Advertisement [300x250]</span></div></div>
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

def cb(title, fields, results, btn="Calculate"):
    r_html = "".join(['<div class="col-6"><div class="result-label">{0}</div><div class="result-value" id="{1}">-</div></div>'.format(r[0], r[1]) for r in results])
    return '<div class="calc-box"><h2 class="calc-title">{0}</h2>{1}<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>{2}</button><div class="result-box" id="resultBox"><div class="row g-3 text-center">{3}</div></div></div>'.format(title, fields, btn, r_html)

# Love compatibility (fixed)
page("love-compatibility-calculator.html","Love Compatibility Calculator",
"Calculate love compatibility between two people based on names and birthdates. Fun relationship compatibility quiz.",
"love compatibility calculator, relationship compatibility, couple compatibility test, love percentage, soulmate",
"&#10084;","#880e4f","#ad1457","lifestyle","&#127774;","Lifestyle",
"""<div class="calc-box">
<h2 class="calc-title">Love Compatibility Calculator</h2>
<div class="alert" style="background:rgba(233,30,99,0.1);border-left:4px solid #e91e63;padding:10px;border-radius:8px;font-size:0.85rem;margin-bottom:16px">
<strong>For Entertainment Only!</strong> This is a fun calculator, not a scientific tool.
</div>
<div class="row g-3">
<div class="col-md-6"><label class="form-label">Your Name</label><input type="text" class="form-control" id="f1" value="Alice" placeholder="Your name"></div>
<div class="col-md-6"><label class="form-label">Partner's Name</label><input type="text" class="form-control" id="f2" value="Bob" placeholder="Their name"></div>
<div class="col-md-6"><label class="form-label">Your Birthdate</label><input type="date" class="form-control" id="f3"></div>
<div class="col-md-6"><label class="form-label">Their Birthdate</label><input type="date" class="form-control" id="f4"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-heart-fill me-2"></i>Calculate Compatibility</button>
<div class="result-box" id="resultBox">
<div class="text-center">
<div style="font-size:3rem;margin-bottom:8px" id="heartIcon">&#10084;</div>
<div class="result-label">Compatibility Score</div>
<div class="result-value" id="r1" style="font-size:3rem">-</div>
<div id="r2" style="margin-top:8px;font-weight:600;color:var(--primary)"></div>
<div id="r3" style="margin-top:6px;font-size:0.9rem;color:var(--text-secondary)"></div>
</div></div></div>""",
"""<script>
document.getElementById('f3').valueAsDate=new Date('1995-01-01');
document.getElementById('f4').valueAsDate=new Date('1993-06-15');
function hashStr(s){let h=0;for(let i=0;i<s.length;i++)h=(h<<5)-h+s.charCodeAt(i);return Math.abs(h);}
function calc(){const n1=document.getElementById('f1').value,n2=document.getElementById('f2').value,d1=document.getElementById('f3').value,d2=document.getElementById('f4').value;const h=hashStr((n1+n2).toLowerCase()+(d1||'')+(d2||''));const score=50+h%51;let title,sub;if(score>=90){title='You are soulmates!';sub='Your love is written in the stars.';}else if(score>=75){title='Great compatibility!';sub='You complement each other beautifully.';}else if(score>=60){title='Good match!';sub='With effort, you can build something special.';}else if(score>=45){title='Some challenges ahead';sub='Understanding each other is key.';}else{title='Work in progress';sub='Every relationship takes dedication.';}document.getElementById('r1').textContent=score+'%';document.getElementById('r2').textContent=title;document.getElementById('r3').textContent=sub;document.getElementById('resultBox').classList.add('show');}
</script>""")

# Random password generator (fixed - no emoji surrogates)
page("random-password-generator.html","Random Password Generator",
"Generate strong, secure random passwords with custom length and character sets. Copy and use instantly.",
"random password generator, strong password generator, secure password, password creator, generate password online",
"&#128272;","#1a237e","#283593","tech","&#128187;","Tech & Dev",
"""<div class="calc-box">
<h2 class="calc-title">Password Generator</h2>
<div class="row g-3">
<div class="col-md-6"><label class="form-label">Password Length: <span id="lenShow">16</span></label>
<input type="range" class="form-range" id="plen" min="8" max="64" value="16" oninput="document.getElementById('lenShow').textContent=this.value"></div>
<div class="col-md-6"><label class="form-label">Number of Passwords</label>
<input type="number" class="form-control" id="pnum" value="5" min="1" max="20"></div>
</div>
<div class="row g-2 mt-2">
<div class="col-6 col-md-3"><div class="form-check"><input class="form-check-input" type="checkbox" id="upper" checked><label class="form-check-label" for="upper">Uppercase (A-Z)</label></div></div>
<div class="col-6 col-md-3"><div class="form-check"><input class="form-check-input" type="checkbox" id="lower" checked><label class="form-check-label" for="lower">Lowercase (a-z)</label></div></div>
<div class="col-6 col-md-3"><div class="form-check"><input class="form-check-input" type="checkbox" id="numbers" checked><label class="form-check-label" for="numbers">Numbers (0-9)</label></div></div>
<div class="col-6 col-md-3"><div class="form-check"><input class="form-check-input" type="checkbox" id="symbols"><label class="form-check-label" for="symbols">Symbols (!@#$)</label></div></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-shield-lock me-2"></i>Generate Passwords</button>
<div class="result-box" id="resultBox"><div id="pwdResults" style="font-size:0.85rem"></div></div></div>""",
"""<script>
function calc(){const len=+document.getElementById('plen').value,num=+document.getElementById('pnum').value;let chars='';if(document.getElementById('upper').checked)chars+='ABCDEFGHIJKLMNOPQRSTUVWXYZ';if(document.getElementById('lower').checked)chars+='abcdefghijklmnopqrstuvwxyz';if(document.getElementById('numbers').checked)chars+='0123456789';if(document.getElementById('symbols').checked)chars+='!@#$%^&*()_+-=[]{}|;:,.?';if(!chars)return alert('Select at least one character type');const pwds=Array.from({length:num},()=>Array.from({length:len},()=>chars[Math.floor(Math.random()*chars.length)]).join(''));const strength=chars.length>72&&len>=16?'Very Strong':chars.length>50&&len>=12?'Strong':len>=8?'Medium':'Weak';const colors={Very_Strong:'#4caf50',Strong:'#8bc34a',Medium:'#ff9800',Weak:'#f44336'};const col=colors[strength.replace(' ','_')]||'#ff9800';const rows=pwds.map((p,i)=>`<div style="display:flex;justify-content:space-between;align-items:center;padding:8px 12px;margin-bottom:6px;border-radius:8px;background:var(--card-bg);border:1px solid var(--border);font-family:monospace"><span style="word-break:break-all;font-size:0.85rem">${p}</span><button class="btn btn-sm btn-outline-secondary ms-2" onclick="navigator.clipboard.writeText(this.dataset.p)" data-p="${p}">Copy</button></div>`).join('');document.getElementById('pwdResults').innerHTML=`<div style="margin-bottom:8px">Strength: <strong style="color:${col}">${strength}</strong></div>`+rows;document.getElementById('resultBox').classList.add('show');}
</script>""")

# Remaining from batch 4
page("hash-value-calculator.html","Text Hash & Character Counter",
"Count words, characters, sentences in any text. Calculate SHA-256 hash for data integrity verification.",
"hash calculator, text hash, SHA256 calculator, word count tool, character counter, text analyzer",
"&#128196;","#0d47a1","#1565c0","tech","&#128187;","Tech & Dev",
"""<div class="calc-box">
<h2 class="calc-title">Text Analysis Tool</h2>
<div class="mb-3"><label class="form-label">Enter Text</label>
<textarea class="form-control" id="txt" rows="5" placeholder="Enter any text to analyze...">Hello, World! This is SuperCalc text analyzer. It counts words and characters.</textarea></div>
<button class="btn-calculate" onclick="calc()"><i class="bi bi-search me-2"></i>Analyze Text</button>
<div class="result-box" id="resultBox"><div id="hashResults" style="font-size:0.9rem"></div></div></div>""",
"""<script>
async function sha256(msg){const buf=await crypto.subtle.digest('SHA-256',new TextEncoder().encode(msg));return Array.from(new Uint8Array(buf)).map(b=>b.toString(16).padStart(2,'0')).join('');}
async function calc(){const t=document.getElementById('txt').value;const words=t.trim().split(/\s+/).filter(w=>w.length>0).length;const chars=t.length,nosp=t.replace(/\s/g,'').length;const hash=await sha256(t);const rows=[['Characters',chars],['Characters (no spaces)',nosp],['Words',words],['Lines',t.split('\n').length],['Sentences',t.split(/[.!?]+/).filter(s=>s.trim()).length],['Avg Word Length',words>0?(nosp/words).toFixed(1):0],['SHA-256 (first 32 chars)','<code style="font-size:0.75rem">'+hash.slice(0,32)+'...</code>']];document.getElementById('hashResults').innerHTML=rows.map(([k,v])=>`<div style="display:flex;justify-content:space-between;align-items:center;padding:6px 0;border-bottom:1px solid var(--border)"><span>${k}</span><strong>${v}</strong></div>`).join('');document.getElementById('resultBox').classList.add('show');}
</script>""")

page("property-tax-calculator.html","Property Tax Calculator",
"Calculate annual property tax from assessed value and mill rate. Find effective tax rate and monthly payment.",
"property tax calculator, real estate tax, annual property tax, mill rate calculator, assessed value tax",
"&#127968;","#37474f","#455a64","finance","&#128176;","Finance",
cb("Property Tax Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Home Market Value ($)</label><input type="number" class="form-control" id="f1" value="350000" step="5000"></div>
<div class="col-md-6"><label class="form-label">Assessment Rate (%)</label><input type="number" class="form-control" id="f2" value="85" step="1"></div>
<div class="col-md-6"><label class="form-label">Mill Rate (mills)</label><input type="number" class="form-control" id="f3" value="15" step="0.1"></div>
<div class="col-md-6"><label class="form-label">Homestead Exemption ($)</label><input type="number" class="form-control" id="f4" value="25000" step="1000"></div>
</div>""",
[("Assessed Value","r1"),("Annual Property Tax","r2"),("Monthly Payment","r3"),("Effective Tax Rate","r4")]),
"""<script>
function calc(){const m=+document.getElementById('f1').value,r=+document.getElementById('f2').value/100,mill=+document.getElementById('f3').value,ex=+document.getElementById('f4').value;const a=m*r,tax=Math.max(0,a-ex)*mill/1000;document.getElementById('r1').textContent='$'+a.toFixed(0);document.getElementById('r2').textContent='$'+tax.toFixed(0);document.getElementById('r3').textContent='$'+(tax/12).toFixed(0);document.getElementById('r4').textContent=(tax/m*100).toFixed(3)+'%';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("home-affordability-calculator.html","Home Affordability Calculator",
"Calculate how much house you can afford based on income, debts, and down payment. Uses 28/36 DTI rule.",
"home affordability calculator, how much house can I afford, mortgage affordability, maximum home price",
"&#127968;","#1a237e","#283593","finance","&#128176;","Finance",
cb("Home Affordability Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Annual Gross Income ($)</label><input type="number" class="form-control" id="f1" value="80000" step="5000"></div>
<div class="col-md-6"><label class="form-label">Monthly Debts ($)</label><input type="number" class="form-control" id="f2" value="400" step="50"></div>
<div class="col-md-6"><label class="form-label">Down Payment ($)</label><input type="number" class="form-control" id="f3" value="40000" step="5000"></div>
<div class="col-md-6"><label class="form-label">Interest Rate (%)</label><input type="number" class="form-control" id="f4" value="7" step="0.1"></div>
<div class="col-md-6"><label class="form-label">Loan Term (years)</label><input type="number" class="form-control" id="f5" value="30" step="5"></div>
</div>""",
[("Max Home Price","r1"),("Max Mortgage","r2"),("Monthly Payment (est.)","r3"),("DTI Rule Used","r4")],
"Calculate Affordability"),
"""<script>
function calc(){const inc=+document.getElementById('f1').value,debts=+document.getElementById('f2').value,dp=+document.getElementById('f3').value,rate=+document.getElementById('f4').value/100/12,n=+document.getElementById('f5').value*12;const maxPmt=Math.min(inc/12*0.28,inc/12*0.36-debts);const maxLoan=maxPmt*(Math.pow(1+rate,n)-1)/(rate*Math.pow(1+rate,n));const maxHome=maxLoan+dp;document.getElementById('r1').textContent='$'+maxHome.toFixed(0);document.getElementById('r2').textContent='$'+maxLoan.toFixed(0);document.getElementById('r3').textContent='$'+maxPmt.toFixed(0)+'/mo';document.getElementById('r4').textContent='28% front-end / 36% back-end';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("land-area-calculator.html","Land Area Calculator",
"Calculate land area in acres, square feet, square meters, and hectares. Convert between all area units.",
"land area calculator, acres to square feet, plot area calculator, land measurement, hectare to acre",
"&#127807;","#2e7d32","#388e3c","construction","&#127959;","Construction",
"""<div class="calc-box">
<h2 class="calc-title">Land Area Calculator</h2>
<div class="row g-3">
<div class="col-md-4"><label class="form-label">Length</label><input type="number" class="form-control" id="l1" value="100" step="0.1"></div>
<div class="col-md-4"><label class="form-label">Width</label><input type="number" class="form-control" id="l2" value="50" step="0.1"></div>
<div class="col-md-4"><label class="form-label">Unit</label><select class="form-select" id="lu"><option value="1">Meters</option><option value="0.3048">Feet</option><option value="0.9144">Yards</option></select></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-map me-2"></i>Calculate Area</button>
<div class="result-box" id="resultBox"><div id="areaRes" style="font-size:0.9rem"></div></div></div>""",
"""<script>
const au=[['Square Meters (m\u00B2)',1],['Square Feet',0.0929],['Square Yards',0.8361],['Acres',4046.86],['Hectares',10000],['Cents (Indian)',40.4686],['Square Km',1000000]];
function calc(){const l=+document.getElementById('l1').value,w=+document.getElementById('l2').value,u=+document.getElementById('lu').value,sqm=l*u*w*u;const rows=au.map(function(a){return '<div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid var(--border)"><span>'+a[0]+'</span><strong>'+(sqm/a[1]).toPrecision(6)+'</strong></div>';}).join('');document.getElementById('areaRes').innerHTML=rows;document.getElementById('resultBox').classList.add('show');}
</script>""")

page("net-promoter-score-calculator.html","Net Promoter Score (NPS) Calculator",
"Calculate your Net Promoter Score from customer survey responses. Identify promoters, passives, and detractors.",
"NPS calculator, net promoter score calculator, customer satisfaction score, promoter detractor, survey NPS",
"&#128200;","#1b5e20","#2e7d32","business","&#128188;","Business",
cb("NPS Calculator",
"""<div class="row g-3">
<div class="col-12"><label class="form-label" style="color:#f44336">Number of Detractors (Score 0-6)</label><input type="number" class="form-control" id="f1" value="22" min="0"></div>
<div class="col-12"><label class="form-label" style="color:#ff9800">Number of Passives (Score 7-8)</label><input type="number" class="form-control" id="f2" value="35" min="0"></div>
<div class="col-12"><label class="form-label" style="color:#4caf50">Number of Promoters (Score 9-10)</label><input type="number" class="form-control" id="f3" value="55" min="0"></div>
</div>""",
[("Net Promoter Score","r1"),("Interpretation","r2"),("Total Respondents","r3"),("Response Breakdown","r4")]),
"""<script>
function calc(){const det=+document.getElementById('f1').value,pas=+document.getElementById('f2').value,pro=+document.getElementById('f3').value;const total=det+pas+pro;if(!total)return;const nps=Math.round((pro-det)/total*100);const interp=nps<0?'Needs Improvement':nps<30?'Good':nps<70?'Great':'Excellent (World Class)';document.getElementById('r1').textContent=nps;document.getElementById('r2').textContent=interp;document.getElementById('r3').textContent=total+' responses';document.getElementById('r4').textContent='P:'+Math.round(pro/total*100)+'% Pa:'+Math.round(pas/total*100)+'% D:'+Math.round(det/total*100)+'%';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("electricity-usage-calculator.html","Electricity Usage & Bill Calculator",
"Calculate electricity consumption and monthly bill for any appliance. Compare costs and save on energy bills.",
"electricity usage calculator, power consumption calculator, electricity cost per month, kWh calculator, appliance cost",
"&#9889;","#f57f17","#f9a825","environment","&#127807;","Environment",
cb("Electricity Cost Calculator",
"""<div class="row g-3">
<div class="col-md-4"><label class="form-label">Power (Watts)</label><input type="number" class="form-control" id="f1" value="1500" step="10"></div>
<div class="col-md-4"><label class="form-label">Hours Used / Day</label><input type="number" class="form-control" id="f2" value="4" step="0.5"></div>
<div class="col-md-4"><label class="form-label">Days / Month</label><input type="number" class="form-control" id="f3" value="30" step="1"></div>
<div class="col-md-6"><label class="form-label">Electricity Rate ($/kWh)</label><input type="number" class="form-control" id="f4" value="0.13" step="0.01"></div>
<div class="col-md-6"><label class="form-label">Number of Units</label><input type="number" class="form-control" id="f5" value="1" step="1"></div>
</div>""",
[("Daily kWh","r1"),("Monthly kWh","r2"),("Monthly Cost","r3"),("Annual Cost","r4")],
"Calculate Bill"),
"""<script>
function calc(){const w=+document.getElementById('f1').value,h=+document.getElementById('f2').value,d=+document.getElementById('f3').value,rate=+document.getElementById('f4').value,n=+document.getElementById('f5').value;const daily=w/1000*h*n,monthly=daily*d,annual=monthly*12;document.getElementById('r1').textContent=daily.toFixed(3)+' kWh';document.getElementById('r2').textContent=monthly.toFixed(2)+' kWh';document.getElementById('r3').textContent='$'+(monthly*rate).toFixed(2);document.getElementById('r4').textContent='$'+(annual*rate).toFixed(2);document.getElementById('resultBox').classList.add('show');}
</script>""")

# Additional calculators for 250+
page("gpa-calculator-college.html","College GPA Calculator",
"Calculate your college GPA for current semester and cumulative GPA. Add multiple courses with different credit hours.",
"college GPA calculator, semester GPA calculator, cumulative GPA, weighted GPA, credit hours GPA",
"&#127979;","#0d47a1","#1565c0","education","&#127979;","Education",
"""<div class="calc-box">
<h2 class="calc-title">College GPA Calculator</h2>
<div id="courses">
<div class="row g-2 mb-2 align-items-end" id="c1">
<div class="col-4"><label class="form-label">Course Name</label><input type="text" class="form-control" id="cn1" value="Mathematics" placeholder="Course"></div>
<div class="col-3"><label class="form-label">Credits</label><input type="number" class="form-control" id="cc1" value="3" min="1" max="6"></div>
<div class="col-3"><label class="form-label">Grade</label>
<select class="form-select" id="cg1">
<option value="4.0">A (4.0)</option>
<option value="3.7">A- (3.7)</option>
<option value="3.3">B+ (3.3)</option>
<option value="3.0" selected>B (3.0)</option>
<option value="2.7">B- (2.7)</option>
<option value="2.3">C+ (2.3)</option>
<option value="2.0">C (2.0)</option>
<option value="1.7">C- (1.7)</option>
<option value="1.0">D (1.0)</option>
<option value="0.0">F (0.0)</option>
</select></div>
<div class="col-2 d-flex align-items-end"><button class="btn btn-outline-danger btn-sm" onclick="removeCourse(1)">X</button></div>
</div>
</div>
<button class="btn btn-outline-secondary btn-sm mt-2 mb-3" onclick="addCourse()">+ Add Course</button>
<hr>
<div class="row g-3">
<div class="col-md-6"><label class="form-label">Previous Credits Earned</label><input type="number" class="form-control" id="prevCr" value="30" step="1"></div>
<div class="col-md-6"><label class="form-label">Previous Cumulative GPA</label><input type="number" class="form-control" id="prevGpa" value="3.2" step="0.01"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-mortarboard me-2"></i>Calculate GPA</button>
<div class="result-box" id="resultBox">
<div class="row g-3 text-center">
<div class="col-6"><div class="result-label">Semester GPA</div><div class="result-value" id="r1">-</div></div>
<div class="col-6"><div class="result-label">Cumulative GPA</div><div class="result-value" id="r2">-</div></div>
<div class="col-6"><div class="result-label">Total Credits</div><div class="result-value" id="r3">-</div></div>
<div class="col-6"><div class="result-label">Honor Status</div><div class="result-value" id="r4">-</div></div>
</div></div></div>""",
"""<script>
let cc=1;
function addCourse(){cc++;document.getElementById('courses').insertAdjacentHTML('beforeend','<div class="row g-2 mb-2 align-items-end" id="c'+cc+'"><div class="col-4"><input type="text" class="form-control" id="cn'+cc+'" placeholder="Course name"></div><div class="col-3"><input type="number" class="form-control" id="cc'+cc+'" value="3" min="1"></div><div class="col-3"><select class="form-select" id="cg'+cc+'"><option value="4.0">A (4.0)</option><option value="3.7">A- (3.7)</option><option value="3.3">B+ (3.3)</option><option value="3.0" selected>B (3.0)</option><option value="2.7">B-</option><option value="2.0">C</option><option value="1.0">D</option><option value="0.0">F</option></select></div><div class="col-2 d-flex align-items-end"><button class="btn btn-outline-danger btn-sm" onclick="removeCourse('+cc+')">X</button></div></div>');}
function removeCourse(id){document.getElementById('c'+id)?.remove();}
function calc(){let pts=0,crs=0;for(let i=1;i<=cc;i++){const cr=+document.getElementById('cc'+i)?.value||0,gp=+document.getElementById('cg'+i)?.value||0;pts+=cr*gp;crs+=cr;}const semGpa=crs>0?pts/crs:0;const prevCr=+document.getElementById('prevCr').value,prevGpa=+document.getElementById('prevGpa').value;const cumGpa=(prevCr*prevGpa+pts)/(prevCr+crs);const honor=cumGpa>=3.9?'Summa Cum Laude':cumGpa>=3.7?'Magna Cum Laude':cumGpa>=3.5?'Cum Laude':cumGpa>=3.0?'Good Standing':'Standard';document.getElementById('r1').textContent=semGpa.toFixed(2);document.getElementById('r2').textContent=cumGpa.toFixed(2);document.getElementById('r3').textContent=(prevCr+crs)+' credits';document.getElementById('r4').textContent=honor;document.getElementById('resultBox').classList.add('show');}
</script>""")

page("army-body-fat-calculator.html","Military Body Fat Calculator",
"Calculate body fat percentage using US Army/Navy standards. Check if you meet military fitness requirements.",
"army body fat calculator, military body fat, US army fitness standards, navy body fat formula, military fitness",
"&#128170;","#1b5e20","#2e7d32","health","&#10084;","Health",
cb("Military Body Fat Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Service Branch</label>
<select class="form-select" id="f0">
<option value="army">US Army</option>
<option value="navy">US Navy</option>
</select></div>
<div class="col-md-6"><label class="form-label">Gender</label><select class="form-select" id="f1"><option value="m">Male</option><option value="f">Female</option></select></div>
<div class="col-md-4"><label class="form-label">Age</label><input type="number" class="form-control" id="f2" value="25" min="17" max="60"></div>
<div class="col-md-4"><label class="form-label">Height (inches)</label><input type="number" class="form-control" id="f3" value="70" step="0.5"></div>
<div class="col-md-4"><label class="form-label">Weight (lbs)</label><input type="number" class="form-control" id="f4" value="180" step="1"></div>
<div class="col-md-6"><label class="form-label">Neck (inches)</label><input type="number" class="form-control" id="f5" value="15" step="0.25"></div>
<div class="col-md-6"><label class="form-label">Waist (inches)</label><input type="number" class="form-control" id="f6" value="33" step="0.25"></div>
<div id="hipField" style="display:none" class="col-md-6"><label class="form-label">Hip (inches) - Female only</label><input type="number" class="form-control" id="f7" value="38" step="0.25"></div>
</div>""",
[("Body Fat %","r1"),("Max Allowed %","r2"),("Pass/Fail","r3"),("Category","r4")],
"Calculate"),
"""<script>
document.getElementById('f1').onchange=function(){document.getElementById('hipField').style.display=this.value==='f'?'block':'none';};
const maxBF={army:{m:{17:20,21:22,28:24,36:26,40:28},f:{17:30,21:32,28:34,36:36,40:38}},navy:{m:{17:22,21:23,28:25,36:27,40:27},f:{17:33,21:34,28:35,36:36,40:36}}};
function getMax(branch,g,age){const tbl=maxBF[branch][g];for(const[a,v] of Object.entries(tbl).reverse()){if(age>=+a)return v;}return Object.values(tbl)[0];}
function calc(){const br=document.getElementById('f0').value,g=document.getElementById('f1').value,age=+document.getElementById('f2').value,h=+document.getElementById('f3').value,w=+document.getElementById('f4').value,neck=+document.getElementById('f5').value,waist=+document.getElementById('f6').value,hip=+document.getElementById('f7').value;let bf;if(g==='m'){bf=86.010*Math.log10(waist-neck)-70.041*Math.log10(h)+36.76;}else{bf=163.205*Math.log10(waist+hip-neck)-97.684*Math.log10(h)-78.387;}const max=getMax(br,g,age);const pass=bf<=max;document.getElementById('r1').textContent=bf.toFixed(1)+'%';document.getElementById('r2').textContent=max+'%';document.getElementById('r3').textContent=pass?'PASS ✓':'FAIL ✗';document.getElementById('r4').textContent=pass?'Within Standards':'Exceeds Limit';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("macronutrient-calculator.html","Macronutrient Calculator",
"Calculate optimal daily macros: protein, carbohydrates, and fats based on your goals and calorie intake.",
"macronutrient calculator, macro calculator, daily protein carbs fat, macro ratio calculator, diet macros",
"&#129380;","#e65100","#f57c00","health","&#10084;","Health",
cb("Macronutrient Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Daily Calorie Goal</label><input type="number" class="form-control" id="f1" value="2200" step="50"></div>
<div class="col-md-6"><label class="form-label">Diet Goal</label>
<select class="form-select" id="f2">
<option value="40,30,30">Balanced (40/30/30)</option>
<option value="50,25,25">High Carb (50/25/25)</option>
<option value="30,40,30" selected>High Protein (30/40/30)</option>
<option value="10,60,30">Ketogenic (10/60/30)</option>
<option value="25,35,40">Low Carb (25/35/40)</option>
</select></div>
</div>""",
[("Daily Protein (g)","r1"),("Daily Carbs (g)","r2"),("Daily Fat (g)","r3"),("Calorie Split","r4")],
"Calculate Macros"),
"""<script>
function calc(){const cal=+document.getElementById('f1').value,split=document.getElementById('f2').value.split(',').map(Number);const [carb_pct,fat_pct,pro_pct]=split;const protein=cal*pro_pct/100/4,carbs=cal*carb_pct/100/4,fat=cal*fat_pct/100/9;document.getElementById('r1').textContent=protein.toFixed(0)+'g';document.getElementById('r2').textContent=carbs.toFixed(0)+'g';document.getElementById('r3').textContent=fat.toFixed(0)+'g';document.getElementById('r4').textContent=carb_pct+'% C / '+pro_pct+'% P / '+fat_pct+'% F';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("body-surface-area-calculator.html","Body Surface Area Calculator",
"Calculate body surface area (BSA) using Mosteller, DuBois, and Haycock formulas. Essential for medical dosing.",
"body surface area calculator, BSA calculator, Mosteller formula, DuBois formula, medical BSA, drug dosing",
"&#128138;","#4a148c","#6a1b9a","health","&#10084;","Health",
cb("Body Surface Area (BSA) Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Weight (kg)</label><input type="number" class="form-control" id="f1" value="70" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Height (cm)</label><input type="number" class="form-control" id="f2" value="175" step="1"></div>
</div>""",
[("BSA (Mosteller)","r1"),("BSA (DuBois)","r2"),("BSA (Haycock)","r3"),("BSA Category","r4")],
"Calculate BSA"),
"""<script>
function calc(){const w=+document.getElementById('f1').value,h=+document.getElementById('f2').value;const most=Math.sqrt(w*h/3600),dub=0.007184*Math.pow(h,0.725)*Math.pow(w,0.425),hay=0.024265*Math.pow(h,0.3964)*Math.pow(w,0.5378);const cat=most<1.5?'Small':most<1.9?'Average':most<2.3?'Large':'Very Large';document.getElementById('r1').textContent=most.toFixed(4)+' m\u00B2';document.getElementById('r2').textContent=dub.toFixed(4)+' m\u00B2';document.getElementById('r3').textContent=hay.toFixed(4)+' m\u00B2';document.getElementById('r4').textContent=cat;document.getElementById('resultBox').classList.add('show');}
</script>""")

page("lean-body-mass-calculator.html","Lean Body Mass Calculator",
"Calculate lean body mass (LBM) and fat-free mass using Boer, James, and Hume formulas.",
"lean body mass calculator, fat free mass, LBM calculator, muscle mass calculator, body composition",
"&#128170;","#b71c1c","#c62828","health","&#10084;","Health",
cb("Lean Body Mass Calculator",
"""<div class="row g-3">
<div class="col-md-4"><label class="form-label">Weight (kg)</label><input type="number" class="form-control" id="f1" value="75" step="0.5"></div>
<div class="col-md-4"><label class="form-label">Height (cm)</label><input type="number" class="form-control" id="f2" value="175" step="1"></div>
<div class="col-md-4"><label class="form-label">Gender</label><select class="form-select" id="f3"><option value="m">Male</option><option value="f">Female</option></select></div>
</div>""",
[("LBM (Boer formula)","r1"),("LBM (James formula)","r2"),("Fat Mass (est.)","r3"),("Body Fat % (est.)","r4")],
"Calculate LBM"),
"""<script>
function calc(){const w=+document.getElementById('f1').value,h=+document.getElementById('f2').value,g=document.getElementById('f3').value;let boer,james;if(g==='m'){boer=0.407*w+0.267*h-19.2;james=1.1*w-128*(w/h)*(w/h);}else{boer=0.252*w+0.473*h-48.3;james=1.07*w-148*(w/h)*(w/h);}const avgLbm=(boer+james)/2,fat=w-avgLbm,bf=fat/w*100;document.getElementById('r1').textContent=boer.toFixed(2)+' kg';document.getElementById('r2').textContent=james.toFixed(2)+' kg';document.getElementById('r3').textContent=fat.toFixed(2)+' kg';document.getElementById('r4').textContent=bf.toFixed(1)+'%';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("wind-chill-calculator.html","Wind Chill Calculator",
"Calculate wind chill temperature and heat index. Find the real feel temperature based on wind speed and humidity.",
"wind chill calculator, feels like temperature, wind chill formula, heat index calculator, real feel temperature",
"&#127752;","#1a237e","#283593","science","&#128301;","Science",
cb("Wind Chill & Heat Index Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Air Temperature</label><input type="number" class="form-control" id="f1" value="0" step="1"></div>
<div class="col-md-6"><label class="form-label">Temperature Unit</label><select class="form-select" id="f2"><option value="C" selected>Celsius (&#176;C)</option><option value="F">Fahrenheit (&#176;F)</option></select></div>
<div class="col-md-6"><label class="form-label">Wind Speed (km/h)</label><input type="number" class="form-control" id="f3" value="20" step="1"></div>
<div class="col-md-6"><label class="form-label">Relative Humidity (%)</label><input type="number" class="form-control" id="f4" value="50" step="5" min="0" max="100"></div>
</div>""",
[("Wind Chill","r1"),("Heat Index","r2"),("Apparent Temp","r3"),("Danger Level","r4")],
"Calculate"),
"""<script>
function calc(){let T=+document.getElementById('f1').value,v=+document.getElementById('f3').value,rh=+document.getElementById('f4').value;const unit=document.getElementById('f2').value;if(unit==='C')T=T*9/5+32;const wc=35.74+0.6215*T-35.75*Math.pow(v*0.621,0.16)+0.4275*T*Math.pow(v*0.621,0.16);const hi=-42.379+2.04901523*T+10.14333127*rh-0.22475541*T*rh-6.83783e-3*T*T-5.481717e-2*rh*rh+1.22874e-3*T*T*rh+8.5282e-4*T*rh*rh-1.99e-6*T*T*rh*rh;function toC(f){return ((f-32)*5/9).toFixed(1);}const wcC=unit==='C'?toC(wc):wc.toFixed(1),hiC=unit==='C'?toC(hi):hi.toFixed(1),appT=((+wcC + +hiC)/2).toFixed(1);const danger=+hiC>54?'Extreme Danger':+hiC>40?'Danger':+hiC>32?'Caution':'Normal';document.getElementById('r1').textContent=wcC+'&#176;'+(unit);document.getElementById('r2').textContent=hiC+'&#176;'+(unit);document.getElementById('r3').textContent=appT+'&#176;'+(unit);document.getElementById('r4').textContent=danger;document.getElementById('resultBox').classList.add('show');}
</script>""")

page("currency-inflation-calculator.html","Currency Inflation Calculator",
"Calculate the impact of inflation on purchasing power over time. See what a past amount is worth today.",
"inflation calculator, purchasing power calculator, currency inflation, what is X worth today, CPI calculator",
"&#128178;","#b71c1c","#c62828","finance","&#128176;","Finance",
cb("Inflation & Purchasing Power Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Original Amount ($)</label><input type="number" class="form-control" id="f1" value="1000" step="100"></div>
<div class="col-md-6"><label class="form-label">Annual Inflation Rate (%)</label><input type="number" class="form-control" id="f2" value="6" step="0.1"></div>
<div class="col-md-6"><label class="form-label">Number of Years</label><input type="number" class="form-control" id="f3" value="10" step="1"></div>
</div>""",
[("Future Value (same buying power)","r1"),("Purchasing Power Lost","r2"),("Real Value Today","r3"),("Loss Percentage","r4")],
"Calculate Inflation"),
"""<script>
function calc(){const P=+document.getElementById('f1').value,r=+document.getElementById('f2').value/100,n=+document.getElementById('f3').value;const fv=P*Math.pow(1+r,n),real=P/Math.pow(1+r,n),loss=P-real;document.getElementById('r1').textContent='$'+fv.toFixed(2);document.getElementById('r2').textContent='$'+loss.toFixed(2);document.getElementById('r3').textContent='$'+real.toFixed(2);document.getElementById('r4').textContent=(loss/P*100).toFixed(1)+'%';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("pace-converter-calculator.html","Running Pace Converter",
"Convert running pace between min/km and min/mile. Calculate finish times for 5K, 10K, half marathon, and marathon.",
"pace converter, min/km to min/mile, running pace calculator, race time calculator, marathon time calculator",
"&#127939;","#1b5e20","#2e7d32","health","&#10084;","Health",
"""<div class="calc-box">
<h2 class="calc-title">Pace Converter &amp; Race Calculator</h2>
<div class="row g-3">
<div class="col-md-4"><label class="form-label">Minutes</label><input type="number" class="form-control" id="pm" value="5" min="0" max="59"></div>
<div class="col-md-4"><label class="form-label">Seconds</label><input type="number" class="form-control" id="ps" value="30" min="0" max="59"></div>
<div class="col-md-4"><label class="form-label">Per Unit</label><select class="form-select" id="pu"><option value="km" selected>per km</option><option value="mi">per mile</option></select></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-stopwatch me-2"></i>Convert &amp; Calculate</button>
<div class="result-box" id="resultBox"><div id="paceResults" style="font-size:0.9rem"></div></div></div>""",
"""<script>
function fmt(s){const h=Math.floor(s/3600),m=Math.floor((s%3600)/60),sec=Math.round(s%60);return h>0?h+'h '+m+'m '+sec+'s':m+'m '+sec+'s';}
function fmtPace(s){return Math.floor(s/60)+':'+(Math.round(s%60)).toString().padStart(2,'0');}
function calc(){const m=+document.getElementById('pm').value,s=+document.getElementById('ps').value,unit=document.getElementById('pu').value;const secPerUnit=m*60+s;const secPerKm=unit==='km'?secPerUnit:secPerUnit/1.60934,secPerMi=unit==='mi'?secPerUnit:secPerUnit*1.60934;const races=[['1 mile',1609.34],['5K',5000],['10K',10000],['Half Marathon',21097.5],['Marathon',42195]];const rows=races.map(function(r){return '<div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid var(--border)"><span>'+r[0]+'</span><strong>'+fmt(r[1]/1000*secPerKm)+'</strong></div>';}).join('');document.getElementById('paceResults').innerHTML='<div style="padding:8px 0;border-bottom:1px solid var(--border);margin-bottom:8px"><strong>'+fmtPace(secPerKm)+' /km</strong> = <strong>'+fmtPace(secPerMi)+' /mile</strong></div>'+rows;document.getElementById('resultBox').classList.add('show');}
</script>""")

page("bac-calculator.html","Blood Alcohol Content (BAC) Calculator",
"Estimate Blood Alcohol Content (BAC) based on drinks consumed, weight, gender, and time. Know your limit.",
"BAC calculator, blood alcohol calculator, drunk driving limit, alcohol calculator, how many drinks to drive",
"&#127867;","#880e4f","#ad1457","health","&#10084;","Health",
cb("Blood Alcohol Content (BAC) Calculator",
"""<div class="alert" style="background:rgba(255,152,0,0.1);border-left:4px solid #ff9800;padding:12px;border-radius:8px;margin-bottom:16px;font-size:0.85rem">
<strong>Warning:</strong> This is an estimate only. Never drive if you have consumed alcohol.
</div>
<div class="row g-3">
<div class="col-md-6"><label class="form-label">Number of Drinks</label><input type="number" class="form-control" id="f1" value="3" step="0.5" min="0"></div>
<div class="col-md-6"><label class="form-label">Drink Type (standard drink = 14g alcohol)</label>
<select class="form-select" id="f2">
<option value="1">Beer 12oz (1 drink)</option>
<option value="1">Wine 5oz (1 drink)</option>
<option value="1">Shot 1.5oz (1 drink)</option>
<option value="0.5">Light Beer 12oz</option>
<option value="1.5">Strong Beer 22oz</option>
</select></div>
<div class="col-md-4"><label class="form-label">Body Weight (lbs)</label><input type="number" class="form-control" id="f3" value="160" step="5"></div>
<div class="col-md-4"><label class="form-label">Gender</label><select class="form-select" id="f4"><option value="0.73">Male (r=0.73)</option><option value="0.66">Female (r=0.66)</option></select></div>
<div class="col-md-4"><label class="form-label">Hours Since Drinking</label><input type="number" class="form-control" id="f5" value="1" step="0.5" min="0"></div>
</div>""",
[("Estimated BAC","r1"),("Legal Limit","r2"),("Time to Sober","r3"),("Status","r4")],
"Estimate BAC"),
"""<script>
function calc(){const drinks=+document.getElementById('f1').value,mult=+document.getElementById('f2').value,wt=+document.getElementById('f3').value,r=+document.getElementById('f4').value,hrs=+document.getElementById('f5').value;const bac=((drinks*mult*5.14)/(wt*r))-(0.015*hrs);const est=Math.max(0,bac);const soberTime=est/0.015;const legal=0.08;const status=est===0?'Sober':est<0.02?'Very Low':est<legal?'Low (<Legal Limit)':est<0.15?'Over Legal Limit':est<0.25?'High - Dangerous':'Very Dangerous';document.getElementById('r1').textContent=est.toFixed(3)+'%';document.getElementById('r2').textContent='0.08% (US)';document.getElementById('r3').textContent=soberTime.toFixed(1)+' hours';document.getElementById('r4').textContent=status;document.getElementById('resultBox').classList.add('show');}
</script>""")

page("hydration-calculator.html","Daily Water Intake Calculator",
"Calculate how much water you should drink per day based on weight, activity level, and climate.",
"water intake calculator, daily water requirement, how much water to drink, hydration calculator, water per day",
"&#128167;","#006064","#00838f","health","&#10084;","Health",
cb("Daily Water Intake Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Body Weight (kg)</label><input type="number" class="form-control" id="f1" value="70" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Activity Level</label>
<select class="form-select" id="f2">
<option value="1.0">Sedentary (office work)</option>
<option value="1.2" selected>Lightly Active</option>
<option value="1.4">Moderately Active</option>
<option value="1.6">Very Active (athlete)</option>
</select></div>
<div class="col-md-6"><label class="form-label">Climate</label>
<select class="form-select" id="f3">
<option value="1.0">Cool / Temperate</option>
<option value="1.1" selected>Moderate</option>
<option value="1.2">Hot and Humid</option>
<option value="1.3">Extreme Heat</option>
</select></div>
<div class="col-md-6"><label class="form-label">Pregnancy/Nursing</label>
<select class="form-select" id="f4">
<option value="0">No</option>
<option value="0.3">Pregnant (+300ml)</option>
<option value="0.7">Nursing (+700ml)</option>
</select></div>
</div>""",
[("Daily Water (Liters)","r1"),("Daily Water (Glasses)","r2"),("Per Hour (awake)","r3"),("Oz Per Day","r4")],
"Calculate"),
"""<script>
function calc(){const w=+document.getElementById('f1').value,act=+document.getElementById('f2').value,cli=+document.getElementById('f3').value,extra=+document.getElementById('f4').value;const liters=w*0.033*act*cli+extra;document.getElementById('r1').textContent=liters.toFixed(2)+' L';document.getElementById('r2').textContent=Math.round(liters/0.25)+' glasses (250ml)';document.getElementById('r3').textContent=(liters/16).toFixed(2)+' L/hr';document.getElementById('r4').textContent=(liters*33.814).toFixed(0)+' oz';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("minutes-to-hours-calculator.html","Minutes to Hours Converter",
"Convert minutes to hours and minutes. Also converts hours to minutes, seconds to hours, and any time format.",
"minutes to hours converter, convert minutes to hours, time format converter, hours minutes calculator, time calculator",
"&#8987;","#0d47a1","#1565c0","converters","&#128259;","Converters",
"""<div class="calc-box">
<h2 class="calc-title">Time Format Converter</h2>
<div class="d-flex gap-2 mb-3 flex-wrap">
<button class="cat-pill active" onclick="setMode('mth',this)">Minutes to H:M</button>
<button class="cat-pill" onclick="setMode('htm',this)">Hours to Minutes</button>
<button class="cat-pill" onclick="setMode('stm',this)">Seconds to All</button>
</div>
<div class="row g-3">
<div class="col-md-6"><label class="form-label" id="inLbl">Minutes</label>
<input type="number" class="form-control" id="tIn" value="150" step="1" min="0"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-clock me-2"></i>Convert Time</button>
<div class="result-box" id="resultBox"><div id="timeConvRes" style="font-size:0.95rem"></div></div></div>""",
"""<script>
let tcMode='mth';
function setMode(m,b){tcMode=m;document.querySelectorAll('.cat-pill').forEach(p=>p.classList.remove('active'));b.classList.add('active');const labels={mth:'Total Minutes',htm:'Total Hours',stm:'Total Seconds'};document.getElementById('inLbl').textContent=labels[m];}
function calc(){const v=+document.getElementById('tIn').value;let rows=[];if(tcMode==='mth'){const h=Math.floor(v/60),m=Math.round(v%60);rows=[['Hours',h+'h'],['Minutes',m+'m'],['Hours:Minutes',h+':'+String(m).padStart(2,'0')],['Total Seconds',v*60+' s'],['Days',(v/1440).toFixed(3)]];}else if(tcMode==='htm'){const m=v*60;rows=[['Minutes',m+'m'],['Hours:Minutes',Math.floor(v)+':'+String(Math.round((v%1)*60)).padStart(2,'0')],['Total Seconds',m*60+' s'],['Days',(v/24).toFixed(4)]];}else{rows=[['Seconds',v+'s'],['Minutes',(v/60).toFixed(2)+'m'],['Hours',(v/3600).toFixed(4)+'h'],['H:M:S',Math.floor(v/3600)+'h '+Math.floor((v%3600)/60)+'m '+Math.round(v%60)+'s'],['Days',(v/86400).toFixed(6)+'d']];}document.getElementById('timeConvRes').innerHTML=rows.map(function(r){return '<div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid var(--border)"><span>'+r[0]+'</span><strong>'+r[1]+'</strong></div>';}).join('');document.getElementById('resultBox').classList.add('show');}
</script>""")

page("square-root-calculator.html","Square Root Calculator",
"Calculate square root, cube root, and nth root of any number. Also calculates perfect squares list.",
"square root calculator, cube root calculator, nth root, calculate square root, perfect square, sqrt",
"&#8730;","#4a148c","#6a1b9a","math","&#128290;","Math",
cb("Square Root & Nth Root Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Number</label><input type="number" class="form-control" id="f1" value="144" step="any"></div>
<div class="col-md-6"><label class="form-label">Root Order (n)</label><input type="number" class="form-control" id="f2" value="2" min="2" step="1"></div>
</div>""",
[("Square Root (&#8730;n)","r1"),("Cube Root (&#8731;n)","r2"),("Nth Root","r3"),("n\u00B2 (Squared)","r4")]),
"""<script>
function calc(){const n=+document.getElementById('f1').value,r=+document.getElementById('f2').value;document.getElementById('r1').textContent=n>=0?Math.sqrt(n).toFixed(6):'N/A (negative)';document.getElementById('r2').textContent=Math.cbrt(n).toFixed(6);document.getElementById('r3').textContent=Math.pow(Math.abs(n),1/r).toFixed(6);document.getElementById('r4').textContent=(n*n).toExponential(4);document.getElementById('resultBox').classList.add('show');}
</script>""")

page("electricity-unit-calculator.html","Electricity Unit (kWh) Calculator",
"Convert electricity units and calculate cost. Understand your electricity bill in kWh, watts, and amperes.",
"electricity unit calculator, kWh calculator, watt to unit, electricity units to kWh, electricity consumption",
"&#9889;","#f57f17","#f9a825","environment","&#127807;","Environment",
cb("Electricity Unit Calculator",
"""<div class="row g-3">
<div class="col-md-4"><label class="form-label">Watts</label><input type="number" class="form-control" id="f1" value="1000" step="10"></div>
<div class="col-md-4"><label class="form-label">Hours</label><input type="number" class="form-control" id="f2" value="10" step="0.5"></div>
<div class="col-md-4"><label class="form-label">Rate ($/unit)</label><input type="number" class="form-control" id="f3" value="0.13" step="0.01"></div>
</div>""",
[("Units (kWh)","r1"),("Amperes at 230V","r2"),("Cost","r3"),("Monthly (30 days)","r4")]),
"""<script>
function calc(){const w=+document.getElementById('f1').value,h=+document.getElementById('f2').value,rate=+document.getElementById('f3').value;const kwh=w*h/1000,amp=w/230;document.getElementById('r1').textContent=kwh.toFixed(3)+' kWh';document.getElementById('r2').textContent=amp.toFixed(2)+' A';document.getElementById('r3').textContent='$'+(kwh*rate).toFixed(4);document.getElementById('r4').textContent='$'+(kwh*30*rate).toFixed(2)+' / '+(kwh*30).toFixed(1)+' kWh';document.getElementById('resultBox').classList.add('show');}
</script>""")

print("\n=== Batch 4 (fixed) complete! ===")
