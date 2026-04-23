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

# =========================================
# BATCH 3 - MORE CALCULATORS
# =========================================

# FINANCE
page("net-pay-calculator.html","Net Pay / Take Home Salary Calculator",
"Calculate your exact take-home pay after all deductions, taxes, PF, insurance, and other deductions.",
"net pay calculator, take home salary calculator, salary after deductions, PF deduction calculator, in hand salary",
"&#128184;","#1a237e","#283593","finance","&#128176;","Finance",
cb("Net Pay Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Gross Annual Salary ($)</label><input type="number" class="form-control" id="f1" value="60000" step="1000"></div>
<div class="col-md-6"><label class="form-label">Federal Tax (%)</label><input type="number" class="form-control" id="f2" value="22" step="0.5"></div>
<div class="col-md-6"><label class="form-label">State Tax (%)</label><input type="number" class="form-control" id="f3" value="5" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Social Security (%)</label><input type="number" class="form-control" id="f4" value="6.2" step="0.1"></div>
<div class="col-md-6"><label class="form-label">Medicare (%)</label><input type="number" class="form-control" id="f5" value="1.45" step="0.01"></div>
<div class="col-md-6"><label class="form-label">Other Deductions/yr ($)</label><input type="number" class="form-control" id="f6" value="2400" step="100"></div>
</div>""",
[("Annual Net Pay","r1"),("Monthly Take-Home","r2"),("Bi-Weekly Pay","r3"),("Effective Tax Rate","r4")]),
"""<script>
function calc(){const g=+document.getElementById('f1').value,ft=+document.getElementById('f2').value/100,st=+document.getElementById('f3').value/100,ss=+document.getElementById('f4').value/100,med=+document.getElementById('f5').value/100,other=+document.getElementById('f6').value;const ded=g*(ft+st+ss+med)+other,net=g-ded;document.getElementById('r1').textContent='$'+net.toFixed(0);document.getElementById('r2').textContent='$'+(net/12).toFixed(2);document.getElementById('r3').textContent='$'+(net/26).toFixed(2);document.getElementById('r4').textContent=(ded/g*100).toFixed(1)+'%';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("lease-calculator.html","Car Lease Calculator",
"Calculate monthly car lease payment, total lease cost, and compare lease vs buy options for any vehicle.",
"car lease calculator, auto lease calculator, monthly lease payment, lease vs buy calculator, vehicle lease",
"&#128663;","#0d47a1","#1565c0","finance","&#128176;","Finance",
cb("Car Lease Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Vehicle Price ($)</label><input type="number" class="form-control" id="f1" value="30000" step="500"></div>
<div class="col-md-6"><label class="form-label">Down Payment ($)</label><input type="number" class="form-control" id="f2" value="3000" step="500"></div>
<div class="col-md-6"><label class="form-label">Residual Value (%)</label><input type="number" class="form-control" id="f3" value="55" step="1"></div>
<div class="col-md-6"><label class="form-label">Money Factor (APR/2400)</label><input type="number" class="form-control" id="f4" value="0.0015" step="0.0001"></div>
<div class="col-md-6"><label class="form-label">Lease Term (months)</label><input type="number" class="form-control" id="f5" value="36" step="12"></div>
<div class="col-md-6"><label class="form-label">Sales Tax (%)</label><input type="number" class="form-control" id="f6" value="8" step="0.5"></div>
</div>""",
[("Monthly Payment","r1"),("Total Lease Cost","r2"),("Residual Value","r3"),("APR Equivalent","r4")]),
"""<script>
function calc(){const vp=+document.getElementById('f1').value,dp=+document.getElementById('f2').value,res=+document.getElementById('f3').value/100,mf=+document.getElementById('f4').value,n=+document.getElementById('f5').value,tax=+document.getElementById('f6').value/100;const cap=vp-dp,rv=vp*res,depn=(cap-rv)/n,fin=(cap+rv)*mf,base=depn+fin,monthly=base*(1+tax);document.getElementById('r1').textContent='$'+monthly.toFixed(2);document.getElementById('r2').textContent='$'+(monthly*n+dp).toFixed(0);document.getElementById('r3').textContent='$'+rv.toFixed(0);document.getElementById('r4').textContent=(mf*2400).toFixed(2)+'%';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("gold-calculator.html","Gold Price Calculator",
"Calculate gold value by weight in grams, tola, troy ounce, and kilogram at current gold prices by purity.",
"gold calculator, gold price calculator, gold value calculator, 24k gold price, gold tola price, gold purity calculator",
"&#129351;","#f57f17","#f9a825","finance","&#128176;","Finance",
"""<div class="calc-box">
<h2 class="calc-title">Gold Price Calculator</h2>
<div class="row g-3">
<div class="col-md-6"><label class="form-label">Gold Price (per troy oz, $)</label><input type="number" class="form-control" id="f1" value="2350" step="10"></div>
<div class="col-md-6"><label class="form-label">Weight</label><input type="number" class="form-control" id="f2" value="10" step="0.1"></div>
<div class="col-md-6"><label class="form-label">Weight Unit</label>
<select class="form-select" id="f3">
<option value="31.1035">Troy Ounce</option>
<option value="1" selected>Gram</option>
<option value="11.6638">Tola</option>
<option value="1000">Kilogram</option>
</select></div>
<div class="col-md-6"><label class="form-label">Purity (Karat)</label>
<select class="form-select" id="f4">
<option value="1">24K (99.9% Pure)</option>
<option value="0.9167" selected>22K (91.67%)</option>
<option value="0.75">18K (75%)</option>
<option value="0.585">14K (58.5%)</option>
<option value="0.417">10K (41.7%)</option>
</select></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-coin me-2"></i>Calculate Gold Value</button>
<div class="result-box" id="resultBox">
<div class="row g-3 text-center">
<div class="col-6"><div class="result-label">Gold Value</div><div class="result-value" id="r1">-</div></div>
<div class="col-6"><div class="result-label">Price Per Gram</div><div class="result-value" id="r2">-</div></div>
<div class="col-6"><div class="result-label">Pure Gold Weight</div><div class="result-value" id="r3">-</div></div>
<div class="col-6"><div class="result-label">Price Per Tola</div><div class="result-value" id="r4">-</div></div>
</div></div></div>""",
"""<script>
function calc(){const ozPrice=+document.getElementById('f1').value,wt=+document.getElementById('f2').value,unit=+document.getElementById('f3').value,pur=+document.getElementById('f4').value;const pgram=ozPrice/31.1035,ptola=pgram*11.6638,grams=wt*(unit/31.1035)*31.1035,pure=grams*pur/31.1035,val=pure*ozPrice*31.1035/31.1035;const gramVal=pgram*pur,totalGrams=wt*(unit===1?1:unit/31.1035*(unit===31.1035?1:unit===11.6638?11.6638/31.1035:1000/31.1035));document.getElementById('r1').textContent='$'+(pgram*pur*(wt*(unit===31.1035?31.1035:unit===11.6638?11.6638:unit===1?1:1000))).toFixed(2);document.getElementById('r2').textContent='$'+gramVal.toFixed(2);document.getElementById('r3').textContent=(wt*(unit===31.1035?31.1035:unit===11.6638?11.6638:unit===1000?1000:1)*pur).toFixed(4)+'g pure';document.getElementById('r4').textContent='$'+ptola.toFixed(2);document.getElementById('resultBox').classList.add('show');}
</script>""")

page("emi-prepayment-calculator.html","EMI Prepayment Calculator",
"Calculate EMI prepayment savings on home loan or personal loan. See interest saved and loan tenure reduction.",
"EMI prepayment calculator, home loan prepayment, partial prepayment calculator, loan foreclosure, loan tenure reduction",
"&#127968;","#880e4f","#ad1457","finance","&#128176;","Finance",
cb("EMI Prepayment Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Original Loan Amount ($)</label><input type="number" class="form-control" id="f1" value="200000" step="5000"></div>
<div class="col-md-6"><label class="form-label">Annual Interest Rate (%)</label><input type="number" class="form-control" id="f2" value="8.5" step="0.1"></div>
<div class="col-md-6"><label class="form-label">Loan Tenure (months)</label><input type="number" class="form-control" id="f3" value="240" step="12"></div>
<div class="col-md-6"><label class="form-label">EMIs Already Paid</label><input type="number" class="form-control" id="f4" value="24" step="1"></div>
<div class="col-md-6"><label class="form-label">Prepayment Amount ($)</label><input type="number" class="form-control" id="f5" value="20000" step="1000"></div>
</div>""",
[("EMIs Saved","r1"),("Interest Saved","r2"),("New Tenure (months)","r3"),("New Outstanding Balance","r4")],
"Calculate Savings"),
"""<script>
function calc(){const P=+document.getElementById('f1').value,r=+document.getElementById('f2').value/100/12,n=+document.getElementById('f3').value,paid=+document.getElementById('f4').value,prep=+document.getElementById('f5').value;const emi=P*r*Math.pow(1+r,n)/(Math.pow(1+r,n)-1);let bal=P;for(let i=0;i<paid;i++){bal=bal*(1+r)-emi;}const newBal=Math.max(0,bal-prep);const remOld=n-paid;function calcMonths(b,e){let m=0,b2=b;while(b2>0&&m<600){b2=b2*(1+r)-e;m++;}return m;}const mOld=calcMonths(bal,emi),mNew=calcMonths(newBal,emi);const saved=mOld-mNew;document.getElementById('r1').textContent=saved+' EMIs';document.getElementById('r2').textContent='$'+(saved*emi).toFixed(0);document.getElementById('r3').textContent=mNew+' months';document.getElementById('r4').textContent='$'+newBal.toFixed(0);document.getElementById('resultBox').classList.add('show');}
</script>""")

# HEALTH
page("alcohol-unit-calculator.html","Alcohol Unit Calculator",
"Calculate alcohol units in any drink. Track your weekly consumption and safe drinking limits by drink type.",
"alcohol unit calculator, units of alcohol, how many units in a beer, alcohol consumption calculator, safe drinking limit",
"&#127867;","#880e4f","#ad1457","health","&#10084;","Health",
"""<div class="calc-box">
<h2 class="calc-title">Alcohol Unit Calculator</h2>
<div class="alert" style="background:rgba(255,152,0,0.1);border-left:4px solid #ff9800;padding:12px;border-radius:8px;margin-bottom:16px">
<small><strong>Guideline:</strong> Men: max 14 units/week | Women: max 14 units/week | 1 unit = 10ml pure alcohol</small>
</div>
<div id="drinks"></div>
<button class="btn btn-outline-secondary btn-sm mt-2" onclick="addDrink()">+ Add Another Drink</button>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate Units</button>
<div class="result-box" id="resultBox">
<div class="row g-3 text-center">
<div class="col-6"><div class="result-label">Total Units</div><div class="result-value" id="r1">-</div></div>
<div class="col-6"><div class="result-label">Calories</div><div class="result-value" id="r2">-</div></div>
<div class="col-6"><div class="result-label">Pure Alcohol (g)</div><div class="result-value" id="r3">-</div></div>
<div class="col-6"><div class="result-label">Weekly Limit Used</div><div class="result-value" id="r4">-</div></div>
</div></div></div>""",
"""<script>
let dc=0;
const drinks={beer:{name:'Beer (4.5%)',abv:4.5,ml:500,cal:215},wine:{name:'Wine (13%)',abv:13,ml:175,cal:160},spirits:{name:'Spirit (40%)',abv:40,ml:25,cal:55},cider:{name:'Cider (4%)',abv:4,ml:440,cal:200}};
function addDrink(){dc++;const d=document.getElementById('drinks');d.innerHTML+=`<div class="row g-2 align-items-end mb-2"><div class="col-5"><select class="form-select form-select-sm" id="dt${dc}"><option value="beer">Beer 500ml</option><option value="wine">Wine 175ml</option><option value="spirits">Spirit 25ml</option><option value="cider">Cider 440ml</option></select></div><div class="col-3"><input type="number" class="form-control form-control-sm" id="qty${dc}" value="1" min="1" max="20"></div><div class="col-4"><small class="text-muted">quantity</small></div></div>`;}
function calc(){let units=0,cal=0;for(let i=1;i<=dc;i++){const type=document.getElementById('dt'+i)?.value,qty=+document.getElementById('qty'+i)?.value||0;if(!type)continue;const d=drinks[type];units+=d.abv*d.ml*qty/1000;cal+=d.cal*qty;}document.getElementById('r1').textContent=units.toFixed(1)+' units';document.getElementById('r2').textContent=cal.toFixed(0)+' kcal';document.getElementById('r3').textContent=(units*8).toFixed(1)+'g';document.getElementById('r4').textContent=(units/14*100).toFixed(0)+'%';document.getElementById('resultBox').classList.add('show');}
document.addEventListener('DOMContentLoaded',()=>{addDrink();addDrink();});
</script>""")

page("bmi-prime-calculator.html","BMI Prime Calculator",
"Calculate BMI Prime and Ponderal Index. BMI Prime is a decimal number where 1.0 is the upper limit of normal BMI.",
"BMI prime calculator, ponderal index calculator, BMI ratio calculator, healthy BMI range, body mass index prime",
"&#128170;","#0d47a1","#1565c0","health","&#10084;","Health",
cb("BMI Prime & Ponderal Index Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Weight (kg)</label><input type="number" class="form-control" id="f1" value="70" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Height (cm)</label><input type="number" class="form-control" id="f2" value="175" step="1"></div>
<div class="col-md-6"><label class="form-label">Age (years)</label><input type="number" class="form-control" id="f3" value="25" step="1"></div>
<div class="col-md-6"><label class="form-label">Gender</label><select class="form-select" id="f4"><option>Male</option><option>Female</option></select></div>
</div>""",
[("BMI","r1"),("BMI Prime","r2"),("Ponderal Index","r3"),("Healthy Weight Range","r4")]),
"""<script>
function calc(){const w=+document.getElementById('f1').value,h=+document.getElementById('f2').value/100;const bmi=w/(h*h),prime=bmi/25,pi=w/(h**3);let cat;if(bmi<16)cat='Severely Underweight';else if(bmi<18.5)cat='Underweight';else if(bmi<25)cat='Normal';else if(bmi<30)cat='Overweight';else if(bmi<35)cat='Obese I';else cat='Obese II+';const minW=(18.5*h*h).toFixed(1),maxW=(24.9*h*h).toFixed(1);document.getElementById('r1').textContent=bmi.toFixed(2)+' ('+cat+')';document.getElementById('r2').textContent=prime.toFixed(3);document.getElementById('r3').textContent=pi.toFixed(2)+' kg/m\u00B3';document.getElementById('r4').textContent=minW+' - '+maxW+' kg';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("body-fat-percentage-calculator.html","Body Fat Percentage Calculator",
"Calculate body fat percentage using Navy method, BMI method, and skinfold measurements. Find your fat-free mass.",
"body fat percentage calculator, body fat calculator, navy body fat formula, how to calculate body fat, lean body mass",
"&#128170;","#1b5e20","#2e7d32","health","&#10084;","Health",
cb("Body Fat Calculator (Navy Method)",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Gender</label><select class="form-select" id="f0" onchange="toggleGender()"><option value="m">Male</option><option value="f">Female</option></select></div>
<div class="col-md-6"><label class="form-label">Height (cm)</label><input type="number" class="form-control" id="f1" value="175" step="1"></div>
<div class="col-md-6"><label class="form-label">Neck Circumference (cm)</label><input type="number" class="form-control" id="f2" value="38" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Waist Circumference (cm)</label><input type="number" class="form-control" id="f3" value="85" step="0.5"></div>
<div class="col-md-6" id="hipWrap"><label class="form-label">Hip Circumference (cm) - Women</label><input type="number" class="form-control" id="f4" value="95" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Weight (kg)</label><input type="number" class="form-control" id="f5" value="75" step="0.5"></div>
</div>""",
[("Body Fat %","r1"),("Fat Mass","r2"),("Lean Mass","r3"),("Category","r4")]),
"""<script>
function toggleGender(){document.getElementById('hipWrap').style.display=document.getElementById('f0').value==='f'?'block':'none';}
function calc(){const g=document.getElementById('f0').value,h=+document.getElementById('f1').value,neck=+document.getElementById('f2').value,waist=+document.getElementById('f3').value,hip=+document.getElementById('f4').value,wt=+document.getElementById('f5').value;let bf;if(g==='m'){bf=86.010*Math.log10(waist-neck)-70.041*Math.log10(h)+36.76;}else{bf=163.205*Math.log10(waist+hip-neck)-97.684*Math.log10(h)-78.387;}bf=Math.max(0,Math.min(70,bf));const fat=wt*bf/100,lean=wt-fat;let cat;if(g==='m'){cat=bf<6?'Essential Fat':bf<14?'Athletic':bf<18?'Fitness':bf<25?'Average':'Obese';}else{cat=bf<14?'Essential Fat':bf<21?'Athletic':bf<25?'Fitness':bf<32?'Average':'Obese';}document.getElementById('r1').textContent=bf.toFixed(1)+'%';document.getElementById('r2').textContent=fat.toFixed(1)+' kg';document.getElementById('r3').textContent=lean.toFixed(1)+' kg';document.getElementById('r4').textContent=cat;document.getElementById('resultBox').classList.add('show');}
</script>""")

page("one-rep-max-calculator.html","One Rep Max (1RM) Calculator",
"Calculate your one-rep max (1RM) for bench press, squat, deadlift using multiple formulas. Find training percentages.",
"one rep max calculator, 1RM calculator, bench press max calculator, squat 1RM, deadlift calculator, strength training",
"&#128170;","#b71c1c","#c62828","health","&#10084;","Health",
cb("1 Rep Max Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Weight Lifted (kg)</label><input type="number" class="form-control" id="f1" value="100" step="2.5"></div>
<div class="col-md-6"><label class="form-label">Reps Performed</label><input type="number" class="form-control" id="f2" value="5" min="1" max="12"></div>
</div>""",
[("Estimated 1RM","r1"),("80% (8 reps)","r2"),("85% (5 reps)","r3"),("90% (3 reps)","r4")],
"Calculate 1RM"),
"""<script>
function calc(){const w=+document.getElementById('f1').value,r=+document.getElementById('f2').value;const epley=w*(1+r/30),brzycki=w*(36/(37-r));const orm=(epley+brzycki)/2;document.getElementById('r1').textContent=orm.toFixed(1)+' kg';document.getElementById('r2').textContent=(orm*0.80).toFixed(1)+' kg';document.getElementById('r3').textContent=(orm*0.85).toFixed(1)+' kg';document.getElementById('r4').textContent=(orm*0.90).toFixed(1)+' kg';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("target-heart-rate-calculator.html","Target Heart Rate Calculator",
"Calculate maximum and target heart rate for fat burning, cardio, and HIIT training by age and fitness level.",
"target heart rate calculator, maximum heart rate, heart rate zones for exercise, fat burning heart rate, cardio heart rate",
"&#10084;","#b71c1c","#c62828","health","&#10084;","Health",
cb("Target Heart Rate Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Age (years)</label><input type="number" class="form-control" id="f1" value="30" min="10" max="100"></div>
<div class="col-md-6"><label class="form-label">Resting Heart Rate (bpm)</label><input type="number" class="form-control" id="f2" value="70" min="40" max="100"></div>
</div>
<div class="mt-3" id="zoneTable"></div>""",
[("Max HR (220-age)","r1"),("Fat Burn Zone","r2"),("Cardio Zone","r3"),("Peak Zone","r4")],
"Calculate Zones"),
"""<script>
function calc(){const age=+document.getElementById('f1').value,rhr=+document.getElementById('f2').value;const mhr=220-age,hrr=mhr-rhr;const zones=[['Warm Up (50-60%)',Math.round(rhr+hrr*0.5),Math.round(rhr+hrr*0.6),'#4caf50'],['Fat Burn (60-70%)',Math.round(rhr+hrr*0.6),Math.round(rhr+hrr*0.7),'#2196f3'],['Cardio (70-80%)',Math.round(rhr+hrr*0.7),Math.round(rhr+hrr*0.8),'#ff9800'],['Hard (80-90%)',Math.round(rhr+hrr*0.8),Math.round(rhr+hrr*0.9),'#f44336'],['Max (90-100%)',Math.round(rhr+hrr*0.9),mhr,'#9c27b0']];document.getElementById('zoneTable').innerHTML='<h5 style="margin-top:16px">Heart Rate Zones</h5>'+zones.map(([n,lo,hi,c])=>`<div style="display:flex;justify-content:space-between;padding:8px 12px;margin-bottom:6px;border-radius:8px;background:${c}22;border-left:4px solid ${c}"><span>${n}</span><strong>${lo} - ${hi} bpm</strong></div>`).join('');document.getElementById('r1').textContent=mhr+' bpm';document.getElementById('r2').textContent=zones[1][1]+'-'+zones[1][2]+' bpm';document.getElementById('r3').textContent=zones[2][1]+'-'+zones[2][2]+' bpm';document.getElementById('r4').textContent=zones[3][1]+'-'+zones[3][2]+' bpm';document.getElementById('resultBox').classList.add('show');}
</script>""")

# MATH
page("trigonometry-calculator.html","Trigonometry Calculator",
"Calculate sin, cos, tan, cot, sec, csc for any angle in degrees or radians. Inverse trig functions included.",
"trigonometry calculator, sin cos tan calculator, trig calculator, inverse trigonometry, sin calculator, cos calculator",
"&#128290;","#4a148c","#6a1b9a","math","&#128290;","Math",
cb("Trigonometry Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Angle Value</label><input type="number" class="form-control" id="f1" value="45" step="any"></div>
<div class="col-md-6"><label class="form-label">Unit</label><select class="form-select" id="f2"><option value="deg" selected>Degrees</option><option value="rad">Radians</option></select></div>
</div>""",
[("sin","r1"),("cos","r2"),("tan","r3"),("cot / sec / csc","r4")],
"Calculate"),
"""<script>
function calc(){const v=+document.getElementById('f1').value,unit=document.getElementById('f2').value;const rad=unit==='deg'?v*Math.PI/180:v;const s=Math.sin(rad),c=Math.cos(rad),t=Math.tan(rad);document.getElementById('r1').textContent=s.toFixed(6);document.getElementById('r2').textContent=c.toFixed(6);document.getElementById('r3').textContent=Math.abs(t)>1e10?'undefined':t.toFixed(6);document.getElementById('r4').textContent='cot='+(!Math.abs(s)<1e-10?(c/s).toFixed(4):'undef')+' sec='+(Math.abs(c)>1e-10?(1/c).toFixed(4):'undef')+' csc='+(Math.abs(s)>1e-10?(1/s).toFixed(4):'undef');document.getElementById('resultBox').classList.add('show');}
</script>""")

page("logarithm-calculator.html","Logarithm Calculator",
"Calculate log base 10, natural log (ln), log base 2, and any custom base logarithm instantly.",
"logarithm calculator, log calculator, log base 10 calculator, natural log calculator, ln calculator, log base 2",
"&#128290;","#1a237e","#283593","math","&#128290;","Math",
cb("Logarithm Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Number (x)</label><input type="number" class="form-control" id="f1" value="100" step="any" min="0.0001"></div>
<div class="col-md-6"><label class="form-label">Custom Base (b)</label><input type="number" class="form-control" id="f2" value="10" step="any" min="1.0001"></div>
</div>""",
[("log\u2081\u2080(x)","r1"),("ln(x) - Natural Log","r2"),("log\u2082(x)","r3"),("log_b(x) Custom Base","r4")]),
"""<script>
function calc(){const x=+document.getElementById('f1').value,b=+document.getElementById('f2').value;if(x<=0)return alert('x must be positive');document.getElementById('r1').textContent=Math.log10(x).toFixed(6);document.getElementById('r2').textContent=Math.log(x).toFixed(6);document.getElementById('r3').textContent=(Math.log(x)/Math.log(2)).toFixed(6);document.getElementById('r4').textContent=(Math.log(x)/Math.log(b)).toFixed(6);document.getElementById('resultBox').classList.add('show');}
</script>""")

page("matrix-calculator.html","Matrix Calculator",
"Add, subtract, and multiply 2x2 and 3x3 matrices. Find determinant, inverse, and transpose of any matrix.",
"matrix calculator, matrix multiplication, matrix determinant, matrix inverse, 2x2 matrix, 3x3 matrix calculator",
"&#128290;","#0d47a1","#1565c0","math","&#128290;","Math",
"""<div class="calc-box">
<h2 class="calc-title">2x2 Matrix Calculator</h2>
<div class="d-flex gap-2 mb-3 flex-wrap">
<button class="cat-pill active" onclick="setOp('det',this)">Determinant</button>
<button class="cat-pill" onclick="setOp('inv',this)">Inverse</button>
<button class="cat-pill" onclick="setOp('trans',this)">Transpose</button>
<button class="cat-pill" onclick="setOp('mul',this)">Multiply A\xd7B</button>
</div>
<h6>Matrix A</h6>
<div class="row g-2 mb-3">
<div class="col-3"><input type="number" class="form-control" id="a11" value="1"></div>
<div class="col-3"><input type="number" class="form-control" id="a12" value="2"></div>
<div class="col-3"><input type="number" class="form-control" id="a21" value="3"></div>
<div class="col-3"><input type="number" class="form-control" id="a22" value="4"></div>
</div>
<div id="matBSection">
<h6>Matrix B</h6>
<div class="row g-2 mb-3">
<div class="col-3"><input type="number" class="form-control" id="b11" value="5"></div>
<div class="col-3"><input type="number" class="form-control" id="b12" value="6"></div>
<div class="col-3"><input type="number" class="form-control" id="b21" value="7"></div>
<div class="col-3"><input type="number" class="form-control" id="b22" value="8"></div>
</div></div>
<button class="btn-calculate" onclick="calc()"><i class="bi bi-grid me-2"></i>Calculate</button>
<div class="result-box" id="resultBox"><div id="matResult" style="text-align:center;font-size:1.1rem"></div></div></div>""",
"""<script>
let mop='det';
function setOp(op,b){mop=op;document.querySelectorAll('.cat-pill').forEach(p=>p.classList.remove('active'));b.classList.add('active');document.getElementById('matBSection').style.display=op==='mul'?'block':'none';}
function gv(id){return +document.getElementById(id).value;}
function matFmt(m){return `<table style="margin:auto;border-collapse:collapse">${m.map(row=>'<tr>'+row.map(v=>`<td style="padding:6px 12px;border:1px solid var(--border)">${isFinite(v)?v.toFixed(4):v}</td>`).join('')+'</tr>').join('')}</table>`;}
function calc(){const a=[[gv('a11'),gv('a12')],[gv('a21'),gv('a22')]];const det=a[0][0]*a[1][1]-a[0][1]*a[1][0];let res='';if(mop==='det'){res='<div class="result-value">det(A) = <strong>'+det.toFixed(4)+'</strong></div>';}else if(mop==='inv'){if(Math.abs(det)<1e-10)res='<div style="color:red">Matrix is singular (det=0), no inverse exists</div>';else{const inv=[[a[1][1]/det,-a[0][1]/det],[-a[1][0]/det,a[0][0]/det]];res='<h6>A\u207B\xb9 =</h6>'+matFmt(inv);}}else if(mop==='trans'){res='<h6>A\u1d40 =</h6>'+matFmt([[a[0][0],a[1][0]],[a[0][1],a[1][1]]]);}else{const b=[[gv('b11'),gv('b12')],[gv('b21'),gv('b22')]];const c=[[a[0][0]*b[0][0]+a[0][1]*b[1][0],a[0][0]*b[0][1]+a[0][1]*b[1][1]],[a[1][0]*b[0][0]+a[1][1]*b[1][0],a[1][0]*b[0][1]+a[1][1]*b[1][1]]];res='<h6>A \u00d7 B =</h6>'+matFmt(c);}document.getElementById('matResult').innerHTML=res;document.getElementById('resultBox').classList.add('show');}
</script>""")

# SCIENCE
page("ph-calculator.html","pH Calculator",
"Calculate pH from hydrogen ion concentration, or find [H+] from pH value. Classify acids, bases, and neutral solutions.",
"pH calculator, pH from concentration, hydrogen ion concentration, acid base calculator, buffer pH calculator",
"&#9878;","#1b5e20","#2e7d32","science","&#128301;","Science",
cb("pH Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Calculation Mode</label>
<select class="form-select" id="f0">
<option value="from_h">From [H+] concentration → pH</option>
<option value="from_ph">From pH → [H+] concentration</option>
</select></div>
<div class="col-md-6"><label class="form-label" id="f1Label">[H+] concentration (mol/L)</label>
<input type="number" class="form-control" id="f1" value="0.001" step="any"></div>
</div>""",
[("pH Value","r1"),("pOH Value","r2"),("[H+] (mol/L)","r3"),("Solution Type","r4")],
"Calculate pH"),
"""<script>
function calc(){const mode=document.getElementById('f0').value,v=+document.getElementById('f1').value;let ph,h;if(mode==='from_h'){h=v;ph=-Math.log10(h);}else{ph=v;h=Math.pow(10,-ph);}const poh=14-ph;const type=ph<7?'Acidic (pH < 7)':ph===7?'Neutral (pH = 7)':'Basic/Alkaline (pH > 7)';document.getElementById('r1').textContent=ph.toFixed(4);document.getElementById('r2').textContent=poh.toFixed(4);document.getElementById('r3').textContent=h.toExponential(4)+' mol/L';document.getElementById('r4').textContent=type;document.getElementById('resultBox').classList.add('show');}
</script>""")

page("acceleration-calculator.html","Acceleration Calculator",
"Calculate acceleration, initial velocity, final velocity, or time using kinematic equations. Newton's second law included.",
"acceleration calculator, calculate acceleration, velocity time calculator, kinematic equations, force mass acceleration",
"&#128165;","#b71c1c","#c62828","science","&#128301;","Science",
cb("Acceleration Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Initial Velocity (m/s)</label><input type="number" class="form-control" id="f1" value="0" step="any" placeholder="Leave blank to solve"></div>
<div class="col-md-6"><label class="form-label">Final Velocity (m/s)</label><input type="number" class="form-control" id="f2" value="30" step="any" placeholder="Leave blank to solve"></div>
<div class="col-md-6"><label class="form-label">Time (seconds)</label><input type="number" class="form-control" id="f3" value="10" step="any" placeholder="Leave blank to solve"></div>
<div class="col-md-6"><label class="form-label">Mass (kg) - for Force calc</label><input type="number" class="form-control" id="f4" value="1000" step="any"></div>
</div>""",
[("Acceleration (m/s\u00B2)","r1"),("Distance (m)","r2"),("Force (N)","r3"),("Acceleration (g-force)","r4")]),
"""<script>
function calc(){let u=parseFloat(document.getElementById('f1').value),v=parseFloat(document.getElementById('f2').value),t=parseFloat(document.getElementById('f3').value),m=+document.getElementById('f4').value||1;const has=x=>!isNaN(x);let a,s;if(has(u)&&has(v)&&has(t)){a=(v-u)/t;s=(u+v)/2*t;}else if(has(u)&&has(v)&&!has(t)){a=undefined;s=undefined;}else if(has(u)&&has(a=0)&&has(t)){v=u+a*t;s=u*t+0.5*a*t*t;}else{a=(v-u)/t;s=(u+v)/2*t;}if(a===undefined)a=(v-u)/t;if(s===undefined)s=(u+v)/2*t;document.getElementById('r1').textContent=a.toFixed(4)+' m/s\u00B2';document.getElementById('r2').textContent=Math.abs(s).toFixed(4)+' m';document.getElementById('r3').textContent=(m*a).toFixed(2)+' N';document.getElementById('r4').textContent=(a/9.81).toFixed(4)+' g';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("molarity-calculator.html","Molarity Calculator",
"Calculate molarity, moles, volume, and molecular weight of solutions. Dilution calculator included for lab work.",
"molarity calculator, molarity formula, calculate molarity, moles calculator, solution concentration calculator, dilution",
"&#128300;","#4a148c","#6a1b9a","science","&#128301;","Science",
cb("Molarity Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Moles of Solute (mol)</label><input type="number" class="form-control" id="f1" value="0.5" step="any" placeholder="Leave blank to solve"></div>
<div class="col-md-6"><label class="form-label">Volume of Solution (L)</label><input type="number" class="form-control" id="f2" value="1" step="any" placeholder="Leave blank to solve"></div>
<div class="col-md-6"><label class="form-label">Molarity (mol/L)</label><input type="number" class="form-control" id="f3" step="any" placeholder="Leave blank to solve"></div>
<div class="col-md-6"><label class="form-label">Molecular Weight (g/mol)</label><input type="number" class="form-control" id="f4" value="58.44" step="any"><small class="text-muted">NaCl = 58.44, HCl = 36.46, H\u2082O = 18.02</small></div>
</div>""",
[("Molarity (M)","r1"),("Moles","r2"),("Volume (L)","r3"),("Mass of Solute (g)","r4")]),
"""<script>
function calc(){let n=parseFloat(document.getElementById('f1').value),v=parseFloat(document.getElementById('f2').value),m=parseFloat(document.getElementById('f3').value),mw=+document.getElementById('f4').value;const has=x=>!isNaN(x);if(has(n)&&has(v))m=n/v;else if(has(m)&&has(v))n=m*v;else if(has(m)&&has(n))v=n/m;else return alert('Enter any 2 values');const mass=n*mw;document.getElementById('r1').textContent=m.toFixed(4)+' M';document.getElementById('r2').textContent=n.toFixed(4)+' mol';document.getElementById('r3').textContent=v.toFixed(4)+' L';document.getElementById('r4').textContent=mass.toFixed(4)+' g';document.getElementById('resultBox').classList.add('show');}
</script>""")

# CONSTRUCTION
page("concrete-volume-calculator.html","Concrete Volume Calculator",
"Calculate concrete volume for slabs, columns, beams, and footings. Get bags of concrete needed for any project.",
"concrete calculator, concrete volume calculator, how many bags of concrete, concrete slab calculator, cement calculator",
"&#127959;","#616161","#757575","construction","&#127959;","Construction",
"""<div class="calc-box">
<h2 class="calc-title">Concrete Volume Calculator</h2>
<div class="d-flex gap-2 mb-3 flex-wrap">
<button class="cat-pill active" onclick="setShape('slab',this)">Slab</button>
<button class="cat-pill" onclick="setShape('column',this)">Column</button>
<button class="cat-pill" onclick="setShape('footing',this)">Footing</button>
</div>
<div id="slabDiv">
<div class="row g-3">
<div class="col-md-4"><label class="form-label">Length (ft)</label><input type="number" class="form-control" id="sl" value="20" step="0.5"></div>
<div class="col-md-4"><label class="form-label">Width (ft)</label><input type="number" class="form-control" id="sw" value="10" step="0.5"></div>
<div class="col-md-4"><label class="form-label">Thickness (inches)</label><input type="number" class="form-control" id="st" value="4" step="0.5"></div>
</div>
</div>
<div id="columnDiv" style="display:none">
<div class="row g-3">
<div class="col-md-4"><label class="form-label">Diameter (inches)</label><input type="number" class="form-control" id="cd" value="12" step="1"></div>
<div class="col-md-4"><label class="form-label">Height (ft)</label><input type="number" class="form-control" id="ch" value="10" step="0.5"></div>
<div class="col-md-4"><label class="form-label">Quantity</label><input type="number" class="form-control" id="cq" value="4" step="1"></div>
</div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-calculator me-2"></i>Calculate Concrete</button>
<div class="result-box" id="resultBox">
<div class="row g-3 text-center">
<div class="col-6"><div class="result-label">Volume (cu yd)</div><div class="result-value" id="r1">-</div></div>
<div class="col-6"><div class="result-label">Volume (cu ft)</div><div class="result-value" id="r2">-</div></div>
<div class="col-6"><div class="result-label">60-lb Bags Needed</div><div class="result-value" id="r3">-</div></div>
<div class="col-6"><div class="result-label">80-lb Bags Needed</div><div class="result-value" id="r4">-</div></div>
</div></div></div>""",
"""<script>
let cshape='slab';
function setShape(s,b){cshape=s;document.querySelectorAll('.cat-pill').forEach(p=>p.classList.remove('active'));b.classList.add('active');document.getElementById('slabDiv').style.display=s==='slab'?'block':'none';document.getElementById('columnDiv').style.display=s==='column'?'block':'none';}
function calc(){let cf=0;if(cshape==='slab'){cf=+document.getElementById('sl').value * +document.getElementById('sw').value * +document.getElementById('st').value/12;}else if(cshape==='column'){const r=+document.getElementById('cd').value/24;cf=Math.PI*r*r* +document.getElementById('ch').value * +document.getElementById('cq').value;}const cy=cf/27;const bags60=Math.ceil(cy*27/0.45),bags80=Math.ceil(cy*27/0.60);document.getElementById('r1').textContent=cy.toFixed(3)+' cu yd';document.getElementById('r2').textContent=cf.toFixed(2)+' cu ft';document.getElementById('r3').textContent=bags60+' bags';document.getElementById('r4').textContent=bags80+' bags';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("brick-wall-calculator.html","Brick Wall Calculator",
"Calculate how many bricks you need for any wall. Includes mortar, coursing, and different brick sizes.",
"brick calculator, how many bricks, brick wall calculator, mortar calculator, standard brick size, brick count",
"&#127959;","#5d4037","#6d4c41","construction","&#127959;","Construction",
cb("Brick Wall Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Wall Length (ft)</label><input type="number" class="form-control" id="f1" value="20" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Wall Height (ft)</label><input type="number" class="form-control" id="f2" value="8" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Wall Thickness</label>
<select class="form-select" id="f3"><option value="0.375">Single Brick (3.75")</option><option value="0.75" selected>Double Brick (7.5")</option></select></div>
<div class="col-md-6"><label class="form-label">Mortar Joint (inches)</label><input type="number" class="form-control" id="f4" value="0.375" step="0.125"></div>
</div>""",
[("Bricks Needed","r1"),("With 10% Waste","r2"),("Wall Area (sq ft)","r3"),("Mortar Bags (60lb)","r4")],
"Calculate Bricks"),
"""<script>
function calc(){const l=+document.getElementById('f1').value,h=+document.getElementById('f2').value,thick=+document.getElementById('f3').value,mortar=+document.getElementById('f4').value;const area=l*h,brickH=(2.25+mortar)/12,brickL=(7.625+mortar)/12;const bricksPerSqFt=1/(brickH*brickL);const bricks=Math.ceil(area*bricksPerSqFt*(thick/0.375)),withWaste=Math.ceil(bricks*1.1);document.getElementById('r1').textContent=bricks.toLocaleString();document.getElementById('r2').textContent=withWaste.toLocaleString();document.getElementById('r3').textContent=area.toFixed(1)+' sq ft';document.getElementById('r4').textContent=Math.ceil(area*0.02)+' bags';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("fence-calculator.html","Fence Calculator",
"Calculate fencing materials needed for any yard or property. Posts, rails, pickets, and total cost estimate.",
"fence calculator, how much fencing do I need, picket fence calculator, privacy fence, fence cost calculator",
"&#127807;","#2e7d32","#388e3c","construction","&#127959;","Construction",
cb("Fence Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Total Fence Length (ft)</label><input type="number" class="form-control" id="f1" value="200" step="5"></div>
<div class="col-md-6"><label class="form-label">Fence Type</label>
<select class="form-select" id="f2">
<option value="6">6-ft Privacy (wood)</option>
<option value="4" selected>4-ft Picket</option>
<option value="8">Chain Link</option>
</select></div>
<div class="col-md-6"><label class="form-label">Post Spacing (ft)</label><input type="number" class="form-control" id="f3" value="8" step="1"></div>
<div class="col-md-6"><label class="form-label">Cost Per Linear Foot ($)</label><input type="number" class="form-control" id="f4" value="20" step="1"></div>
</div>""",
[("Total Posts Needed","r1"),("Fence Panels","r2"),("Total Linear Ft","r3"),("Estimated Cost","r4")],
"Calculate Fence"),
"""<script>
function calc(){const len=+document.getElementById('f1').value,h=+document.getElementById('f2').value,sp=+document.getElementById('f3').value,cost=+document.getElementById('f4').value;const posts=Math.ceil(len/sp)+1,panels=Math.ceil(len/sp);document.getElementById('r1').textContent=posts+' posts';document.getElementById('r2').textContent=panels+' panels';document.getElementById('r3').textContent=len+' ft';document.getElementById('r4').textContent='$'+(len*cost).toFixed(0);document.getElementById('resultBox').classList.add('show');}
</script>""")

page("stair-calculator.html","Stair Calculator",
"Calculate stair dimensions: rise, run, total stairs, stringer length, and angle for any staircase.",
"stair calculator, staircase calculator, rise and run calculator, number of stairs, stringer length, stair angle",
"&#127959;","#546e7a","#607d8b","construction","&#127959;","Construction",
cb("Stair Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Total Rise Height (inches)</label><input type="number" class="form-control" id="f1" value="120" step="1"></div>
<div class="col-md-6"><label class="form-label">Desired Rise Per Step (inches)</label><input type="number" class="form-control" id="f2" value="7.5" step="0.25"></div>
<div class="col-md-6"><label class="form-label">Tread Depth / Run (inches)</label><input type="number" class="form-control" id="f3" value="10" step="0.25"></div>
</div>""",
[("Number of Steps","r1"),("Actual Rise Per Step","r2"),("Total Run (ft)","r3"),("Stringer Length (ft)","r4")],
"Calculate Stairs"),
"""<script>
function calc(){const totalRise=+document.getElementById('f1').value,desRise=+document.getElementById('f2').value,tread=+document.getElementById('f3').value;const steps=Math.round(totalRise/desRise),actRise=totalRise/steps,totalRun=steps*tread,stringer=Math.sqrt(totalRise*totalRise+totalRun*totalRun);document.getElementById('r1').textContent=steps+' steps';document.getElementById('r2').textContent=actRise.toFixed(3)+'"';document.getElementById('r3').textContent=(totalRun/12).toFixed(2)+' ft';document.getElementById('r4').textContent=(stringer/12).toFixed(2)+' ft';document.getElementById('resultBox').classList.add('show');}
</script>""")

# EDUCATION
page("study-hours-calculator.html","Study Hours Calculator",
"Calculate how many hours you should study per week based on your courses and credit hours. Effective study planning.",
"study hours calculator, how many hours to study, study schedule calculator, credit hours study time, exam study planner",
"&#128218;","#1a237e","#283593","education","&#127979;","Education",
cb("Study Hours Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Number of Courses</label><input type="number" class="form-control" id="f1" value="5" min="1" max="15"></div>
<div class="col-md-6"><label class="form-label">Credit Hours Per Course (avg)</label><input type="number" class="form-control" id="f2" value="3" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Class Hours Per Week</label><input type="number" class="form-control" id="f3" value="15" step="1"></div>
<div class="col-md-6"><label class="form-label">Study Multiplier</label>
<select class="form-select" id="f4">
<option value="2">2x (Standard Rule)</option>
<option value="3" selected>3x (Recommended)</option>
<option value="4">4x (Intensive)</option>
</select></div>
</div>""",
[("Total Credit Hours","r1"),("Study Hours/Week","r2"),("Study Hours/Day","r3"),("Total Time Commitment","r4")],
"Calculate Study Plan"),
"""<script>
function calc(){const c=+document.getElementById('f1').value,cr=+document.getElementById('f2').value,cls=+document.getElementById('f3').value,mult=+document.getElementById('f4').value;const total=c*cr,study=total*mult,daily=study/7;document.getElementById('r1').textContent=total+' credits';document.getElementById('r2').textContent=study+' hrs/week';document.getElementById('r3').textContent=daily.toFixed(1)+' hrs/day';document.getElementById('r4').textContent=(cls+study).toFixed(0)+' hrs/week';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("reading-time-calculator.html","Reading Time Calculator",
"Calculate how long it will take to read any document or book based on word count and your reading speed.",
"reading time calculator, words per minute, how long to read, book reading time, reading speed calculator",
"&#128218;","#0d47a1","#1565c0","education","&#127979;","Education",
cb("Reading Time Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Word Count</label><input type="number" class="form-control" id="f1" value="5000" step="100"></div>
<div class="col-md-6"><label class="form-label">Reading Speed</label>
<select class="form-select" id="f2">
<option value="100">Slow (100 wpm)</option>
<option value="200" selected>Average (200 wpm)</option>
<option value="300">Fast (300 wpm)</option>
<option value="400">Speed Reader (400 wpm)</option>
<option value="600">Expert (600 wpm)</option>
</select></div>
</div>""",
[("Reading Time","r1"),("Pages (300 words/pg)","r2"),("Comprehension Time","r3"),("Audio Book Time","r4")],
"Calculate"),
"""<script>
function calc(){const wc=+document.getElementById('f1').value,wpm=+document.getElementById('f2').value;const mins=wc/wpm,pages=wc/300,comp=mins*1.3,audio=wc/130;function fmt(m){return m<60?Math.round(m)+' min':(Math.floor(m/60)+'h '+(Math.round(m%60))+'m');}document.getElementById('r1').textContent=fmt(mins);document.getElementById('r2').textContent=pages.toFixed(0)+' pages';document.getElementById('r3').textContent=fmt(comp);document.getElementById('r4').textContent=fmt(audio);document.getElementById('resultBox').classList.add('show');}
</script>""")

# TRAVEL
page("flight-time-calculator.html","Flight Time Calculator",
"Estimate flight time between any two cities based on distance and aircraft speed. With layover and timezone info.",
"flight time calculator, how long is the flight, flight duration calculator, travel time calculator, air distance",
"&#9992;","#0d47a1","#1565c0","travel","&#9992;","Travel",
cb("Flight Time Estimator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Distance (km)</label><input type="number" class="form-control" id="f1" value="5000" step="100"></div>
<div class="col-md-6"><label class="form-label">Aircraft Type</label>
<select class="form-select" id="f2">
<option value="880">Commercial Jet (880 km/h)</option>
<option value="950" selected>Modern Aircraft (950 km/h)</option>
<option value="1100">Fast Jet (1100 km/h)</option>
<option value="1200">Concorde-class (1200 km/h)</option>
</select></div>
<div class="col-md-6"><label class="form-label">Boarding + Delays (minutes)</label><input type="number" class="form-control" id="f3" value="60" step="15"></div>
<div class="col-md-6"><label class="form-label">Layover Time (hours)</label><input type="number" class="form-control" id="f4" value="0" step="0.5"></div>
</div>""",
[("Flight Time (Air)","r1"),("Total Travel Time","r2"),("Distance (miles)","r3"),("Time Zones Crossed (est.)","r4")],
"Estimate Flight Time"),
"""<script>
function fmt(h){return Math.floor(h)+'h '+Math.round((h%1)*60)+'m';}
function calc(){const d=+document.getElementById('f1').value,spd=+document.getElementById('f2').value,delay=+document.getElementById('f3').value/60,lay=+document.getElementById('f4').value;const air=d/spd,total=air+delay+lay;document.getElementById('r1').textContent=fmt(air);document.getElementById('r2').textContent=fmt(total);document.getElementById('r3').textContent=(d*0.621371).toFixed(0)+' miles';document.getElementById('r4').textContent=Math.round(d/1600)+' zones (est.)';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("mileage-reimbursement-calculator.html","Mileage Reimbursement Calculator",
"Calculate mileage reimbursement for work travel. Uses IRS standard rates. Track business miles and total compensation.",
"mileage reimbursement calculator, IRS mileage rate, business mileage calculator, travel reimbursement, work miles",
"&#128664;","#1b5e20","#2e7d32","travel","&#9992;","Travel",
cb("Mileage Reimbursement Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Total Miles Driven</label><input type="number" class="form-control" id="f1" value="500" step="1"></div>
<div class="col-md-6"><label class="form-label">Reimbursement Rate ($/mile)</label><input type="number" class="form-control" id="f2" value="0.67" step="0.01"><small class="text-muted">IRS 2024: $0.67/mile</small></div>
<div class="col-md-6"><label class="form-label">Fuel Economy (mpg)</label><input type="number" class="form-control" id="f3" value="30" step="1"></div>
<div class="col-md-6"><label class="form-label">Fuel Price ($/gallon)</label><input type="number" class="form-control" id="f4" value="3.50" step="0.01"></div>
</div>""",
[("Reimbursement Amount","r1"),("Actual Fuel Cost","r2"),("Net Profit","r3"),("Gallons Used","r4")]),
"""<script>
function calc(){const mi=+document.getElementById('f1').value,rate=+document.getElementById('f2').value,mpg=+document.getElementById('f3').value,price=+document.getElementById('f4').value;const reimb=mi*rate,fuel=mi/mpg*price,profit=reimb-fuel;document.getElementById('r1').textContent='$'+reimb.toFixed(2);document.getElementById('r2').textContent='$'+fuel.toFixed(2);document.getElementById('r3').textContent='$'+profit.toFixed(2);document.getElementById('r4').textContent=(mi/mpg).toFixed(1)+' gal';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("travel-budget-calculator.html","Travel Budget Calculator",
"Plan your travel budget for any trip. Calculate costs for flights, hotels, food, activities, and shopping.",
"travel budget calculator, trip budget calculator, vacation cost calculator, holiday budget planner, travel expenses",
"&#9992;","#880e4f","#ad1457","travel","&#9992;","Travel",
cb("Travel Budget Planner",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Number of Travelers</label><input type="number" class="form-control" id="f0" value="2" min="1"></div>
<div class="col-md-6"><label class="form-label">Trip Duration (days)</label><input type="number" class="form-control" id="f1" value="7" min="1"></div>
<div class="col-md-6"><label class="form-label">Flights Per Person ($)</label><input type="number" class="form-control" id="f2" value="500" step="50"></div>
<div class="col-md-6"><label class="form-label">Hotel Per Night ($)</label><input type="number" class="form-control" id="f3" value="120" step="10"></div>
<div class="col-md-6"><label class="form-label">Food Per Day Per Person ($)</label><input type="number" class="form-control" id="f4" value="60" step="10"></div>
<div class="col-md-6"><label class="form-label">Activities Per Day ($)</label><input type="number" class="form-control" id="f5" value="50" step="10"></div>
<div class="col-md-6"><label class="form-label">Transport Per Day ($)</label><input type="number" class="form-control" id="f6" value="30" step="10"></div>
<div class="col-md-6"><label class="form-label">Shopping / Misc ($)</label><input type="number" class="form-control" id="f7" value="200" step="50"></div>
</div>""",
[("Total Budget","r1"),("Per Person","r2"),("Per Day (Total)","r3"),("Per Day Per Person","r4")],
"Calculate Budget"),
"""<script>
function calc(){const n=+document.getElementById('f0').value,days=+document.getElementById('f1').value,fly=+document.getElementById('f2').value,hotel=+document.getElementById('f3').value,food=+document.getElementById('f4').value,act=+document.getElementById('f5').value,trans=+document.getElementById('f6').value,shop=+document.getElementById('f7').value;const total=fly*n+hotel*days+food*n*days+act*days+trans*days+shop;document.getElementById('r1').textContent='$'+total.toFixed(0);document.getElementById('r2').textContent='$'+(total/n).toFixed(0);document.getElementById('r3').textContent='$'+(total/days).toFixed(0);document.getElementById('r4').textContent='$'+(total/days/n).toFixed(0);document.getElementById('resultBox').classList.add('show');}
</script>""")

# ENVIRONMENT
page("carbon-footprint-calculator.html","Carbon Footprint Calculator",
"Calculate your personal carbon footprint from home energy, transport, diet, and consumption. Offset recommendations included.",
"carbon footprint calculator, CO2 calculator, personal carbon calculator, greenhouse gas calculator, climate change",
"&#127807;","#1b5e20","#2e7d32","environment","&#127807;","Environment",
cb("Carbon Footprint Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Car Miles Per Year</label><input type="number" class="form-control" id="f1" value="12000" step="500"></div>
<div class="col-md-6"><label class="form-label">Car Fuel Economy (mpg)</label><input type="number" class="form-control" id="f2" value="28" step="1"></div>
<div class="col-md-6"><label class="form-label">Short Haul Flights/Year</label><input type="number" class="form-control" id="f3" value="2" min="0"></div>
<div class="col-md-6"><label class="form-label">Long Haul Flights/Year</label><input type="number" class="form-control" id="f4" value="1" min="0"></div>
<div class="col-md-6"><label class="form-label">Monthly Electric Bill ($)</label><input type="number" class="form-control" id="f5" value="100" step="10"></div>
<div class="col-md-6"><label class="form-label">Diet Type</label>
<select class="form-select" id="f6">
<option value="0.5">Vegan</option>
<option value="1.0">Vegetarian</option>
<option value="1.8" selected>Average Omnivore</option>
<option value="2.5">Heavy Meat Eater</option>
</select></div>
</div>""",
[("Annual CO\u2082 (tons)","r1"),("vs. World Average","r2"),("Trees to Offset","r3"),("Carbon Cost ($20/ton)","r4")],
"Calculate Footprint"),
"""<script>
function calc(){const miles=+document.getElementById('f1').value,mpg=+document.getElementById('f2').value,sh=+document.getElementById('f3').value,lh=+document.getElementById('f4').value,elec=+document.getElementById('f5').value,diet=+document.getElementById('f6').value;const car=miles/mpg*8.89/1000,fly=sh*0.5+lh*2.0,energy=elec*12*0.0005,food=diet;const total=car+fly+energy+food;const world=4.7,trees=total*45;document.getElementById('r1').textContent=total.toFixed(2)+' tons CO\u2082';document.getElementById('r2').textContent=total>world?'+'+(total-world).toFixed(1)+'t above avg':'Under world avg';document.getElementById('r3').textContent=Math.round(trees)+' trees/year';document.getElementById('r4').textContent='$'+(total*20).toFixed(0)+'/year';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("solar-savings-calculator.html","Solar Panel Savings Calculator",
"Calculate solar panel system savings, payback period, and ROI. Find out how much you can save with solar energy.",
"solar savings calculator, solar panel ROI, solar payback period, solar energy savings, how much solar panels save",
"&#9728;","#f57f17","#f9a825","environment","&#127807;","Environment",
cb("Solar Panel Savings Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Monthly Electric Bill ($)</label><input type="number" class="form-control" id="f1" value="150" step="10"></div>
<div class="col-md-6"><label class="form-label">System Size (kW)</label><input type="number" class="form-control" id="f2" value="6" step="0.5"></div>
<div class="col-md-6"><label class="form-label">System Cost ($)</label><input type="number" class="form-control" id="f3" value="18000" step="500"></div>
<div class="col-md-6"><label class="form-label">Peak Sun Hours/Day</label><input type="number" class="form-control" id="f4" value="5" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Electricity Rate ($/kWh)</label><input type="number" class="form-control" id="f5" value="0.13" step="0.01"></div>
<div class="col-md-6"><label class="form-label">Federal Tax Credit (%)</label><input type="number" class="form-control" id="f6" value="30" step="1"></div>
</div>""",
[("Annual Production (kWh)","r1"),("Annual Savings","r2"),("Payback Period","r3"),("25-Year Savings","r4")],
"Calculate Solar ROI"),
"""<script>
function calc(){const bill=+document.getElementById('f1').value,kw=+document.getElementById('f2').value,cost=+document.getElementById('f3').value,sun=+document.getElementById('f4').value,rate=+document.getElementById('f5').value,credit=+document.getElementById('f6').value/100;const annual=kw*sun*365*0.8,savings=annual*rate,netCost=cost*(1-credit),payback=netCost/savings,life25=savings*25-cost*(1-credit);document.getElementById('r1').textContent=annual.toFixed(0)+' kWh';document.getElementById('r2').textContent='$'+savings.toFixed(0)+'/yr';document.getElementById('r3').textContent=payback.toFixed(1)+' years';document.getElementById('r4').textContent='$'+life25.toFixed(0);document.getElementById('resultBox').classList.add('show');}
</script>""")

page("water-footprint-calculator.html","Water Footprint Calculator",
"Calculate your daily and annual water footprint from food, clothing, and consumption habits. Save water tips.",
"water footprint calculator, water consumption calculator, virtual water, water usage calculator, daily water use",
"&#128167;","#006064","#00838f","environment","&#127807;","Environment",
cb("Water Footprint Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Shower Duration (min/day)</label><input type="number" class="form-control" id="f1" value="8" step="1"></div>
<div class="col-md-6"><label class="form-label">Baths Per Week</label><input type="number" class="form-control" id="f2" value="1" step="1"></div>
<div class="col-md-6"><label class="form-label">Flush Toilets Per Day</label><input type="number" class="form-control" id="f3" value="6" step="1"></div>
<div class="col-md-6"><label class="form-label">Laundry Loads Per Week</label><input type="number" class="form-control" id="f4" value="4" step="1"></div>
<div class="col-md-6"><label class="form-label">Diet Type</label>
<select class="form-select" id="f5">
<option value="500">Vegan (500 L/day)</option>
<option value="1000">Vegetarian (1000 L/day)</option>
<option value="2000" selected>Mixed Diet (2000 L/day)</option>
<option value="3000">Heavy Meat (3000 L/day)</option>
</select></div>
</div>""",
[("Daily Water Use (L)","r1"),("Annual Use (m\u00B3)","r2"),("vs. Global Average","r3"),("Water Cost (est.)","r4")],
"Calculate Water Footprint"),
"""<script>
function calc(){const sh=+document.getElementById('f1').value,bath=+document.getElementById('f2').value,flush=+document.getElementById('f3').value,laundry=+document.getElementById('f4').value,diet=+document.getElementById('f5').value;const daily=sh*65+bath*150/7+flush*6+laundry*50/7+diet;const annual=daily*365/1000;document.getElementById('r1').textContent=daily.toFixed(0)+' L/day';document.getElementById('r2').textContent=annual.toFixed(1)+' m\u00B3/yr';document.getElementById('r3').textContent=daily>137?'Above':(daily<137?'Below':'Equal to')+' 137L avg';document.getElementById('r4').textContent='$'+(annual*0.5).toFixed(0)+'/year';document.getElementById('resultBox').classList.add('show');}
</script>""")

# LIFESTYLE / FUN
page("age-on-planet-calculator.html","Age on Other Planets Calculator",
"Find out how old you would be on Mars, Jupiter, Venus, and other planets. Calculate your age in alien years.",
"age on other planets, how old on Mars, age on Mars calculator, planet age calculator, space age calculator",
"&#127756;","#4a148c","#6a1b9a","lifestyle","&#127774;","Lifestyle",
"""<div class="calc-box">
<h2 class="calc-title">Age on Other Planets</h2>
<div class="row g-3">
<div class="col-md-6"><label class="form-label">Date of Birth</label><input type="date" class="form-control" id="f1"></div>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-globe me-2"></i>Calculate Planet Age</button>
<div class="result-box" id="resultBox">
<div id="planetResults" style="font-size:0.9rem"></div>
</div></div>""",
"""<script>
document.getElementById('f1').valueAsDate=new Date('1990-01-01');
const planets=[['Mercury',0.241,'&#9791;'],['Venus',0.615,'&#9792;'],['Earth',1,'&#127758;'],['Mars',1.881,'&#127775;'],['Jupiter',11.86,'&#10027;'],['Saturn',29.46,'&#127774;'],['Uranus',84.01,'&#128161;'],['Neptune',164.8,'&#128168;']];
function calc(){const dob=new Date(document.getElementById('f1').value);const earthAge=(Date.now()-dob)/(365.25*24*3600*1000);const rows=planets.map(([name,period,icon])=>{const age=earthAge/period;return `<div style="display:flex;justify-content:space-between;align-items:center;padding:8px 12px;margin-bottom:6px;border-radius:8px;background:var(--card-bg);border:1px solid var(--border)"><span>${icon} <strong>${name}</strong></span><span>${age.toFixed(2)} years<br><small style="color:var(--text-secondary)">${(age*period*365.25).toFixed(0)} Earth days</small></span></div>`;}).join('');document.getElementById('planetResults').innerHTML=rows;document.getElementById('resultBox').classList.add('show');}
</script>""")

page("life-expectancy-calculator.html","Life Expectancy Calculator",
"Estimate your life expectancy based on lifestyle, health factors, and demographics. Tips to live longer included.",
"life expectancy calculator, how long will I live, lifespan calculator, longevity calculator, health age calculator",
"&#127774;","#1b5e20","#2e7d32","lifestyle","&#127774;","Lifestyle",
cb("Life Expectancy Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Current Age</label><input type="number" class="form-control" id="f1" value="30" min="1" max="100"></div>
<div class="col-md-6"><label class="form-label">Gender</label><select class="form-select" id="f2"><option value="75">Male (avg 75 yrs)</option><option value="80">Female (avg 80 yrs)</option></select></div>
<div class="col-md-6"><label class="form-label">Smoking</label><select class="form-select" id="f3"><option value="0">Never Smoked</option><option value="-5">Former Smoker</option><option value="-10">Current Smoker</option></select></div>
<div class="col-md-6"><label class="form-label">Exercise</label><select class="form-select" id="f4"><option value="-3">None</option><option value="0" selected>Occasionally</option><option value="3">Regular (3-4x/week)</option><option value="5">Daily Athlete</option></select></div>
<div class="col-md-6"><label class="form-label">BMI Category</label><select class="form-select" id="f5"><option value="-3">Obese</option><option value="-1">Overweight</option><option value="2" selected>Normal Weight</option><option value="1">Slightly Underweight</option></select></div>
<div class="col-md-6"><label class="form-label">Diet Quality</label><select class="form-select" id="f6"><option value="-2">Poor</option><option value="0" selected>Average</option><option value="2">Healthy</option><option value="4">Excellent</option></select></div>
</div>""",
[("Estimated Lifespan","r1"),("Years Remaining","r2"),("Life Lived (%)","r3"),("Health Age","r4")],
"Estimate Lifespan"),
"""<script>
function calc(){const age=+document.getElementById('f1').value,base=+document.getElementById('f2').value,smoke=+document.getElementById('f3').value,ex=+document.getElementById('f4').value,bmi=+document.getElementById('f5').value,diet=+document.getElementById('f6').value;const life=base+smoke+ex+bmi+diet;const rem=Math.max(0,life-age);document.getElementById('r1').textContent=Math.round(life)+' years';document.getElementById('r2').textContent=Math.round(rem)+' years';document.getElementById('r3').textContent=(age/life*100).toFixed(1)+'%';document.getElementById('r4').textContent=Math.round(age-smoke-ex-bmi-diet)+' years';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("name-value-calculator.html","Name Value Calculator",
"Calculate the numerical value of your name using A=1, Z=26 alphabet coding. Fun name numerology tool.",
"name value calculator, name number calculator, alphabet value calculator, word value calculator, name to number",
"&#128290;","#880e4f","#ad1457","lifestyle","&#127774;","Lifestyle",
"""<div class="calc-box">
<h2 class="calc-title">Name Value Calculator</h2>
<div class="mb-3"><label class="form-label">Enter Name or Any Text</label>
<input type="text" class="form-control" id="f1" value="SuperCalc" placeholder="Enter any name or word"></div>
<button class="btn-calculate" onclick="calc()"><i class="bi bi-123 me-2"></i>Calculate Value</button>
<div class="result-box" id="resultBox">
<div class="row g-3 text-center">
<div class="col-6"><div class="result-label">Letter Sum (A=1)</div><div class="result-value" id="r1">-</div></div>
<div class="col-6"><div class="result-label">Reduced to Single Digit</div><div class="result-value" id="r2">-</div></div>
<div class="col-6"><div class="result-label">Letter Count</div><div class="result-value" id="r3">-</div></div>
<div class="col-6"><div class="result-label">Vowel Sum</div><div class="result-value" id="r4">-</div></div>
</div>
<div id="breakdown" style="margin-top:12px;font-size:0.85rem;text-align:center;word-break:break-all"></div>
</div></div>""",
"""<script>
function reduce(n){while(n>9&&n!==11&&n!==22&&n!==33){n=String(n).split('').reduce((a,b)=>a+ +b,0);}return n;}
function calc(){const t=document.getElementById('f1').value.toUpperCase().replace(/[^A-Z]/g,'');const vals=t.split('').map(c=>c.charCodeAt(0)-64);const sum=vals.reduce((a,b)=>a+b,0);const vowels='AEIOU';const vsum=t.split('').filter(c=>vowels.includes(c)).map(c=>c.charCodeAt(0)-64).reduce((a,b)=>a+b,0);document.getElementById('r1').textContent=sum;document.getElementById('r2').textContent=reduce(sum);document.getElementById('r3').textContent=t.length;document.getElementById('r4').textContent=vsum;document.getElementById('breakdown').innerHTML=t.split('').map((c,i)=>`<span title="${c}=${vals[i]}" style="display:inline-block;padding:2px 6px;margin:2px;background:var(--card-bg);border:1px solid var(--border);border-radius:4px">${c}<sup>${vals[i]}</sup></span>`).join('');document.getElementById('resultBox').classList.add('show');}
</script>""")

# TECH
page("bandwidth-calculator.html","Bandwidth Calculator",
"Calculate required bandwidth for streaming, video calls, downloads, and multiple users on your network.",
"bandwidth calculator, internet speed required, streaming bandwidth, video call bandwidth, network bandwidth calculator",
"&#128205;","#0d47a1","#1565c0","tech","&#128187;","Tech & Dev",
cb("Bandwidth Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">4K Streaming Devices</label><input type="number" class="form-control" id="f1" value="1" min="0"></div>
<div class="col-md-6"><label class="form-label">HD Streaming Devices</label><input type="number" class="form-control" id="f2" value="2" min="0"></div>
<div class="col-md-6"><label class="form-label">Video Calls (simultaneous)</label><input type="number" class="form-control" id="f3" value="1" min="0"></div>
<div class="col-md-6"><label class="form-label">Online Gaming Devices</label><input type="number" class="form-control" id="f4" value="1" min="0"></div>
<div class="col-md-6"><label class="form-label">Smart Home / IoT Devices</label><input type="number" class="form-control" id="f5" value="5" min="0"></div>
<div class="col-md-6"><label class="form-label">General Browsing Users</label><input type="number" class="form-control" id="f6" value="3" min="0"></div>
</div>""",
[("Min. Required Mbps","r1"),("Recommended Mbps","r2"),("Devices Count","r3"),("Plan Suggestion","r4")],
"Calculate Bandwidth"),
"""<script>
function calc(){const s4k=+document.getElementById('f1').value*25,hd=+document.getElementById('f2').value*5,vc=+document.getElementById('f3').value*3,game=+document.getElementById('f4').value*3,iot=+document.getElementById('f5').value*0.5,browse=+document.getElementById('f6').value*5;const min=s4k+hd+vc+game+iot+browse,rec=min*1.5;const total=+document.getElementById('f1').value+ +document.getElementById('f2').value+ +document.getElementById('f3').value+ +document.getElementById('f4').value+ +document.getElementById('f5').value+ +document.getElementById('f6').value;const plan=rec<25?'25 Mbps':rec<50?'50 Mbps':rec<100?'100 Mbps':rec<200?'200 Mbps':rec<500?'500 Mbps':'1 Gbps+';document.getElementById('r1').textContent=min.toFixed(0)+' Mbps';document.getElementById('r2').textContent=rec.toFixed(0)+' Mbps';document.getElementById('r3').textContent=total+' devices';document.getElementById('r4').textContent=plan;document.getElementById('resultBox').classList.add('show');}
</script>""")

page("pixel-density-calculator.html","Pixel Density (PPI) Calculator",
"Calculate pixels per inch (PPI) and dots per inch (DPI) for any screen. Compare display sharpness across devices.",
"PPI calculator, pixels per inch, DPI calculator, screen pixel density, display sharpness, retina display calculator",
"&#128250;","#4a148c","#6a1b9a","tech","&#128187;","Tech & Dev",
cb("Pixel Density Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Horizontal Pixels</label><input type="number" class="form-control" id="f1" value="1920" step="1"></div>
<div class="col-md-6"><label class="form-label">Vertical Pixels</label><input type="number" class="form-control" id="f2" value="1080" step="1"></div>
<div class="col-md-6"><label class="form-label">Screen Size (inches diagonal)</label><input type="number" class="form-control" id="f3" value="15.6" step="0.1"></div>
</div>""",
[("PPI (Pixels/Inch)","r1"),("Total Pixels","r2"),("Display Type","r3"),("Viewing Distance","r4")]),
"""<script>
function calc(){const w=+document.getElementById('f1').value,h=+document.getElementById('f2').value,s=+document.getElementById('f3').value;const diag=Math.sqrt(w*w+h*h),ppi=diag/s;let type,dist;if(ppi<100)type='Low Res';else if(ppi<150)type='Standard HD';else if(ppi<220)type='Full HD';else if(ppi<300)type='High DPI';else type='Retina/UHD';dist=Math.round(2540/ppi*1.5);document.getElementById('r1').textContent=ppi.toFixed(1)+' PPI';document.getElementById('r2').textContent=(w*h/1e6).toFixed(2)+' Megapixels';document.getElementById('r3').textContent=type;document.getElementById('r4').textContent=dist+'cm (min)';document.getElementById('resultBox').classList.add('show');}
</script>""")

# FOOD / NUTRITION
page("calorie-deficit-calculator.html","Calorie Deficit Calculator",
"Calculate your calorie deficit for weight loss. Find out how many calories to cut per day to reach your goal weight.",
"calorie deficit calculator, weight loss calorie calculator, how many calories to lose weight, calorie cut calculator",
"&#128293;","#b71c1c","#c62828","health","&#10084;","Health",
cb("Calorie Deficit Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Current Weight (kg)</label><input type="number" class="form-control" id="f1" value="85" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Goal Weight (kg)</label><input type="number" class="form-control" id="f2" value="75" step="0.5"></div>
<div class="col-md-6"><label class="form-label">Weekly Loss Goal</label>
<select class="form-select" id="f3">
<option value="0.25">0.25 kg/week (Slow)</option>
<option value="0.5" selected>0.5 kg/week (Moderate)</option>
<option value="0.75">0.75 kg/week (Fast)</option>
<option value="1.0">1.0 kg/week (Aggressive)</option>
</select></div>
<div class="col-md-6"><label class="form-label">TDEE (calories/day)</label><input type="number" class="form-control" id="f4" value="2500" step="50"></div>
</div>""",
[("Daily Calorie Target","r1"),("Daily Deficit","r2"),("Weeks to Goal","r3"),("Total Deficit","r4")],
"Calculate Deficit"),
"""<script>
function calc(){const cw=+document.getElementById('f1').value,gw=+document.getElementById('f2').value,wloss=+document.getElementById('f3').value,tdee=+document.getElementById('f4').value;const deficit=wloss*7700/7,target=tdee-deficit,diff=cw-gw,weeks=diff/wloss;document.getElementById('r1').textContent=Math.round(target)+' kcal/day';document.getElementById('r2').textContent=Math.round(deficit)+' kcal/day';document.getElementById('r3').textContent=weeks.toFixed(0)+' weeks';document.getElementById('r4').textContent=(diff*7700).toFixed(0)+' kcal total';document.getElementById('resultBox').classList.add('show');}
</script>""")

page("recipe-scaling-calculator.html","Recipe Scaling Calculator",
"Scale any recipe up or down instantly. Convert servings and ingredient quantities for any number of people.",
"recipe scaling calculator, scale recipe, convert recipe servings, adjust recipe portions, cooking quantity calculator",
"&#127859;","#e65100","#f57c00","lifestyle","&#127774;","Lifestyle",
"""<div class="calc-box">
<h2 class="calc-title">Recipe Scaling Calculator</h2>
<div class="row g-3">
<div class="col-md-6"><label class="form-label">Original Servings</label><input type="number" class="form-control" id="origServ" value="4" min="1"></div>
<div class="col-md-6"><label class="form-label">Desired Servings</label><input type="number" class="form-control" id="newServ" value="10" min="1"></div>
</div>
<div class="mt-3" id="ingredients">
<label class="form-label">Ingredients (one per line: quantity unit name)</label>
<textarea class="form-control" id="ingList" rows="6" placeholder="2 cups flour\n1.5 tsp salt\n3 eggs\n0.5 cup butter">2 cups flour
1.5 tsp salt
3 eggs
0.5 cup butter
1 tbsp vanilla extract</textarea>
</div>
<button class="btn-calculate mt-4" onclick="calc()"><i class="bi bi-egg me-2"></i>Scale Recipe</button>
<div class="result-box" id="resultBox">
<div id="scaledResults" style="font-size:0.95rem"></div>
</div></div>""",
"""<script>
function calc(){const orig=+document.getElementById('origServ').value,newS=+document.getElementById('newServ').value,factor=newS/orig;const lines=document.getElementById('ingList').value.split('\n').filter(l=>l.trim());const rows=lines.map(l=>{const m=l.match(/^([\d.\/]+)\s*(.+)/);if(!m)return `<div style="padding:6px 0;border-bottom:1px solid var(--border)">${l}</div>`;const qty=eval(m[1]),rest=m[2],scaled=qty*factor;return `<div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid var(--border)"><span>${rest}</span><strong>${Number.isInteger(scaled)?scaled:scaled.toFixed(2)}</strong></div>`;}).join('');document.getElementById('scaledResults').innerHTML=`<div style="font-weight:600;margin-bottom:8px">Scaled for ${newS} servings (${factor.toFixed(2)}x):</div>`+rows;document.getElementById('resultBox').classList.add('show');}
</script>""")

page("food-cost-calculator.html","Food Cost Calculator",
"Calculate food cost percentage and profit margin for restaurants and catering. Recipe cost and menu price calculator.",
"food cost calculator, recipe cost calculator, restaurant food cost, food cost percentage, menu price calculator",
"&#127869;","#880e4f","#ad1457","business","&#128188;","Business",
cb("Food Cost Calculator",
"""<div class="row g-3">
<div class="col-md-6"><label class="form-label">Ingredient Cost ($)</label><input type="number" class="form-control" id="f1" value="3.50" step="0.01"></div>
<div class="col-md-6"><label class="form-label">Menu Price ($)</label><input type="number" class="form-control" id="f2" value="15.00" step="0.01"></div>
<div class="col-md-6"><label class="form-label">Target Food Cost %</label><input type="number" class="form-control" id="f3" value="30" step="1"></div>
<div class="col-md-6"><label class="form-label">Number of Servings Sold/Day</label><input type="number" class="form-control" id="f4" value="50" step="5"></div>
</div>""",
[("Food Cost %","r1"),("Gross Profit","r2"),("Suggested Price","r3"),("Daily Profit","r4")],
"Calculate Food Cost"),
"""<script>
function calc(){const cost=+document.getElementById('f1').value,price=+document.getElementById('f2').value,target=+document.getElementById('f3').value/100,qty=+document.getElementById('f4').value;const fc=cost/price*100,profit=price-cost,suggested=cost/target;document.getElementById('r1').textContent=fc.toFixed(1)+'%';document.getElementById('r2').textContent='$'+profit.toFixed(2)+' ('+((profit/price)*100).toFixed(1)+'%)';document.getElementById('r3').textContent='$'+suggested.toFixed(2);document.getElementById('r4').textContent='$'+(profit*qty).toFixed(0);document.getElementById('resultBox').classList.add('show');}
</script>""")

print("\n=== Batch 3 complete! ===")
