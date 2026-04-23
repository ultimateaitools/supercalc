# Build multiple calculator pages from template data
param([string]$batch = "all")

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)

function Write-Calc($filename, $title, $desc, $keywords, $icon, $gradient, $category, $catUrl, $catLabel, $bodyHtml, $scriptHtml) {
    $path = "d:\Datomate AI Lab\CalcWebsite\$filename"
    $html = @"
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>$title | SuperCalc</title>
  <meta name="description" content="$desc">
  <meta name="keywords" content="$keywords">
  <link rel="canonical" href="https://supercalc.online/$filename">
  <meta property="og:title" content="$title | SuperCalc"><meta property="og:description" content="$desc"><meta property="og:type" content="website">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
  <link rel="stylesheet" href="css/style.css">
  <script type="application/ld+json">{"@context":"https://schema.org","@type":"WebApplication","name":"$title","url":"https://supercalc.online/$filename","applicationCategory":"UtilitiesApplication","offers":{"@type":"Offer","price":"0"}}</script>
</head>
<body>
<nav class="navbar navbar-expand-lg"><div class="container"><a class="navbar-brand" href="index.html">&#9889; Super<span>Calc</span></a><button class="navbar-toggler border-0" type="button" data-bs-toggle="collapse" data-bs-target="#nav"><span></span></button><div class="collapse navbar-collapse" id="nav"><ul class="navbar-nav me-auto ms-3"><li><a class="nav-link" href="index.html#$catUrl">$catLabel</a></li></ul><div class="d-flex gap-2"><button class="theme-toggle" id="themeToggle"><i class="bi bi-moon-fill" id="themeIcon"></i></button></div></div></div></nav>
<div class="calc-page-header" style="background:linear-gradient(135deg,$gradient)">
  <div class="container"><nav class="breadcrumb-nav"><a href="index.html">Home</a> <i class="bi bi-chevron-right"></i><span>$title</span></nav>
  <h1 class="calc-page-title">$icon $title</h1>
  <p class="calc-page-subtitle">$desc</p></div>
</div>
<div class="container my-4">
  <div class="row g-4">
    <div class="col-lg-8">$bodyHtml</div>
    <div class="col-lg-4"><div class="sidebar-ad"><span style="font-size:0.7rem;color:var(--text-muted)">Advertisement [ 300x250 ]</span></div></div>
  </div>
</div>
<footer><div class="container"><div class="footer-bottom"><p>&copy; 2025 SuperCalc.online &mdash; Free Online Calculators</p><div><a href="privacy.html">Privacy</a> &bull; <a href="terms.html">Terms</a> &bull; <a href="about.html">About</a></div></div></div></footer>
<button class="back-to-top" id="backToTop"><i class="bi bi-arrow-up"></i></button>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
<script src="js/main.js"></script>
$scriptHtml
</body>
</html>
"@
    [System.IO.File]::WriteAllText($path, $html, $utf8NoBom)
    Write-Host "Created: $filename"
}

# ===================== BATCH 2 =====================

# 1. Debt Payoff Calculator
Write-Calc "debt-payoff-calculator.html" "Debt Payoff Calculator" "Calculate how long it will take to pay off your debt and total interest paid using avalanche or snowball method." "debt payoff calculator, debt snowball, debt avalanche, pay off debt, credit card payoff" "💳" "#1a237e,#283593" "finance" "finance" "💰 Finance" @'
<div class="calc-box">
  <h2 class="calc-title">Debt Payoff Calculator</h2>
  <div class="row g-3">
    <div class="col-md-6"><label class="form-label">Total Debt Amount ($)</label><input type="number" class="form-control" id="debtAmt" value="10000" step="100"></div>
    <div class="col-md-6"><label class="form-label">Annual Interest Rate (%)</label><input type="number" class="form-control" id="debtRate" value="18" step="0.1"></div>
    <div class="col-md-6"><label class="form-label">Monthly Payment ($)</label><input type="number" class="form-control" id="debtPay" value="300" step="10"></div>
    <div class="col-md-6"><label class="form-label">Extra Monthly Payment ($)</label><input type="number" class="form-control" id="debtExtra" value="0" step="10"></div>
  </div>
  <button class="btn-calculate mt-4" onclick="calcDebt()"><i class="bi bi-calculator me-2"></i>Calculate Payoff</button>
  <div class="result-box" id="resultBox">
    <div class="row g-3 text-center">
      <div class="col-6"><div class="result-label">Months to Pay Off</div><div class="result-value" id="debtMonths">-</div></div>
      <div class="col-6"><div class="result-label">Total Interest Paid</div><div class="result-value" id="debtInterest">-</div></div>
      <div class="col-6"><div class="result-label">Total Amount Paid</div><div class="result-value" id="debtTotal">-</div></div>
      <div class="col-6"><div class="result-label">Interest Saved (Extra)</div><div class="result-value" id="debtSaved">-</div></div>
    </div>
  </div>
