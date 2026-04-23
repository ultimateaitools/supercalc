/* ============================================================
   CalcPro.online - Calculator Engine
   All 250+ Calculator Functions
   ============================================================ */

'use strict';

const CalcEngine = {

  /* ------------------------------------------
     FINANCE CALCULATORS
  ------------------------------------------ */

  // EMI Calculator
  emi(principal, annualRate, tenureMonths) {
    const r = annualRate / 12 / 100;
    const n = tenureMonths;
    if (r === 0) return { emi: principal / n, totalAmount: principal, totalInterest: 0 };
    const emi = (principal * r * Math.pow(1 + r, n)) / (Math.pow(1 + r, n) - 1);
    const totalAmount = emi * n;
    const totalInterest = totalAmount - principal;
    return { emi, totalAmount, totalInterest };
  },

  // GST Calculator
  gst(amount, rate, type) {
    if (type === 'add') {
      const gstAmt = (amount * rate) / 100;
      return { original: amount, gstAmount: gstAmt, total: amount + gstAmt, cgst: gstAmt / 2, sgst: gstAmt / 2 };
    } else {
      const original = (amount * 100) / (100 + rate);
      const gstAmt = amount - original;
      return { original, gstAmount: gstAmt, total: amount, cgst: gstAmt / 2, sgst: gstAmt / 2 };
    }
  },

  // SIP Calculator
  sip(monthlyAmount, annualReturn, years) {
    const r = annualReturn / 12 / 100;
    const n = years * 12;
    const futureValue = monthlyAmount * ((Math.pow(1 + r, n) - 1) / r) * (1 + r);
    const invested = monthlyAmount * n;
    const returns = futureValue - invested;
    return { futureValue, invested, returns };
  },

  // Lump Sum Calculator
  lumpsum(amount, annualReturn, years) {
    const futureValue = amount * Math.pow(1 + annualReturn / 100, years);
    const returns = futureValue - amount;
    return { futureValue, invested: amount, returns };
  },

  // FD Calculator
  fd(principal, annualRate, years, frequency) {
    const freqMap = { annually: 1, semiAnnually: 2, quarterly: 4, monthly: 12 };
    const n = freqMap[frequency] || 4;
    const r = annualRate / 100;
    const maturity = principal * Math.pow(1 + r / n, n * years);
    const interest = maturity - principal;
    return { maturity, interest, principal };
  },

  // RD Calculator
  rd(monthlyDeposit, annualRate, months) {
    const r = annualRate / 400;
    const n = months;
    let maturity = 0;
    for (let i = 1; i <= n; i++) {
      maturity += monthlyDeposit * Math.pow(1 + r, 4 * (n - i + 1) / 12);
    }
    const invested = monthlyDeposit * n;
    const interest = maturity - invested;
    return { maturity, interest, invested };
  },

  // PPF Calculator
  ppf(yearlyDeposit, years = 15) {
    const rate = 0.071; // 7.1% current PPF rate
    let balance = 0;
    let totalInvested = 0;
    for (let i = 0; i < years; i++) {
      balance = (balance + yearlyDeposit) * (1 + rate);
      totalInvested += yearlyDeposit;
    }
    const interest = balance - totalInvested;
    return { maturity: balance, interest, invested: totalInvested };
  },

  // Compound Interest
  compoundInterest(principal, rate, time, n = 1) {
    const amount = principal * Math.pow(1 + rate / (100 * n), n * time);
    const interest = amount - principal;
    return { amount, interest, principal };
  },

  // Simple Interest
  simpleInterest(principal, rate, time) {
    const interest = (principal * rate * time) / 100;
    const amount = principal + interest;
    return { amount, interest, principal };
  },

  // Income Tax (India FY 2024-25 - New Regime)
  incomeTax(annualIncome) {
    let tax = 0;
    const slabs = [
      { limit: 300000, rate: 0 },
      { limit: 600000, rate: 5 },
      { limit: 900000, rate: 10 },
      { limit: 1200000, rate: 15 },
      { limit: 1500000, rate: 20 },
      { limit: Infinity, rate: 30 }
    ];
    let prev = 0;
    for (const slab of slabs) {
      if (annualIncome > prev) {
        const taxable = Math.min(annualIncome, slab.limit) - prev;
        tax += (taxable * slab.rate) / 100;
        prev = slab.limit;
      }
      if (annualIncome <= slab.limit) break;
    }
    // Rebate u/s 87A for income <= 7 lakh
    if (annualIncome <= 700000) tax = 0;
    const cess = tax * 0.04;
    const totalTax = tax + cess;
    return { tax, cess, totalTax, monthlyTax: totalTax / 12, effectiveRate: (totalTax / annualIncome) * 100 };
  },

  // HRA Calculator
  hra(basicSalary, hra, rentPaid, isMetro) {
    const annual = {
      basic: basicSalary * 12,
      hra: hra * 12,
      rent: rentPaid * 12
    };
    const exemption1 = annual.hra;
    const exemption2 = annual.rent - (0.1 * annual.basic);
    const exemption3 = isMetro ? 0.5 * annual.basic : 0.4 * annual.basic;
    const exempt = Math.max(0, Math.min(exemption1, exemption2, exemption3));
    const taxable = annual.hra - exempt;
    return { exempt, taxable, monthlyExempt: exempt / 12 };
  },

  // Gratuity
  gratuity(lastSalary, yearsOfService) {
    const gratuity = (lastSalary * yearsOfService * 15) / 26;
    return { gratuity, maxExempt: 2000000 };
  },

  // Salary CTC to In-Hand
  salaryBreakdown(ctc) {
    const basic = ctc * 0.5;
    const hra = basic * 0.5;
    const pf = basic * 0.12;
    const professional = 2400;
    const inhand = ctc - pf * 2 - professional;
    const monthly = inhand / 12;
    return { ctc, basic: basic / 12, hra: hra / 12, pf: pf / 12, professional: professional / 12, monthly, inhand };
  },

  // Discount
  discount(originalPrice, discountPercent) {
    const discountAmt = (originalPrice * discountPercent) / 100;
    const finalPrice = originalPrice - discountAmt;
    return { finalPrice, discountAmt, savings: discountAmt };
  },

  // ROI
  roi(investment, returns) {
    const profit = returns - investment;
    const roiPercent = (profit / investment) * 100;
    return { profit, roiPercent };
  },

  // Break Even
  breakEven(fixedCost, variableCost, sellingPrice) {
    const contribution = sellingPrice - variableCost;
    const units = fixedCost / contribution;
    const revenue = units * sellingPrice;
    return { units, revenue, contribution };
  },

  // Tip Calculator
  tip(billAmount, tipPercent, splitCount = 1) {
    const tipAmount = (billAmount * tipPercent) / 100;
    const total = billAmount + tipAmount;
    const perPerson = total / splitCount;
    return { tipAmount, total, perPerson };
  },

  // Profit & Loss
  profitLoss(costPrice, sellingPrice) {
    const diff = sellingPrice - costPrice;
    const percent = (Math.abs(diff) / costPrice) * 100;
    const type = diff >= 0 ? 'Profit' : 'Loss';
    return { amount: Math.abs(diff), percent, type };
  },

  // Markup
  markup(cost, markupPercent) {
    const markup = (cost * markupPercent) / 100;
    const sellPrice = cost + markup;
    const grossMargin = (markup / sellPrice) * 100;
    return { sellPrice, markup, grossMargin };
  },

  // Commission
  commission(salesAmount, commissionRate) {
    const commission = (salesAmount * commissionRate) / 100;
    return { commission, net: salesAmount - commission };
  },

  // Inflation
  inflation(currentAmount, inflationRate, years) {
    const futureValue = currentAmount * Math.pow(1 + inflationRate / 100, years);
    return { futureValue, increase: futureValue - currentAmount };
  },

  // Retirement
  retirement(currentAge, retireAge, monthlyExpense, returnRate, inflationRate) {
    const years = retireAge - currentAge;
    const lifeExpectancy = 85;
    const postRetireYears = lifeExpectancy - retireAge;
    const inflatedExpense = monthlyExpense * Math.pow(1 + inflationRate / 100, years);
    const annualExpense = inflatedExpense * 12;
    const realReturn = (returnRate - inflationRate) / 100;
    const corpus = annualExpense * ((1 - Math.pow(1 + realReturn, -postRetireYears)) / realReturn);
    return { corpus, inflatedExpense, years, postRetireYears };
  },

  // Credit Card Interest
  creditCard(balance, monthlyRate, minPayment) {
    let bal = balance;
    let totalInterest = 0;
    let months = 0;
    while (bal > 0 && months < 600) {
      const interest = (bal * monthlyRate) / 100;
      totalInterest += interest;
      bal = bal + interest - minPayment;
      months++;
      if (minPayment <= interest) break;
    }
    return { months, totalInterest, totalPaid: balance + totalInterest };
  },

  /* ------------------------------------------
     HEALTH CALCULATORS
  ------------------------------------------ */

  // BMI
  bmi(weight, height) {
    const bmi = weight / (height * height);
    let category, color;
    if (bmi < 18.5) { category = 'Underweight'; color = '#3B82F6'; }
    else if (bmi < 25) { category = 'Normal weight'; color = '#10B981'; }
    else if (bmi < 30) { category = 'Overweight'; color = '#F59E0B'; }
    else { category = 'Obese'; color = '#EF4444'; }
    return { bmi, category, color };
  },

  // BMR (Mifflin-St Jeor)
  bmr(weight, height, age, gender) {
    let bmr;
    if (gender === 'male') bmr = 10 * weight + 6.25 * height - 5 * age + 5;
    else bmr = 10 * weight + 6.25 * height - 5 * age - 161;
    return { bmr };
  },

  // TDEE
  tdee(bmr, activityLevel) {
    const multipliers = {
      sedentary: 1.2,
      light: 1.375,
      moderate: 1.55,
      active: 1.725,
      veryActive: 1.9
    };
    const tdee = bmr * (multipliers[activityLevel] || 1.55);
    return {
      tdee,
      weightLoss: tdee - 500,
      weightGain: tdee + 500,
      maintain: tdee
    };
  },

  // Ideal Weight (Robinson Formula)
  idealWeight(height, gender) {
    const inchesOver5ft = (height * 100 / 2.54) - 60;
    let weight;
    if (gender === 'male') weight = 52 + 1.9 * inchesOver5ft;
    else weight = 49 + 1.7 * inchesOver5ft;
    return { weight, min: weight * 0.9, max: weight * 1.1 };
  },

  // Body Fat % (US Navy Method)
  bodyFat(waist, neck, height, gender, hip = 0) {
    let bodyFat;
    if (gender === 'male') {
      bodyFat = 495 / (1.0324 - 0.19077 * Math.log10(waist - neck) + 0.15456 * Math.log10(height)) - 450;
    } else {
      bodyFat = 495 / (1.29579 - 0.35004 * Math.log10(waist + hip - neck) + 0.22100 * Math.log10(height)) - 450;
    }
    return { bodyFat: Math.max(0, bodyFat) };
  },

  // Heart Rate Zones
  heartRate(age, restingHR = 70) {
    const maxHR = 220 - age;
    const hrr = maxHR - restingHR;
    return {
      max: maxHR,
      zone1: { min: Math.round(restingHR + hrr * 0.5), max: Math.round(restingHR + hrr * 0.6), name: 'Warm Up' },
      zone2: { min: Math.round(restingHR + hrr * 0.6), max: Math.round(restingHR + hrr * 0.7), name: 'Fat Burn' },
      zone3: { min: Math.round(restingHR + hrr * 0.7), max: Math.round(restingHR + hrr * 0.8), name: 'Cardio' },
      zone4: { min: Math.round(restingHR + hrr * 0.8), max: Math.round(restingHR + hrr * 0.9), name: 'Hard' },
      zone5: { min: Math.round(restingHR + hrr * 0.9), max: maxHR, name: 'Maximum' }
    };
  },

  // Pregnancy Due Date
  pregnancyDue(lmpDate) {
    const lmp = new Date(lmpDate);
    const due = new Date(lmp.getTime() + 280 * 24 * 60 * 60 * 1000);
    const today = new Date();
    const weeksPregnant = Math.floor((today - lmp) / (7 * 24 * 60 * 60 * 1000));
    const daysLeft = Math.floor((due - today) / (24 * 60 * 60 * 1000));
    return { dueDate: due, weeksPregnant: Math.max(0, weeksPregnant), daysLeft: Math.max(0, daysLeft), trimester: weeksPregnant < 13 ? 1 : weeksPregnant < 27 ? 2 : 3 };
  },

  // One Rep Max
  oneRepMax(weight, reps) {
    const orm = weight / (1.0278 - 0.0278 * reps);
    return {
      orm,
      p95: orm * 0.95, p90: orm * 0.90, p85: orm * 0.85,
      p80: orm * 0.80, p75: orm * 0.75, p70: orm * 0.70
    };
  },

  // Water Intake
  waterIntake(weight, activityLevel) {
    const base = weight * 35; // ml
    const activityBonus = { low: 0, moderate: 500, high: 1000, athlete: 1500 };
    const total = base + (activityBonus[activityLevel] || 0);
    return { ml: total, liters: total / 1000, glasses: Math.round(total / 250) };
  },

  // Protein Intake
  proteinIntake(weight, goal) {
    const ratios = { maintain: 1.6, gain: 2.0, loss: 2.2, athlete: 2.4 };
    const grams = weight * (ratios[goal] || 1.6);
    return { grams, calories: grams * 4 };
  },

  // Running Pace
  runningPace(distance, timeMinutes) {
    const paceMin = timeMinutes / distance;
    const speed = distance / (timeMinutes / 60);
    return {
      pace: paceMin,
      paceFormatted: `${Math.floor(paceMin)}:${String(Math.round((paceMin % 1) * 60)).padStart(2, '0')}`,
      speed
    };
  },

  // Sleep Calculator
  sleepCycles(bedtime) {
    const [h, m] = bedtime.split(':').map(Number);
    const base = h * 60 + m + 15; // 15 min to fall asleep
    const cycles = [1, 2, 3, 4, 5, 6].map(c => {
      const wake = base + c * 90;
      return {
        cycles: c,
        wakeTime: `${String(Math.floor((wake % (24 * 60)) / 60)).padStart(2, '0')}:${String(wake % 60).padStart(2, '0')}`
      };
    });
    return cycles;
  },

  /* ------------------------------------------
     MATH CALCULATORS
  ------------------------------------------ */

  // Percentage
  percentage(type, a, b) {
    if (type === 'whatPercent') return { result: (a / b) * 100 };
    if (type === 'percentOf') return { result: (a / 100) * b };
    if (type === 'increase') return { result: ((b - a) / a) * 100 };
    if (type === 'decrease') return { result: ((a - b) / a) * 100 };
    return { result: 0 };
  },

  // Age Calculator
  ageCalc(birthDate) {
    const birth = new Date(birthDate);
    const today = new Date();
    let years = today.getFullYear() - birth.getFullYear();
    let months = today.getMonth() - birth.getMonth();
    let days = today.getDate() - birth.getDate();
    if (days < 0) { months--; days += new Date(today.getFullYear(), today.getMonth(), 0).getDate(); }
    if (months < 0) { years--; months += 12; }
    const totalDays = Math.floor((today - birth) / (24 * 60 * 60 * 1000));
    const totalWeeks = Math.floor(totalDays / 7);
    const nextBirthday = new Date(today.getFullYear(), birth.getMonth(), birth.getDate());
    if (nextBirthday < today) nextBirthday.setFullYear(today.getFullYear() + 1);
    const daysToNext = Math.floor((nextBirthday - today) / (24 * 60 * 60 * 1000));
    return { years, months, days, totalDays, totalWeeks, daysToNext };
  },

  // LCM & HCF
  gcd(a, b) { return b === 0 ? a : this.gcd(b, a % b); },
  lcm(a, b) { return (a * b) / this.gcd(a, b); },

  // Prime Check
  isPrime(n) {
    if (n < 2) return false;
    for (let i = 2; i <= Math.sqrt(n); i++) if (n % i === 0) return false;
    return true;
  },

  // Quadratic Solver
  quadratic(a, b, c) {
    const discriminant = b * b - 4 * a * c;
    if (discriminant > 0) {
      return { x1: (-b + Math.sqrt(discriminant)) / (2 * a), x2: (-b - Math.sqrt(discriminant)) / (2 * a), type: 'two_real' };
    } else if (discriminant === 0) {
      return { x1: -b / (2 * a), x2: -b / (2 * a), type: 'one_real' };
    } else {
      return { real: -b / (2 * a), imag: Math.sqrt(-discriminant) / (2 * a), type: 'complex' };
    }
  },

  // Statistics
  statistics(numbers) {
    const n = numbers.length;
    const sorted = [...numbers].sort((a, b) => a - b);
    const mean = numbers.reduce((s, v) => s + v, 0) / n;
    const median = n % 2 === 0 ? (sorted[n/2-1] + sorted[n/2]) / 2 : sorted[Math.floor(n/2)];
    const freq = {};
    numbers.forEach(v => freq[v] = (freq[v] || 0) + 1);
    const maxFreq = Math.max(...Object.values(freq));
    const mode = Object.keys(freq).filter(k => freq[k] === maxFreq).map(Number);
    const variance = numbers.reduce((s, v) => s + Math.pow(v - mean, 2), 0) / n;
    const stdDev = Math.sqrt(variance);
    const range = sorted[n-1] - sorted[0];
    return { mean, median, mode, stdDev, variance, range, min: sorted[0], max: sorted[n-1], sum: numbers.reduce((s, v) => s + v, 0), count: n };
  },

  // Pythagorean
  pythagorean(a, b, c) {
    if (!a) return { a: Math.sqrt(c*c - b*b) };
    if (!b) return { b: Math.sqrt(c*c - a*a) };
    return { c: Math.sqrt(a*a + b*b) };
  },

  // Roman Numeral
  toRoman(num) {
    const vals = [1000,900,500,400,100,90,50,40,10,9,5,4,1];
    const syms = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I'];
    let result = '';
    for (let i = 0; i < vals.length; i++) {
      while (num >= vals[i]) { result += syms[i]; num -= vals[i]; }
    }
    return result;
  },

  fromRoman(str) {
    const map = {I:1,V:5,X:10,L:50,C:100,D:500,M:1000};
    let result = 0;
    for (let i = 0; i < str.length; i++) {
      const cur = map[str[i]], next = map[str[i+1]];
      result += (next && cur < next) ? -cur : cur;
    }
    return result;
  },

  /* ------------------------------------------
     UNIT CONVERTERS
  ------------------------------------------ */

  convertLength(value, from, to) {
    const toMeter = { m:1, km:1000, cm:0.01, mm:0.001, mi:1609.34, yd:0.9144, ft:0.3048, in:0.0254, nm:1852 };
    return value * toMeter[from] / toMeter[to];
  },

  convertWeight(value, from, to) {
    const toKg = { kg:1, g:0.001, mg:0.000001, lb:0.453592, oz:0.0283495, t:1000, st:6.35029 };
    return value * toKg[from] / toKg[to];
  },

  convertTemp(value, from, to) {
    let celsius;
    if (from === 'c') celsius = value;
    else if (from === 'f') celsius = (value - 32) * 5/9;
    else celsius = value - 273.15;
    if (to === 'c') return celsius;
    if (to === 'f') return celsius * 9/5 + 32;
    return celsius + 273.15;
  },

  convertSpeed(value, from, to) {
    const toMs = { ms:1, kmh:1/3.6, mph:0.44704, kt:0.514444, fps:0.3048 };
    return value * toMs[from] / toMs[to];
  },

  convertData(value, from, to) {
    const toBytes = { B:1, KB:1024, MB:1048576, GB:1073741824, TB:1099511627776 };
    return value * toBytes[from] / toBytes[to];
  },

  /* ------------------------------------------
     DATE & TIME CALCULATORS
  ------------------------------------------ */

  dateDiff(date1, date2) {
    const d1 = new Date(date1), d2 = new Date(date2);
    const diff = Math.abs(d2 - d1);
    const days = Math.floor(diff / (24*60*60*1000));
    const weeks = Math.floor(days / 7);
    const months = Math.floor(days / 30.44);
    const years = Math.floor(days / 365.25);
    return { days, weeks, months, years, hours: days * 24, minutes: days * 24 * 60 };
  },

  addDays(date, days) {
    const d = new Date(date);
    d.setDate(d.getDate() + days);
    return d;
  },

  workingDays(date1, date2) {
    const d1 = new Date(date1), d2 = new Date(date2);
    let count = 0;
    const cur = new Date(d1);
    while (cur <= d2) {
      const day = cur.getDay();
      if (day !== 0 && day !== 6) count++;
      cur.setDate(cur.getDate() + 1);
    }
    return count;
  },

  /* ------------------------------------------
     CONSTRUCTION CALCULATORS
  ------------------------------------------ */

  concrete(length, width, depth) {
    const volume = length * width * depth;
    const cement = volume * 8; // bags per m3 (approx for M20)
    const sand = volume * 0.44; // m3
    const aggregate = volume * 0.88; // m3
    return { volume, cement, sand, aggregate };
  },

  bricks(length, width, height, thickness = 0.23) {
    const volume = length * width * height;
    const brickVol = 0.19 * 0.09 * 0.09;
    const mortar = 0.1;
    const bricks = Math.ceil(volume / (brickVol * (1 + mortar)));
    return { bricks, volume };
  },

  paint(length, width, height, doors = 1, windows = 2) {
    const wallArea = 2 * (length + width) * height;
    const doorArea = doors * 2;
    const windowArea = windows * 1.5;
    const paintableArea = wallArea - doorArea - windowArea;
    const liters = paintableArea / 12; // 12 sqm per liter (2 coats)
    return { area: paintableArea, liters, cans: Math.ceil(liters / 4) };
  },

  tiles(length, width, tileLength, tileWidth, wastage = 10) {
    const roomArea = length * width;
    const tileArea = (tileLength / 100) * (tileWidth / 100);
    const base = Math.ceil(roomArea / tileArea);
    const total = Math.ceil(base * (1 + wastage / 100));
    return { tiles: total, area: roomArea, tileArea };
  },

  acTonnage(length, width, height, sunExposure = 'moderate') {
    const btu = length * width * height * 337;
    const multiplier = { low: 0.8, moderate: 1.0, high: 1.2 };
    const required = btu * (multiplier[sunExposure] || 1);
    const tons = required / 12000;
    return { tons: Math.ceil(tons * 2) / 2, btu: required };
  },

  solarPanels(monthlyUsage, sunHours = 5, panelWatt = 400) {
    const dailyUsage = monthlyUsage / 30;
    const systemSize = dailyUsage / sunHours;
    const panels = Math.ceil((systemSize * 1000) / panelWatt);
    return { panels, systemSize, dailyUsage };
  },

  /* ------------------------------------------
     ELECTRICITY CALCULATORS
  ------------------------------------------ */

  electricityBill(appliances, days, tariff) {
    let totalUnits = 0;
    appliances.forEach(a => {
      totalUnits += (a.watts * a.hours * days) / 1000;
    });
    const bill = totalUnits * tariff;
    return { totalUnits, bill };
  },

  batteryLife(capacity, current) {
    const hours = capacity / current;
    return { hours, minutes: hours * 60 };
  },

  ledSavings(watts, ledWatts, dailyHours, tariff, count = 1) {
    const oldUnits = (watts * dailyHours * 365 * count) / 1000;
    const newUnits = (ledWatts * dailyHours * 365 * count) / 1000;
    const savings = (oldUnits - newUnits) * tariff;
    return { savings, unitsSaved: oldUnits - newUnits, co2Saved: (oldUnits - newUnits) * 0.82 };
  },

  /* ------------------------------------------
     AUTOMOTIVE CALCULATORS
  ------------------------------------------ */

  fuelCost(distance, mileage, fuelPrice) {
    const liters = distance / mileage;
    const cost = liters * fuelPrice;
    return { liters, cost };
  },

  evCharge(batteryCapacity, currentCharge, targetCharge, electricityRate) {
    const kwhNeeded = batteryCapacity * (targetCharge - currentCharge) / 100;
    const cost = kwhNeeded * electricityRate;
    return { kwhNeeded, cost };
  },

  carDepreciation(purchasePrice, year) {
    const rates = [0.20, 0.15, 0.15, 0.12, 0.10, 0.08, 0.08, 0.08, 0.05, 0.05];
    let value = purchasePrice;
    const yearly = [];
    for (let i = 0; i < Math.min(year, rates.length); i++) {
      value -= value * rates[i];
      yearly.push({ year: i+1, value });
    }
    return { currentValue: value, depreciation: purchasePrice - value, yearly };
  },

  /* ------------------------------------------
     REAL ESTATE CALCULATORS
  ------------------------------------------ */

  stampDuty(propertyValue, state = 'general') {
    const rates = { general: 0.07, metro: 0.06, female: 0.05 };
    const rate = rates[state] || 0.07;
    const stampDuty = propertyValue * rate;
    const registration = propertyValue * 0.01;
    return { stampDuty, registration, total: stampDuty + registration };
  },

  rentalYield(propertyValue, monthlyRent) {
    const annualRent = monthlyRent * 12;
    const grossYield = (annualRent / propertyValue) * 100;
    const netYield = grossYield * 0.8; // accounting for expenses
    return { grossYield, netYield, annualRent };
  },

  /* ------------------------------------------
     EDUCATION CALCULATORS
  ------------------------------------------ */

  gpa(courses) {
    const gradePoints = { 'A+':4.0, 'A':4.0, 'A-':3.7, 'B+':3.3, 'B':3.0, 'B-':2.7, 'C+':2.3, 'C':2.0, 'D':1.0, 'F':0 };
    const totalCredits = courses.reduce((s, c) => s + c.credits, 0);
    const totalPoints = courses.reduce((s, c) => s + (gradePoints[c.grade] || 0) * c.credits, 0);
    return { gpa: totalPoints / totalCredits, totalCredits };
  },

  cgpaToPercent(cgpa, scale = 10) {
    if (scale === 10) return { percent: cgpa * 9.5 };
    if (scale === 4) return { percent: (cgpa / 4) * 100 };
    return { percent: cgpa };
  },

  /* ------------------------------------------
     TRAVEL CALCULATORS
  ------------------------------------------ */

  flightDistance(lat1, lon1, lat2, lon2) {
    const R = 6371;
    const dLat = (lat2 - lat1) * Math.PI / 180;
    const dLon = (lon2 - lon1) * Math.PI / 180;
    const a = Math.sin(dLat/2)**2 + Math.cos(lat1 * Math.PI/180) * Math.cos(lat2 * Math.PI/180) * Math.sin(dLon/2)**2;
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
    const km = R * c;
    return { km, miles: km * 0.621371, nm: km * 0.539957, flightHours: km / 900 };
  },

  /* ------------------------------------------
     FOOD CALCULATORS
  ------------------------------------------ */

  fastingWindow(startTime, fastHours) {
    const [h, m] = startTime.split(':').map(Number);
    const endMin = (h * 60 + m + fastHours * 60) % (24 * 60);
    const endH = Math.floor(endMin / 60);
    const endM = endMin % 60;
    return {
      eatStart: startTime,
      eatEnd: `${String(endH).padStart(2,'0')}:${String(endM).padStart(2,'0')}`,
      fastHours,
      eatingWindow: 24 - fastHours
    };
  },

  recipScale(original, servings, targetServings) {
    return original * (targetServings / servings);
  },

  /* ------------------------------------------
     BUSINESS CALCULATORS
  ------------------------------------------ */

  ecommerceProfit(sellPrice, costPrice, platformFee, shippingCost) {
    const revenue = sellPrice;
    const platformFeeAmt = (sellPrice * platformFee) / 100;
    const totalCost = costPrice + platformFeeAmt + shippingCost;
    const profit = revenue - totalCost;
    const margin = (profit / revenue) * 100;
    return { profit, margin, totalCost, platformFeeAmt };
  },

  freelancerRate(annualSalary, hoursPerWeek = 40, weeks = 50, overhead = 30) {
    const targetRevenue = annualSalary * (1 + overhead / 100);
    const billableHours = hoursPerWeek * weeks * 0.75;
    const hourlyRate = targetRevenue / billableHours;
    return { hourlyRate, dailyRate: hourlyRate * 8, monthlyRate: targetRevenue / 12 };
  },

  /* ------------------------------------------
     TECH CALCULATORS
  ------------------------------------------ */

  hexToRgb(hex) {
    const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? { r: parseInt(result[1],16), g: parseInt(result[2],16), b: parseInt(result[3],16) } : null;
  },

  rgbToHex(r, g, b) {
    return '#' + [r, g, b].map(x => x.toString(16).padStart(2, '0')).join('');
  },

  bandwidthCalc(fileSize, speed) {
    const seconds = fileSize / speed;
    return { seconds, minutes: seconds / 60, hours: seconds / 3600 };
  },

  aspectRatio(w, h) {
    const g = this.gcd(w, h);
    return { ratio: `${w/g}:${h/g}`, decimal: w/h };
  },

  passwordStrength(password) {
    let score = 0;
    const checks = {
      length: password.length >= 8,
      longLength: password.length >= 12,
      uppercase: /[A-Z]/.test(password),
      lowercase: /[a-z]/.test(password),
      numbers: /[0-9]/.test(password),
      symbols: /[^A-Za-z0-9]/.test(password)
    };
    score = Object.values(checks).filter(Boolean).length;
    const levels = ['', 'Very Weak', 'Weak', 'Fair', 'Strong', 'Very Strong', 'Excellent'];
    return { score, level: levels[score] || 'Excellent', checks };
  },

  decimalToBinary(n) { return n.toString(2); },
  binaryToDecimal(b) { return parseInt(b, 2); },
  decimalToHex(n) { return n.toString(16).toUpperCase(); },
  hexToDecimal(h) { return parseInt(h, 16); },
};

// Expose globally
window.CalcEngine = CalcEngine;
