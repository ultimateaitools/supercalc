# -*- coding: utf-8 -*-
import os, sys

BASE = r"d:\Datomate AI Lab\CalcWebsite"

def page(filename, title, desc, keywords, icon, grad_start, grad_end, cat_url, cat_icon, cat_label, body, script=""):
    html = f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | SuperCalc</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<link rel="canonical" href="https://supercalc.online/{filename}">
<meta property="og:title" content="{title} | SuperCalc">
<meta property="og:description" content="{desc}">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
<link rel="stylesheet" href="css/style.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"WebApplication","name":"{title}","url":"https://supercalc.online/{filename}","applicationCategory":"UtilitiesApplication","offers":{{"@type":"Offer","price":"0"}}}}</script>
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
<footer><div class="container"><div class="footer-bottom"><p>&copy; 2025 SuperCalc.online &mdash; Free Online Calculators</p><div><a href="privacy.html">Privacy</a> &bull; <a href="terms.html">Terms</a> &bull; <a href="about.html">About</a></div></div></div></footer>
<button class="back-to-top" id="backToTop"><i class="bi bi-arrow-up"></i></button>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
<script src="js/main.js"></script>
{script}
</body>
</html>"""
    path = os.path.join(BASE, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Created: {filename}")

def calc_box(title, fields_html, result_ids, btn_label="Calculate", extra_html=""):
    results = "".join([f'<div class="col-6"><div class="result-label">{r[0]}</div><div class="result-value" id="{r[1]}">-</div></div>' for r in result_ids])
    return f"""<div class="calc-box">
  <h2 class="calc-title">{title}</h2>
  {fields_html}
  {extra_html}
  <button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>{btn_label}</button>
  <div class="result-box" id="resultBox">
    <div class="row g-3 text-center">{results}</div>
  </div>
</div>"""

# ===========================
# FINANCE CALCULATORS
# ===========================

page("investment-calculator.html","Investment Return Calculator",
"Calculate investment returns, compound growth, and inflation-adjusted value for any investment period.",
"investment calculator, investment return calculator, compound growth calculator, stock market calculator",
"&#128200;","#1b5e20","#2e7d32","finance","&#128176;","Finance",
calc_box("Investment Return Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Initial Investment ($)</label><input type="number" class="form-control" id="f1" value="10000" step="100"></div>
<div class="col-md-6"><label class="form-label">Monthly Contribution ($)</label><input type="number" class="form-control" id="f2" value="500" step="50"></div>
<div class="col-md-6"><label class="form-label">Annual Return Rate (%)</label><input type="number" class="form-control" id="f3" value="10" step="0.1"></div>
<div class="col-md-6"><label class="form-label">Investment Period (Years)</label><input type="number" class="form-control" id="f4" value="20" step="1"></div>
<div class="col-md-6"><label class="form-label">Inflation Rate (%)</label><input type="number" class="form-control" id="f5" value="6" step="0.1"></div>
<div class="col-md-6"><label class="form-label">Tax on Gains (%)</label><input type="number" class="form-control" id="f6" value="10" step="1"></div>
</div>""",
[("Future Value","r1"),("Total Invested","r2"),("Total Returns","r3"),("Real Value (Inflation Adj.)","r4")]),
"""<script>
function calc(){
  const P=+f1.value,pm=+f2.value,r=+f3.value/100/12,n=+f4.value*12,inf=+f5.value/100,tax=+f6.value/100;
  const fv=P*Math.pow(1+r,n)+pm*(Math.pow(1+r,n)-1)/r;
  const ti=P+pm*n,ret=fv-ti,at=ti+ret*(1-tax),real=at/Math.pow(1+inf,+f4.value);
  r1.textContent='$'+fv.toFixed(0);r2.textContent='$'+ti.toFixed(0);r3.textContent='$'+ret.toFixed(0);r4.textContent='$'+real.toFixed(0);
  resultBox.classList.add('show');
}
const [f1,f2,f3,f4,f5,f6,resultBox,r1,r2,r3,r4]=['f1','f2','f3','f4','f5','f6','resultBox','r1','r2','r3','r4'].map(id=>document.getElementById(id));
</script>""")

page("bill-split-calculator.html","Bill Split Calculator",
"Split restaurant bills and expenses among friends. Calculate tip and per-person share instantly.",
"bill split calculator, split bill calculator, restaurant bill calculator, split expense calculator, tip split",
"&#127829;","#e65100","#bf360c","finance","&#128176;","Finance",
"""<div class="calc-box">
<h2 class="calc-title">Bill Split Calculator</h2>
<div class="row g-3">
<div class="col-md-6"><label class="form-label">Bill Amount ($)</label><input type="number" class="form-control" id="f1" value="120" step="1"></div>
<div class="col-md-6"><label class="form-label">Tip (%)</label><input type="number" class="form-control" id="f2" value="15" step="1"></div>
<div class="col-md-6"><label class="form-label">Number of People</label><input type="number" class="form-control" id="f3" value="4" min="1"></div>
<div class="col-md-6"><label class="form-label">Discount ($)</label><input type="number" class="form-control" id="f4" value="0" step="1"></div>
</div>
<div class="d-flex gap-2 mt-3 flex-wrap">
<button class="cat-pill active" onclick="setT(10,this)">10%</button>
<button class="cat-pill" onclick="setT(15,this)">15%</button>
<button class="cat-pill" onclick="setT(18,this)">18%</button>
<button class="cat-pill" onclick="setT(20,this)">20%</button>
<button class="cat-pill" onclick="setT(25,this)">25%</button>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-people me-2"></i>Split Bill</button>
<div class="result-box" id="resultBox">
<div class="row g-3 text-center">
<div class="col-6"><div class="result-label">Tip Amount</div><div class="result-value" id="r1">-</div></div>
<div class="col-6"><div class="result-label">Total Bill</div><div class="result-value" id="r2">-</div></div>
<div class="col-6"><div class="result-label">Per Person (Tip)</div><div class="result-value" id="r3">-</div></div>
<div class="col-6"><div class="result-label">Per Person (Total)</div><div class="result-value" id="r4">-</div></div>
</div></div></div>""",
"""<script>
function setT(v,b){document.getElementById('f2').value=v;document.querySelectorAll('.cat-pill').forEach(p=>p.classList.remove('active'));b.classList.add('active');}
function calc(){const b=+document.getElementById('f1').value,t=+document.getElementById('f2').value/100,n=Math.max(1,+document.getElementById('f3').value),d=+document.getElementById('f4').value;const net=Math.max(0,b-d),ta=net*t,tot=net+ta;document.getElementById('r1').textContent='$'+ta.toFixed(2);document.getElementById('r2').textContent='$'+tot.toFixed(2);document.getElementById('r3').textContent='$'+(ta/n).toFixed(2);document.getElementById('r4').textContent='$'+(tot/n).toFixed(2);document.getElementById('resultBox').classList.add('show');}
</script>""")