</div>
'@ @'
<script>
function calcDebt(){
  const P=+document.getElementById('debtAmt').value, r=(+document.getElementById('debtRate').value/100/12),
        pay=+document.getElementById('debtPay').value, extra=+document.getElementById('debtExtra').value;
  function months(pmt){let bal=P,m=0,int=0;while(bal>0&&m<600){const i=bal*r;int+=i;bal=bal+i-pmt;m++;}return{m,int};}
  const base=months(pay), ext=months(pay+extra);
  document.getElementById('debtMonths').textContent=base.m+' months';
  document.getElementById('debtInterest').textContent='$'+base.int.toFixed(2);
  document.getElementById('debtTotal').textContent='$'+(P+base.int).toFixed(2);
  document.getElementById('debtSaved').textContent=extra>0?'$'+(base.int-ext.int).toFixed(2):'-';
  document.getElementById('resultBox').classList.add('show');
}
</script>
'@

# 2. Investment Calculator
Write-Calc "investment-calculator.html" "Investment Return Calculator" "Calculate investment returns with compound interest, inflation adjustment, and tax impact for any investment period." "investment calculator, return on investment, compound growth, investment growth calculator" "📈" "#1b5e20,#2e7d32" "finance" "finance" "💰 Finance" @'
<div class="calc-box">
  <h2 class="calc-title">Investment Return Calculator</h2>
  <div class="row g-3">
    <div class="col-md-6"><label class="form-label">Initial Investment ($)</label><input type="number" class="form-control" id="invInit" value="10000" step="100"></div>
    <div class="col-md-6"><label class="form-label">Monthly Contribution ($)</label><input type="number" class="form-control" id="invMonthly" value="500" step="50"></div>
    <div class="col-md-6"><label class="form-label">Annual Return Rate (%)</label><input type="number" class="form-control" id="invRate" value="10" step="0.1"></div>
    <div class="col-md-6"><label class="form-label">Investment Period (Years)</label><input type="number" class="form-control" id="invYears" value="20" step="1"></div>
    <div class="col-md-6"><label class="form-label">Inflation Rate (%)</label><input type="number" class="form-control" id="invInflation" value="6" step="0.1"></div>
    <div class="col-md-6"><label class="form-label">Tax on Returns (%)</label><input type="number" class="form-control" id="invTax" value="10" step="1"></div>
  </div>
  <button class="btn-calculate mt-4" onclick="calcInvestment()"><i class="bi bi-graph-up me-2"></i>Calculate Returns</button>
  <div class="result-box" id="resultBox">
    <div class="row g-3 text-center">
      <div class="col-6"><div class="result-label">Future Value</div><div class="result-value" id="invFV">-</div></div>
      <div class="col-6"><div class="result-label">Total Invested</div><div class="result-value" id="invTotal">-</div></div>
      <div class="col-6"><div class="result-label">Total Returns</div><div class="result-value" id="invReturns">-</div></div>
      <div class="col-6"><div class="result-label">Inflation Adjusted Value</div><div class="result-value" id="invReal">-</div></div>
    </div>
  </div>
</div>
'@ @'
<script>
function calcInvestment(){
  const P=+document.getElementById('invInit').value, pmt=+document.getElementById('invMonthly').value,
        r=+document.getElementById('invRate').value/100/12, n=+document.getElementById('invYears').value*12,
        inf=+document.getElementById('invInflation').value/100, tax=+document.getElementById('invTax').value/100;
  const fv = P*Math.pow(1+r,n) + pmt*(Math.pow(1+r,n)-1)/r;
  const totalIn = P + pmt*n;
  const returns = fv - totalIn;
  const afterTax = totalIn + returns*(1-tax);
  const real = afterTax / Math.pow(1+inf, +document.getElementById('invYears').value);
  document.getElementById('invFV').textContent='$'+fv.toFixed(0);
  document.getElementById('invTotal').textContent='$'+totalIn.toFixed(0);
  document.getElementById('invReturns').textContent='$'+returns.toFixed(0);
  document.getElementById('invReal').textContent='$'+real.toFixed(0);
  document.getElementById('resultBox').classList.add('show');
}
</script>
'@

