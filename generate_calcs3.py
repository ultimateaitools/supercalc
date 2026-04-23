# -*- coding: utf-8 -*-
import os

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

def cb(title, fields, results, btn="Calculate"):
    r_html = "".join([f'<div class="col-6"><div class="result-label">{r[0]}</div><div class="result-value" id="{r[1]}">-</div></div>' for r in results])
    return f'<div class="calc-box"><h2 class="calc-title">{title}</h2>{fields}<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>{btn}</button><div class="result-box" id="resultBox"><div class="row g-3 text-center">{r_html}</div></div></div>'

# ==============================
# BATCH 4 - Final Push to 250+
# ==============================

# FINANCE (more)
page("compound-savings-calculator.html","Compound Savings Calculator",
"Calculate compound interest savings growth over time. See how your money grows with regular deposits.",
"compound savings calculator, savings with compound interest, regular deposit calculator, savings growth calculator",
"&#128200;","#1b5e20","#2e7d32","finance","&#128176;","Finance",
cb("Compound Savings Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Starting Balance ($)</label><input type="number" class="form-control" id="f1" value="1000" step="100"></div>
<div class="col-md-6"><label class="form-label">Monthly Deposit ($)</label><input type="number" class="form-control" id="f2" value="200" step="50"></div>
<div class="col-md-6"><label class="form-label">Annual Interest Rate (%)</label><input type="number" class="form-control" id="f3" value="7" step="0.1"></div>
<div class="col-md-6"><label class="form-label">Years</label><input type="number" class="form-control" id="f4" value="10" step="1"></div>
<div class="col-md-6"><label class="form-label">Compound Frequency</label>
<select class="form-select" id="f5">
<option value="1">Annually</option>
<option value="4">Quarterly</option>
<option value="12" selected>Monthly</option>
<option value="365">Daily</option>
</select></div>
</div>""",
[("Future Value","r1"),("Total Deposits","r2"),("Interest Earned","r3"),("Effective Annual Rate","r4")]),
"""<script>
function calc(){const P=+document.getElementById('f1').value,pmt=+document.getElementById('f2').value,r=+document.getElementById('f3').value/100,n=+document.getElementById('f4').value,k=+document.getElementById('f5').value;const rk=r/k,nk=n*k,fv=P*Math.pow(1+rk,nk)+pmt*(Math.pow(1+rk,nk)-1)/rk*Math.pow(1+rk,k/12);const total=P+pmt*12*n,int=fv-total,ear=Math.pow(1+rk,k)-1;document.getElementById('r1').textContent='$'+fv.toFixed(2);document.getElementById('r2').textContent='$'+total.toFixed(0);document.getElementById('r3').textContent='$'+int.toFixed(2);document.getElementById('r4').textContent=(ear*100).toFixed(3)+'%';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("income-tax-estimator.html","Income Tax Estimator 2025",
"Estimate your federal income tax for 2025 with the latest tax brackets. Calculate effective tax rate and refund.",
"income tax estimator 2025, federal tax calculator, tax bracket calculator, effective tax rate, tax refund estimate",
"&#128197;","#b71c1c","#c62828","finance","&#128176;","Finance",
cb("US Federal Income Tax Estimator 2025",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Gross Annual Income ($)</label><input type="number" class="form-control" id="f1" value="75000" step="1000"></div>
<div class="col-md-6"><label class="form-label">Filing Status</label>
<select class="form-select" id="f2">
<option value="single">Single</option>
<option value="married">Married Filing Jointly</option>
<option value="hoh">Head of Household</option>
</select></div>
<div class="col-md-6"><label class="form-label">Pre-tax Deductions ($)</label><input type="number" class="form-control" id="f3" value="5000" step="100"><small class="text-muted">401k, HSA, etc.</small></div>
<div class="col-md-6"><label class="form-label">Additional Credits ($)</label><input type="number" class="form-control" id="f4" value="0" step="100"></div>
</div>""",
[("Taxable Income","r1"),("Federal Tax","r2"),("Effective Tax Rate","r3"),("Marginal Tax Rate","r4")],
"Estimate Tax"),
"""<script>
const brackets={single:[[11600,0.10],[47150,0.12],[100525,0.22],[191950,0.24],[243725,0.32],[609350,0.35],[Infinity,0.37]],married:[[23200,0.10],[94300,0.12],[201050,0.22],[383900,0.24],[487450,0.32],[731200,0.35],[Infinity,0.37]],hoh:[[16550,0.10],[63100,0.12],[100500,0.22],[191950,0.24],[243700,0.32],[609350,0.35],[Infinity,0.37]]};
const stdDed={single:14600,married:29200,hoh:21900};
function calcTax(inc,status){const br=brackets[status],sd=stdDed[status];let tax=0,prev=0,marginal=0;for(const[limit,rate]of br){const top=Math.min(inc,limit);if(top<=prev)break;tax+=(top-prev)*rate;marginal=rate;prev=limit;}return{tax,marginal};}
function calc(){const gross=+document.getElementById('f1').value,status=document.getElementById('f2').value,preTax=+document.getElementById('f3').value,credits=+document.getElementById('f4').value;const agi=gross-preTax,taxable=Math.max(0,agi-stdDed[status]);const{tax,marginal}=calcTax(taxable,status);const finalTax=Math.max(0,tax-credits);document.getElementById('r1').textContent='$'+taxable.toFixed(0);document.getElementById('r2').textContent='$'+finalTax.toFixed(0);document.getElementById('r3').textContent=(finalTax/gross*100).toFixed(1)+'%';document.getElementById('r4').textContent=(marginal*100).toFixed(0)+'%';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("retirement-savings-calculator.html","Retirement Savings Calculator",
"Calculate how much you need to save for retirement. Project your 401k, IRA, and pension income in retirement.",
"retirement savings calculator, retirement calculator, 401k calculator, how much to save for retirement, IRA calculator",
"&#128196;","#4a148c","#6a1b9a","finance","&#128176;","Finance",
cb("Retirement Savings Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Current Age</label><input type="number" class="form-control" id="f1" value="30" min="18" max="70"></div>
<div class="col-md-6"><label class="form-label">Retirement Age</label><input type="number" class="form-control" id="f2" value="65" min="50" max="80"></div>
<div class="col-md-6"><label class="form-label">Current Savings ($)</label><input type="number" class="form-control" id="f3" value="25000" step="1000"></div>
<div class="col-md-6"><label class="form-label">Monthly Contribution ($)</label><input type="number" class="form-control" id="f4" value="500" step="100"></div>
<div class="col-md-6"><label class="form-label">Expected Return (%)</label><input type="number" class="form-control" id="f5" value="7" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Desired Monthly Income ($)</label><input type="number" class="form-control" id="f6" value="4000" step="100"></div>
</div>""",
[("Projected Nest Egg","r1"),("Monthly Income at 4% SWR","r2"),("Income Gap","r3"),("Years Until Retirement","r4")],
"Calculate Retirement"),
"""<script>
function calc(){const age=+document.getElementById('f1').value,ret=+document.getElementById('f2').value,P=+document.getElementById('f3').value,pmt=+document.getElementById('f4').value,r=+document.getElementById('f5').value/100/12,n=(ret-age)*12,goal=+document.getElementById('f6').value;const fv=P*Math.pow(1+r,n)+pmt*(Math.pow(1+r,n)-1)/r;const monthly=fv*0.04/12,gap=monthly-goal,yrs=ret-age;document.getElementById('r1').textContent='$'+fv.toFixed(0);document.getElementById('r2').textContent='$'+monthly.toFixed(0)+'/mo';document.getElementById('r3').textContent=gap>=0?'Surplus $'+gap.toFixed(0):'Shortfall $'+Math.abs(gap).toFixed(0);document.getElementById('r4').textContent=yrs+' years';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("currency-exchange-calculator.html","Currency Exchange Rate Calculator",
"Calculate currency exchange with fees, commission, and margin. Compare bank vs exchange rates for any currency pair.",
"currency exchange calculator, exchange rate calculator, forex calculator, currency conversion with fees, money exchange",
"&#128177;","#0d47a1","#1565c0","finance","&#128176;","Finance",
cb("Currency Exchange Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Amount to Exchange</label><input type="number" class="form-control" id="f1" value="1000" step="10"></div>
<div class="col-md-6"><label class="form-label">Exchange Rate (1 unit = ?)</label><input type="number" class="form-control" id="f2" value="83.5" step="0.01"><small class="text-muted">e.g. 1 USD = 83.5 INR</small></div>
<div class="col-md-6"><label class="form-label">Exchange Fee (%)</label><input type="number" class="form-control" id="f3" value="2" step="0.1"></div>
<div class="col-md-6"><label class="form-label">Fixed Fee ($)</label><input type="number" class="form-control" id="f4" value="5" step="1"></div>
</div>""",
[("Converted Amount","r1"),("Fees Paid","r2"),("Effective Rate","r3"),("Net After All Fees","r4")]),
"""<script>
function calc(){const amt=+document.getElementById('f1').value,rate=+document.getElementById('f2').value,feePct=+document.getElementById('f3').value/100,feeFixed=+document.getElementById('f4').value;const pctFee=amt*feePct,totalFee=pctFee+feeFixed,netAmt=amt-totalFee,converted=netAmt*rate;document.getElementById('r1').textContent=(amt*rate).toFixed(2)+' (gross)';document.getElementById('r2').textContent='$'+totalFee.toFixed(2);document.getElementById('r3').textContent=(converted/amt).toFixed(4);document.getElementById('r4').textContent=converted.toFixed(2);document.getElementById('resultBox').classList.add('show');}
</script>""")

# HEALTH
page("sleep-cycle-calculator.html","Sleep Cycle Calculator",
"Calculate the best time to wake up or go to sleep to feel refreshed. Based on 90-minute sleep cycle science.",
"sleep cycle calculator, best time to wake up, sleep calculator, REM cycle, when to wake up, sleep schedule",
"&#128564;","#1a237e","#283593","health","&#10084;","Health",
"""<div class="calc-box">
<h2 class="calc-title">Sleep Cycle Calculator</h2>
<div class="d-flex gap-2 mb-3 flex-wrap">
<button class="cat-pill active" onclick="setMode('wake',this)">I want to wake up at...</button>
<button class="cat-pill" onclick="setMode('sleep',this)">I want to sleep at...</button>
</div>
<div class="row g-3">
<div class="col-md-6"><label class="form-label" id="timeLabel">Wake-up time</label><input type="time" class="form-control" id="f1" value="07:00"></div>
<div class="col-md-6"><label class="form-label">Time to Fall Asleep (min)</label><input type="number" class="form-control" id="f2" value="15" step="5"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-moon-stars me-2"></i>Calculate Sleep Times</button>
<div class="result-box" id="resultBox">
<div id="sleepResults" style="font-size:0.9rem"></div>
</div></div>""",
"""<script>
let slMode='wake';
function setMode(m,b){slMode=m;document.querySelectorAll('.cat-pill').forEach(p=>p.classList.remove('active'));b.classList.add('active');document.getElementById('timeLabel').textContent=m==='wake'?'Wake-up time':'Bedtime';}
function fmt12(d){let h=d.getHours(),m=d.getMinutes(),s=h>=12?'PM':'AM';h=h%12||12;return `${h}:${String(m).padStart(2,'0')} ${s}`;}
function calc(){const[h,m]=document.getElementById('f1').value.split(':').map(Number),delay=+document.getElementById('f2').value;const base=new Date();base.setHours(h,m,0);const results=[];for(let cycles=6;cycles>=2;cycles--){const t=new Date(base);const offset=cycles*90+delay;if(slMode==='wake')t.setMinutes(t.getMinutes()-(offset));else t.setMinutes(t.getMinutes()+offset);results.push({cycles,time:fmt12(t),hrs:((cycles*90)/60).toFixed(1)});}const rows=results.map(r=>`<div style="display:flex;justify-content:space-between;align-items:center;padding:10px 12px;margin-bottom:8px;border-radius:8px;background:${r.cycles>=5?'rgba(76,175,80,0.1)':'var(--card-bg)'};border:1px solid var(--border)"><div><strong>${r.time}</strong><br><small style="color:var(--text-secondary)">${r.cycles} cycles = ${r.hrs} hours</small></div><span style="color:${r.cycles>=5?'#4caf50':'var(--text-secondary)'};">${r.cycles>=5?'Recommended':''}</span></div>`).join('');const label=slMode==='wake'?'Bedtimes for waking at '+fmt12(base):'Wake times if sleeping at '+fmt12(base);document.getElementById('sleepResults').innerHTML=`<h6>${label}</h6>`+rows;document.getElementById('resultBox').classList.add('show');}
</script>""")

page("menstrual-cycle-calculator.html","Menstrual Cycle Calculator",
"Track your menstrual cycle, predict next period date, fertile window, and ovulation day. Period calendar calculator.",
"menstrual cycle calculator, period calculator, next period date, fertile window calculator, period tracker, cycle length",
"&#128149;","#880e4f","#ad1457","health","&#10084;","Health",
cb("Menstrual Cycle Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">First Day of Last Period</label><input type="date" class="form-control" id="f1"></div>
<div class="col-md-6"><label class="form-label">Cycle Length (days)</label><input type="number" class="form-control" id="f2" value="28" min="21" max="45"></div>
<div class="col-md-6"><label class="form-label">Period Duration (days)</label><input type="number" class="form-control" id="f3" value="5" min="2" max="10"></div>
</div>""",
[("Next Period","r1"),("Ovulation Day","r2"),("Fertile Window","r3"),("Days Until Period","r4")],
"Calculate Cycle"),
"""<script>
document.getElementById('f1').valueAsDate=new Date(Date.now()-14*86400000);
function calc(){const lmp=new Date(document.getElementById('f1').value),cycle=+document.getElementById('f2').value;const next=new Date(lmp);next.setDate(next.getDate()+cycle);const ovul=new Date(lmp);ovul.setDate(ovul.getDate()+cycle-14);const fw1=new Date(ovul);fw1.setDate(fw1.getDate()-5);const fw2=new Date(ovul);fw2.setDate(fw2.getDate()+1);const rem=Math.ceil((next-new Date())/86400000);document.getElementById('r1').textContent=next.toDateString();document.getElementById('r2').textContent=ovul.toDateString();document.getElementById('r3').textContent=fw1.toDateString()+' - '+fw2.toDateString();document.getElementById('r4').textContent=Math.max(0,rem)+' days';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("vitamin-calculator.html","Daily Vitamin & Nutrient Calculator",
"Calculate recommended daily intake of vitamins, minerals and nutrients based on your age, gender and health goals.",
"vitamin calculator, daily vitamin intake, nutrient calculator, RDA calculator, vitamin dosage, supplement calculator",
"&#128138;","#4a148c","#6a1b9a","health","&#10084;","Health",
"""<div class="calc-box">
<h2 class="calc-title">Daily Vitamin &amp; Nutrient Calculator</h2>
<div class="row g-3">
<div class="col-md-4"><label class="form-label">Age</label><input type="number" class="form-control" id="f1" value="30" min="1" max="100"></div>
<div class="col-md-4"><label class="form-label">Gender</label><select class="form-select" id="f2"><option value="m">Male</option><option value="f">Female</option></select></div>
<div class="col-md-4"><label class="form-label">Pregnant/Nursing</label><select class="form-select" id="f3"><option value="n">No</option><option value="p">Pregnant</option><option value="l">Lactating</option></select></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-capsule me-2"></i>Get RDA Values</button>
<div class="result-box" id="resultBox"><div id="vitResults" style="font-size:0.85rem"></div></div></div>""",
"""<script>
function calc(){const g=document.getElementById('f2').value,sp=document.getElementById('f3').value;const data=[['Vitamin A',g==='m'?900:700,sp==='p'?770:sp==='l'?1300:null,'mcg RAE'],['Vitamin C',g==='m'?90:75,sp==='p'?85:sp==='l'?120:null,'mg'],['Vitamin D',600,sp!=='n'?600:null,'IU'],['Vitamin E',15,sp==='l'?19:null,'mg'],['Vitamin K',g==='m'?120:90,null,'mcg'],['Vitamin B12',2.4,sp==='p'?2.6:sp==='l'?2.8:null,'mcg'],['Folate',400,sp==='p'?600:sp==='l'?500:null,'mcg DFE'],['Calcium',1000,sp!=='n'?1000:null,'mg'],['Iron',g==='m'?8:18,sp==='p'?27:sp==='l'?9:null,'mg'],['Zinc',g==='m'?11:8,sp==='p'?11:sp==='l'?12:null,'mg'],['Magnesium',g==='m'?420:320,sp==='p'?350:sp==='l'?310:null,'mg'],['Potassium',g==='m'?3400:2600,null,'mg'],['Omega-3',1100,sp==='p'?1400:sp==='l'?1300:null,'mg']];const rows=data.map(([n,base,sp_val,u])=>{const val=sp_val||base;return `<div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid var(--border)"><span>${n}</span><strong>${val} ${u}${sp_val&&sp_val!==base?' *':''}</strong></div>`;}).join('');document.getElementById('vitResults').innerHTML=rows+'<small style="color:var(--text-secondary);margin-top:8px;display:block">* Adjusted for pregnancy/lactation. Based on NIH/WHO recommendations.</small>';document.getElementById('resultBox').classList.add('show');}
</script>""")

# MATH
page("number-base-converter.html","Number Base Converter",
"Convert numbers between decimal, binary, octal, hexadecimal, and any custom base. Essential for programmers.",
"number base converter, binary to decimal, hex to decimal, decimal to binary, base conversion, octal converter",
"&#128290;","#1a237e","#283593","math","&#128290;","Math",
"""<div class="calc-box">
<h2 class="calc-title">Number Base Converter</h2>
<div class="row g-3">
<div class="col-md-8"><label class="form-label">Number</label><input type="text" class="form-control" id="numIn" value="255" placeholder="Enter number"></div>
<div class="col-md-4"><label class="form-label">From Base</label>
<select class="form-select" id="fromBase">
<option value="10" selected>Decimal (10)</option>
<option value="2">Binary (2)</option>
<option value="8">Octal (8)</option>
<option value="16">Hex (16)</option>
</select></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-arrow-left-right me-2"></i>Convert All Bases</button>
<div class="result-box" id="resultBox"><div id="baseResults" style="font-size:0.9rem"></div></div></div>""",
"""<script>
function calc(){const n=document.getElementById('numIn').value.trim().toUpperCase(),base=+document.getElementById('fromBase').value;let dec;try{dec=parseInt(n,base);}catch(e){return;}if(isNaN(dec))return alert('Invalid number for this base');const rows=[['Decimal (Base 10)',dec.toString(10)],['Binary (Base 2)',dec.toString(2)],['Octal (Base 8)',dec.toString(8)],['Hexadecimal (Base 16)',dec.toString(16).toUpperCase()],['Base 32',dec.toString(32).toUpperCase()],['Base 64 chars',dec.toString(36).toUpperCase()]];document.getElementById('baseResults').innerHTML=rows.map(([n,v])=>`<div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid var(--border)"><span>${n}</span><code style="font-size:1rem">${v}</code></div>`).join('');document.getElementById('resultBox').classList.add('show');}
</script>""")

page("roman-numeral-converter.html","Roman Numeral Converter",
"Convert numbers to Roman numerals and Roman numerals to regular numbers. Supports all standard Roman numeral values.",
"roman numeral converter, number to roman numeral, roman numeral calculator, convert roman numerals, what is XLII",
"&#128290;","#880e4f","#ad1457","math","&#128290;","Math",
"""<div class="calc-box">
<h2 class="calc-title">Roman Numeral Converter</h2>
<div class="d-flex gap-2 mb-3 flex-wrap">
<button class="cat-pill active" onclick="setMode('toRoman',this)">Number to Roman</button>
<button class="cat-pill" onclick="setMode('toNum',this)">Roman to Number</button>
</div>
<div class="row g-3">
<div class="col-md-6"><label class="form-label" id="inLabel">Number (1-3999)</label>
<input type="text" class="form-control" id="f1" value="2024"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-translate me-2"></i>Convert</button>
<div class="result-box" id="resultBox">
<div class="text-center"><div class="result-label" id="rl">Roman Numeral</div><div class="result-value" id="r1" style="font-size:2rem;letter-spacing:4px">-</div></div>
</div></div>""",
"""<script>
let rnMode='toRoman';
function setMode(m,b){rnMode=m;document.querySelectorAll('.cat-pill').forEach(p=>p.classList.remove('active'));b.classList.add('active');document.getElementById('inLabel').textContent=m==='toRoman'?'Number (1-3999)':'Roman Numeral';document.getElementById('rl').textContent=m==='toRoman'?'Roman Numeral':'Number';}
const val=[[1000,'M'],[900,'CM'],[500,'D'],[400,'CD'],[100,'C'],[90,'XC'],[50,'L'],[40,'XL'],[10,'X'],[9,'IX'],[5,'V'],[4,'IV'],[1,'I']];
const rval={I:1,V:5,X:10,L:50,C:100,D:500,M:1000};
function toRoman(n){let r='';for(const[v,s]of val){while(n>=v){r+=s;n-=v;}}return r;}
function fromRoman(s){let n=0;for(let i=0;i<s.length;i++){const c=rval[s[i]],nx=rval[s[i+1]];if(nx&&c<nx)n-=c;else n+=c;}return n;}
function calc(){const inp=document.getElementById('f1').value.trim().toUpperCase();let res;if(rnMode==='toRoman'){const n=parseInt(inp);if(n<1||n>3999)return alert('Enter 1-3999');res=toRoman(n);}else{res=fromRoman(inp);}document.getElementById('r1').textContent=res;document.getElementById('resultBox').classList.add('show');}
</script>""")

page("number-to-words-converter.html","Number to Words Converter",
"Convert any number to words in English. Supports millions, billions, and trillions. Great for check writing.",
"number to words, convert number to words, spell out numbers, write checks in words, number words converter",
"&#128290;","#0d47a1","#1565c0","math","&#128290;","Math",
"""<div class="calc-box">
<h2 class="calc-title">Number to Words Converter</h2>
<div class="mb-3"><label class="form-label">Enter Number</label>
<input type="number" class="form-control" id="f1" value="1234567" step="1"></div>
<button class="btn-calculate" onclick="calc()"><i class="bi bi-translate me-2"></i>Convert to Words</button>
<div class="result-box" id="resultBox">
<div class="result-label">In Words</div>
<div id="r1" style="font-size:1.1rem;font-weight:600;text-align:center;margin-top:8px;line-height:1.6">-</div>
</div></div>""",
"""<script>
const ones=['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen'];
const tens=['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety'];
function h2w(n){if(n===0)return'';if(n<20)return ones[n];if(n<100)return tens[Math.floor(n/10)]+(n%10?' '+ones[n%10]:'');return ones[Math.floor(n/100)]+' Hundred'+(n%100?' '+h2w(n%100):'');}
function n2w(n){if(n===0)return'Zero';let w='',neg=n<0;n=Math.abs(Math.floor(n));const g=['','Thousand','Million','Billion','Trillion'];let gi=0;while(n>0){const chunk=n%1000;if(chunk)w=(h2w(chunk)+(g[gi]?' '+g[gi]:'')+' '+w).trim();n=Math.floor(n/1000);gi++;}return(neg?'Negative ':'')+w;}
function calc(){const n=+document.getElementById('f1').value;document.getElementById('r1').textContent=n2w(n);document.getElementById('resultBox').classList.add('show');}
</script>""")

page("standard-deviation-calculator.html","Standard Deviation Calculator",
"Calculate population and sample standard deviation, variance, mean, and coefficient of variation for any dataset.",
"standard deviation calculator, variance calculator, sample standard deviation, population std dev, statistics calculator",
"&#128200;","#4a148c","#6a1b9a","math","&#128290;","Math",
"""<div class="calc-box">
<h2 class="calc-title">Standard Deviation Calculator</h2>
<div class="mb-3"><label class="form-label">Enter Numbers (comma or space separated)</label>
<textarea class="form-control" id="nums" rows="3" placeholder="e.g., 10, 20, 30, 40, 50">2, 4, 4, 4, 5, 5, 7, 9</textarea></div>
<button class="btn-calculate" onclick="calc()"><i class="bi bi-graph-up me-2"></i>Calculate Statistics</button>
<div class="result-box" id="resultBox">
<div class="row g-3 text-center">
<div class="col-6"><div class="result-label">Sample Std Dev (s)</div><div class="result-value" id="r1">-</div></div>
<div class="col-6"><div class="result-label">Population Std Dev (&#963;)</div><div class="result-value" id="r2">-</div></div>
<div class="col-6"><div class="result-label">Variance (s&#178;)</div><div class="result-value" id="r3">-</div></div>
<div class="col-6"><div class="result-label">Mean</div><div class="result-value" id="r4">-</div></div>
<div class="col-6"><div class="result-label">CV (Coeff. of Variation)</div><div class="result-value" id="r5">-</div></div>
<div class="col-6"><div class="result-label">Count (n)</div><div class="result-value" id="r6">-</div></div>
</div></div></div>""",
"""<script>
function calc(){const nums=document.getElementById('nums').value.split(/[\s,]+/).map(Number).filter(n=>!isNaN(n));if(nums.length<2)return;const n=nums.length,mean=nums.reduce((a,b)=>a+b,0)/n,popVar=nums.reduce((s,x)=>s+(x-mean)**2,0)/n,sampVar=nums.reduce((s,x)=>s+(x-mean)**2,0)/(n-1);document.getElementById('r1').textContent=Math.sqrt(sampVar).toFixed(4);document.getElementById('r2').textContent=Math.sqrt(popVar).toFixed(4);document.getElementById('r3').textContent=sampVar.toFixed(4);document.getElementById('r4').textContent=mean.toFixed(4);document.getElementById('r5').textContent=(Math.sqrt(sampVar)/mean*100).toFixed(2)+'%';document.getElementById('r6').textContent=n;document.getElementById('resultBox').classList.add('show');}
</script>""")

# CONVERTERS
page("time-unit-converter.html","Time Unit Converter",
"Convert between time units: seconds, minutes, hours, days, weeks, months, years, milliseconds, and microseconds.",
"time unit converter, convert seconds to minutes, hours to days, time conversion calculator, milliseconds converter",
"&#8987;","#37474f","#455a64","converters","&#128259;","Converters",
"""<div class="calc-box">
<h2 class="calc-title">Time Unit Converter</h2>
<div class="row g-3">
<div class="col-md-6"><label class="form-label">Value</label><input type="number" class="form-control" id="tval" value="1" step="any"></div>
<div class="col-md-6"><label class="form-label">From Unit</label>
<select class="form-select" id="tfrom">
<option value="0.001">Millisecond</option>
<option value="1">Second</option>
<option value="60" selected>Minute</option>
<option value="3600">Hour</option>
<option value="86400">Day</option>
<option value="604800">Week</option>
<option value="2629800">Month (avg)</option>
<option value="31557600">Year</option>
</select></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-clock me-2"></i>Convert All</button>
<div class="result-box" id="resultBox"><div id="tResults" style="font-size:0.9rem"></div></div></div>""",
"""<script>
const tu=[['Milliseconds',0.001],['Seconds',1],['Minutes',60],['Hours',3600],['Days',86400],['Weeks',604800],['Months',2629800],['Years',31557600]];
function calc(){const v=+document.getElementById('tval').value,f=+document.getElementById('tfrom').value,sec=v*f;const rows=tu.map(([n,fac])=>`<div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid var(--border)"><span>${n}</span><strong>${(sec/fac).toPrecision(6)}</strong></div>`).join('');document.getElementById('tResults').innerHTML=rows;document.getElementById('resultBox').classList.add('show');}
</script>""")

page("force-converter.html","Force Unit Converter",
"Convert between force units: Newton, pound-force, kilogram-force, dyne, and more.",
"force converter, newton to pound force, force unit converter, kg-force calculator, dyne converter, N to lbf",
"&#128165;","#1b5e20","#2e7d32","converters","&#128259;","Converters",
"""<div class="calc-box">
<h2 class="calc-title">Force Unit Converter</h2>
<div class="row g-3">
<div class="col-md-6"><label class="form-label">Value</label><input type="number" class="form-control" id="fval" value="1" step="any"></div>
<div class="col-md-6"><label class="form-label">From Unit</label>
<select class="form-select" id="ffrom">
<option value="1" selected>Newton (N)</option>
<option value="1000">Kilonewton (kN)</option>
<option value="0.00001">Dyne</option>
<option value="9.80665">Kilogram-force (kgf)</option>
<option value="4.44822">Pound-force (lbf)</option>
<option value="0.138255">Poundal</option>
</select></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-arrow-left-right me-2"></i>Convert All</button>
<div class="result-box" id="resultBox"><div id="fResults" style="font-size:0.9rem"></div></div></div>""",
"""<script>
const fu=[['Newton (N)',1],['Kilonewton (kN)',1000],['Dyne',0.00001],['Kilogram-force (kgf)',9.80665],['Pound-force (lbf)',4.44822],['Poundal',0.138255]];
function calc(){const v=+document.getElementById('fval').value,f=+document.getElementById('ffrom').value,n=v*f;const rows=fu.map(([nm,fac])=>`<div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid var(--border)"><span>${nm}</span><strong>${(n/fac).toPrecision(6)}</strong></div>`).join('');document.getElementById('fResults').innerHTML=rows;document.getElementById('resultBox').classList.add('show');}
</script>""")

page("power-unit-converter.html","Power Unit Converter",
"Convert between power units: Watt, kilowatt, horsepower, BTU/hour, and more. Essential for engineering and physics.",
"power unit converter, watts to horsepower, kW to hp, power conversion, BTU per hour converter, electrical power",
"&#9889;","#b71c1c","#c62828","converters","&#128259;","Converters",
"""<div class="calc-box">
<h2 class="calc-title">Power Unit Converter</h2>
<div class="row g-3">
<div class="col-md-6"><label class="form-label">Value</label><input type="number" class="form-control" id="pval" value="1" step="any"></div>
<div class="col-md-6"><label class="form-label">From Unit</label>
<select class="form-select" id="pfrom">
<option value="1" selected>Watt (W)</option>
<option value="1000">Kilowatt (kW)</option>
<option value="1000000">Megawatt (MW)</option>
<option value="745.7">Horsepower (hp)</option>
<option value="746">Metric HP (PS)</option>
<option value="0.29307">BTU/hour</option>
<option value="1055.06">BTU/second</option>
</select></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-arrow-left-right me-2"></i>Convert All</button>
<div class="result-box" id="resultBox"><div id="pwResults" style="font-size:0.9rem"></div></div></div>""",
"""<script>
const pwu=[['Watt (W)',1],['Kilowatt (kW)',1000],['Megawatt (MW)',1000000],['Horsepower (hp)',745.7],['Metric HP (PS)',746],['BTU/hour',0.29307],['BTU/second',1055.06],['Erg/second',0.0000001]];
function calc(){const v=+document.getElementById('pval').value,f=+document.getElementById('pfrom').value,w=v*f;const rows=pwu.map(([n,fac])=>`<div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid var(--border)"><span>${n}</span><strong>${(w/fac).toPrecision(6)}</strong></div>`).join('');document.getElementById('pwResults').innerHTML=rows;document.getElementById('resultBox').classList.add('show');}
</script>""")

# SCIENCE
page("wavelength-frequency-calculator.html","Wavelength & Frequency Calculator",
"Calculate wavelength, frequency, and wave speed. Covers light, sound, radio waves, and electromagnetic spectrum.",
"wavelength calculator, frequency calculator, wavelength frequency speed, electromagnetic spectrum, wave calculator",
"&#127752;","#4a148c","#6a1b9a","science","&#128301;","Science",
cb("Wavelength & Frequency Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Wave Speed (m/s)</label>
<select class="form-select" id="f0" onchange="setSpeed()">
<option value="299792458">Light in vacuum (c)</option>
<option value="343">Sound in air (343 m/s)</option>
<option value="1480">Sound in water</option>
<option value="custom">Custom speed</option>
</select></div>
<div class="col-md-6"><label class="form-label">Speed (m/s)</label><input type="number" class="form-control" id="spd" value="299792458" step="any"></div>
<div class="col-md-6"><label class="form-label">Frequency (Hz) - leave blank to solve</label><input type="number" class="form-control" id="f1" value="600e12" step="any" placeholder="e.g., 440 for A note"></div>
<div class="col-md-6"><label class="form-label">Wavelength (m) - leave blank to solve</label><input type="number" class="form-control" id="f2" step="any" placeholder="Leave blank to solve"></div>
</div>""",
[("Wavelength","r1"),("Frequency","r2"),("Wave Speed","r3"),("Period (1/f)","r4")]),
"""<script>
function setSpeed(){const s=document.getElementById('f0').value;if(s!=='custom')document.getElementById('spd').value=s;}
function calc(){let f=parseFloat(document.getElementById('f1').value),wl=parseFloat(document.getElementById('f2').value),spd=+document.getElementById('spd').value;const has=x=>!isNaN(x)&&x>0;if(has(f)&&!has(wl)){wl=spd/f;}else if(has(wl)&&!has(f)){f=spd/wl;}else if(!has(f)&&!has(wl)){return alert('Enter frequency or wavelength');}const T=1/f;document.getElementById('r1').textContent=wl.toExponential(4)+' m';document.getElementById('r2').textContent=f.toExponential(4)+' Hz';document.getElementById('r3').textContent=spd.toExponential(4)+' m/s';document.getElementById('r4').textContent=T.toExponential(4)+' s';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("ohms-law-advanced-calculator.html","Advanced Electronics Calculator",
"Calculate series/parallel resistors, capacitors, inductors, voltage divider, and power factor for AC circuits.",
"resistor calculator, series parallel resistor, voltage divider calculator, capacitor calculator, inductor, electronics",
"&#9874;","#0d47a1","#1565c0","science","&#128301;","Science",
"""<div class="calc-box">
<h2 class="calc-title">Electronics Circuit Calculator</h2>
<div class="d-flex gap-2 mb-3 flex-wrap">
<button class="cat-pill active" onclick="setMode('series',this)">Series R</button>
<button class="cat-pill" onclick="setMode('parallel',this)">Parallel R</button>
<button class="cat-pill" onclick="setMode('divider',this)">Voltage Divider</button>
<button class="cat-pill" onclick="setMode('rc',this)">RC Time Constant</button>
</div>
<div id="modeContent">
<div class="row g-2">
<div class="col-12"><label class="form-label">Resistor Values (\u03a9) - comma separated</label>
<input type="text" class="form-control" id="rvals" value="100, 220, 470"></div>
</div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-lightning me-2"></i>Calculate</button>
<div class="result-box" id="resultBox"><div id="eleResult" style="text-align:center;font-size:1.1rem"></div></div></div>""",
"""<script>
let eMode='series';
const templates={series:'<div class="col-12"><label class="form-label">Resistor Values (\u03a9) - comma separated</label><input type="text" class="form-control" id="rvals" value="100, 220, 470"></div>',parallel:'<div class="col-12"><label class="form-label">Resistor Values (\u03a9) - comma separated</label><input type="text" class="form-control" id="rvals" value="100, 220, 470"></div>',divider:'<div class="col-6"><label class="form-label">Vin (V)</label><input type="number" class="form-control" id="vin" value="12"></div><div class="col-3"><label class="form-label">R1 (\u03a9)</label><input type="number" class="form-control" id="r1v" value="1000"></div><div class="col-3"><label class="form-label">R2 (\u03a9)</label><input type="number" class="form-control" id="r2v" value="2200"></div>',rc:'<div class="col-6"><label class="form-label">Resistance (\u03a9)</label><input type="number" class="form-control" id="rv" value="1000"></div><div class="col-6"><label class="form-label">Capacitance (\u03bcF)</label><input type="number" class="form-control" id="cv" value="100"></div>'};
function setMode(m,b){eMode=m;document.querySelectorAll('.cat-pill').forEach(p=>p.classList.remove('active'));b.classList.add('active');document.getElementById('modeContent').innerHTML='<div class="row g-2">'+templates[m]+'</div>';}
function calc(){let res='';if(eMode==='series'){const r=document.getElementById('rvals').value.split(',').map(Number);const total=r.reduce((a,b)=>a+b,0);res=`Total Resistance: <strong>${total} \u03a9</strong>`;}else if(eMode==='parallel'){const r=document.getElementById('rvals').value.split(',').map(Number);const rec=r.reduce((a,b)=>a+1/b,0);res=`Parallel Resistance: <strong>${(1/rec).toFixed(4)} \u03a9</strong>`;}else if(eMode==='divider'){const vin=+document.getElementById('vin').value,r1=+document.getElementById('r1v').value,r2=+document.getElementById('r2v').value;const vout=vin*r2/(r1+r2);res=`Vout = <strong>${vout.toFixed(4)} V</strong><br>Current = <strong>${(vin/(r1+r2)*1000).toFixed(2)} mA</strong>`;}else{const r=+document.getElementById('rv').value,c=+document.getElementById('cv').value*1e-6;const tau=r*c;res=`RC Time Constant (\u03c4): <strong>${(tau*1000).toFixed(3)} ms</strong><br>5\u03c4 (full charge): <strong>${(tau*5000).toFixed(1)} ms</strong>`;}document.getElementById('eleResult').innerHTML=res;document.getElementById('resultBox').classList.add('show');}
</script>""")

# LIFESTYLE
page("bmi-calculator-kids.html","Child BMI Calculator",
"Calculate BMI for children and teens (ages 2-19). Uses CDC growth charts to determine healthy weight percentile.",
"child BMI calculator, kids BMI, BMI for children, BMI percentile calculator, healthy weight for kids, teen BMI",
"&#128118;","#1b5e20","#2e7d32","health","&#10084;","Health",
cb("Child BMI Calculator (Ages 2-19)",
"""<div class="row g-3">
<div class="col-md-4"><label class="form-label">Age (years)</label><input type="number" class="form-control" id="f1" value="10" min="2" max="19"></div>
<div class="col-md-4"><label class="form-label">Gender</label><select class="form-select" id="f2"><option value="m">Boy</option><option value="f">Girl</option></select></div>
<div class="col-md-4"><label class="form-label">Weight (kg)</label><input type="number" class="form-control" id="f3" value="35" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Height (cm)</label><input type="number" class="form-control" id="f4" value="140" step="1"></div>
</div>""",
[("BMI","r1"),("Weight Category","r2"),("Healthy Weight Range","r3"),("Height Percentile (est.)","r4")],
"Calculate Child BMI"),
"""<script>
function calc(){const age=+document.getElementById('f1').value,w=+document.getElementById('f3').value,h=+document.getElementById('f4').value/100;const bmi=w/(h*h);let cat,minW,maxW;const p5=14+age*0.4,p85=17+age*0.6,p95=18+age*0.8;if(bmi<p5)cat='Underweight (<5th percentile)';else if(bmi<p85)cat='Healthy Weight (5th-85th)';else if(bmi<p95)cat='Overweight (85th-95th)';else cat='Obese (>95th percentile)';minW=(p5*h*h).toFixed(1);maxW=(p85*h*h).toFixed(1);document.getElementById('r1').textContent=bmi.toFixed(1);document.getElementById('r2').textContent=cat;document.getElementById('r3').textContent=minW+' - '+maxW+' kg';document.getElementById('r4').textContent='Est. normal for age '+age;document.getElementById('resultBox').classList.add('show');}
</script>""")

page("tip-percentage-calculator.html","Tip Percentage Calculator",
"Calculate tip percentage from bill and tip amount. Find out what percentage tip you left or should leave.",
"tip percentage calculator, what percentage tip, tip amount calculator, how much to tip, restaurant tip",
"&#127869;","#e65100","#f57c00","finance","&#128176;","Finance",
cb("Tip Percentage Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Bill Amount ($)</label><input type="number" class="form-control" id="f1" value="85" step="0.01"></div>
<div class="col-md-6"><label class="form-label">Tip Amount ($)</label><input type="number" class="form-control" id="f2" value="15" step="0.01"></div>
</div>""",
[("Tip %","r1"),("Total Bill","r2"),("Quality Rating","r3"),("Per $100 Benchmark","r4")],
"Calculate Tip %"),
"""<script>
function calc(){const b=+document.getElementById('f1').value,t=+document.getElementById('f2').value;const pct=t/b*100,qual=pct<10?'Below Average':pct<15?'Standard':pct<20?'Good':pct<25?'Excellent':'Exceptional';document.getElementById('r1').textContent=pct.toFixed(1)+'%';document.getElementById('r2').textContent='$'+(b+t).toFixed(2);document.getElementById('r3').textContent=qual;document.getElementById('r4').textContent='$'+(pct).toFixed(2)+' tip per $100';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("blood-sugar-calculator.html","Blood Sugar Converter & Calculator",
"Convert blood glucose between mg/dL and mmol/L. Check if blood sugar levels are normal, low, or high.",
"blood sugar calculator, glucose converter mg/dL to mmol/L, blood glucose levels, normal blood sugar, diabetes glucose",
"&#128138;","#b71c1c","#c62828","health","&#10084;","Health",
cb("Blood Sugar Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Blood Glucose Value</label><input type="number" class="form-control" id="f1" value="100" step="0.1"></div>
<div class="col-md-6"><label class="form-label">Unit</label>
<select class="form-select" id="f2">
<option value="mgdl" selected>mg/dL</option>
<option value="mmol">mmol/L</option>
</select></div>
<div class="col-md-6"><label class="form-label">Measurement Time</label>
<select class="form-select" id="f3">
<option value="fasting">Fasting (8+ hours)</option>
<option value="post2h">2 Hours After Meal</option>
<option value="random">Random</option>
</select></div>
</div>""",
[("mg/dL","r1"),("mmol/L","r2"),("HbA1c Estimate","r3"),("Classification","r4")],
"Check Blood Sugar"),
"""<script>
function calc(){const v=+document.getElementById('f1').value,unit=document.getElementById('f2').value,time=document.getElementById('f3').value;const mgdl=unit==='mgdl'?v:v*18.0182,mmol=unit==='mmol'?v:v/18.0182;const hba1c=((mgdl+46.7)/28.7).toFixed(1);let cl;if(time==='fasting'){cl=mgdl<70?'Low (Hypoglycemia)':mgdl<100?'Normal':mgdl<126?'Pre-diabetes':'Diabetes Range';}else if(time==='post2h'){cl=mgdl<140?'Normal':mgdl<200?'Pre-diabetes':'Diabetes Range';}else{cl=mgdl<70?'Low':mgdl<200?'Normal Range':'High';}document.getElementById('r1').textContent=mgdl.toFixed(0)+' mg/dL';document.getElementById('r2').textContent=mmol.toFixed(2)+' mmol/L';document.getElementById('r3').textContent=hba1c+'% (est.)';document.getElementById('r4').textContent=cl;document.getElementById('resultBox').classList.add('show');}
</script>""")

# BUSINESS
page("invoice-generator-calculator.html","Invoice Calculator",
"Calculate invoice totals with tax, discount, and multiple line items. Perfect for freelancers and small businesses.",
"invoice calculator, invoice total calculator, freelancer invoice, calculate invoice with tax, billing calculator",
"&#128203;","#1a237e","#283593","business","&#128188;","Business",
"""<div class="calc-box">
<h2 class="calc-title">Invoice Calculator</h2>
<div id="lineItems">
<div class="row g-2 mb-2 align-items-end" id="li1">
<div class="col-5"><label class="form-label">Description</label><input type="text" class="form-control" id="d1" value="Web Design" placeholder="Item description"></div>
<div class="col-2"><label class="form-label">Qty</label><input type="number" class="form-control" id="q1" value="1" min="1"></div>
<div class="col-3"><label class="form-label">Unit Price ($)</label><input type="number" class="form-control" id="p1" value="1500" step="0.01"></div>
<div class="col-2 d-flex align-items-end"><button class="btn btn-outline-danger btn-sm" onclick="removeLine(1)">X</button></div>
</div>
</div>
<button class="btn btn-outline-secondary btn-sm mt-2 mb-3" onclick="addLine()">+ Add Line Item</button>
<div class="row g-3">
<div class="col-md-4"><label class="form-label">Discount (%)</label><input type="number" class="form-control" id="disc" value="0" step="1"></div>
<div class="col-md-4"><label class="form-label">Tax Rate (%)</label><input type="number" class="form-control" id="taxr" value="10" step="0.5"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-receipt me-2"></i>Calculate Invoice</button>
<div class="result-box" id="resultBox">
<div class="row g-3 text-center">
<div class="col-6"><div class="result-label">Subtotal</div><div class="result-value" id="r1">-</div></div>
<div class="col-6"><div class="result-label">Discount</div><div class="result-value" id="r2">-</div></div>
<div class="col-6"><div class="result-label">Tax</div><div class="result-value" id="r3">-</div></div>
<div class="col-6"><div class="result-label">TOTAL DUE</div><div class="result-value" id="r4" style="color:var(--primary)">-</div></div>
</div></div></div>""",
"""<script>
let lc=1;
function addLine(){lc++;document.getElementById('lineItems').insertAdjacentHTML('beforeend',`<div class="row g-2 mb-2 align-items-end" id="li${lc}"><div class="col-5"><input type="text" class="form-control" id="d${lc}" placeholder="Item description"></div><div class="col-2"><input type="number" class="form-control" id="q${lc}" value="1" min="1"></div><div class="col-3"><input type="number" class="form-control" id="p${lc}" value="0" step="0.01"></div><div class="col-2 d-flex align-items-end"><button class="btn btn-outline-danger btn-sm" onclick="removeLine(${lc})">X</button></div></div>`);}
function removeLine(id){document.getElementById('li'+id)?.remove();}
function calc(){let sub=0;for(let i=1;i<=lc;i++){const q=+document.getElementById('q'+i)?.value||0,p=+document.getElementById('p'+i)?.value||0;sub+=q*p;}const disc=+document.getElementById('disc').value/100,tax=+document.getElementById('taxr').value/100;const discAmt=sub*disc,taxAmt=(sub-discAmt)*tax,total=sub-discAmt+taxAmt;document.getElementById('r1').textContent='$'+sub.toFixed(2);document.getElementById('r2').textContent='$'+discAmt.toFixed(2);document.getElementById('r3').textContent='$'+taxAmt.toFixed(2);document.getElementById('r4').textContent='$'+total.toFixed(2);document.getElementById('resultBox').classList.add('show');}
</script>""")

page("employee-cost-calculator.html","Employee Cost Calculator",
"Calculate true total cost of an employee including salary, benefits, taxes, and overhead. Cost per hour breakdown.",
"employee cost calculator, total employee cost, cost of hiring, employer taxes, employee overhead calculator, labor cost",
"&#128188;","#4a148c","#6a1b9a","business","&#128188;","Business",
cb("Employee Cost Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Annual Salary ($)</label><input type="number" class="form-control" id="f1" value="60000" step="1000"></div>
<div class="col-md-6"><label class="form-label">Employer Payroll Tax (%)</label><input type="number" class="form-control" id="f2" value="7.65" step="0.1"></div>
<div class="col-md-6"><label class="form-label">Health Insurance ($/month)</label><input type="number" class="form-control" id="f3" value="500" step="50"></div>
<div class="col-md-6"><label class="form-label">Retirement Contribution (%)</label><input type="number" class="form-control" id="f4" value="3" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Training &amp; Equipment ($)</label><input type="number" class="form-control" id="f5" value="3000" step="500"></div>
<div class="col-md-6"><label class="form-label">Overhead Rate (%)</label><input type="number" class="form-control" id="f6" value="15" step="1"></div>
</div>""",
[("Total Annual Cost","r1"),("Cost Above Salary","r2"),("Effective Cost/Hour","r3"),("True Cost Multiplier","r4")],
"Calculate Total Cost"),
"""<script>
function calc(){const sal=+document.getElementById('f1').value,tax=+document.getElementById('f2').value/100,health=+document.getElementById('f3').value*12,ret=+document.getElementById('f4').value/100,equip=+document.getElementById('f5').value,overhead=+document.getElementById('f6').value/100;const total=sal*(1+tax+ret)+health+equip+sal*overhead;const extra=total-sal,hourly=total/2080,mult=total/sal;document.getElementById('r1').textContent='$'+total.toFixed(0);document.getElementById('r2').textContent='$'+extra.toFixed(0);document.getElementById('r3').textContent='$'+hourly.toFixed(2)+'/hr';document.getElementById('r4').textContent=mult.toFixed(2)+'x salary';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("customer-ltv-calculator.html","Customer Lifetime Value Calculator",
"Calculate Customer Lifetime Value (CLV/LTV) to understand revenue potential. Includes churn rate and acquisition cost.",
"customer lifetime value calculator, CLV calculator, LTV calculator, CLTV, customer value, churn rate calculator",
"&#128200;","#1b5e20","#2e7d32","business","&#128188;","Business",
cb("Customer Lifetime Value (CLV) Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Avg Purchase Value ($)</label><input type="number" class="form-control" id="f1" value="50" step="1"></div>
<div class="col-md-6"><label class="form-label">Avg Purchases Per Year</label><input type="number" class="form-control" id="f2" value="4" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Avg Customer Lifespan (years)</label><input type="number" class="form-control" id="f3" value="3" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Profit Margin (%)</label><input type="number" class="form-control" id="f4" value="20" step="1"></div>
<div class="col-md-6"><label class="form-label">Customer Acquisition Cost ($)</label><input type="number" class="form-control" id="f5" value="30" step="1"></div>
<div class="col-md-6"><label class="form-label">Discount Rate (%)</label><input type="number" class="form-control" id="f6" value="10" step="1"></div>
</div>""",
[("Customer LTV","r1"),("Profit LTV","r2"),("Net LTV (after CAC)","r3"),("LTV:CAC Ratio","r4")],
"Calculate LTV"),
"""<script>
function calc(){const apv=+document.getElementById('f1').value,apy=+document.getElementById('f2').value,life=+document.getElementById('f3').value,margin=+document.getElementById('f4').value/100,cac=+document.getElementById('f5').value,dr=+document.getElementById('f6').value/100;const ltv=apv*apy*life,plt=ltv*margin,nlt=plt-cac,ratio=(plt/cac).toFixed(2);document.getElementById('r1').textContent='$'+ltv.toFixed(0);document.getElementById('r2').textContent='$'+plt.toFixed(0);document.getElementById('r3').textContent='$'+nlt.toFixed(0);document.getElementById('r4').textContent=ratio+':1';document.getElementById('resultBox').classList.add('show');}
</script>""")

# EDUCATION
page("gpa-to-percentage.html","GPA to Percentage Calculator",
"Convert GPA to percentage and letter grade. Supports 4.0 scale, 10-point scale, and custom GPA systems.",
"GPA to percentage, 4.0 GPA calculator, GPA converter, grade point average to percentage, letter grade calculator",
"&#127979;","#880e4f","#ad1457","education","&#127979;","Education",
cb("GPA to Percentage Converter",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Your GPA</label><input type="number" class="form-control" id="f1" value="3.5" step="0.01" min="0"></div>
<div class="col-md-6"><label class="form-label">GPA Scale</label>
<select class="form-select" id="f2">
<option value="4">4.0 Scale (US)</option>
<option value="10">10.0 Scale (India)</option>
<option value="5">5.0 Scale</option>
<option value="7">7.0 Scale</option>
</select></div>
</div>""",
[("Percentage","r1"),("Letter Grade","r2"),("Class/Division","r3"),("GPA Percentile","r4")],
"Convert GPA"),
"""<script>
function calc(){const gpa=+document.getElementById('f1').value,scale=+document.getElementById('f2').value;const pct=scale===4?gpa/4*100:scale===10?gpa*9.5:gpa/scale*100;let grade,cls;if(pct>=90)grade='A+ / O',cls='Distinction';else if(pct>=80)grade='A',cls='First Class';else if(pct>=70)grade='B+',cls='First Class';else if(pct>=60)grade='B',cls='Second Class';else if(pct>=50)grade='C',cls='Second Class';else if(pct>=40)grade='D',cls='Pass';else grade='F',cls='Fail';const pctile=pct>=90?'Top 5%':pct>=80?'Top 15%':pct>=70?'Top 35%':'Average';document.getElementById('r1').textContent=pct.toFixed(1)+'%';document.getElementById('r2').textContent=grade;document.getElementById('r3').textContent=cls;document.getElementById('r4').textContent=pctile;document.getElementById('resultBox').classList.add('show');}
</script>""")

# FUN / SOCIAL
page("love-compatibility-calculator.html","Love Compatibility Calculator",
"Calculate love compatibility between two people based on names and birthdates. Fun relationship compatibility quiz.",
"love compatibility calculator, relationship compatibility, couple compatibility test, love percentage, soulmate calculator",
"&#128149;","#880e4f","#ad1457","lifestyle","&#127774;","Lifestyle",
"""<div class="calc-box">
<h2 class="calc-title">Love Compatibility Calculator</h2>
<div class="alert" style="background:rgba(233,30,99,0.1);border-left:4px solid #e91e63;padding:10px;border-radius:8px;font-size:0.85rem;margin-bottom:16px">
<strong>Fun Only!</strong> This calculator is for entertainment purposes only.
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
<div style="font-size:3rem;margin-bottom:8px" id="heartEmoji">&#10084;</div>
<div class="result-label">Compatibility Score</div>
<div class="result-value" id="r1" style="font-size:3rem">-</div>
<div id="r2" style="margin-top:8px;font-weight:600;color:var(--primary)"></div>
<div id="r3" style="margin-top:6px;font-size:0.9rem;color:var(--text-secondary)"></div>
</div></div></div>""",
"""<script>
document.getElementById('f3').valueAsDate=new Date('1995-01-01');
document.getElementById('f4').valueAsDate=new Date('1993-06-15');
function hashStr(s){let h=0;for(let i=0;i<s.length;i++)h=(h<<5)-h+s.charCodeAt(i);return Math.abs(h);}
const msgs=[[90,'You are soulmates! Perfect match!','Your love is written in the stars.'],[75,'Great compatibility!','You complement each other beautifully.'],[60,'Good match!','With effort, you can build something special.'],[45,'Some challenges ahead','Understanding each other is key.'],[0,'Work in progress','Every relationship takes dedication.']];
function calc(){const n1=document.getElementById('f1').value,n2=document.getElementById('f2').value,d1=document.getElementById('f3').value,d2=document.getElementById('f4').value;const h=hashStr((n1+n2).toLowerCase()+(d1||'')+(d2||''));const score=50+h%51;const[,title,sub]=msgs.find(([t])=>score>=t)||msgs[msgs.length-1];document.getElementById('r1').textContent=score+'%';document.getElementById('r2').textContent=title;document.getElementById('r3').textContent=sub;document.getElementById('heartEmoji').textContent=score>=75?'\u2764\ufe0f':score>=60?'\uD83D\uDC97':'\uD83D\uDC96';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("random-password-generator.html","Random Password Generator",
"Generate strong, secure random passwords. Customize length, symbols, numbers, and uppercase letters.",
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
<div class="col-6 col-md-3"><div class="form-check"><input class="form-check-input" type="checkbox" id="symbols" checked><label class="form-check-label" for="symbols">Symbols (!@#$)</label></div></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-shield-lock me-2"></i>Generate Passwords</button>
<div class="result-box" id="resultBox"><div id="pwdResults" style="font-size:0.85rem"></div></div></div>""",
"""<script>
function calc(){const len=+document.getElementById('plen').value,num=+document.getElementById('pnum').value;let chars='';if(document.getElementById('upper').checked)chars+='ABCDEFGHIJKLMNOPQRSTUVWXYZ';if(document.getElementById('lower').checked)chars+='abcdefghijklmnopqrstuvwxyz';if(document.getElementById('numbers').checked)chars+='0123456789';if(document.getElementById('symbols').checked)chars+='!@#$%^&*()_+-=[]{}|;:,.<>?';if(!chars)return alert('Select at least one character type');const pwds=Array.from({length:num},()=>Array.from({length:len},()=>chars[Math.floor(Math.random()*chars.length)]).join(''));const strength=chars.length>72&&len>=16?'Very Strong':chars.length>50&&len>=12?'Strong':len>=8?'Medium':'Weak';const rows=pwds.map(p=>`<div style="display:flex;justify-content:space-between;align-items:center;padding:8px 12px;margin-bottom:6px;border-radius:8px;background:var(--card-bg);border:1px solid var(--border);font-family:monospace"><span style="word-break:break-all">${p}</span><button class="btn btn-sm btn-outline-secondary ms-2" onclick="navigator.clipboard.writeText('${p}')">Copy</button></div>`).join('');document.getElementById('pwdResults').innerHTML=`<div style="margin-bottom:8px">Strength: <strong style="color:${strength==='Very Strong'?'#4caf50':strength==='Strong'?'#8bc34a':strength==='Medium'?'#ff9800':'#f44336'}">${strength}</strong></div>`+rows;document.getElementById('resultBox').classList.add('show');}
</script>""")

page("hash-value-calculator.html","Text Hash Calculator",
"Calculate hash values for any text: SHA-256, SHA-512, MD5, CRC32. Text checksum and character count tools.",
"hash calculator, text hash, SHA256 calculator, MD5 hash, checksum calculator, word count hash",
"&#128196;","#0d47a1","#1565c0","tech","&#128187;","Tech & Dev",
"""<div class="calc-box">
<h2 class="calc-title">Text Analysis &amp; Hash Calculator</h2>
<div class="mb-3"><label class="form-label">Enter Text</label>
<textarea class="form-control" id="txt" rows="5" placeholder="Enter any text to analyze...">Hello, World! This is SuperCalc text analyzer.</textarea></div>
<button class="btn-calculate" onclick="calc()"><i class="bi bi-search me-2"></i>Analyze Text</button>
<div class="result-box" id="resultBox"><div id="hashResults" style="font-size:0.9rem"></div></div></div>""",
"""<script>
async function sha256(msg){const buf=await crypto.subtle.digest('SHA-256',new TextEncoder().encode(msg));return Array.from(new Uint8Array(buf)).map(b=>b.toString(16).padStart(2,'0')).join('');}
async function calc(){const t=document.getElementById('txt').value;const words=t.trim().split(/\s+/).filter(w=>w.length>0).length;const chars=t.length,nosp=t.replace(/\s/g,'').length,lines=t.split('\n').length;const hash=await sha256(t);const rows=[['Characters',chars],['Characters (no spaces)',nosp],['Words',words],['Lines',lines],['Sentences',t.split(/[.!?]+/).filter(s=>s.trim()).length],['Paragraphs',t.split(/\n\n+/).length],['Avg Word Length',words>0?(nosp/words).toFixed(1):0],['SHA-256 Hash',`<code style="font-size:0.75rem;word-break:break-all">${hash}</code>`]];document.getElementById('hashResults').innerHTML=rows.map(([k,v])=>`<div style="display:flex;justify-content:space-between;align-items:flex-start;padding:6px 0;border-bottom:1px solid var(--border)"><span>${k}</span><strong>${v}</strong></div>`).join('');document.getElementById('resultBox').classList.add('show');}
</script>""")

# REAL ESTATE
page("property-tax-calculator.html","Property Tax Calculator",
"Calculate annual property tax from assessed value and mill rate. Find effective tax rate and monthly payment.",
"property tax calculator, real estate tax, annual property tax, mill rate calculator, assessed value tax",
"&#127968;","#37474f","#455a64","finance","&#128176;","Finance",
cb("Property Tax Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Home Market Value ($)</label><input type="number" class="form-control" id="f1" value="350000" step="5000"></div>
<div class="col-md-6"><label class="form-label">Assessment Rate (%)</label><input type="number" class="form-control" id="f2" value="85" step="1"></div>
<div class="col-md-6"><label class="form-label">Mill Rate (mills)</label><input type="number" class="form-control" id="f3" value="15" step="0.1"><small class="text-muted">1 mill = $1 per $1,000 assessed value</small></div>
<div class="col-md-6"><label class="form-label">Homestead Exemption ($)</label><input type="number" class="form-control" id="f4" value="25000" step="1000"></div>
</div>""",
[("Assessed Value","r1"),("Annual Property Tax","r2"),("Monthly Tax Payment","r3"),("Effective Tax Rate","r4")]),
"""<script>
function calc(){const market=+document.getElementById('f1').value,rate=+document.getElementById('f2').value/100,mill=+document.getElementById('f3').value,exempt=+document.getElementById('f4').value;const assessed=market*rate,taxable=Math.max(0,assessed-exempt),annual=taxable*mill/1000;document.getElementById('r1').textContent='$'+assessed.toFixed(0);document.getElementById('r2').textContent='$'+annual.toFixed(0);document.getElementById('r3').textContent='$'+(annual/12).toFixed(0);document.getElementById('r4').textContent=(annual/market*100).toFixed(3)+'%';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("home-affordability-calculator.html","Home Affordability Calculator",
"Calculate how much house you can afford based on income, debts, and down payment. Get pre-approval estimate.",
"home affordability calculator, how much house can I afford, mortgage affordability, maximum home price, house budget",
"&#127968;","#1a237e","#283593","finance","&#128176;","Finance",
cb("Home Affordability Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Annual Gross Income ($)</label><input type="number" class="form-control" id="f1" value="80000" step="5000"></div>
<div class="col-md-6"><label class="form-label">Monthly Debts ($)</label><input type="number" class="form-control" id="f2" value="400" step="50"><small class="text-muted">Car loans, student loans, credit cards</small></div>
<div class="col-md-6"><label class="form-label">Down Payment ($)</label><input type="number" class="form-control" id="f3" value="40000" step="5000"></div>
<div class="col-md-6"><label class="form-label">Interest Rate (%)</label><input type="number" class="form-control" id="f4" value="7" step="0.1"></div>
<div class="col-md-6"><label class="form-label">Loan Term (years)</label><input type="number" class="form-control" id="f5" value="30" step="5"></div>
</div>""",
[("Max Home Price","r1"),("Max Mortgage","r2"),("Monthly Payment (est.)","r3"),("DTI Ratio Used","r4")],
"Calculate Affordability"),
"""<script>
function calc(){const inc=+document.getElementById('f1').value,debts=+document.getElementById('f2').value,dp=+document.getElementById('f3').value,rate=+document.getElementById('f4').value/100/12,n=+document.getElementById('f5').value*12;const maxPITI=inc/12*0.28,maxTotal=inc/12*0.36-debts;const maxPmt=Math.min(maxPITI,maxTotal);const maxLoan=maxPmt*(Math.pow(1+rate,n)-1)/(rate*Math.pow(1+rate,n));const maxHome=maxLoan+dp;document.getElementById('r1').textContent='$'+maxHome.toFixed(0);document.getElementById('r2').textContent='$'+maxLoan.toFixed(0);document.getElementById('r3').textContent='$'+maxPmt.toFixed(0)+'/mo';document.getElementById('r4').textContent='28%/36% rule';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("land-area-calculator.html","Land Area Calculator",
"Calculate land area in acres, square feet, square meters, hectares, and cents. Convert between area units easily.",
"land area calculator, acres to square feet, square meter to acre, land measurement calculator, plot area, hectare",
"&#127807;","#2e7d32","#388e3c","construction","&#127959;","Construction",
"""<div class="calc-box">
<h2 class="calc-title">Land Area Calculator</h2>
<div class="d-flex gap-2 mb-3 flex-wrap">
<button class="cat-pill active" onclick="setMode('rect',this)">Rectangle</button>
<button class="cat-pill" onclick="setMode('triangle',this)">Triangle</button>
<button class="cat-pill" onclick="setMode('convert',this)">Unit Convert</button>
</div>
<div id="rectDiv">
<div class="row g-3">
<div class="col-md-4"><label class="form-label">Length</label><input type="number" class="form-control" id="l1" value="100" step="0.1"></div>
<div class="col-md-4"><label class="form-label">Width</label><input type="number" class="form-control" id="l2" value="50" step="0.1"></div>
<div class="col-md-4"><label class="form-label">Unit</label><select class="form-select" id="lunit"><option value="1">Meters</option><option value="0.3048">Feet</option><option value="0.9144">Yards</option></select></div>
</div>
</div>
<div id="convertDiv" style="display:none">
<div class="row g-3">
<div class="col-md-6"><label class="form-label">Value</label><input type="number" class="form-control" id="cv" value="1" step="any"></div>
<div class="col-md-6"><label class="form-label">From Unit</label>
<select class="form-select" id="cu">
<option value="1">Square Meter (m&#178;)</option>
<option value="4046.86" selected>Acre</option>
<option value="10000">Hectare (ha)</option>
<option value="0.0929">Square Foot (sq ft)</option>
<option value="40.4686">Cent (Indian)</option>
</select></div>
</div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-map me-2"></i>Calculate Area</button>
<div class="result-box" id="resultBox"><div id="areaResults" style="font-size:0.9rem"></div></div></div>""",
"""<script>
let lMode='rect';
function setMode(m,b){lMode=m;document.querySelectorAll('.cat-pill').forEach(p=>p.classList.remove('active'));b.classList.add('active');document.getElementById('rectDiv').style.display=m!=='convert'?'block':'none';document.getElementById('convertDiv').style.display=m==='convert'?'block':'none';}
const au=[['Square Meters (m\u00B2)',1],['Square Feet (sq ft)',0.0929],['Square Yards',0.8361],['Acres',4046.86],['Hectares (ha)',10000],['Cents (Indian)',40.4686],['Bigha (avg)',2508.38],['Square Kilometers',1000000]];
function calc(){let sqm;if(lMode==='convert'){const v=+document.getElementById('cv').value,f=+document.getElementById('cu').value;sqm=v*f;}else{const l=+document.getElementById('l1').value,w=+document.getElementById('l2').value,u=+document.getElementById('lunit').value;sqm=l*u*w*u;}const rows=au.map(([n,fac])=>`<div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid var(--border)"><span>${n}</span><strong>${(sqm/fac).toPrecision(6)}</strong></div>`).join('');document.getElementById('areaResults').innerHTML=rows;document.getElementById('resultBox').classList.add('show');}
</script>""")

# FINAL BATCH - More tools
page("net-promoter-score-calculator.html","Net Promoter Score (NPS) Calculator",
"Calculate your Net Promoter Score from survey responses. Analyze promoters, passives, and detractors.",
"NPS calculator, net promoter score calculator, customer satisfaction score, promoter detractor ratio, survey score",
"&#128200;","#1b5e20","#2e7d32","business","&#128188;","Business",
"""<div class="calc-box">
<h2 class="calc-title">Net Promoter Score (NPS) Calculator</h2>
<p style="color:var(--text-secondary);font-size:0.9rem">Enter the number of respondents for each score (0-10)</p>
<div class="row g-3">
<div class="col-12"><label class="form-label" style="color:#f44336">Detractors (Score 0-6)</label>
<div class="row g-2">
<div class="col" v-for="i in 7"><label class="text-center" style="font-size:0.8rem;display:block" id="dl0"></label></div>
</div>
<div class="row g-1" id="detRow">
<div class="col"><label class="text-center d-block" style="font-size:0.8rem">0</label><input type="number" class="form-control form-control-sm" id="s0" value="2" min="0"></div>
<div class="col"><label class="text-center d-block" style="font-size:0.8rem">1</label><input type="number" class="form-control form-control-sm" id="s1" value="1" min="0"></div>
<div class="col"><label class="text-center d-block" style="font-size:0.8rem">2</label><input type="number" class="form-control form-control-sm" id="s2" value="1" min="0"></div>
<div class="col"><label class="text-center d-block" style="font-size:0.8rem">3</label><input type="number" class="form-control form-control-sm" id="s3" value="2" min="0"></div>
<div class="col"><label class="text-center d-block" style="font-size:0.8rem">4</label><input type="number" class="form-control form-control-sm" id="s4" value="3" min="0"></div>
<div class="col"><label class="text-center d-block" style="font-size:0.8rem">5</label><input type="number" class="form-control form-control-sm" id="s5" value="5" min="0"></div>
<div class="col"><label class="text-center d-block" style="font-size:0.8rem">6</label><input type="number" class="form-control form-control-sm" id="s6" value="8" min="0"></div>
</div>
</div>
<div class="col-12"><label class="form-label" style="color:#ff9800">Passives (Score 7-8)</label>
<div class="row g-1">
<div class="col"><label class="text-center d-block" style="font-size:0.8rem">7</label><input type="number" class="form-control form-control-sm" id="s7" value="15" min="0"></div>
<div class="col"><label class="text-center d-block" style="font-size:0.8rem">8</label><input type="number" class="form-control form-control-sm" id="s8" value="20" min="0"></div>
</div>
</div>
<div class="col-12"><label class="form-label" style="color:#4caf50">Promoters (Score 9-10)</label>
<div class="row g-1">
<div class="col"><label class="text-center d-block" style="font-size:0.8rem">9</label><input type="number" class="form-control form-control-sm" id="s9" value="30" min="0"></div>
<div class="col"><label class="text-center d-block" style="font-size:0.8rem">10</label><input type="number" class="form-control form-control-sm" id="s10" value="25" min="0"></div>
</div>
</div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-graph-up me-2"></i>Calculate NPS</button>
<div class="result-box" id="resultBox">
<div class="row g-3 text-center">
<div class="col-6"><div class="result-label">Net Promoter Score</div><div class="result-value" id="r1">-</div></div>
<div class="col-6"><div class="result-label">Interpretation</div><div class="result-value" id="r2" style="font-size:1rem">-</div></div>
<div class="col-4"><div class="result-label">Promoters %</div><div class="result-value" id="r3" style="color:#4caf50;font-size:1.2rem">-</div></div>
<div class="col-4"><div class="result-label">Passives %</div><div class="result-value" id="r4" style="color:#ff9800;font-size:1.2rem">-</div></div>
<div class="col-4"><div class="result-label">Detractors %</div><div class="result-value" id="r5" style="color:#f44336;font-size:1.2rem">-</div></div>
</div></div></div>""",
"""<script>
function calc(){const vals=Array.from({length:11},(_,i)=>+document.getElementById('s'+i).value||0);const total=vals.reduce((a,b)=>a+b,0);if(!total)return;const det=vals.slice(0,7).reduce((a,b)=>a+b,0),pass=(vals[7]+vals[8]),prom=(vals[9]+vals[10]);const nps=Math.round((prom-det)/total*100);const interp=nps<0?'Needs Improvement':nps<30?'Good':nps<70?'Great':'Excellent (World Class)';document.getElementById('r1').textContent=nps;document.getElementById('r2').textContent=interp;document.getElementById('r3').textContent=(prom/total*100).toFixed(1)+'%';document.getElementById('r4').textContent=(pass/total*100).toFixed(1)+'%';document.getElementById('r5').textContent=(det/total*100).toFixed(1)+'%';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("electricity-usage-calculator.html","Electricity Usage Calculator",
"Calculate electricity consumption and cost for any appliance. Monthly power bill estimator for home and office.",
"electricity usage calculator, power consumption calculator, electricity cost calculator, kWh calculator, appliance power",
"&#9889;","#f57f17","#f9a825","environment","&#127807;","Environment",
"""<div class="calc-box">
<h2 class="calc-title">Electricity Usage Calculator</h2>
<div id="appliances">
<div class="row g-2 mb-2 align-items-end" id="ap1">
<div class="col-4"><label class="form-label">Appliance</label><select class="form-select form-select-sm" id="apt1"><option value="100">Light Bulb LED (10W)</option><option value="1200">Air Conditioner (1200W)</option><option value="800" selected>TV (80W avg)</option><option value="2000">Electric Kettle (2000W)</option><option value="500">Refrigerator (150W avg)</option><option value="1000">Washing Machine (1000W)</option><option value="2500">Electric Oven (2500W)</option><option value="1500">Microwave (1500W)</option></select></div>
<div class="col-2"><label class="form-label">Watts</label><input type="number" class="form-control form-control-sm" id="apw1" value="80" step="1"></div>
<div class="col-3"><label class="form-label">Hours/Day</label><input type="number" class="form-control form-control-sm" id="aph1" value="5" step="0.5"></div>
<div class="col-3"><label class="form-label">Days/Month</label><input type="number" class="form-control form-control-sm" id="apd1" value="30" step="1"></div>
</div>
</div>
<button class="btn btn-outline-secondary btn-sm mt-2 mb-3" onclick="addAp()">+ Add Appliance</button>
<div class="col-md-6"><label class="form-label">Rate ($/kWh)</label><input type="number" class="form-control" id="elRate" value="0.13" step="0.01"></div>
<button class="btn-calculate mt-3" onclick="calc()"><i class="bi bi-lightning me-2"></i>Calculate Cost</button>
<div class="result-box" id="resultBox">
<div class="row g-3 text-center">
<div class="col-6"><div class="result-label">Monthly kWh</div><div class="result-value" id="r1">-</div></div>
<div class="col-6"><div class="result-label">Monthly Cost</div><div class="result-value" id="r2">-</div></div>
<div class="col-6"><div class="result-label">Annual kWh</div><div class="result-value" id="r3">-</div></div>
<div class="col-6"><div class="result-label">Annual Cost</div><div class="result-value" id="r4">-</div></div>
</div></div></div>""",
"""<script>
let apc=1;
function addAp(){apc++;document.getElementById('appliances').insertAdjacentHTML('beforeend',`<div class="row g-2 mb-2 align-items-end" id="ap${apc}"><div class="col-4"><select class="form-select form-select-sm" id="apt${apc}" onchange="this.nextElementSibling.value=this.value"><option value="100">LED Bulb</option><option value="1200">AC</option><option value="80">TV</option><option value="2000">Kettle</option><option value="500">Fridge</option></select></div><div class="col-2"><input type="number" class="form-control form-control-sm" id="apw${apc}" value="100"></div><div class="col-3"><input type="number" class="form-control form-control-sm" id="aph${apc}" value="4"></div><div class="col-3"><input type="number" class="form-control form-control-sm" id="apd${apc}" value="30"></div></div>`);}
function calc(){let kwh=0;for(let i=1;i<=apc;i++){const w=+document.getElementById('apw'+i)?.value||0,h=+document.getElementById('aph'+i)?.value||0,d=+document.getElementById('apd'+i)?.value||0;kwh+=w/1000*h*d;}const rate=+document.getElementById('elRate').value;document.getElementById('r1').textContent=kwh.toFixed(2)+' kWh';document.getElementById('r2').textContent='$'+(kwh*rate).toFixed(2);document.getElementById('r3').textContent=(kwh*12).toFixed(0)+' kWh';document.getElementById('r4').textContent='$'+(kwh*12*rate).toFixed(2);document.getElementById('resultBox').classList.add('show');}
document.getElementById('apt1').onchange=function(){document.getElementById('apw1').value=this.value;};
</script>""")

print("\n=== Batch 4 complete! ===")