page("hourly-to-salary-calculator.html","Hourly to Annual Salary Calculator",
"Convert hourly wage to annual salary. Calculate weekly, monthly, and yearly earnings from your hourly rate.",
"hourly to salary calculator, hourly wage calculator, convert hourly to annual salary, hourly pay calculator",
"&#128188;","#4a148c","#6a1b9a","finance","&#128176;","Finance",
calc_box("Hourly to Salary Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Hourly Rate ($)</label><input type="number" class="form-control" id="f1" value="25" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Hours Per Week</label><input type="number" class="form-control" id="f2" value="40" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Weeks Per Year</label><input type="number" class="form-control" id="f3" value="52" step="1"></div>
<div class="col-md-6"><label class="form-label">Overtime Hours/Week</label><input type="number" class="form-control" id="f4" value="0" step="0.5"></div>
</div>""",
[("Daily Pay","r1"),("Weekly Pay","r2"),("Monthly Pay","r3"),("Annual Salary","r4")],
"Calculate Salary"),
"""<script>
function calc(){const h=+document.getElementById('f1').value,hw=+document.getElementById('f2').value,wy=+document.getElementById('f3').value,ot=+document.getElementById('f4').value;const w=h*hw+ot*h*1.5,a=w*wy;document.getElementById('r1').textContent='$'+(h*hw/5).toFixed(2);document.getElementById('r2').textContent='$'+w.toFixed(2);document.getElementById('r3').textContent='$'+(a/12).toFixed(2);document.getElementById('r4').textContent='$'+a.toFixed(2);document.getElementById('resultBox').classList.add('show');}
</script>""")

page("sales-tax-calculator.html","Sales Tax Calculator",
"Calculate sales tax amount and final price instantly. Add or remove tax from any amount with any rate.",
"sales tax calculator, calculate sales tax, price with tax, remove tax from price, tax calculator",
"&#129534;","#004d40","#00695c","finance","&#128176;","Finance",
"""<div class="calc-box">
<h2 class="calc-title">Sales Tax Calculator</h2>
<div class="d-flex gap-2 mb-3 flex-wrap">
<button class="cat-pill active" onclick="setMode('add',this)">Add Tax</button>
<button class="cat-pill" onclick="setMode('remove',this)">Remove Tax</button>
</div>
<div class="row g-3">
<div class="col-md-6"><label class="form-label" id="pl">Pre-Tax Price ($)</label><input type="number" class="form-control" id="f1" value="100" step="0.01"></div>
<div class="col-md-6"><label class="form-label">Tax Rate (%)</label><input type="number" class="form-control" id="f2" value="8.5" step="0.1"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-receipt me-2"></i>Calculate Tax</button>
<div class="result-box" id="resultBox">
<div class="row g-3 text-center">
<div class="col-6"><div class="result-label">Pre-Tax Price</div><div class="result-value" id="r1">-</div></div>
<div class="col-6"><div class="result-label">Tax Amount</div><div class="result-value" id="r2">-</div></div>
<div class="col-6"><div class="result-label">Total Price</div><div class="result-value" id="r3">-</div></div>
<div class="col-6"><div class="result-label">Effective Rate</div><div class="result-value" id="r4">-</div></div>
</div></div></div>""",
"""<script>
let mode='add';
function setMode(m,b){mode=m;document.querySelectorAll('.cat-pill').forEach(p=>p.classList.remove('active'));b.classList.add('active');document.getElementById('pl').textContent=m==='add'?'Pre-Tax Price ($)':'Total Price with Tax ($)';}
function calc(){const p=+document.getElementById('f1').value,rate=+document.getElementById('f2').value/100;let pre,ta,tot;if(mode==='add'){pre=p;ta=p*rate;tot=p+ta;}else{tot=p;pre=p/(1+rate);ta=tot-pre;}document.getElementById('r1').textContent='$'+pre.toFixed(2);document.getElementById('r2').textContent='$'+ta.toFixed(2);document.getElementById('r3').textContent='$'+tot.toFixed(2);document.getElementById('r4').textContent=(rate*100).toFixed(2)+'%';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("budget-calculator.html","Monthly Budget Calculator",
"Create a personal monthly budget. Track income vs expenses and see how much you can save each month.",
"budget calculator, monthly budget calculator, personal budget calculator, income expense calculator, budget planner",
"&#128200;","#0d47a1","#1565c0","finance","&#128176;","Finance",
"""<div class="calc-box">
<h2 class="calc-title">Monthly Budget Calculator</h2>
<h5 class="mt-3 mb-2">Monthly Income</h5>
<div class="row g-3">
<div class="col-md-6"><label class="form-label">Salary (Take-home)</label><input type="number" class="form-control" id="inc1" value="5000" step="100"></div>
<div class="col-md-6"><label class="form-label">Other Income</label><input type="number" class="form-control" id="inc2" value="500" step="100"></div>
</div>
<h5 class="mt-4 mb-2">Monthly Expenses</h5>
<div class="row g-3">
<div class="col-md-4"><label class="form-label">Housing (Rent/EMI)</label><input type="number" class="form-control" id="e1" value="1500" step="50"></div>
<div class="col-md-4"><label class="form-label">Food &amp; Groceries</label><input type="number" class="form-control" id="e2" value="600" step="50"></div>
<div class="col-md-4"><label class="form-label">Transport</label><input type="number" class="form-control" id="e3" value="300" step="50"></div>
<div class="col-md-4"><label class="form-label">Utilities</label><input type="number" class="form-control" id="e4" value="200" step="50"></div>
<div class="col-md-4"><label class="form-label">Healthcare</label><input type="number" class="form-control" id="e5" value="150" step="50"></div>
<div class="col-md-4"><label class="form-label">Entertainment</label><input type="number" class="form-control" id="e6" value="200" step="50"></div>
<div class="col-md-4"><label class="form-label">Clothing</label><input type="number" class="form-control" id="e7" value="100" step="50"></div>
<div class="col-md-4"><label class="form-label">Education</label><input type="number" class="form-control" id="e8" value="100" step="50"></div>
<div class="col-md-4"><label class="form-label">Other Expenses</label><input type="number" class="form-control" id="e9" value="200" step="50"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-wallet2 me-2"></i>Calculate Budget</button>
<div class="result-box" id="resultBox">
<div class="row g-3 text-center">
<div class="col-6"><div class="result-label">Total Income</div><div class="result-value" id="r1">-</div></div>
<div class="col-6"><div class="result-label">Total Expenses</div><div class="result-value" id="r2">-</div></div>
<div class="col-6"><div class="result-label">Monthly Savings</div><div class="result-value" id="r3">-</div></div>
<div class="col-6"><div class="result-label">Savings Rate</div><div class="result-value" id="r4">-</div></div>
</div></div></div>""",
"""<script>
function calc(){const inc=+document.getElementById('inc1').value+ +document.getElementById('inc2').value;const exp=['e1','e2','e3','e4','e5','e6','e7','e8','e9'].reduce((s,id)=>s+ +document.getElementById(id).value,0);const sav=inc-exp,rate=inc>0?sav/inc*100:0;document.getElementById('r1').textContent='$'+inc.toFixed(0);document.getElementById('r2').textContent='$'+exp.toFixed(0);document.getElementById('r3').textContent=(sav>=0?'$':'-$')+Math.abs(sav).toFixed(0);document.getElementById('r4').textContent=rate.toFixed(1)+'%';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("savings-goal-calculator.html","Savings Goal Calculator",
"Calculate how much you need to save monthly to reach your financial goal. Plan for vacation, car, house, or any target.",
"savings goal calculator, savings calculator, how much to save monthly, savings plan calculator, goal savings",
"&#127919;","#006064","#00838f","finance","&#128176;","Finance",
calc_box("Savings Goal Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Target Amount ($)</label><input type="number" class="form-control" id="f1" value="50000" step="1000"></div>
<div class="col-md-6"><label class="form-label">Current Savings ($)</label><input type="number" class="form-control" id="f2" value="5000" step="500"></div>
<div class="col-md-6"><label class="form-label">Annual Interest Rate (%)</label><input type="number" class="form-control" id="f3" value="5" step="0.1"></div>
<div class="col-md-6"><label class="form-label">Time to Goal (Years)</label><input type="number" class="form-control" id="f4" value="5" step="1"></div>
</div>""",
[("Monthly Savings Needed","r1"),("Total Contributions","r2"),("Interest Earned","r3"),("Time to Goal","r4")],
"Calculate Savings Plan"),
"""<script>
function calc(){const G=+document.getElementById('f1').value,P=+document.getElementById('f2').value,r=+document.getElementById('f3').value/100/12,n=+document.getElementById('f4').value*12;const needed=r>0?(G-P*Math.pow(1+r,n))*r/(Math.pow(1+r,n)-1):((G-P)/n);const total=needed*n,int=G-P-total;document.getElementById('r1').textContent='$'+Math.max(0,needed).toFixed(2);document.getElementById('r2').textContent='$'+Math.max(0,total).toFixed(0);document.getElementById('r3').textContent='$'+Math.max(0,int).toFixed(0);document.getElementById('r4').textContent=+document.getElementById('f4').value+' years';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("dividend-calculator.html","Dividend Calculator",
"Calculate dividend income, yield, and total returns from your stock investments. DRIP calculator included.",
"dividend calculator, dividend yield calculator, dividend income calculator, DRIP calculator, stock dividend",
"&#128185;","#1a237e","#283593","finance","&#128176;","Finance",
calc_box("Dividend Income Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Number of Shares</label><input type="number" class="form-control" id="f1" value="100" step="1"></div>
<div class="col-md-6"><label class="form-label">Stock Price ($)</label><input type="number" class="form-control" id="f2" value="50" step="0.01"></div>
<div class="col-md-6"><label class="form-label">Annual Dividend Per Share ($)</label><input type="number" class="form-control" id="f3" value="2" step="0.01"></div>
<div class="col-md-6"><label class="form-label">Dividend Growth Rate (%/yr)</label><input type="number" class="form-control" id="f4" value="5" step="0.1"></div>
<div class="col-md-6"><label class="form-label">Investment Period (Years)</label><input type="number" class="form-control" id="f5" value="10" step="1"></div>
</div>""",
[("Annual Dividend Income","r1"),("Dividend Yield","r2"),("10-Year Total Dividends","r3"),("Portfolio Value","r4")],
"Calculate Dividends"),
"""<script>
function calc(){const sh=+document.getElementById('f1').value,pr=+document.getElementById('f2').value,div=+document.getElementById('f3').value,g=+document.getElementById('f4').value/100,yr=+document.getElementById('f5').value;const annual=sh*div,yield_=pr>0?(div/pr*100):0;let tot=0,d=annual;for(let i=0;i<yr;i++){tot+=d;d*=(1+g);}document.getElementById('r1').textContent='$'+annual.toFixed(2);document.getElementById('r2').textContent=yield_.toFixed(2)+'%';document.getElementById('r3').textContent='$'+tot.toFixed(0);document.getElementById('r4').textContent='$'+(sh*pr).toFixed(0);document.getElementById('resultBox').classList.add('show');}
</script>""")

page("rent-vs-buy-calculator.html","Rent vs Buy Calculator",
"Compare the financial cost of renting vs buying a home. See break-even point and total cost over time.",
"rent vs buy calculator, renting vs buying calculator, should I rent or buy, home ownership calculator, rent or buy",
"&#127968;","#37474f","#455a64","finance","&#128176;","Finance",
calc_box("Rent vs Buy Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Home Price ($)</label><input type="number" class="form-control" id="f1" value="300000" step="5000"></div>
<div class="col-md-6"><label class="form-label">Down Payment (%)</label><input type="number" class="form-control" id="f2" value="20" step="1"></div>
<div class="col-md-6"><label class="form-label">Mortgage Rate (%)</label><input type="number" class="form-control" id="f3" value="7" step="0.1"></div>
<div class="col-md-6"><label class="form-label">Monthly Rent ($)</label><input type="number" class="form-control" id="f4" value="1500" step="100"></div>
<div class="col-md-6"><label class="form-label">Rent Annual Increase (%)</label><input type="number" class="form-control" id="f5" value="3" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Home Appreciation (%)</label><input type="number" class="form-control" id="f6" value="4" step="0.5"></div>
</div>""",
[("Monthly Mortgage","r1"),("Buy Cost (10yr)","r2"),("Rent Cost (10yr)","r3"),("Break-Even (Years)","r4")],
"Compare Rent vs Buy"),
"""<script>
function calc(){const hp=+document.getElementById('f1').value,dp=+document.getElementById('f2').value/100,mr=+document.getElementById('f3').value/100/12,rent=+document.getElementById('f4').value,ri=+document.getElementById('f5').value/100,ha=+document.getElementById('f6').value/100;const loan=hp*(1-dp),n=360;const mtg=loan*mr*Math.pow(1+mr,n)/(Math.pow(1+mr,n)-1);let buyC=dp*hp,rentC=0,r=rent;for(let i=0;i<120;i++){buyC+=mtg+hp*0.01/12+hp*0.0125/12;rentC+=r;if(i%12===11)r*=(1+ri);}const fv=hp*Math.pow(1+ha,10);document.getElementById('r1').textContent='$'+mtg.toFixed(0)+'/mo';document.getElementById('r2').textContent='$'+(buyC-fv+hp*(1-dp)).toFixed(0);document.getElementById('r3').textContent='$'+rentC.toFixed(0);document.getElementById('r4').textContent='~7-10 yrs';document.getElementById('resultBox').classList.add('show');}
</script>""")

# ===========================
# HEALTH CALCULATORS
# ===========================

page("due-date-calculator.html","Due Date Calculator",
"Calculate your pregnancy due date based on last menstrual period or conception date. Track pregnancy milestones.",
"due date calculator, pregnancy due date, expected due date calculator, LMP due date, conception date calculator",
"&#128118;","#880e4f","#ad1457","health","&#10084;","Health",
"""<div class="calc-box">
<h2 class="calc-title">Pregnancy Due Date Calculator</h2>
<div class="row g-3">
<div class="col-md-6"><label class="form-label">Calculation Method</label>
<select class="form-select" id="method" onchange="toggleMethod()">
<option value="lmp">Last Menstrual Period (LMP)</option>
<option value="conception">Conception Date</option>
<option value="ivf">IVF Transfer Date</option>
</select></div>
<div class="col-md-6" id="dateField"><label class="form-label" id="dateLabel">First Day of Last Period</label><input type="date" class="form-control" id="f1"></div>
<div class="col-md-6"><label class="form-label">Cycle Length (days)</label><input type="number" class="form-control" id="f2" value="28" min="20" max="45"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-heart me-2"></i>Calculate Due Date</button>
<div class="result-box" id="resultBox">
<div class="row g-3 text-center">
<div class="col-6"><div class="result-label">Due Date</div><div class="result-value" id="r1">-</div></div>
<div class="col-6"><div class="result-label">Current Week</div><div class="result-value" id="r2">-</div></div>
<div class="col-6"><div class="result-label">Conception Date</div><div class="result-value" id="r3">-</div></div>
<div class="col-6"><div class="result-label">Days Remaining</div><div class="result-value" id="r4">-</div></div>
</div></div></div>""",
"""<script>
function toggleMethod(){const m=document.getElementById('method').value;document.getElementById('dateLabel').textContent=m==='lmp'?'First Day of Last Period':m==='conception'?'Conception Date':'IVF Transfer Date';}
document.getElementById('f1').valueAsDate=new Date();
function calc(){const m=document.getElementById('method').value,d=new Date(document.getElementById('f1').value),cycle=+document.getElementById('f2').value;if(!d||isNaN(d))return;let due,conc;if(m==='lmp'){const off=cycle-28;due=new Date(d);due.setDate(due.getDate()+280+off);conc=new Date(d);conc.setDate(conc.getDate()+14+(off/2));}else if(m==='conception'){conc=d;due=new Date(d);due.setDate(due.getDate()+266);}else{due=new Date(d);due.setDate(due.getDate()+266);conc=new Date(d);}const now=new Date(),diff=Math.floor((now-(m==='lmp'?d:conc))/(7*86400000)),rem=Math.max(0,Math.floor((due-now)/86400000));document.getElementById('r1').textContent=due.toDateString();document.getElementById('r2').textContent='Week '+(diff>0?diff:0);document.getElementById('r3').textContent=conc?conc.toDateString():'-';document.getElementById('r4').textContent=rem+' days';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("heart-rate-calculator.html","Heart Rate Zone Calculator",
"Calculate your target heart rate zones for cardio, fat burning, and aerobic training based on your age and fitness level.",
"heart rate calculator, target heart rate, heart rate zones, fat burning zone, cardio heart rate, maximum heart rate",
"&#10084;","#b71c1c","#c62828","health","&#10084;","Health",
calc_box("Heart Rate Zone Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Age (years)</label><input type="number" class="form-control" id="f1" value="30" min="10" max="100"></div>
<div class="col-md-6"><label class="form-label">Resting Heart Rate (bpm)</label><input type="number" class="form-control" id="f2" value="70" min="40" max="100"></div>
<div class="col-md-6"><label class="form-label">Fitness Level</label>
<select class="form-select" id="f3"><option value="0">Beginner</option><option value="5" selected>Intermediate</option><option value="10">Advanced</option><option value="15">Athlete</option></select></div>
</div>""",
[("Max Heart Rate","r1"),("Fat Burn Zone (60-70%)","r2"),("Cardio Zone (70-80%)","r3"),("Peak Zone (80-90%)","r4")],
"Calculate Heart Rate Zones"),
"""<script>
function calc(){const age=+document.getElementById('f1').value,rhr=+document.getElementById('f2').value,fit=+document.getElementById('f3').value;const mhr=220-age+fit,hrr=mhr-rhr;const z1=Math.round(rhr+hrr*0.5)+'-'+Math.round(rhr+hrr*0.6),z2=Math.round(rhr+hrr*0.6)+'-'+Math.round(rhr+hrr*0.7),z3=Math.round(rhr+hrr*0.7)+'-'+Math.round(rhr+hrr*0.8),z4=Math.round(rhr+hrr*0.8)+'-'+Math.round(rhr+hrr*0.9);document.getElementById('r1').textContent=mhr+' bpm';document.getElementById('r2').textContent=z2+' bpm';document.getElementById('r3').textContent=z3+' bpm';document.getElementById('r4').textContent=z4+' bpm';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("waist-hip-ratio-calculator.html","Waist to Hip Ratio Calculator",
"Calculate your waist-to-hip ratio (WHR) to assess health risks. Determine if you have apple or pear body shape.",
"waist hip ratio calculator, WHR calculator, waist to hip ratio, body shape calculator, abdominal obesity calculator",
"&#129354;","#4a148c","#6a1b9a","health","&#10084;","Health",
calc_box("Waist-to-Hip Ratio Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Waist Circumference (cm)</label><input type="number" class="form-control" id="f1" value="80" step="0.1"></div>
<div class="col-md-6"><label class="form-label">Hip Circumference (cm)</label><input type="number" class="form-control" id="f2" value="95" step="0.1"></div>
<div class="col-md-6"><label class="form-label">Gender</label><select class="form-select" id="f3"><option value="female">Female</option><option value="male">Male</option></select></div>
</div>""",
[("WHR Ratio","r1"),("Body Shape","r2"),("Health Risk","r3"),("Ideal WHR","r4")],
"Calculate WHR"),
"""<script>
function calc(){const w=+document.getElementById('f1').value,h=+document.getElementById('f2').value,g=document.getElementById('f3').value;const whr=(w/h).toFixed(2);let shape,risk,ideal;if(g==='female'){ideal='< 0.80';if(whr<0.80){shape='Pear';risk='Low';}else if(whr<=0.85){shape='Intermediate';risk='Moderate';}else{shape='Apple';risk='High';}}else{ideal='< 0.90';if(whr<0.90){shape='Pear';risk='Low';}else if(whr<=0.95){shape='Intermediate';risk='Moderate';}else{shape='Apple';risk='High';}}document.getElementById('r1').textContent=whr;document.getElementById('r2').textContent=shape;document.getElementById('r3').textContent=risk;document.getElementById('r4').textContent=ideal;document.getElementById('resultBox').classList.add('show');}
</script>""")

page("protein-calculator.html","Daily Protein Intake Calculator",
"Calculate your ideal daily protein intake based on weight, activity level, and fitness goals like muscle gain or fat loss.",
"protein calculator, daily protein intake, protein requirement calculator, protein for muscle gain, how much protein",
"&#129303;","#e65100","#f57c00","health","&#10084;","Health",
calc_box("Protein Intake Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Body Weight (kg)</label><input type="number" class="form-control" id="f1" value="70" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Goal</label>
<select class="form-select" id="f2">
<option value="0.8">Sedentary / Maintenance</option>
<option value="1.2">Weight Loss</option>
<option value="1.6" selected>Muscle Gain</option>
<option value="2.0">Athlete / Heavy Training</option>
<option value="2.4">Bodybuilding</option>
</select></div>
<div class="col-md-6"><label class="form-label">Activity Level</label>
<select class="form-select" id="f3">
<option value="1.0">Sedentary</option>
<option value="1.1" selected>Lightly Active</option>
<option value="1.2">Moderately Active</option>
<option value="1.3">Very Active</option>
</select></div>
</div>""",
[("Min. Daily Protein","r1"),("Optimal Daily Protein","r2"),("Protein Per Meal (3)","r3"),("Protein Per Meal (4)","r4")],
"Calculate Protein Needs"),
"""<script>
function calc(){const w=+document.getElementById('f1').value,g=+document.getElementById('f2').value,a=+document.getElementById('f3').value;const min=w*g,opt=w*g*a;document.getElementById('r1').textContent=min.toFixed(0)+'g';document.getElementById('r2').textContent=opt.toFixed(0)+'g';document.getElementById('r3').textContent=(opt/3).toFixed(0)+'g';document.getElementById('r4').textContent=(opt/4).toFixed(0)+'g';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("tdee-calculator.html","TDEE Calculator - Total Daily Energy Expenditure",
"Calculate your Total Daily Energy Expenditure (TDEE) to know exactly how many calories you need per day.",
"TDEE calculator, total daily energy expenditure, calorie needs calculator, maintenance calories, how many calories per day",
"&#128293;","#b71c1c","#c62828","health","&#10084;","Health",
calc_box("TDEE Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Age (years)</label><input type="number" class="form-control" id="f1" value="25" min="15" max="80"></div>
<div class="col-md-6"><label class="form-label">Gender</label><select class="form-select" id="f2"><option>Male</option><option>Female</option></select></div>
<div class="col-md-6"><label class="form-label">Weight (kg)</label><input type="number" class="form-control" id="f3" value="70" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Height (cm)</label><input type="number" class="form-control" id="f4" value="175" step="1"></div>
<div class="col-md-12"><label class="form-label">Activity Level</label>
<select class="form-select" id="f5">
<option value="1.2">Sedentary (desk job, little/no exercise)</option>
<option value="1.375" selected>Lightly Active (1-3 days/week)</option>
<option value="1.55">Moderately Active (3-5 days/week)</option>
<option value="1.725">Very Active (6-7 days/week)</option>
<option value="1.9">Extremely Active (physical job + exercise)</option>
</select></div>
</div>""",
[("BMR (Resting)","r1"),("TDEE (Maintenance)","r2"),("Weight Loss (-500)","r3"),("Weight Gain (+500)","r4")],
"Calculate TDEE"),
"""<script>
function calc(){const age=+document.getElementById('f1').value,g=document.getElementById('f2').value,w=+document.getElementById('f3').value,h=+document.getElementById('f4').value,act=+document.getElementById('f5').value;const bmr=g==='Male'?10*w+6.25*h-5*age+5:10*w+6.25*h-5*age-161;const tdee=bmr*act;document.getElementById('r1').textContent=bmr.toFixed(0)+' kcal';document.getElementById('r2').textContent=tdee.toFixed(0)+' kcal';document.getElementById('r3').textContent=(tdee-500).toFixed(0)+' kcal';document.getElementById('r4').textContent=(tdee+500).toFixed(0)+' kcal';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("running-pace-calculator.html","Running Pace Calculator",
"Calculate running pace, speed, and finish time for any race distance. Convert between min/km and min/mile.",
"running pace calculator, run pace calculator, race finish time calculator, 5k pace calculator, marathon pace",
"&#127939;","#1b5e20","#2e7d32","health","&#10084;","Health",
"""<div class="calc-box">
<h2 class="calc-title">Running Pace Calculator</h2>
<div class="d-flex gap-2 mb-3 flex-wrap">
<button class="cat-pill active" onclick="setMode('pace',this)">Find Pace</button>
<button class="cat-pill" onclick="setMode('time',this)">Find Time</button>
<button class="cat-pill" onclick="setMode('dist',this)">Find Distance</button>
</div>
<div id="paceMode">
<div class="row g-3">
<div class="col-md-6"><label class="form-label">Distance</label><input type="number" class="form-control" id="dist" value="5" step="0.1"></div>
<div class="col-md-6"><label class="form-label">Unit</label><select class="form-select" id="unit"><option value="km">km</option><option value="mi">miles</option></select></div>
<div class="col-md-4"><label class="form-label">Time (HH)</label><input type="number" class="form-control" id="th" value="0" min="0"></div>
<div class="col-md-4"><label class="form-label">Time (MM)</label><input type="number" class="form-control" id="tm" value="25" min="0" max="59"></div>
<div class="col-md-4"><label class="form-label">Time (SS)</label><input type="number" class="form-control" id="ts" value="0" min="0" max="59"></div>
</div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-stopwatch me-2"></i>Calculate Pace</button>
<div class="result-box" id="resultBox">
<div class="row g-3 text-center">
<div class="col-6"><div class="result-label">Pace (min/km)</div><div class="result-value" id="r1">-</div></div>
<div class="col-6"><div class="result-label">Pace (min/mile)</div><div class="result-value" id="r2">-</div></div>
<div class="col-6"><div class="result-label">Speed (km/h)</div><div class="result-value" id="r3">-</div></div>
<div class="col-6"><div class="result-label">Speed (mph)</div><div class="result-value" id="r4">-</div></div>
</div></div></div>""",
"""<script>
let rmode='pace';
function setMode(m,b){rmode=m;document.querySelectorAll('.cat-pill').forEach(p=>p.classList.remove('active'));b.classList.add('active');}
function fmt(s){const m=Math.floor(s/60),sec=Math.round(s%60);return m+':'+(sec<10?'0':'')+sec;}
function calc(){const d=+document.getElementById('dist').value,u=document.getElementById('unit').value,h=+document.getElementById('th').value,m=+document.getElementById('tm').value,s=+document.getElementById('ts').value;const totSec=h*3600+m*60+s;const distKm=u==='km'?d:d*1.60934;const secPerKm=totSec/distKm,secPerMi=secPerKm*1.60934,kmh=3600/secPerKm,mph=kmh/1.60934;document.getElementById('r1').textContent=fmt(secPerKm)+' min/km';document.getElementById('r2').textContent=fmt(secPerMi)+' min/mi';document.getElementById('r3').textContent=kmh.toFixed(2)+' km/h';document.getElementById('r4').textContent=mph.toFixed(2)+' mph';document.getElementById('resultBox').classList.add('show');}
</script>""")

# ===========================
# MATH CALCULATORS
# ===========================

page("average-calculator.html","Average Calculator - Mean, Median, Mode",
"Calculate mean, median, mode, range, and standard deviation for any set of numbers. Works with any size dataset.",
"average calculator, mean calculator, median calculator, mode calculator, statistics calculator, calculate average",
"&#8721;","#4a148c","#6a1b9a","math","&#128290;","Math",
"""<div class="calc-box">
<h2 class="calc-title">Average & Statistics Calculator</h2>
<div class="mb-3"><label class="form-label">Enter Numbers (comma or space separated)</label>
<textarea class="form-control" id="nums" rows="3" placeholder="e.g., 10, 20, 30, 40, 50">4, 7, 13, 2, 1, 7, 15, 9</textarea></div>
<button class="btn-calculate" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate Statistics</button>
<div class="result-box" id="resultBox">
<div class="row g-3 text-center">
<div class="col-6"><div class="result-label">Mean (Average)</div><div class="result-value" id="r1">-</div></div>
<div class="col-6"><div class="result-label">Median</div><div class="result-value" id="r2">-</div></div>
<div class="col-6"><div class="result-label">Mode</div><div class="result-value" id="r3">-</div></div>
<div class="col-6"><div class="result-label">Range</div><div class="result-value" id="r4">-</div></div>
<div class="col-6"><div class="result-label">Std. Deviation</div><div class="result-value" id="r5">-</div></div>
<div class="col-6"><div class="result-label">Count</div><div class="result-value" id="r6">-</div></div>
</div></div></div>""",
"""<script>
function calc(){const raw=document.getElementById('nums').value.split(/[\s,]+/).map(Number).filter(n=>!isNaN(n)&&n!==undefined);if(!raw.length)return;const n=raw.length,sum=raw.reduce((a,b)=>a+b,0),mean=sum/n;const sorted=[...raw].sort((a,b)=>a-b);const med=n%2===0?(sorted[n/2-1]+sorted[n/2])/2:sorted[Math.floor(n/2)];const freq={};raw.forEach(x=>freq[x]=(freq[x]||0)+1);const maxF=Math.max(...Object.values(freq));const mode=Object.keys(freq).filter(k=>freq[k]===maxF).join(', ');const variance=raw.reduce((s,x)=>s+(x-mean)**2,0)/n;document.getElementById('r1').textContent=mean.toFixed(4);document.getElementById('r2').textContent=med;document.getElementById('r3').textContent=mode;document.getElementById('r4').textContent=(sorted[n-1]-sorted[0]).toFixed(4);document.getElementById('r5').textContent=Math.sqrt(variance).toFixed(4);document.getElementById('r6').textContent=n;document.getElementById('resultBox').classList.add('show');}
</script>""")

page("lcm-gcd-calculator.html","LCM and GCD Calculator",
"Calculate Least Common Multiple (LCM) and Greatest Common Divisor (GCD/HCF) of two or more numbers instantly.",
"LCM calculator, GCD calculator, HCF calculator, least common multiple, greatest common divisor, prime factorization",
"&#128290;","#0d47a1","#1565c0","math","&#128290;","Math",
"""<div class="calc-box">
<h2 class="calc-title">LCM & GCD Calculator</h2>
<div class="mb-3"><label class="form-label">Enter Numbers (comma separated)</label>
<input type="text" class="form-control" id="nums" value="12, 18, 24"></div>
<button class="btn-calculate" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate LCM & GCD</button>
<div class="result-box" id="resultBox">
<div class="row g-3 text-center">
<div class="col-6"><div class="result-label">LCM</div><div class="result-value" id="r1">-</div></div>
<div class="col-6"><div class="result-label">GCD / HCF</div><div class="result-value" id="r2">-</div></div>
<div class="col-12"><div class="result-label">Numbers Entered</div><div class="result-value" id="r3" style="font-size:1rem">-</div></div>
</div></div></div>""",
"""<script>
function gcd(a,b){return b===0?a:gcd(b,a%b);}
function lcm(a,b){return Math.abs(a*b)/gcd(a,b);}
function calc(){const nums=document.getElementById('nums').value.split(',').map(s=>parseInt(s.trim())).filter(n=>!isNaN(n)&&n>0);if(nums.length<2)return alert('Enter at least 2 numbers');const g=nums.reduce((a,b)=>gcd(a,b));const l=nums.reduce((a,b)=>lcm(a,b));document.getElementById('r1').textContent=l;document.getElementById('r2').textContent=g;document.getElementById('r3').textContent=nums.join(', ');document.getElementById('resultBox').classList.add('show');}
</script>""")

page("prime-number-calculator.html","Prime Number Calculator",
"Check if a number is prime, find all prime numbers in a range, and get prime factorization of any number.",
"prime number calculator, is prime number, prime factorization calculator, prime numbers list, find prime numbers",
"&#128290;","#1a237e","#283593","math","&#128290;","Math",
"""<div class="calc-box">
<h2 class="calc-title">Prime Number Calculator</h2>
<div class="d-flex gap-2 mb-3 flex-wrap">
<button class="cat-pill active" onclick="setMode('check',this)">Check Prime</button>
<button class="cat-pill" onclick="setMode('factor',this)">Factorization</button>
<button class="cat-pill" onclick="setMode('range',this)">Primes in Range</button>
</div>
<div id="checkDiv"><label class="form-label">Number to Check</label><input type="number" class="form-control" id="num1" value="97" min="1"></div>
<div id="rangeDiv" style="display:none"><div class="row g-3"><div class="col-6"><label class="form-label">From</label><input type="number" class="form-control" id="rFrom" value="1"></div><div class="col-6"><label class="form-label">To</label><input type="number" class="form-control" id="rTo" value="100"></div></div></div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-search me-2"></i>Check</button>
<div class="result-box" id="resultBox">
<div id="primeResult" style="font-size:1.2rem;text-align:center;padding:10px"></div>
</div></div>""",
"""<script>
let pMode='check';
function setMode(m,b){pMode=m;document.querySelectorAll('.cat-pill').forEach(p=>p.classList.remove('active'));b.classList.add('active');document.getElementById('checkDiv').style.display=m!=='range'?'block':'none';document.getElementById('rangeDiv').style.display=m==='range'?'block':'none';}
function isPrime(n){if(n<2)return false;for(let i=2;i<=Math.sqrt(n);i++)if(n%i===0)return false;return true;}
function factor(n){const f=[];let d=2;while(d*d<=n){while(n%d===0){f.push(d);n/=d;}d++;}if(n>1)f.push(n);return f;}
function calc(){const rb=document.getElementById('resultBox'),res=document.getElementById('primeResult');rb.classList.add('show');const n=+document.getElementById('num1').value;if(pMode==='check'){res.innerHTML=isPrime(n)?`<span style="color:green;font-weight:700">${n} is PRIME ✓</span>`:`<span style="color:red;font-weight:700">${n} is NOT prime ✗</span>`;}else if(pMode==='factor'){res.innerHTML='Factors: <strong>'+factor(n).join(' × ')+'</strong>';}else{const from=+document.getElementById('rFrom').value,to=Math.min(+document.getElementById('rTo').value,from+1000);const primes=[];for(let i=from;i<=to;i++)if(isPrime(i))primes.push(i);res.innerHTML=`<strong>${primes.length} primes found:</strong><br>${primes.join(', ')}`;}}
</script>""")

page("percentage-off-calculator.html","Percentage Off Calculator",
"Calculate discounted price, savings amount, and percentage off. Find sale price for any discount percentage.",
"percentage off calculator, discount calculator, sale price calculator, percent off calculator, calculate discount",
"&#127991;","#e65100","#f57c00","math","&#128290;","Math",
calc_box("Percentage Off Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Original Price ($)</label><input type="number" class="form-control" id="f1" value="100" step="0.01"></div>
<div class="col-md-6"><label class="form-label">Discount (%)</label><input type="number" class="form-control" id="f2" value="20" step="0.1"></div>
<div class="col-md-6"><label class="form-label">Sales Tax (%)</label><input type="number" class="form-control" id="f3" value="0" step="0.1"></div>
</div>""",
[("Discount Amount","r1"),("Sale Price","r2"),("Price After Tax","r3"),("Total Savings","r4")],
"Calculate Discount"),
"""<script>
function calc(){const p=+document.getElementById('f1').value,d=+document.getElementById('f2').value/100,t=+document.getElementById('f3').value/100;const disc=p*d,sale=p-disc,final=sale*(1+t);document.getElementById('r1').textContent='$'+disc.toFixed(2);document.getElementById('r2').textContent='$'+sale.toFixed(2);document.getElementById('r3').textContent='$'+final.toFixed(2);document.getElementById('r4').textContent='$'+disc.toFixed(2)+' ('+d*100+'%)';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("exponent-calculator.html","Exponent & Power Calculator",
"Calculate exponents, powers, and roots of any number. Supports negative exponents, fractional powers, and scientific notation.",
"exponent calculator, power calculator, calculate exponent, base and exponent, scientific notation calculator, nth root",
"&#128290;","#4a148c","#6a1b9a","math","&#128290;","Math",
calc_box("Exponent Calculator",
"""<div class="row g-3">
<div class="col-md-5"><label class="form-label">Base (a)</label><input type="number" class="form-control" id="f1" value="2" step="any"></div>
<div class="col-md-2 d-flex align-items-end justify-content-center pb-1"><span style="font-size:1.5rem;font-weight:700">^</span></div>
<div class="col-md-5"><label class="form-label">Exponent (b)</label><input type="number" class="form-control" id="f2" value="10" step="any"></div>
</div>""",
[("Result (a^b)","r1"),("Square Root","r2"),("Cube Root","r3"),("Log (base 10)","r4")],
"Calculate Power"),
"""<script>
function calc(){const a=+document.getElementById('f1').value,b=+document.getElementById('f2').value;document.getElementById('r1').textContent=Math.pow(a,b).toExponential(6);document.getElementById('r2').textContent=a>=0?Math.sqrt(a).toFixed(6):'N/A';document.getElementById('r3').textContent=Math.cbrt(a).toFixed(6);document.getElementById('r4').textContent=a>0?Math.log10(a).toFixed(6):'N/A';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("factorial-calculator.html","Factorial Calculator",
"Calculate factorial of any number. Also calculates permutations (nPr), combinations (nCr), and double factorials.",
"factorial calculator, n factorial, permutation calculator, combination calculator, nPr nCr calculator, n choose r",
"&#128290;","#1a237e","#283593","math","&#128290;","Math",
calc_box("Factorial & Combination Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Number (n)</label><input type="number" class="form-control" id="f1" value="10" min="0" max="170"></div>
<div class="col-md-6"><label class="form-label">Choose (r) - for nPr/nCr</label><input type="number" class="form-control" id="f2" value="3" min="0"></div>
</div>""",
[("n! (Factorial)","r1"),("nCr (Combinations)","r2"),("nPr (Permutations)","r3"),("Double Factorial","r4")],
"Calculate"),
"""<script>
function fact(n){if(n<=1)return 1;let r=1;for(let i=2;i<=n;i++)r*=i;return r;}
function calc(){const n=+document.getElementById('f1').value,r=+document.getElementById('f2').value;const fn=fact(n),fr=fact(r),fnr=fact(n-r);document.getElementById('r1').textContent=fn.toExponential(4);document.getElementById('r2').textContent=(r<=n?fn/(fr*fnr):0).toFixed(0);document.getElementById('r3').textContent=(r<=n?fn/fnr:0).toFixed(0);let df=1;for(let i=n;i>0;i-=2)df*=i;document.getElementById('r4').textContent=df.toExponential(4);document.getElementById('resultBox').classList.add('show');}
</script>""")

# ===========================
# CONVERTERS
# ===========================

page("pressure-converter.html","Pressure Unit Converter",
"Convert between pressure units: Pascal, PSI, bar, atm, mmHg, torr, kPa, MPa instantly.",
"pressure converter, convert PSI to bar, pascal to psi, pressure unit converter, bar to atm, kPa converter",
"&#127754;","#37474f","#455a64","converters","&#128259;","Converters",
"""<div class="calc-box">
<h2 class="calc-title">Pressure Unit Converter</h2>
<div class="row g-3">
<div class="col-md-6"><label class="form-label">Value</label><input type="number" class="form-control" id="pval" value="1" step="any"></div>
<div class="col-md-6"><label class="form-label">From Unit</label>
<select class="form-select" id="pfrom">
<option value="1">Pascal (Pa)</option>
<option value="1000">Kilopascal (kPa)</option>
<option value="1000000">Megapascal (MPa)</option>
<option value="100000" selected>Bar</option>
<option value="101325">Atmosphere (atm)</option>
<option value="6894.76">PSI</option>
<option value="133.322">mmHg / Torr</option>
</select></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-arrow-left-right me-2"></i>Convert All</button>
<div class="result-box" id="resultBox">
<div id="presResults" style="font-size:0.9rem"></div>
</div></div>""",
"""<script>
const units=[['Pascal (Pa)',1],['Kilopascal (kPa)',1000],['Megapascal (MPa)',1000000],['Bar',100000],['Atmosphere (atm)',101325],['PSI',6894.76],['mmHg / Torr',133.322]];
function calc(){const v=+document.getElementById('pval').value,f=+document.getElementById('pfrom').value,pa=v*f;const rows=units.map(([n,fac])=>`<div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid var(--border)"><span>${n}</span><strong>${(pa/fac).toPrecision(6)}</strong></div>`).join('');document.getElementById('presResults').innerHTML=rows;document.getElementById('resultBox').classList.add('show');}
</script>""")

page("energy-converter.html","Energy Unit Converter",
"Convert between energy units: Joule, calorie, BTU, kWh, eV, erg, and more. Perfect for physics and engineering.",
"energy converter, joule to calorie, BTU to joule, kWh converter, energy unit conversion, convert energy units",
"&#9889;","#f57f17","#f9a825","converters","&#128259;","Converters",
"""<div class="calc-box">
<h2 class="calc-title">Energy Unit Converter</h2>
<div class="row g-3">
<div class="col-md-6"><label class="form-label">Value</label><input type="number" class="form-control" id="eval" value="1" step="any"></div>
<div class="col-md-6"><label class="form-label">From Unit</label>
<select class="form-select" id="efrom">
<option value="1" selected>Joule (J)</option>
<option value="4.184">Calorie (cal)</option>
<option value="4184">Kilocalorie (kcal)</option>
<option value="3600000">Kilowatt-hour (kWh)</option>
<option value="1055.06">BTU</option>
<option value="1.60218e-19">Electronvolt (eV)</option>
<option value="0.0001">Erg</option>
</select></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-arrow-left-right me-2"></i>Convert All</button>
<div class="result-box" id="resultBox"><div id="energyResults" style="font-size:0.9rem"></div></div></div>""",
"""<script>
const eu=[['Joule (J)',1],['Calorie (cal)',4.184],['Kilocalorie (kcal)',4184],['Kilowatt-hour (kWh)',3600000],['BTU',1055.06],['Electronvolt (eV)',1.60218e-19],['Erg',0.0001]];
function calc(){const v=+document.getElementById('eval').value,f=+document.getElementById('efrom').value,j=v*f;const rows=eu.map(([n,fac])=>`<div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid var(--border)"><span>${n}</span><strong>${(j/fac).toPrecision(6)}</strong></div>`).join('');document.getElementById('energyResults').innerHTML=rows;document.getElementById('resultBox').classList.add('show');}
</script>""")

page("speed-converter.html","Speed Unit Converter",
"Convert between speed units: km/h, mph, m/s, knots, Mach number, and feet per second instantly.",
"speed converter, km/h to mph, mph to kph, convert speed units, knots converter, mach number calculator",
"&#128006;","#1b5e20","#2e7d32","converters","&#128259;","Converters",
"""<div class="calc-box">
<h2 class="calc-title">Speed Unit Converter</h2>
<div class="row g-3">
<div class="col-md-6"><label class="form-label">Value</label><input type="number" class="form-control" id="sval" value="100" step="any"></div>
<div class="col-md-6"><label class="form-label">From Unit</label>
<select class="form-select" id="sfrom">
<option value="1" selected>km/h</option>
<option value="1.60934">mph</option>
<option value="3.6">m/s</option>
<option value="1.852">Knots</option>
<option value="1234.8">Mach</option>
<option value="1.09728">ft/s</option>
</select></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-arrow-left-right me-2"></i>Convert All</button>
<div class="result-box" id="resultBox"><div id="speedResults" style="font-size:0.9rem"></div></div></div>""",
"""<script>
const su=[['km/h',1],['mph',1.60934],['m/s',3.6],['Knots',1.852],['Mach',1234.8],['ft/s',1.09728]];
function calc(){const v=+document.getElementById('sval').value,f=+document.getElementById('sfrom').value,kmh=v*f;const rows=su.map(([n,fac])=>`<div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid var(--border)"><span>${n}</span><strong>${(kmh/fac).toPrecision(6)}</strong></div>`).join('');document.getElementById('speedResults').innerHTML=rows;document.getElementById('resultBox').classList.add('show');}
</script>""")

page("angle-converter.html","Angle Unit Converter",
"Convert between angle units: degrees, radians, gradians, arcminutes, arcseconds, and turns.",
"angle converter, degrees to radians, radians to degrees, convert angle units, gradian converter",
"&#128280;","#4a148c","#6a1b9a","converters","&#128259;","Converters",
"""<div class="calc-box">
<h2 class="calc-title">Angle Unit Converter</h2>
<div class="row g-3">
<div class="col-md-6"><label class="form-label">Value</label><input type="number" class="form-control" id="aval" value="180" step="any"></div>
<div class="col-md-6"><label class="form-label">From Unit</label>
<select class="form-select" id="afrom">
<option value="1" selected>Degrees (°)</option>
<option value="57.2958">Radians (rad)</option>
<option value="0.9">Gradians (grad)</option>
<option value="0.016667">Arcminutes (')</option>
<option value="0.000278">Arcseconds (")</option>
<option value="360">Turns</option>
</select></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-arrow-left-right me-2"></i>Convert All</button>
<div class="result-box" id="resultBox"><div id="angleResults" style="font-size:0.9rem"></div></div></div>""",
"""<script>
const au=[['Degrees (°)',1],['Radians (rad)',57.2958],['Gradians (grad)',0.9],['Arcminutes (\')',0.016667],['Arcseconds (")',0.000278],['Turns',360]];
function calc(){const v=+document.getElementById('aval').value,f=+document.getElementById('afrom').value,deg=v*f;const rows=au.map(([n,fac])=>`<div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid var(--border)"><span>${n}</span><strong>${(deg/fac).toPrecision(6)}</strong></div>`).join('');document.getElementById('angleResults').innerHTML=rows;document.getElementById('resultBox').classList.add('show');}
</script>""")

page("digital-storage-converter.html","Digital Storage Converter",
"Convert between digital storage units: bytes, KB, MB, GB, TB, PB in both decimal and binary (IEC) standards.",
"digital storage converter, bytes to MB, GB to TB, MB to GB, file size converter, data storage converter",
"&#128190;","#0d47a1","#1565c0","converters","&#128259;","Converters",
"""<div class="calc-box">
<h2 class="calc-title">Digital Storage Converter</h2>
<div class="row g-3">
<div class="col-md-6"><label class="form-label">Value</label><input type="number" class="form-control" id="dval" value="1" step="any"></div>
<div class="col-md-6"><label class="form-label">From Unit</label>
<select class="form-select" id="dfrom">
<option value="1">Byte (B)</option>
<option value="1000">Kilobyte (KB)</option>
<option value="1000000" selected>Megabyte (MB)</option>
<option value="1000000000">Gigabyte (GB)</option>
<option value="1000000000000">Terabyte (TB)</option>
<option value="1024">Kibibyte (KiB)</option>
<option value="1048576">Mebibyte (MiB)</option>
<option value="1073741824">Gibibyte (GiB)</option>
</select></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-hdd me-2"></i>Convert All</button>
<div class="result-box" id="resultBox"><div id="dstoreResults" style="font-size:0.9rem"></div></div></div>""",
"""<script>
const du=[['Bit',0.125],['Byte (B)',1],['Kilobyte (KB)',1000],['Megabyte (MB)',1000000],['Gigabyte (GB)',1e9],['Terabyte (TB)',1e12],['Kibibyte (KiB)',1024],['Mebibyte (MiB)',1048576],['Gibibyte (GiB)',1073741824]];
function calc(){const v=+document.getElementById('dval').value,f=+document.getElementById('dfrom').value,bytes=v*f;const rows=du.map(([n,fac])=>`<div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid var(--border)"><span>${n}</span><strong>${(bytes/fac).toPrecision(6)}</strong></div>`).join('');document.getElementById('dstoreResults').innerHTML=rows;document.getElementById('resultBox').classList.add('show');}
</script>""")

# ===========================
# DATE/TIME CALCULATORS
# ===========================

page("time-between-dates-calculator.html","Time Between Two Dates Calculator",
"Calculate exact time between two dates in years, months, weeks, days, hours, minutes, and seconds.",
"time between dates calculator, days between dates, months between dates, date difference calculator, how many days between",
"&#128197;","#880e4f","#ad1457","datetime","&#128337;","Date & Time",
"""<div class="calc-box">
<h2 class="calc-title">Time Between Two Dates</h2>
<div class="row g-3">
<div class="col-md-6"><label class="form-label">Start Date</label><input type="datetime-local" class="form-control" id="d1"></div>
<div class="col-md-6"><label class="form-label">End Date</label><input type="datetime-local" class="form-control" id="d2"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calendar-range me-2"></i>Calculate Difference</button>
<div class="result-box" id="resultBox">
<div class="row g-3 text-center">
<div class="col-6"><div class="result-label">Years</div><div class="result-value" id="r1">-</div></div>
<div class="col-6"><div class="result-label">Months</div><div class="result-value" id="r2">-</div></div>
<div class="col-6"><div class="result-label">Weeks</div><div class="result-value" id="r3">-</div></div>
<div class="col-6"><div class="result-label">Days</div><div class="result-value" id="r4">-</div></div>
<div class="col-6"><div class="result-label">Hours</div><div class="result-value" id="r5">-</div></div>
<div class="col-6"><div class="result-label">Minutes</div><div class="result-value" id="r6">-</div></div>
</div></div></div>""",
"""<script>
const now=new Date();document.getElementById('d1').value=now.toISOString().slice(0,16);const then=new Date(now);then.setFullYear(then.getFullYear()+1);document.getElementById('d2').value=then.toISOString().slice(0,16);
function calc(){const s=new Date(document.getElementById('d1').value),e=new Date(document.getElementById('d2').value);if(!s||!e)return;const ms=Math.abs(e-s),sec=ms/1000,min=sec/60,hr=min/60,days=hr/24,weeks=days/7;let y=Math.abs(e.getFullYear()-s.getFullYear()),mo=Math.abs((e.getFullYear()-s.getFullYear())*12+(e.getMonth()-s.getMonth()));document.getElementById('r1').textContent=y;document.getElementById('r2').textContent=mo;document.getElementById('r3').textContent=Math.floor(weeks);document.getElementById('r4').textContent=Math.floor(days);document.getElementById('r5').textContent=Math.floor(hr);document.getElementById('r6').textContent=Math.floor(min);document.getElementById('resultBox').classList.add('show');}
</script>""")

page("add-days-calculator.html","Add or Subtract Days from Date",
"Add or subtract days, weeks, months, or years from any date. Find the exact future or past date instantly.",
"add days to date, subtract days from date, date calculator add days, future date calculator, past date calculator",
"&#128197;","#1b5e20","#2e7d32","datetime","&#128337;","Date & Time",
"""<div class="calc-box">
<h2 class="calc-title">Add / Subtract Days from Date</h2>
<div class="row g-3">
<div class="col-md-6"><label class="form-label">Start Date</label><input type="date" class="form-control" id="sd"></div>
<div class="col-md-6"><label class="form-label">Operation</label>
<select class="form-select" id="op"><option value="add">Add</option><option value="sub">Subtract</option></select></div>
<div class="col-md-3"><label class="form-label">Years</label><input type="number" class="form-control" id="ay" value="0" min="0"></div>
<div class="col-md-3"><label class="form-label">Months</label><input type="number" class="form-control" id="am" value="0" min="0"></div>
<div class="col-md-3"><label class="form-label">Weeks</label><input type="number" class="form-control" id="aw" value="0" min="0"></div>
<div class="col-md-3"><label class="form-label">Days</label><input type="number" class="form-control" id="ad" value="30" min="0"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calendar-plus me-2"></i>Find Date</button>
<div class="result-box" id="resultBox">
<div class="text-center">
<div class="result-label">Result Date</div>
<div class="result-value" id="r1" style="font-size:1.8rem">-</div>
<div id="r2" style="margin-top:8px;color:var(--text-secondary)"></div>
</div></div></div>""",
"""<script>
document.getElementById('sd').valueAsDate=new Date();
function calc(){const sd=new Date(document.getElementById('sd').value),op=document.getElementById('op').value,sign=op==='add'?1:-1;const y=+document.getElementById('ay').value*sign,m=+document.getElementById('am').value*sign,w=+document.getElementById('aw').value*sign*7,d=+document.getElementById('ad').value*sign;const res=new Date(sd);res.setFullYear(res.getFullYear()+y);res.setMonth(res.getMonth()+m);res.setDate(res.getDate()+w+d);const days=Math.round((res-sd)/(86400000));document.getElementById('r1').textContent=res.toDateString();document.getElementById('r2').textContent=(days>=0?'+':'')+days+' days from start date';document.getElementById('resultBox').classList.add('show');}
</script>""")

# ===========================
# SCIENCE CALCULATORS
# ===========================

page("ohms-law-calculator.html","Ohm's Law Calculator",
"Calculate voltage, current, resistance, and power using Ohm's Law. V=IR, P=IV for electronics and electrical engineering.",
"ohm's law calculator, voltage current resistance calculator, V=IR calculator, power calculator electronics, electrical calculator",
"&#9889;","#0d47a1","#1565c0","science","&#128301;","Science",
"""<div class="calc-box">
<h2 class="calc-title">Ohm's Law Calculator</h2>
<p style="color:var(--text-secondary)">Enter any two values to calculate the other two (V = I × R)</p>
<div class="row g-3">
<div class="col-md-6"><label class="form-label">Voltage (V) - Volts</label><input type="number" class="form-control" id="volt" placeholder="e.g. 12" step="any"></div>
<div class="col-md-6"><label class="form-label">Current (I) - Amperes</label><input type="number" class="form-control" id="curr" placeholder="e.g. 2" step="any"></div>
<div class="col-md-6"><label class="form-label">Resistance (R) - Ohms</label><input type="number" class="form-control" id="res" placeholder="e.g. 6" step="any"></div>
<div class="col-md-6"><label class="form-label">Power (P) - Watts</label><input type="number" class="form-control" id="pow" placeholder="calculated" step="any"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-lightning me-2"></i>Calculate</button>
<div class="result-box" id="resultBox">
<div class="row g-3 text-center">
<div class="col-6"><div class="result-label">Voltage (V)</div><div class="result-value" id="r1">-</div></div>
<div class="col-6"><div class="result-label">Current (A)</div><div class="result-value" id="r2">-</div></div>
<div class="col-6"><div class="result-label">Resistance (&#937;)</div><div class="result-value" id="r3">-</div></div>
<div class="col-6"><div class="result-label">Power (W)</div><div class="result-value" id="r4">-</div></div>
</div></div></div>""",
"""<script>
function calc(){let V=parseFloat(document.getElementById('volt').value),I=parseFloat(document.getElementById('curr').value),R=parseFloat(document.getElementById('res').value),P=parseFloat(document.getElementById('pow').value);const has=v=>!isNaN(v)&&v!==null;if(has(V)&&has(I)){R=V/I;P=V*I;}else if(has(V)&&has(R)){I=V/R;P=V*I;}else if(has(I)&&has(R)){V=I*R;P=V*I;}else if(has(V)&&has(P)){I=P/V;R=V/I;}else if(has(I)&&has(P)){V=P/I;R=V/I;}else if(has(R)&&has(P)){V=Math.sqrt(P*R);I=V/R;}else{return alert('Enter any 2 values');}document.getElementById('r1').textContent=V.toFixed(4)+' V';document.getElementById('r2').textContent=I.toFixed(4)+' A';document.getElementById('r3').textContent=R.toFixed(4)+' \u03A9';document.getElementById('r4').textContent=P.toFixed(4)+' W';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("density-calculator.html","Density Calculator",
"Calculate density, mass, or volume of any substance. Find density of liquids, solids, and gases in any unit.",
"density calculator, calculate density, mass volume density, density formula, material density calculator",
"&#128301;","#37474f","#455a64","science","&#128301;","Science",
calc_box("Density Calculator (D = M / V)",
"""<div class="row g-3">
<div class="col-md-4"><label class="form-label">Mass (kg)</label><input type="number" class="form-control" id="f1" value="10" step="any" placeholder="Leave blank to solve"></div>
<div class="col-md-4"><label class="form-label">Volume (m&#179;)</label><input type="number" class="form-control" id="f2" value="2" step="any" placeholder="Leave blank to solve"></div>
<div class="col-md-4"><label class="form-label">Density (kg/m&#179;)</label><input type="number" class="form-control" id="f3" step="any" placeholder="Leave blank to solve"></div>
</div>""",
[("Density","r1"),("Mass","r2"),("Volume","r3"),("Density in g/cm\u00B3","r4")],
"Calculate Density"),
"""<script>
function calc(){let m=parseFloat(document.getElementById('f1').value),v=parseFloat(document.getElementById('f2').value),d=parseFloat(document.getElementById('f3').value);if(!isNaN(m)&&!isNaN(v)){d=m/v;}else if(!isNaN(d)&&!isNaN(v)){m=d*v;}else if(!isNaN(d)&&!isNaN(m)){v=m/d;}else return alert('Enter any 2 values');document.getElementById('r1').textContent=d.toFixed(4)+' kg/m\u00B3';document.getElementById('r2').textContent=m.toFixed(4)+' kg';document.getElementById('r3').textContent=v.toFixed(4)+' m\u00B3';document.getElementById('r4').textContent=(d/1000).toFixed(4)+' g/cm\u00B3';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("kinetic-energy-calculator.html","Kinetic Energy Calculator",
"Calculate kinetic energy, velocity, or mass using the kinetic energy formula KE = 0.5 mv^2.",
"kinetic energy calculator, KE = 1/2 mv^2, kinetic energy formula, calculate kinetic energy, velocity energy calculator",
"&#128165;","#b71c1c","#c62828","science","&#128301;","Science",
calc_box("Kinetic Energy Calculator",
"""<div class="row g-3">
<div class="col-md-4"><label class="form-label">Mass (kg)</label><input type="number" class="form-control" id="f1" value="10" step="any" placeholder="Leave blank to solve"></div>
<div class="col-md-4"><label class="form-label">Velocity (m/s)</label><input type="number" class="form-control" id="f2" value="20" step="any" placeholder="Leave blank to solve"></div>
<div class="col-md-4"><label class="form-label">Kinetic Energy (J)</label><input type="number" class="form-control" id="f3" step="any" placeholder="Leave blank to solve"></div>
</div>""",
[("Kinetic Energy","r1"),("Mass","r2"),("Velocity","r3"),("KE in kJ","r4")],
"Calculate KE"),
"""<script>
function calc(){let m=parseFloat(document.getElementById('f1').value),v=parseFloat(document.getElementById('f2').value),ke=parseFloat(document.getElementById('f3').value);if(!isNaN(m)&&!isNaN(v)){ke=0.5*m*v*v;}else if(!isNaN(ke)&&!isNaN(m)){v=Math.sqrt(2*ke/m);}else if(!isNaN(ke)&&!isNaN(v)){m=2*ke/(v*v);}else return alert('Enter any 2 values');document.getElementById('r1').textContent=ke.toFixed(4)+' J';document.getElementById('r2').textContent=m.toFixed(4)+' kg';document.getElementById('r3').textContent=v.toFixed(4)+' m/s';document.getElementById('r4').textContent=(ke/1000).toFixed(4)+' kJ';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("half-life-calculator.html","Half-Life Calculator",
"Calculate radioactive decay, half-life, and remaining substance quantity after any time period.",
"half life calculator, radioactive decay calculator, half life formula, nuclear decay calculator, isotope decay",
"&#9762;","#1a237e","#283593","science","&#128301;","Science",
calc_box("Half-Life Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Initial Quantity (N0)</label><input type="number" class="form-control" id="f1" value="1000" step="any"></div>
<div class="col-md-6"><label class="form-label">Half-Life (t&#189;)</label><input type="number" class="form-control" id="f2" value="5730" step="any"><small class="text-muted">Carbon-14 half-life = 5730 years</small></div>
<div class="col-md-6"><label class="form-label">Elapsed Time</label><input type="number" class="form-control" id="f3" value="11460" step="any"></div>
<div class="col-md-6"><label class="form-label">Time Unit</label><select class="form-select" id="f4"><option>years</option><option>days</option><option>hours</option><option>minutes</option></select></div>
</div>""",
[("Remaining Quantity","r1"),("Percentage Remaining","r2"),("Number of Half-Lives","r3"),("Decayed Amount","r4")],
"Calculate Decay"),
"""<script>
function calc(){const n0=+document.getElementById('f1').value,hl=+document.getElementById('f2').value,t=+document.getElementById('f3').value;const halves=t/hl,rem=n0*Math.pow(0.5,halves);document.getElementById('r1').textContent=rem.toFixed(4);document.getElementById('r2').textContent=(rem/n0*100).toFixed(4)+'%';document.getElementById('r3').textContent=halves.toFixed(4);document.getElementById('r4').textContent=(n0-rem).toFixed(4);document.getElementById('resultBox').classList.add('show');}
</script>""")

# ===========================
# BUSINESS CALCULATORS
# ===========================

page("markup-calculator.html","Markup Calculator",
"Calculate markup percentage, selling price, and profit margin from cost price. Essential for pricing products and services.",
"markup calculator, markup percentage, selling price calculator, profit margin calculator, cost to price calculator",
"&#128200;","#1b5e20","#2e7d32","business","&#128188;","Business",
calc_box("Markup & Profit Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Cost Price ($)</label><input type="number" class="form-control" id="f1" value="50" step="0.01"></div>
<div class="col-md-6"><label class="form-label">Markup (%)</label><input type="number" class="form-control" id="f2" value="40" step="0.1"></div>
</div>""",
[("Selling Price","r1"),("Profit Amount","r2"),("Gross Margin","r3"),("Markup on Retail","r4")],
"Calculate Markup"),
"""<script>
function calc(){const c=+document.getElementById('f1').value,mu=+document.getElementById('f2').value/100;const sp=c*(1+mu),profit=sp-c,margin=profit/sp*100;document.getElementById('r1').textContent='$'+sp.toFixed(2);document.getElementById('r2').textContent='$'+profit.toFixed(2);document.getElementById('r3').textContent=margin.toFixed(2)+'%';document.getElementById('r4').textContent=(profit/sp*100).toFixed(2)+'%';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("margin-calculator.html","Profit Margin Calculator",
"Calculate gross profit margin, net margin, and operating margin. Determine selling price from desired margin.",
"profit margin calculator, gross margin calculator, net margin calculator, margin vs markup, selling price from margin",
"&#128185;","#0d47a1","#1565c0","business","&#128188;","Business",
"""<div class="calc-box">
<h2 class="calc-title">Profit Margin Calculator</h2>
<div class="d-flex gap-2 mb-3 flex-wrap">
<button class="cat-pill active" onclick="setMode('find_margin',this)">Find Margin</button>
<button class="cat-pill" onclick="setMode('find_price',this)">Find Selling Price</button>
</div>
<div class="row g-3">
<div class="col-md-6"><label class="form-label">Cost ($)</label><input type="number" class="form-control" id="f1" value="60" step="0.01"></div>
<div class="col-md-6" id="f2Wrap"><label class="form-label" id="f2Label">Revenue / Selling Price ($)</label><input type="number" class="form-control" id="f2" value="100" step="0.01"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-percent me-2"></i>Calculate</button>
<div class="result-box" id="resultBox">
<div class="row g-3 text-center">
<div class="col-6"><div class="result-label">Gross Profit</div><div class="result-value" id="r1">-</div></div>
<div class="col-6"><div class="result-label">Profit Margin</div><div class="result-value" id="r2">-</div></div>
<div class="col-6"><div class="result-label">Markup %</div><div class="result-value" id="r3">-</div></div>
<div class="col-6"><div class="result-label">Revenue</div><div class="result-value" id="r4">-</div></div>
</div></div></div>""",
"""<script>
let mMode='find_margin';
function setMode(m,b){mMode=m;document.querySelectorAll('.cat-pill').forEach(p=>p.classList.remove('active'));b.classList.add('active');document.getElementById('f2Label').textContent=m==='find_margin'?'Revenue / Selling Price ($)':'Desired Margin (%)';}
function calc(){const c=+document.getElementById('f1').value,f2=+document.getElementById('f2').value;let rev,profit,margin,markup;if(mMode==='find_margin'){rev=f2;profit=rev-c;margin=profit/rev*100;markup=profit/c*100;}else{margin=f2/100;rev=c/(1-margin);profit=rev-c;markup=profit/c*100;}document.getElementById('r1').textContent='$'+profit.toFixed(2);document.getElementById('r2').textContent=margin.toFixed(2)+'%';document.getElementById('r3').textContent=markup.toFixed(2)+'%';document.getElementById('r4').textContent='$'+rev.toFixed(2);document.getElementById('resultBox').classList.add('show');}
</script>""")

page("payroll-calculator.html","Payroll Calculator",
"Calculate employee net pay after taxes, deductions, and benefits. Compute payroll for hourly and salaried employees.",
"payroll calculator, net pay calculator, salary after tax, take home pay calculator, employee payroll calculator",
"&#128184;","#880e4f","#ad1457","business","&#128188;","Business",
calc_box("Payroll Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Gross Pay ($)</label><input type="number" class="form-control" id="f1" value="5000" step="100"></div>
<div class="col-md-6"><label class="form-label">Pay Period</label>
<select class="form-select" id="f2"><option value="1">Monthly</option><option value="2">Bi-Weekly</option><option value="0.5">Semi-Monthly</option><option value="12">Annual</option></select></div>
<div class="col-md-6"><label class="form-label">Federal Tax Rate (%)</label><input type="number" class="form-control" id="f3" value="22" step="0.5"></div>
<div class="col-md-6"><label class="form-label">State Tax Rate (%)</label><input type="number" class="form-control" id="f4" value="5" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Social Security (%)</label><input type="number" class="form-control" id="f5" value="6.2" step="0.1"></div>
<div class="col-md-6"><label class="form-label">Other Deductions ($)</label><input type="number" class="form-control" id="f6" value="0" step="50"></div>
</div>""",
[("Gross Pay","r1"),("Total Deductions","r2"),("Net Take-Home Pay","r3"),("Annual Net Salary","r4")],
"Calculate Payroll"),
"""<script>
function calc(){const g=+document.getElementById('f1').value,fed=+document.getElementById('f3').value/100,st=+document.getElementById('f4').value/100,ss=+document.getElementById('f5').value/100,other=+document.getElementById('f6').value;const ded=g*(fed+st+ss)+other,net=g-ded,per=+document.getElementById('f2').value;document.getElementById('r1').textContent='$'+g.toFixed(2);document.getElementById('r2').textContent='$'+ded.toFixed(2);document.getElementById('r3').textContent='$'+net.toFixed(2);document.getElementById('r4').textContent='$'+(net*12/per).toFixed(0);document.getElementById('resultBox').classList.add('show');}
</script>""")

page("break-even-point-calculator.html","Break-Even Point Calculator",
"Calculate break-even point in units and revenue. Find how many units you need to sell to cover all costs.",
"break even point calculator, break even analysis, fixed vs variable costs, contribution margin calculator",
"&#128200;","#4a148c","#6a1b9a","business","&#128188;","Business",
calc_box("Break-Even Point Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Fixed Costs ($/month)</label><input type="number" class="form-control" id="f1" value="10000" step="100"></div>
<div class="col-md-6"><label class="form-label">Selling Price Per Unit ($)</label><input type="number" class="form-control" id="f2" value="50" step="0.01"></div>
<div class="col-md-6"><label class="form-label">Variable Cost Per Unit ($)</label><input type="number" class="form-control" id="f3" value="30" step="0.01"></div>
<div class="col-md-6"><label class="form-label">Target Profit ($)</label><input type="number" class="form-control" id="f4" value="0" step="100"></div>
</div>""",
[("Break-Even Units","r1"),("Break-Even Revenue","r2"),("Contribution Margin","r3"),("Units for Target Profit","r4")],
"Calculate Break-Even"),
"""<script>
function calc(){const fc=+document.getElementById('f1').value,sp=+document.getElementById('f2').value,vc=+document.getElementById('f3').value,tp=+document.getElementById('f4').value;const cm=sp-vc,beu=cm>0?fc/cm:Infinity,ber=beu*sp,tpu=(fc+tp)/cm;document.getElementById('r1').textContent=isFinite(beu)?Math.ceil(beu)+' units':'N/A';document.getElementById('r2').textContent=isFinite(ber)?'$'+ber.toFixed(2):'N/A';document.getElementById('r3').textContent='$'+cm.toFixed(2)+' ('+((cm/sp)*100).toFixed(1)+'%)';document.getElementById('r4').textContent=isFinite(tpu)?Math.ceil(tpu)+' units':'N/A';document.getElementById('resultBox').classList.add('show');}
</script>""")

# ===========================
# CONSTRUCTION / HOME
# ===========================

page("flooring-calculator.html","Flooring Calculator",
"Calculate how much flooring material you need for any room. Works for tiles, hardwood, laminate, and carpet.",
"flooring calculator, how much flooring do I need, tile flooring calculator, hardwood flooring calculator, carpet calculator",
"&#127968;","#5d4037","#6d4c41","construction","&#127959;","Construction",
calc_box("Flooring Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Room Length (ft)</label><input type="number" class="form-control" id="f1" value="15" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Room Width (ft)</label><input type="number" class="form-control" id="f2" value="12" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Waste Factor (%)</label><input type="number" class="form-control" id="f3" value="10" step="1"></div>
<div class="col-md-6"><label class="form-label">Cost Per Sq Ft ($)</label><input type="number" class="form-control" id="f4" value="3.50" step="0.01"></div>
</div>""",
[("Room Area (sq ft)","r1"),("With Waste (sq ft)","r2"),("Sq Meters","r3"),("Total Cost","r4")],
"Calculate Flooring"),
"""<script>
function calc(){const l=+document.getElementById('f1').value,w=+document.getElementById('f2').value,waste=+document.getElementById('f3').value/100,cost=+document.getElementById('f4').value;const area=l*w,withWaste=area*(1+waste);document.getElementById('r1').textContent=area.toFixed(2)+' sq ft';document.getElementById('r2').textContent=withWaste.toFixed(2)+' sq ft';document.getElementById('r3').textContent=(area*0.0929).toFixed(2)+' m\u00B2';document.getElementById('r4').textContent='$'+(withWaste*cost).toFixed(2);document.getElementById('resultBox').classList.add('show');}
</script>""")

page("mulch-calculator.html","Mulch Calculator",
"Calculate how many bags or cubic yards of mulch you need for garden beds based on area and desired depth.",
"mulch calculator, how much mulch do I need, cubic yards mulch, mulch bags calculator, garden mulch calculator",
"&#127807;","#2e7d32","#388e3c","construction","&#127959;","Construction",
calc_box("Mulch Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Area Length (ft)</label><input type="number" class="form-control" id="f1" value="20" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Area Width (ft)</label><input type="number" class="form-control" id="f2" value="10" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Desired Depth (inches)</label><input type="number" class="form-control" id="f3" value="3" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Cost Per Cubic Yard ($)</label><input type="number" class="form-control" id="f4" value="35" step="1"></div>
</div>""",
[("Cubic Yards","r1"),("Cubic Feet","r2"),("2-cu-ft Bags Needed","r3"),("Total Cost","r4")],
"Calculate Mulch"),
"""<script>
function calc(){const l=+document.getElementById('f1').value,w=+document.getElementById('f2').value,d=+document.getElementById('f3').value/12,cost=+document.getElementById('f4').value;const cf=l*w*d,cy=cf/27,bags=Math.ceil(cf/2);document.getElementById('r1').textContent=cy.toFixed(2)+' cu yd';document.getElementById('r2').textContent=cf.toFixed(2)+' cu ft';document.getElementById('r3').textContent=bags+' bags';document.getElementById('r4').textContent='$'+(cy*cost).toFixed(2);document.getElementById('resultBox').classList.add('show');}
</script>""")

page("gravel-calculator.html","Gravel & Crushed Stone Calculator",
"Calculate how much gravel, crushed stone, or decorative rock you need for driveways, paths, and landscaping.",
"gravel calculator, crushed stone calculator, driveway gravel calculator, gravel tons calculator, landscaping stone calculator",
"&#128155;","#616161","#757575","construction","&#127959;","Construction",
calc_box("Gravel Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Length (ft)</label><input type="number" class="form-control" id="f1" value="20" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Width (ft)</label><input type="number" class="form-control" id="f2" value="10" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Depth (inches)</label><input type="number" class="form-control" id="f3" value="4" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Material</label>
<select class="form-select" id="f4">
<option value="1.4">Gravel (1.4 t/m&#179;)</option>
<option value="1.5">Crushed Stone (1.5 t/m&#179;)</option>
<option value="1.6">Sand (1.6 t/m&#179;)</option>
<option value="1.2">Pea Gravel (1.2 t/m&#179;)</option>
</select></div>
<div class="col-md-6"><label class="form-label">Price Per Ton ($)</label><input type="number" class="form-control" id="f5" value="50" step="1"></div>
</div>""",
[("Cubic Yards","r1"),("Cubic Meters","r2"),("Weight (Tons)","r3"),("Total Cost","r4")],
"Calculate Gravel"),
"""<script>
function calc(){const l=+document.getElementById('f1').value,w=+document.getElementById('f2').value,d=+document.getElementById('f3').value/12,dens=+document.getElementById('f4').value,price=+document.getElementById('f5').value;const cf=l*w*d,cy=cf/27,cm=cy*0.7646,tons=cm*dens;document.getElementById('r1').textContent=cy.toFixed(2)+' cu yd';document.getElementById('r2').textContent=cm.toFixed(2)+' m\u00B3';document.getElementById('r3').textContent=tons.toFixed(2)+' tons';document.getElementById('r4').textContent='$'+(tons*price).toFixed(2);document.getElementById('resultBox').classList.add('show');}
</script>""")

page("drywall-calculator.html","Drywall Calculator",
"Calculate how many drywall sheets you need for any room. Accounts for doors, windows, and waste factor.",
"drywall calculator, sheetrock calculator, how many drywall sheets, drywall cost calculator, gypsum board calculator",
"&#127959;","#546e7a","#607d8b","construction","&#127959;","Construction",
calc_box("Drywall Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Room Length (ft)</label><input type="number" class="form-control" id="f1" value="15" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Room Width (ft)</label><input type="number" class="form-control" id="f2" value="12" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Ceiling Height (ft)</label><input type="number" class="form-control" id="f3" value="9" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Number of Doors</label><input type="number" class="form-control" id="f4" value="1" min="0"></div>
<div class="col-md-6"><label class="form-label">Number of Windows</label><input type="number" class="form-control" id="f5" value="2" min="0"></div>
<div class="col-md-6"><label class="form-label">Sheet Size</label>
<select class="form-select" id="f6"><option value="32">4x8 ft (32 sq ft)</option><option value="48">4x12 ft (48 sq ft)</option></select></div>
</div>""",
[("Wall Area (sq ft)","r1"),("Sheets Needed","r2"),("With 10% Waste","r3"),("Ceiling Sheets","r4")],
"Calculate Drywall"),
"""<script>
function calc(){const l=+document.getElementById('f1').value,w=+document.getElementById('f2').value,h=+document.getElementById('f3').value,d=+document.getElementById('f4').value,win=+document.getElementById('f5').value,sh=+document.getElementById('f6').value;const perim=2*(l+w),wallArea=perim*h-d*21-win*15,ceil=l*w,sheets=Math.ceil(wallArea/sh*1.1),ceilSh=Math.ceil(ceil/sh*1.1);document.getElementById('r1').textContent=wallArea.toFixed(0)+' sq ft';document.getElementById('r2').textContent=Math.ceil(wallArea/sh)+' sheets';document.getElementById('r3').textContent=sheets+' sheets';document.getElementById('r4').textContent=ceilSh+' sheets';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("roof-pitch-calculator.html","Roof Pitch Calculator",
"Calculate roof pitch, angle, rafter length, and roof area. Convert between pitch ratio, degrees, and percentage.",
"roof pitch calculator, roof slope calculator, rafter length calculator, roof angle calculator, roof area calculator",
"&#127959;","#4a148c","#6a1b9a","construction","&#127959;","Construction",
calc_box("Roof Pitch Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Rise (vertical inches per 12")</label><input type="number" class="form-control" id="f1" value="6" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Roof Span / Width (ft)</label><input type="number" class="form-control" id="f2" value="30" step="0.5"></div>
</div>""",
[("Roof Pitch","r1"),("Angle (degrees)","r2"),("Rafter Length","r3"),("Roof Multiplier","r4")],
"Calculate Roof Pitch"),
"""<script>
function calc(){const rise=+document.getElementById('f1').value,span=+document.getElementById('f2').value;const run=span/2,angle=Math.atan(rise/12)*180/Math.PI,rafter=Math.sqrt(run*run+((rise/12)*run)*((rise/12)*run)),mult=Math.sqrt(1+(rise/12)*(rise/12));document.getElementById('r1').textContent=rise+'/12 pitch';document.getElementById('r2').textContent=angle.toFixed(2)+'°';document.getElementById('r3').textContent=rafter.toFixed(2)+' ft';document.getElementById('r4').textContent=mult.toFixed(4);document.getElementById('resultBox').classList.add('show');}
</script>""")

# ===========================
# EDUCATION
# ===========================

page("cgpa-to-percentage-calculator.html","CGPA to Percentage Calculator",
"Convert CGPA to percentage and percentage to CGPA. Supports all university scales: 10, 7, 5, and 4 point GPA.",
"CGPA to percentage calculator, CGPA calculator, GPA to percentage, percentage to CGPA, university grade calculator",
"&#127979;","#1a237e","#283593","education","&#127979;","Education",
"""<div class="calc-box">
<h2 class="calc-title">CGPA to Percentage Converter</h2>
<div class="d-flex gap-2 mb-3 flex-wrap">
<button class="cat-pill active" onclick="setMode('cgpa',this)">CGPA to %</button>
<button class="cat-pill" onclick="setMode('pct',this)">% to CGPA</button>
</div>
<div class="row g-3">
<div class="col-md-6"><label class="form-label" id="inputLabel">Your CGPA</label><input type="number" class="form-control" id="f1" value="8.5" step="0.01"></div>
<div class="col-md-6"><label class="form-label">GPA Scale</label>
<select class="form-select" id="f2">
<option value="10">10.0 Scale (Indian Universities)</option>
<option value="7">7.0 Scale</option>
<option value="5">5.0 Scale</option>
<option value="4">4.0 Scale (US)</option>
</select></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-mortarboard me-2"></i>Convert</button>
<div class="result-box" id="resultBox">
<div class="row g-3 text-center">
<div class="col-6"><div class="result-label" id="r1Label">Percentage</div><div class="result-value" id="r1">-</div></div>
<div class="col-6"><div class="result-label">Grade</div><div class="result-value" id="r2">-</div></div>
<div class="col-6"><div class="result-label">Class</div><div class="result-value" id="r3">-</div></div>
<div class="col-6"><div class="result-label">GPA Scale</div><div class="result-value" id="r4">-</div></div>
</div></div></div>""",
"""<script>
let eduMode='cgpa';
function setMode(m,b){eduMode=m;document.querySelectorAll('.cat-pill').forEach(p=>p.classList.remove('active'));b.classList.add('active');document.getElementById('inputLabel').textContent=m==='cgpa'?'Your CGPA':'Your Percentage (%)';}
function calc(){const v=+document.getElementById('f1').value,scale=+document.getElementById('f2').value;let pct,cgpa;if(eduMode==='cgpa'){cgpa=v;pct=scale===10?v*9.5:scale===4?(v/4*100):(v/scale*100);}else{pct=v;cgpa=scale===10?v/9.5:scale===4?v/100*4:v/100*scale;}let grade,cls;if(pct>=90){grade='O / A+';cls='Outstanding';}else if(pct>=75){grade='A';cls='First Class with Distinction';}else if(pct>=60){grade='B';cls='First Class';}else if(pct>=50){grade='C';cls='Second Class';}else if(pct>=40){grade='D';cls='Pass';}else{grade='F';cls='Fail';}document.getElementById('r1').textContent=pct.toFixed(2)+'%';document.getElementById('r2').textContent=grade;document.getElementById('r3').textContent=cls;document.getElementById('r4').textContent=scale+'.0 Scale';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("exam-score-calculator.html","Exam Score & Grade Calculator",
"Calculate your exam score percentage, letter grade, and class position. Works with any grading system.",
"exam score calculator, test score percentage, letter grade calculator, marks to percentage, grade calculator",
"&#128203;","#0d47a1","#1565c0","education","&#127979;","Education",
calc_box("Exam Score Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Marks Obtained</label><input type="number" class="form-control" id="f1" value="85" step="1"></div>
<div class="col-md-6"><label class="form-label">Total Marks</label><input type="number" class="form-control" id="f2" value="100" step="1"></div>
<div class="col-md-6"><label class="form-label">Passing Marks</label><input type="number" class="form-control" id="f3" value="40" step="1"></div>
<div class="col-md-6"><label class="form-label">Grading System</label>
<select class="form-select" id="f4">
<option value="us">US (A, B, C, D, F)</option>
<option value="in" selected>India (O, A+, A, B, C)</option>
</select></div>
</div>""",
[("Score (%)","r1"),("Letter Grade","r2"),("Pass/Fail","r3"),("Rank Category","r4")],
"Calculate Score"),
"""<script>
function calc(){const got=+document.getElementById('f1').value,tot=+document.getElementById('f2').value,pass=+document.getElementById('f3').value,sys=document.getElementById('f4').value;const pct=got/tot*100;let grade,rank;if(sys==='us'){grade=pct>=90?'A+':pct>=80?'A':pct>=70?'B':pct>=60?'C':pct>=50?'D':'F';}else{grade=pct>=90?'O':pct>=80?'A+':pct>=70?'A':pct>=60?'B+':pct>=50?'B':pct>=40?'C':'F';}rank=pct>=90?'Distinction':pct>=75?'First Class':pct>=60?'Second Class':pct>=pass?'Pass':'Fail';document.getElementById('r1').textContent=pct.toFixed(2)+'%';document.getElementById('r2').textContent=grade;document.getElementById('r3').textContent=got>=pass?'PASS \u2713':'FAIL \u2717';document.getElementById('r4').textContent=rank;document.getElementById('resultBox').classList.add('show');}
</script>""")

# ===========================
# LIFESTYLE
# ===========================

page("pet-age-calculator.html","Pet Age Calculator",
"Calculate your pet's age in human years. Dog age, cat age, rabbit age in human years calculator.",
"pet age calculator, dog age in human years, cat age in human years, dog years calculator, pet human age",
"&#128054;","#e65100","#f57c00","lifestyle","&#127774;","Lifestyle",
"""<div class="calc-box">
<h2 class="calc-title">Pet Age Calculator</h2>
<div class="row g-3">
<div class="col-md-6"><label class="form-label">Pet Age (years)</label><input type="number" class="form-control" id="f1" value="5" step="0.5" min="0"></div>
<div class="col-md-6"><label class="form-label">Pet Type</label>
<select class="form-select" id="f2" onchange="calc()">
<option value="dog_small">Dog (Small, <9kg)</option>
<option value="dog_med" selected>Dog (Medium, 9-22kg)</option>
<option value="dog_large">Dog (Large, 22-40kg)</option>
<option value="cat">Cat</option>
<option value="rabbit">Rabbit</option>
<option value="hamster">Hamster</option>
</select></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-heart me-2"></i>Calculate Age</button>
<div class="result-box" id="resultBox">
<div class="row g-3 text-center">
<div class="col-6"><div class="result-label">Human Age Equivalent</div><div class="result-value" id="r1">-</div></div>
<div class="col-6"><div class="result-label">Life Stage</div><div class="result-value" id="r2">-</div></div>
<div class="col-6"><div class="result-label">Pet Age</div><div class="result-value" id="r3">-</div></div>
<div class="col-6"><div class="result-label">Average Lifespan</div><div class="result-value" id="r4">-</div></div>
</div></div></div>""",
"""<script>
function calc(){const y=+document.getElementById('f1').value,type=document.getElementById('f2').value;let human,stage,lifespan;const dogMults={dog_small:[15,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80],dog_med:[15,24,28,32,36,40,44,48,51,54,57,60,63,66,69,72],dog_large:[15,24,28,32,36,42,47,51,55,60,64,69,73,77,82,86]};if(type.startsWith('dog')){const m=dogMults[type];const y_=Math.floor(Math.min(y,m.length));human=y_<m.length?m[y_]:m[m.length-1]+(y-m.length)*5;lifespan=type==='dog_small'?15:type==='dog_med'?13:11;}else if(type==='cat'){human=y<=1?y*15:y<=2?24+(y-1)*4:28+(y-2)*4;lifespan=15;}else if(type==='rabbit'){human=y*9;lifespan=10;}else{human=y*14;lifespan=2.5;}const pct=y/lifespan;stage=pct<0.15?'Puppy/Kitten':pct<0.3?'Juvenile':pct<0.6?'Adult':pct<0.8?'Mature':'Senior';document.getElementById('r1').textContent=Math.round(human)+' years';document.getElementById('r2').textContent=stage;document.getElementById('r3').textContent=y+' pet years';document.getElementById('r4').textContent=lifespan+' years';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("lucky-number-calculator.html","Lucky Number Calculator",
"Find your lucky numbers based on your name and birthdate. Numerology life path number, destiny number, and more.",
"lucky number calculator, numerology calculator, life path number, destiny number, name number, lucky number by name",
"&#127807;","#880e4f","#ad1457","lifestyle","&#127774;","Lifestyle",
"""<div class="calc-box">
<h2 class="calc-title">Numerology &amp; Lucky Number Calculator</h2>
<div class="row g-3">
<div class="col-md-6"><label class="form-label">Full Name</label><input type="text" class="form-control" id="f1" value="John Smith" placeholder="Enter your full name"></div>
<div class="col-md-6"><label class="form-label">Date of Birth</label><input type="date" class="form-control" id="f2"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-stars me-2"></i>Find Lucky Numbers</button>
<div class="result-box" id="resultBox">
<div class="row g-3 text-center">
<div class="col-6"><div class="result-label">Life Path Number</div><div class="result-value" id="r1">-</div></div>
<div class="col-6"><div class="result-label">Destiny Number</div><div class="result-value" id="r2">-</div></div>
<div class="col-6"><div class="result-label">Soul Number</div><div class="result-value" id="r3">-</div></div>
<div class="col-6"><div class="result-label">Lucky Color</div><div class="result-value" id="r4">-</div></div>
</div>
<div id="r5" style="margin-top:12px;text-align:center;font-size:0.9rem;color:var(--text-secondary)"></div>
</div></div>""",
"""<script>
document.getElementById('f2').valueAsDate=new Date('1990-05-15');
function reduce(n){while(n>9&&n!==11&&n!==22&&n!==33){const s=String(n).split('').reduce((a,b)=>a+ +b,0);n=s;}return n;}
function nameNum(name,vowels=false){const v='AEIOU',map={A:1,B:2,C:3,D:4,E:5,F:6,G:7,H:8,I:9,J:1,K:2,L:3,M:4,N:5,O:6,P:7,Q:8,R:9,S:1,T:2,U:3,V:4,W:5,X:6,Y:7,Z:8};return reduce(name.toUpperCase().split('').filter(c=>vowels?v.includes(c):/[A-Z]/.test(c)).map(c=>map[c]||0).reduce((a,b)=>a+b,0));}
const lucky=[null,'Red','Orange','Yellow','Green','Blue','Indigo','Violet','Pink','Gold'];
function calc(){const name=document.getElementById('f1').value,dob=document.getElementById('f2').value;if(!dob)return;const d=new Date(dob);const lp=reduce(d.getFullYear()+d.getMonth()+1+d.getDate());const dest=nameNum(name);const soul=nameNum(name,true);document.getElementById('r1').textContent=lp;document.getElementById('r2').textContent=dest;document.getElementById('r3').textContent=soul;document.getElementById('r4').textContent=lucky[lp]||'Gold';document.getElementById('r5').textContent='Lucky Numbers: '+[lp,dest,soul,(lp+dest)%9+1].join(', ');document.getElementById('resultBox').classList.add('show');}
</script>""")

page("zodiac-sign-calculator.html","Zodiac Sign Calculator",
"Find your zodiac sign by birthday. Get Western astrology sun sign and Chinese zodiac animal sign.",
"zodiac sign calculator, what is my zodiac sign, zodiac birthday calculator, sun sign calculator, Chinese zodiac",
"&#9733;","#4a148c","#6a1b9a","lifestyle","&#127774;","Lifestyle",
"""<div class="calc-box">
<h2 class="calc-title">Zodiac Sign Calculator</h2>
<div class="row g-3">
<div class="col-md-6"><label class="form-label">Date of Birth</label><input type="date" class="form-control" id="f1"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-stars me-2"></i>Find Zodiac Sign</button>
<div class="result-box" id="resultBox">
<div class="row g-3 text-center">
<div class="col-6"><div class="result-label">Western Zodiac</div><div class="result-value" id="r1">-</div></div>
<div class="col-6"><div class="result-label">Element</div><div class="result-value" id="r2">-</div></div>
<div class="col-6"><div class="result-label">Chinese Zodiac</div><div class="result-value" id="r3">-</div></div>
<div class="col-6"><div class="result-label">Ruling Planet</div><div class="result-value" id="r4">-</div></div>
</div>
<div id="r5" style="margin-top:10px;text-align:center;font-size:0.9rem;color:var(--text-secondary)"></div>
</div></div>""",
"""<script>
document.getElementById('f1').valueAsDate=new Date();
const signs=[{n:'Capricorn',el:'Earth',planet:'Saturn',dates:'Dec 22 - Jan 19',traits:'Disciplined, responsible, ambitious'},{n:'Aquarius',el:'Air',planet:'Uranus',dates:'Jan 20 - Feb 18',traits:'Independent, innovative, humanitarian'},{n:'Pisces',el:'Water',planet:'Neptune',dates:'Feb 19 - Mar 20',traits:'Compassionate, intuitive, artistic'},{n:'Aries',el:'Fire',planet:'Mars',dates:'Mar 21 - Apr 19',traits:'Bold, ambitious, confident'},{n:'Taurus',el:'Earth',planet:'Venus',dates:'Apr 20 - May 20',traits:'Reliable, patient, practical'},{n:'Gemini',el:'Air',planet:'Mercury',dates:'May 21 - Jun 20',traits:'Versatile, expressive, curious'},{n:'Cancer',el:'Water',planet:'Moon',dates:'Jun 21 - Jul 22',traits:'Intuitive, sentimental, loyal'},{n:'Leo',el:'Fire',planet:'Sun',dates:'Jul 23 - Aug 22',traits:'Generous, creative, enthusiastic'},{n:'Virgo',el:'Earth',planet:'Mercury',dates:'Aug 23 - Sep 22',traits:'Analytical, practical, diligent'},{n:'Libra',el:'Air',planet:'Venus',dates:'Sep 23 - Oct 22',traits:'Diplomatic, fair, social'},{n:'Scorpio',el:'Water',planet:'Pluto',dates:'Oct 23 - Nov 21',traits:'Resourceful, brave, passionate'},{n:'Sagittarius',el:'Fire',planet:'Jupiter',dates:'Nov 22 - Dec 21',traits:'Generous, idealistic, adventurous'}];
const chinese=['Monkey','Rooster','Dog','Pig','Rat','Ox','Tiger','Rabbit','Dragon','Snake','Horse','Goat'];
function getSign(d){const m=d.getMonth()+1,day=d.getDate();const bounds=[[1,20],[2,19],[3,20],[4,20],[5,21],[6,21],[7,23],[8,23],[9,23],[10,23],[11,22],[12,22]];let idx=m-1;if(day<bounds[idx][1])idx=(idx-1+12)%12;return signs[idx];}
function calc(){const d=new Date(document.getElementById('f1').value);if(isNaN(d))return;const s=getSign(d);const ch=chinese[(d.getFullYear()-2004)%12];document.getElementById('r1').textContent=s.n;document.getElementById('r2').textContent=s.el;document.getElementById('r3').textContent=ch;document.getElementById('r4').textContent=s.planet;document.getElementById('r5').textContent=s.dates+' \u2022 '+s.traits;document.getElementById('resultBox').classList.add('show');}
</script>""")

# ===========================
# TECH / DEVELOPER
# ===========================

page("aspect-ratio-calculator.html","Aspect Ratio Calculator",
"Calculate aspect ratio of any screen or image. Scale resolution while maintaining aspect ratio for any display.",
"aspect ratio calculator, screen resolution calculator, image ratio calculator, 16:9 calculator, resolution scale",
"&#128250;","#1a237e","#283593","tech","&#128187;","Tech & Dev",
calc_box("Aspect Ratio Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Width (px)</label><input type="number" class="form-control" id="f1" value="1920" step="1"></div>
<div class="col-md-6"><label class="form-label">Height (px)</label><input type="number" class="form-control" id="f2" value="1080" step="1"></div>
<div class="col-md-6"><label class="form-label">New Width (px)</label><input type="number" class="form-control" id="f3" value="1280" step="1"></div>
</div>""",
[("Aspect Ratio","r1"),("New Height","r2"),("Total Pixels","r3"),("Diagonal (at 96 PPI)","r4")],
"Calculate Ratio"),
"""<script>
function gcd(a,b){return b===0?a:gcd(b,a%b);}
function calc(){const w=+document.getElementById('f1').value,h=+document.getElementById('f2').value,nw=+document.getElementById('f3').value;const g=gcd(w,h),rw=w/g,rh=h/g,nh=Math.round(nw*h/w),diag=Math.sqrt(w*w+h*h)/96;document.getElementById('r1').textContent=rw+':'+rh;document.getElementById('r2').textContent=nh+' px';document.getElementById('r3').textContent=(w*h).toLocaleString()+' px';document.getElementById('r4').textContent=diag.toFixed(2)+'"';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("download-time-calculator.html","Download Time Calculator",
"Calculate how long it takes to download a file based on file size and internet connection speed.",
"download time calculator, how long to download, internet speed calculator, file download time, bandwidth calculator",
"&#128190;","#0d47a1","#1565c0","tech","&#128187;","Tech & Dev",
calc_box("Download Time Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">File Size</label><input type="number" class="form-control" id="f1" value="1" step="0.1"></div>
<div class="col-md-6"><label class="form-label">File Size Unit</label>
<select class="form-select" id="f2">
<option value="1">MB (Megabytes)</option>
<option value="1024" selected>GB (Gigabytes)</option>
<option value="0.001">KB (Kilobytes)</option>
</select></div>
<div class="col-md-6"><label class="form-label">Connection Speed (Mbps)</label><input type="number" class="form-control" id="f3" value="100" step="1"></div>
</div>""",
[("Download Time","r1"),("File Size (MB)","r2"),("Transfer Speed","r3"),("Data in Bits","r4")],
"Calculate Download Time"),
"""<script>
function fmt(s){if(s<60)return s.toFixed(1)+' seconds';if(s<3600)return (s/60).toFixed(1)+' minutes';return (s/3600).toFixed(2)+' hours';}
function calc(){const fs=+document.getElementById('f1').value,unit=+document.getElementById('f2').value,spd=+document.getElementById('f3').value;const mb=fs*unit,bits=mb*8*1000000,bps=spd*1000000,sec=bits/bps;document.getElementById('r1').textContent=fmt(sec);document.getElementById('r2').textContent=mb.toFixed(2)+' MB';document.getElementById('r3').textContent=spd+' Mbps';document.getElementById('r4').textContent=(bits/1e9).toFixed(2)+' Gb';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("color-code-converter.html","Color Code Converter",
"Convert between HEX, RGB, HSL, HSV, and CMYK color codes. Pick any color and get all color format values instantly.",
"color code converter, hex to rgb, rgb to hex, color converter, HEX RGB HSL converter, CSS color codes",
"&#127774;","#880e4f","#ad1457","tech","&#128187;","Tech & Dev",
"""<div class="calc-box">
<h2 class="calc-title">Color Code Converter</h2>
<div class="row g-3 align-items-end">
<div class="col-md-4"><label class="form-label">Pick a Color</label><input type="color" class="form-control form-control-color w-100" id="cpick" value="#3B82F6" oninput="fromPicker()"></div>
<div class="col-md-4"><label class="form-label">HEX Code</label><input type="text" class="form-control" id="hexIn" value="#3B82F6" placeholder="#RRGGBB"></div>
<div class="col-md-4 d-flex align-items-end"><button class="btn-calculate w-100" onclick="calc()">Convert</button></div>
</div>
<div class="result-box show" id="resultBox" style="margin-top:16px">
<div style="height:80px;border-radius:12px;margin-bottom:12px" id="colorPreview"></div>
<div id="colorResults" style="font-size:0.9rem"></div>
</div></div>""",
"""<script>
function hexToRgb(hex){const r=parseInt(hex.slice(1,3),16),g=parseInt(hex.slice(3,5),16),b=parseInt(hex.slice(5,7),16);return{r,g,b};}
function rgbToHsl(r,g,b){r/=255;g/=255;b/=255;const max=Math.max(r,g,b),min=Math.min(r,g,b);let h,s,l=(max+min)/2;if(max===min){h=s=0;}else{const d=max-min;s=l>0.5?d/(2-max-min):d/(max+min);switch(max){case r:h=(g-b)/d+(g<b?6:0);break;case g:h=(b-r)/d+2;break;case b:h=(r-g)/d+4;break;}h/=6;}return{h:Math.round(h*360),s:Math.round(s*100),l:Math.round(l*100)};}
function fromPicker(){document.getElementById('hexIn').value=document.getElementById('cpick').value;calc();}
function calc(){let hex=document.getElementById('hexIn').value.trim();if(!hex.startsWith('#'))hex='#'+hex;if(!/^#[0-9A-Fa-f]{6}$/.test(hex))return;document.getElementById('cpick').value=hex;const{r,g,b}=hexToRgb(hex);const{h,s,l}=rgbToHsl(r,g,b);document.getElementById('colorPreview').style.background=hex;document.getElementById('colorResults').innerHTML=`
<div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid var(--border)"><span>HEX</span><code>${hex.toUpperCase()}</code></div>
<div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid var(--border)"><span>RGB</span><code>rgb(${r}, ${g}, ${b})</code></div>
<div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid var(--border)"><span>HSL</span><code>hsl(${h}, ${s}%, ${l}%)</code></div>
<div style="display:flex;justify-content:space-between;padding:6px 0"><span>CSS Variable</span><code>--color: ${hex.toUpperCase()}</code></div>`;document.getElementById('resultBox').classList.add('show');}
document.addEventListener('DOMContentLoaded',calc);
</script>""")

page("ip-subnet-calculator.html","IP Subnet Calculator",
"Calculate IP subnet mask, network address, broadcast address, and host range for any IP/CIDR notation.",
"IP subnet calculator, subnet mask calculator, CIDR calculator, network address calculator, IP address range",
"&#127760;","#0d47a1","#1565c0","tech","&#128187;","Tech & Dev",
"""<div class="calc-box">
<h2 class="calc-title">IP Subnet Calculator</h2>
<div class="row g-3">
<div class="col-md-6"><label class="form-label">IP Address</label><input type="text" class="form-control" id="f1" value="192.168.1.0" placeholder="e.g. 192.168.1.0"></div>
<div class="col-md-6"><label class="form-label">Subnet Prefix Length (CIDR)</label>
<select class="form-select" id="f2">
<option value="8">/8 (255.0.0.0)</option>
<option value="16">/16 (255.255.0.0)</option>
<option value="24" selected>/24 (255.255.255.0)</option>
<option value="25">/25 (255.255.255.128)</option>
<option value="26">/26 (255.255.255.192)</option>
<option value="27">/27 (255.255.255.224)</option>
<option value="28">/28 (255.255.255.240)</option>
<option value="29">/29 (255.255.255.248)</option>
<option value="30">/30 (255.255.255.252)</option>
</select></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-diagram-3 me-2"></i>Calculate Subnet</button>
<div class="result-box" id="resultBox"><div id="subnetResults" style="font-size:0.9rem"></div></div></div>""",
"""<script>
function calc(){const ip=document.getElementById('f1').value,cidr=+document.getElementById('f2').value;const parts=ip.split('.').map(Number);if(parts.length!==4)return;const ipInt=parts.reduce((a,b)=>(a<<8)|b)>>>0;const mask=cidr===0?0:(0xFFFFFFFF<<(32-cidr))>>>0;const network=(ipInt&mask)>>>0;const broadcast=(network|(~mask>>>0))>>>0;const hosts=Math.pow(2,32-cidr)-2;function toIP(n){return [(n>>>24)&255,(n>>>16)&255,(n>>>8)&255,n&255].join('.');}const results=[['Network Address',toIP(network)],['Subnet Mask',toIP(mask)],['Broadcast Address',toIP(broadcast)],['First Usable Host',toIP(network+1)],['Last Usable Host',toIP(broadcast-1)],['Total Hosts',hosts.toLocaleString()],['CIDR Notation',ip+'/'+cidr]];document.getElementById('subnetResults').innerHTML=results.map(([k,v])=>`<div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid var(--border)"><span>${k}</span><code>${v}</code></div>`).join('');document.getElementById('resultBox').classList.add('show');}
</script>""")

print("\n=== All calculators created successfully! ===")
print(f"Script finished.")