# 3. Tip Calculator (split bill)
Write-Calc "bill-split-calculator.html" "Bill Split Calculator" "Split bills equally among friends. Calculate tip amount per person, total per person, and custom tip percentages instantly." "bill split calculator, split bill calculator, tip calculator, how to split bill, restaurant bill split" "🍽️" "#e65100,#bf360c" "finance" "finance" "💰 Finance" @'
<div class="calc-box">
  <h2 class="calc-title">Bill Split Calculator</h2>
  <div class="row g-3">
    <div class="col-md-6"><label class="form-label">Bill Amount ($)</label><input type="number" class="form-control" id="billAmt" value="120" step="1"></div>
    <div class="col-md-6"><label class="form-label">Tip Percentage (%)</label><input type="number" class="form-control" id="billTip" value="15" step="1"></div>
    <div class="col-md-6"><label class="form-label">Number of People</label><input type="number" class="form-control" id="billPeople" value="4" step="1" min="1"></div>
    <div class="col-md-6"><label class="form-label">Discount ($)</label><input type="number" class="form-control" id="billDiscount" value="0" step="1"></div>
  </div>
  <div class="d-flex gap-2 mt-3 flex-wrap">
    <button class="cat-pill active" onclick="setTip(10,this)">10%</button>
    <button class="cat-pill" onclick="setTip(15,this)">15%</button>
    <button class="cat-pill" onclick="setTip(18,this)">18%</button>
    <button class="cat-pill" onclick="setTip(20,this)">20%</button>
    <button class="cat-pill" onclick="setTip(25,this)">25%</button>
  </div>
  <button class="btn-calculate mt-4" onclick="calcBill()"><i class="bi bi-people me-2"></i>Split Bill</button>
  <div class="result-box" id="resultBox">
    <div class="row g-3 text-center">
      <div class="col-6"><div class="result-label">Tip Amount</div><div class="result-value" id="tipAmt">-</div></div>
      <div class="col-6"><div class="result-label">Total Bill</div><div class="result-value" id="totalBill">-</div></div>
      <div class="col-6"><div class="result-label">Per Person (Tip)</div><div class="result-value" id="perTip">-</div></div>
      <div class="col-6"><div class="result-label">Per Person (Total)</div><div class="result-value" id="perTotal">-</div></div>
    </div>
  </div>
</div>
'@ @'
<script>
function setTip(v,btn){document.getElementById('billTip').value=v;document.querySelectorAll('.cat-pill').forEach(p=>p.classList.remove('active'));btn.classList.add('active');}
function calcBill(){
  const bill=+document.getElementById('billAmt').value, tip=+document.getElementById('billTip').value/100,
        n=+document.getElementById('billPeople').value||1, disc=+document.getElementById('billDiscount').value;
  const net=Math.max(0,bill-disc), tipAmt=net*tip, total=net+tipAmt;
  document.getElementById('tipAmt').textContent='$'+tipAmt.toFixed(2);
  document.getElementById('totalBill').textContent='$'+total.toFixed(2);
  document.getElementById('perTip').textContent='$'+(tipAmt/n).toFixed(2);
  document.getElementById('perTotal').textContent='$'+(total/n).toFixed(2);
  document.getElementById('resultBox').classList.add('show');
}
</script>
'@

# 4. Hourly to Salary
Write-Calc "hourly-to-salary-calculator.html" "Hourly to Salary Calculator" "Convert hourly wage to annual salary. Calculate weekly, monthly, and yearly earnings based on hours worked per week." "hourly to salary calculator, hourly wage to annual salary, convert hourly to yearly, salary calculator" "💼" "#4a148c,#6a1b9a" "finance" "finance" "💰 Finance" @'
<div class="calc-box">
  <h2 class="calc-title">Hourly to Salary Calculator</h2>
  <div class="row g-3">
    <div class="col-md-6"><label class="form-label">Hourly Rate ($)</label><input type="number" class="form-control" id="hourlyRate" value="25" step="0.5"></div>
    <div class="col-md-6"><label class="form-label">Hours Per Week</label><input type="number" class="form-control" id="hoursWeek" value="40" step="1"></div>
    <div class="col-md-6"><label class="form-label">Weeks Per Year</label><input type="number" class="form-control" id="weeksYear" value="52" step="1"></div>
    <div class="col-md-6"><label class="form-label">Overtime Hours/Week</label><input type="number" class="form-control" id="otHours" value="0" step="0.5"></div>
  </div>
  <button class="btn-calculate mt-4" onclick="calcHourly()"><i class="bi bi-currency-dollar me-2"></i>Calculate Salary</button>
  <div class="result-box" id="resultBox">
    <div class="row g-3 text-center">
      <div class="col-6"><div class="result-label">Daily Pay</div><div class="result-value" id="dailyPay">-</div></div>
      <div class="col-6"><div class="result-label">Weekly Pay</div><div class="result-value" id="weeklyPay">-</div></div>
      <div class="col-6"><div class="result-label">Monthly Pay</div><div class="result-value" id="monthlyPay">-</div></div>
      <div class="col-6"><div class="result-label">Annual Salary</div><div class="result-value" id="annualSalary">-</div></div>
    </div>
  </div>
</div>
'@ @'
<script>
function calcHourly(){
  const h=+document.getElementById('hourlyRate').value, hw=+document.getElementById('hoursWeek').value,
        wy=+document.getElementById('weeksYear').value, ot=+document.getElementById('otHours').value;
  const weekly=h*hw+ot*h*1.5, annual=weekly*wy;
  document.getElementById('dailyPay').textContent='$'+(h*hw/5).toFixed(2);
  document.getElementById('weeklyPay').textContent='$'+weekly.toFixed(2);
  document.getElementById('monthlyPay').textContent='$'+(annual/12).toFixed(2);
  document.getElementById('annualSalary').textContent='$'+annual.toFixed(2);
  document.getElementById('resultBox').classList.add('show');
}
</script>
'@

# 5. Sales Tax Calculator
Write-Calc "sales-tax-calculator.html" "Sales Tax Calculator" "Calculate sales tax amount and total price with any tax rate. Add or remove sales tax from prices instantly." "sales tax calculator, calculate sales tax, tax rate calculator, price with tax, add tax to price" "🧾" "#004d40,#00695c" "finance" "finance" "💰 Finance" @'
<div class="calc-box">
  <h2 class="calc-title">Sales Tax Calculator</h2>
  <div class="mb-3">
    <div class="d-flex gap-2 flex-wrap">
      <button class="cat-pill active" onclick="setMode('add',this)">Add Tax to Price</button>
      <button class="cat-pill" onclick="setMode('remove',this)">Remove Tax from Price</button>
    </div>
  </div>
  <div class="row g-3">
    <div class="col-md-6"><label class="form-label" id="priceLabel">Pre-Tax Price ($)</label><input type="number" class="form-control" id="stPrice" value="100" step="0.01"></div>
    <div class="col-md-6"><label class="form-label">Tax Rate (%)</label><input type="number" class="form-control" id="stRate" value="8.5" step="0.1"></div>
  </div>
  <button class="btn-calculate mt-4" onclick="calcSalesTax()"><i class="bi bi-receipt me-2"></i>Calculate Tax</button>
  <div class="result-box" id="resultBox">
    <div class="row g-3 text-center">
      <div class="col-6"><div class="result-label">Pre-Tax Price</div><div class="result-value" id="stPre">-</div></div>
      <div class="col-6"><div class="result-label">Tax Amount</div><div class="result-value" id="stTaxAmt">-</div></div>
      <div class="col-6"><div class="result-label">Total Price</div><div class="result-value" id="stTotal">-</div></div>
      <div class="col-6"><div class="result-label">Tax Rate</div><div class="result-value" id="stRateShow">-</div></div>
    </div>
  </div>
</div>
'@ @'
<script>
let stMode='add';
function setMode(m,btn){stMode=m;document.querySelectorAll('.cat-pill').forEach(p=>p.classList.remove('active'));btn.classList.add('active');document.getElementById('priceLabel').textContent=m==='add'?'Pre-Tax Price ($)':'Total Price with Tax ($)';}
function calcSalesTax(){
  const price=+document.getElementById('stPrice').value, rate=+document.getElementById('stRate').value/100;
  let pre,taxAmt,total;
  if(stMode==='add'){pre=price;taxAmt=price*rate;total=price+taxAmt;}
  else{total=price;pre=price/(1+rate);taxAmt=total-pre;}
  document.getElementById('stPre').textContent='$'+pre.toFixed(2);
  document.getElementById('stTaxAmt').textContent='$'+taxAmt.toFixed(2);
  document.getElementById('stTotal').textContent='$'+total.toFixed(2);
  document.getElementById('stRateShow').textContent=(rate*100).toFixed(2)+'%';
  document.getElementById('resultBox').classList.add('show');
}
</script>
'@

Write-Host "Batch 2 (Part 1) complete"
