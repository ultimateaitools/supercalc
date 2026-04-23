/* ============================================================
   SuperCalc.online - Main JavaScript
   Search | Dark Mode | UI Interactions | Utilities
   ============================================================ */

'use strict';

/* ── All Calculators Data ── */
const ALL_CALCULATORS = [
  { name: "EMI Calculator", url: "emi-calculator.html", icon: "&#127968;", cat: "Finance", desc: "Calculate loan EMI instantly", badge: "hot" },
  { name: "GST Calculator", url: "gst-calculator.html", icon: "&#128202;", cat: "Finance", desc: "Add or remove GST from amount", badge: "hot" },
  { name: "SIP Calculator", url: "sip-calculator.html", icon: "&#128200;", cat: "Finance", desc: "Mutual fund SIP returns", badge: "top" },
  { name: "Income Tax Calculator", url: "income-tax-calculator.html", icon: "&#129534;", cat: "Finance", desc: "Calculate income tax 2025", badge: "hot" },
  { name: "Compound Interest Calculator", url: "compound-interest-calculator.html", icon: "&#128185;", cat: "Finance", desc: "CI with different frequencies", badge: "top" },
  { name: "FD Calculator", url: "fd-calculator.html", icon: "&#127963;", cat: "Finance", desc: "Fixed deposit maturity amount" },
  { name: "RD Calculator", url: "rd-calculator.html", icon: "&#128179;", cat: "Finance", desc: "Recurring deposit calculator" },
  { name: "PPF Calculator", url: "ppf-calculator.html", icon: "&#128274;", cat: "Finance", desc: "Public provident fund returns" },
  { name: "HRA Calculator", url: "hra-calculator.html", icon: "&#127968;", cat: "Finance", desc: "House rent allowance exemption" },
  { name: "Gratuity Calculator", url: "gratuity-calculator.html", icon: "&#127873;", cat: "Finance", desc: "Employee gratuity amount" },
  { name: "NPS Calculator", url: "nps-calculator.html", icon: "&#128116;", cat: "Finance", desc: "National pension scheme returns" },
  { name: "Simple Interest Calculator", url: "simple-interest-calculator.html", icon: "&#128200;", cat: "Finance", desc: "Simple interest calculation" },
  { name: "Salary Calculator", url: "salary-calculator.html", icon: "&#128188;", cat: "Finance", desc: "CTC to in-hand salary", badge: "top" },
  { name: "Loan Eligibility Calculator", url: "loan-eligibility-calculator.html", icon: "&#9989;", cat: "Finance", desc: "Check how much loan you can get" },
  { name: "Car Loan Calculator", url: "car-loan-calculator.html", icon: "&#128663;", cat: "Finance", desc: "Auto loan EMI calculator" },
  { name: "Home Loan Calculator", url: "home-loan-calculator.html", icon: "&#127969;", cat: "Finance", desc: "Home mortgage EMI and interest" },
  { name: "Retirement Calculator", url: "retirement-calculator.html", icon: "&#127796;", cat: "Finance", desc: "Plan your retirement corpus" },
  { name: "Discount Calculator", url: "discount-calculator.html", icon: "&#127991;", cat: "Finance", desc: "Calculate sale price and savings", badge: "hot" },
  { name: "Profit Loss Calculator", url: "profit-loss-calculator.html", icon: "&#128176;", cat: "Finance", desc: "Business profit/loss percentage" },
  { name: "Break Even Calculator", url: "break-even-calculator.html", icon: "&#9878;", cat: "Finance", desc: "Find break-even point" },
  { name: "ROI Calculator", url: "roi-calculator.html", icon: "&#128202;", cat: "Finance", desc: "Return on investment percentage" },
  { name: "Inflation Calculator", url: "inflation-calculator.html", icon: "&#128200;", cat: "Finance", desc: "Future value of money" },
  { name: "Currency Converter", url: "currency-converter.html", icon: "&#128178;", cat: "Finance", desc: "Live currency exchange rates", badge: "new" },
  { name: "Credit Card Calculator", url: "credit-card-calculator.html", icon: "&#128179;", cat: "Finance", desc: "Credit card interest and payoff" },
  { name: "Net Worth Calculator", url: "net-worth-calculator.html", icon: "&#128176;", cat: "Finance", desc: "Assets minus liabilities", badge: "new" },
  { name: "Loan Comparison Calculator", url: "loan-comparison-calculator.html", icon: "&#9878;", cat: "Finance", desc: "Compare two loan offers", badge: "new" },
  { name: "Mutual Fund SIP Calculator", url: "mutual-fund-sip-calculator.html", icon: "&#128200;", cat: "Finance", desc: "SIP returns and target corpus", badge: "new" },
  { name: "Sukanya Samriddhi Calculator", url: "sukanya-samriddhi-calculator.html", icon: "&#128103;", cat: "Finance", desc: "SSY maturity at 8.2% interest", badge: "new" },
  { name: "Tax Calculator 2025", url: "tax-calculator.html", icon: "&#127963;", cat: "Finance", desc: "New vs old regime comparison", badge: "hot" },
  { name: "Solar Panel Calculator", url: "solar-panel-calculator.html", icon: "&#9728;", cat: "Finance", desc: "Solar savings and payback period", badge: "new" },
  { name: "Mortgage Calculator", url: "mortgage-calculator.html", icon: "&#127864;", cat: "Finance", desc: "Global mortgage calculator" },
  { name: "Stock Return Calculator", url: "stock-return-calculator.html", icon: "&#128202;", cat: "Finance", desc: "Calculate stock returns and CAGR" },
  { name: "Dividend Calculator", url: "dividend-calculator.html", icon: "&#128178;", cat: "Finance", desc: "Dividend income estimator" },
  { name: "Capital Gains Calculator", url: "capital-gains-calculator.html", icon: "&#127963;", cat: "Finance", desc: "Short and long term capital gains" },
  { name: "Freelancer Rate Calculator", url: "freelancer-rate-calculator.html", icon: "&#128187;", cat: "Finance", desc: "Hourly/project rate estimator" },
  { name: "Debt Payoff Calculator", url: "debt-payoff-calculator.html", icon: "&#128279;", cat: "Finance", desc: "Pay off debt strategy planner" },
  { name: "Budget Calculator", url: "budget-calculator.html", icon: "&#128200;", cat: "Finance", desc: "Monthly budget planner" },
  { name: "Savings Goal Calculator", url: "savings-goal-calculator.html", icon: "&#127919;", cat: "Finance", desc: "How long to reach savings goal" },
  { name: "Payroll Calculator", url: "payroll-calculator.html", icon: "&#128176;", cat: "Finance", desc: "Employee payroll and tax" },
  { name: "Lease Calculator", url: "lease-calculator.html", icon: "&#128179;", cat: "Finance", desc: "Vehicle lease payment calculator" },
  { name: "Margin Calculator", url: "margin-calculator.html", icon: "&#128200;", cat: "Finance", desc: "Gross and net profit margin" },
  { name: "Markup Calculator", url: "markup-calculator.html", icon: "&#127991;", cat: "Finance", desc: "Product markup percentage" },
  { name: "Investment Calculator", url: "investment-calculator.html", icon: "&#128176;", cat: "Finance", desc: "Future value of investments" },
  { name: "Sales Tax Calculator", url: "sales-tax-calculator.html", icon: "&#129534;", cat: "Finance", desc: "Calculate sales tax amount" },
  { name: "Compound Savings Calculator", url: "compound-savings-calculator.html", icon: "&#128185;", cat: "Finance", desc: "Savings growth with compounding" },
  { name: "Income Tax Estimator", url: "income-tax-estimator.html", icon: "&#129534;", cat: "Finance", desc: "Quick income tax estimate" },
  { name: "Retirement Savings Calculator", url: "retirement-savings-calculator.html", icon: "&#127796;", cat: "Finance", desc: "Retirement corpus planner" },
  { name: "Currency Exchange Calculator", url: "currency-exchange-calculator.html", icon: "&#128178;", cat: "Finance", desc: "Currency exchange with rates" },
  { name: "Bond Yield Calculator", url: "bond-yield-calculator.html", icon: "&#128200;", cat: "Finance", desc: "Bond yield to maturity" },
  { name: "Options Profit Calculator", url: "options-profit-calculator.html", icon: "&#128202;", cat: "Finance", desc: "Options trading profit/loss" },
  { name: "Depreciation Calculator", url: "depreciation-calculator.html", icon: "&#128200;", cat: "Finance", desc: "Asset depreciation methods" },
  { name: "APY Calculator", url: "apy-calculator.html", icon: "&#128185;", cat: "Finance", desc: "Annual percentage yield" },
  { name: "Mortgage Points Calculator", url: "mortgage-points-calculator.html", icon: "&#127968;", cat: "Finance", desc: "Is buying mortgage points worth it" },
  { name: "Down Payment Calculator", url: "down-payment-calculator.html", icon: "&#127968;", cat: "Finance", desc: "Home down payment and PMI" },
  { name: "Tax Bracket Calculator", url: "tax-bracket-calculator.html", icon: "&#129534;", cat: "Finance", desc: "Find your tax bracket" },
  { name: "Loan EMI Calculator", url: "loan-emi-calculator.html", icon: "&#127968;", cat: "Finance", desc: "Detailed EMI breakdown" },
  { name: "Childbirth Cost Calculator", url: "childbirth-cost-calculator.html", icon: "&#128118;", cat: "Finance", desc: "Hospital delivery cost estimate" },
  { name: "College Cost Calculator", url: "college-cost-calculator.html", icon: "&#127891;", cat: "Finance", desc: "Total college cost planner" },
  { name: "Customer LTV Calculator", url: "customer-ltv-calculator.html", icon: "&#128182;", cat: "Finance", desc: "Customer lifetime value" },
  { name: "Employee Cost Calculator", url: "employee-cost-calculator.html", icon: "&#128188;", cat: "Finance", desc: "Total cost of hiring employee" },
  { name: "Invoice Generator Calculator", url: "invoice-generator-calculator.html", icon: "&#128203;", cat: "Finance", desc: "Professional invoice builder", badge: "new" },
  { name: "Rent vs Buy Calculator", url: "rent-vs-buy-calculator.html", icon: "&#127968;", cat: "Finance", desc: "Rent or buy comparison" },
  { name: "Food Cost Calculator", url: "food-cost-calculator.html", icon: "&#127829;", cat: "Finance", desc: "Restaurant food cost percentage" },
  { name: "Net Pay Calculator", url: "net-pay-calculator.html", icon: "&#128176;", cat: "Finance", desc: "Take-home pay after deductions" },
  { name: "Mileage Reimbursement Calculator", url: "mileage-reimbursement-calculator.html", icon: "&#128663;", cat: "Finance", desc: "IRS mileage reimbursement 2025" },
  { name: "Gold Calculator", url: "gold-calculator.html", icon: "&#128081;", cat: "Finance", desc: "Gold price and weight calculator" },
  { name: "Property Tax Calculator", url: "property-tax-calculator.html", icon: "&#127968;", cat: "Finance", desc: "Annual property tax estimate" },
  { name: "Home Affordability Calculator", url: "home-affordability-calculator.html", icon: "&#127969;", cat: "Finance", desc: "How much house can you afford" },
  { name: "Net Promoter Score Calculator", url: "net-promoter-score-calculator.html", icon: "&#128200;", cat: "Finance", desc: "NPS survey score calculator" },
  { name: "GST India Calculator", url: "gst-india-calculator.html", icon: "&#128202;", cat: "Finance", desc: "India GST with all slabs 2025", badge: "hot" },
  { name: "BMI Calculator", url: "bmi-calculator.html", icon: "&#9878;", cat: "Health", desc: "Body mass index check", badge: "hot" },
  { name: "BMR Calculator", url: "bmr-calculator.html", icon: "&#128293;", cat: "Health", desc: "Basal metabolic rate" },
  { name: "Calorie Calculator", url: "calorie-calculator.html", icon: "&#127822;", cat: "Health", desc: "Daily calorie needs TDEE", badge: "top" },
  { name: "Ideal Weight Calculator", url: "ideal-weight-calculator.html", icon: "&#127919;", cat: "Health", desc: "Your ideal body weight" },
  { name: "Body Fat Calculator", url: "body-fat-calculator.html", icon: "&#128208;", cat: "Health", desc: "Estimate body fat percentage" },
  { name: "Protein Calculator", url: "protein-calculator.html", icon: "&#129385;", cat: "Health", desc: "Daily protein intake needs" },
  { name: "Water Intake Calculator", url: "water-intake-calculator.html", icon: "&#128167;", cat: "Health", desc: "Daily water requirements" },
  { name: "Pregnancy Calculator", url: "pregnancy-calculator.html", icon: "&#129354;", cat: "Health", desc: "Due date and week tracker", badge: "top" },
  { name: "Ovulation Calculator", url: "ovulation-calculator.html", icon: "&#128197;", cat: "Health", desc: "Fertile window calculator" },
  { name: "Heart Rate Calculator", url: "heart-rate-calculator.html", icon: "&#10084;", cat: "Health", desc: "Target heart rate zones" },
  { name: "Running Pace Calculator", url: "running-pace-calculator.html", icon: "&#127939;", cat: "Health", desc: "Running pace and finish time" },
  { name: "Macro Calculator", url: "macro-calculator.html", icon: "&#129367;", cat: "Health", desc: "Protein/carbs/fat ratio" },
  { name: "Sleep Calculator", url: "sleep-calculator.html", icon: "&#128564;", cat: "Health", desc: "Best sleep and wake time cycles" },
  { name: "One Rep Max Calculator", url: "one-rep-max-calculator.html", icon: "&#127947;", cat: "Health", desc: "Gym 1RM strength estimator" },
  { name: "Waist Hip Ratio Calculator", url: "waist-hip-ratio-calculator.html", icon: "&#128208;", cat: "Health", desc: "Waist to hip ratio health check" },
  { name: "Blood Pressure Calculator", url: "blood-pressure-calculator.html", icon: "&#129658;", cat: "Health", desc: "BP category and health risk" },
  { name: "Blood Sugar Calculator", url: "blood-sugar-calculator.html", icon: "&#128200;", cat: "Health", desc: "Blood glucose level guide" },
  { name: "Alcohol Unit Calculator", url: "alcohol-unit-calculator.html", icon: "&#127866;", cat: "Health", desc: "Alcohol units in drinks" },
  { name: "Step Counter Calculator", url: "step-counter-calculator.html", icon: "&#128099;", cat: "Health", desc: "Steps to calories and distance", badge: "new" },
  { name: "Life Expectancy Calculator", url: "life-expectancy-calculator.html", icon: "&#128202;", cat: "Health", desc: "Estimate your life expectancy" },
  { name: "VO2 Max Calculator", url: "vo2max-calculator.html", icon: "&#129330;", cat: "Health", desc: "Aerobic fitness level" },
  { name: "Calorie Deficit Calculator", url: "calorie-deficit-calculator.html", icon: "&#128293;", cat: "Health", desc: "Weight loss calorie deficit" },
  { name: "TDEE Calculator", url: "tdee-calculator.html", icon: "&#128293;", cat: "Health", desc: "Total daily energy expenditure" },
  { name: "Baby Weight Calculator", url: "baby-weight-calculator.html", icon: "&#128118;", cat: "Health", desc: "Baby weight percentile" },
  { name: "BMI Kids Calculator", url: "bmi-calculator-kids.html", icon: "&#129303;", cat: "Health", desc: "BMI for children and teens" },
  { name: "BMI Prime Calculator", url: "bmi-prime-calculator.html", icon: "&#9878;", cat: "Health", desc: "BMI prime ratio calculator" },
  { name: "Body Surface Area Calculator", url: "body-surface-area-calculator.html", icon: "&#129315;", cat: "Health", desc: "BSA for medication dosing" },
  { name: "Lean Body Mass Calculator", url: "lean-body-mass-calculator.html", icon: "&#127947;", cat: "Health", desc: "Lean mass and fat free mass" },
  { name: "Army Body Fat Calculator", url: "army-body-fat-calculator.html", icon: "&#127947;", cat: "Health", desc: "US Army body fat standard" },
  { name: "Macronutrient Calculator", url: "macronutrient-calculator.html", icon: "&#129367;", cat: "Health", desc: "Detailed macros breakdown" },
  { name: "Menstrual Cycle Calculator", url: "menstrual-cycle-calculator.html", icon: "&#128197;", cat: "Health", desc: "Period and cycle tracker" },
  { name: "Sleep Cycle Calculator", url: "sleep-cycle-calculator.html", icon: "&#128564;", cat: "Health", desc: "REM sleep cycle planner" },
  { name: "Vitamin Calculator", url: "vitamin-calculator.html", icon: "&#128138;", cat: "Health", desc: "Daily vitamin requirements" },
  { name: "Hydration Calculator", url: "hydration-calculator.html", icon: "&#128167;", cat: "Health", desc: "Workout hydration needs" },
  { name: "BAC Calculator", url: "bac-calculator.html", icon: "&#127866;", cat: "Health", desc: "Blood alcohol content" },
  { name: "Due Date Calculator", url: "due-date-calculator.html", icon: "&#128118;", cat: "Health", desc: "Pregnancy due date from LMP" },
  { name: "Target Heart Rate Calculator", url: "target-heart-rate-calculator.html", icon: "&#10084;", cat: "Health", desc: "Fat burn and cardio zones" },
  { name: "Waist to Height Ratio", url: "waist-to-height-ratio.html", icon: "&#128208;", cat: "Health", desc: "Cardiovascular risk assessment" },
  { name: "Body Adiposity Index", url: "body-adiposity-index.html", icon: "&#9878;", cat: "Health", desc: "Alternative to BMI calculator" },
  { name: "Creatinine Clearance", url: "creatinine-clearance-calculator.html", icon: "&#129658;", cat: "Health", desc: "eGFR kidney function test" },
  { name: "Dose Calculator", url: "dose-calculator.html", icon: "&#128138;", cat: "Health", desc: "Medication dose by weight" },
  { name: "Tip Percentage Calculator", url: "tip-percentage-calculator.html", icon: "&#128176;", cat: "Health", desc: "Restaurant tip calculator" },
  { name: "Swimming Calorie Calculator", url: "swimming-calorie-calculator.html", icon: "&#127940;", cat: "Health", desc: "Calories burned swimming" },
  { name: "Cycling Calorie Calculator", url: "cycling-calorie-calculator.html", icon: "&#128690;", cat: "Health", desc: "Calories burned cycling" },
  { name: "Walking Calorie Calculator", url: "walking-calorie-calculator.html", icon: "&#128099;", cat: "Health", desc: "Calories burned walking" },
  { name: "Yoga Calorie Calculator", url: "yoga-calorie-calculator.html", icon: "&#129340;", cat: "Health", desc: "Calories burned doing yoga" },
  { name: "Body Fat Percentage Calculator", url: "body-fat-percentage-calculator.html", icon: "&#128208;", cat: "Health", desc: "Accurate body fat estimate" },
  { name: "Pace Converter Calculator", url: "pace-converter-calculator.html", icon: "&#127939;", cat: "Health", desc: "Running pace unit converter" },
  { name: "Wind Chill Calculator", url: "wind-chill-calculator.html", icon: "&#127754;", cat: "Health", desc: "Feels-like temperature" },
  { name: "Percentage Calculator", url: "percentage-calculator.html", icon: "&#128290;", cat: "Math", desc: "All types of percentage calculations", badge: "hot" },
  { name: "Age Calculator", url: "age-calculator.html", icon: "&#127874;", cat: "Math", desc: "Exact age in years/months/days", badge: "hot" },
  { name: "Scientific Calculator", url: "scientific-calculator.html", icon: "&#129518;", cat: "Math", desc: "Full scientific calculator", badge: "top" },
  { name: "Fraction Calculator", url: "fraction-calculator.html", icon: "&#189;", cat: "Math", desc: "Add subtract multiply fractions" },
  { name: "Square Root Calculator", url: "square-root-calculator.html", icon: "&#8730;", cat: "Math", desc: "Square and cube root finder" },
  { name: "Exponent Calculator", url: "exponent-calculator.html", icon: "&#120143;", cat: "Math", desc: "Power and exponent calculator" },
  { name: "LCM GCD Calculator", url: "lcm-gcd-calculator.html", icon: "&#128208;", cat: "Math", desc: "Least common multiple and GCD" },
  { name: "Average Calculator", url: "average-calculator.html", icon: "&#128290;", cat: "Math", desc: "Mean median mode calculator" },
  { name: "Statistics Calculator", url: "statistics-calculator.html", icon: "&#128202;", cat: "Math", desc: "Full stats analysis tool" },
  { name: "Quadratic Calculator", url: "quadratic-calculator.html", icon: "&#120143;", cat: "Math", desc: "Quadratic equation solver" },
  { name: "Trigonometry Calculator", url: "trigonometry-calculator.html", icon: "&#128210;", cat: "Math", desc: "Sin cos tan calculator" },
  { name: "Matrix Calculator", url: "matrix-calculator.html", icon: "&#128208;", cat: "Math", desc: "Matrix operations solver" },
  { name: "Logarithm Calculator", url: "logarithm-calculator.html", icon: "&#128290;", cat: "Math", desc: "Log and natural log calculator" },
  { name: "Factorial Calculator", url: "factorial-calculator.html", icon: "&#128290;", cat: "Math", desc: "Factorial and permutations" },
  { name: "Prime Number Calculator", url: "prime-number-calculator.html", icon: "&#128290;", cat: "Math", desc: "Check if a number is prime" },
  { name: "Random Number Generator", url: "random-number-generator.html", icon: "&#127922;", cat: "Math", desc: "Generate random numbers" },
  { name: "Binary Calculator", url: "binary-calculator.html", icon: "&#128187;", cat: "Math", desc: "Binary/hex/octal converter" },
  { name: "Standard Deviation Calculator", url: "standard-deviation-calculator.html", icon: "&#128202;", cat: "Math", desc: "Population and sample SD" },
  { name: "Half Life Calculator", url: "half-life-calculator.html", icon: "&#9762;", cat: "Math", desc: "Radioactive half-life decay" },
  { name: "Molarity Calculator", url: "molarity-calculator.html", icon: "&#9879;", cat: "Math", desc: "Solution concentration moles" },
  { name: "Density Calculator", url: "density-calculator.html", icon: "&#128208;", cat: "Math", desc: "Mass volume density formula" },
  { name: "Acceleration Calculator", url: "acceleration-calculator.html", icon: "&#127939;", cat: "Math", desc: "Newton motion equations" },
  { name: "Kinetic Energy Calculator", url: "kinetic-energy-calculator.html", icon: "&#9889;", cat: "Math", desc: "Kinetic energy from mass speed" },
  { name: "Ohms Law Calculator", url: "ohms-law-calculator.html", icon: "&#9889;", cat: "Math", desc: "Voltage current resistance" },
  { name: "Ohms Law Advanced", url: "ohms-law-advanced-calculator.html", icon: "&#9889;", cat: "Math", desc: "Advanced circuit calculations" },
  { name: "pH Calculator", url: "ph-calculator.html", icon: "&#9879;", cat: "Math", desc: "Acid base pH level" },
  { name: "Wavelength Frequency Calculator", url: "wavelength-frequency-calculator.html", icon: "&#127754;", cat: "Math", desc: "Wave physics calculator" },
  { name: "Number Base Converter", url: "number-base-converter.html", icon: "&#128187;", cat: "Math", desc: "Binary decimal hex octal" },
  { name: "Roman Numeral Converter", url: "roman-numeral-converter.html", icon: "&#128210;", cat: "Math", desc: "Roman numerals converter" },
  { name: "Number to Words Converter", url: "number-to-words-converter.html", icon: "&#128290;", cat: "Math", desc: "Numbers spelled in words" },
  { name: "Number System Calculator", url: "number-system-calculator.html", icon: "&#128187;", cat: "Math", desc: "Multi-base number system" },
  { name: "Specific Gravity Calculator", url: "specific-gravity-calculator.html", icon: "&#9879;", cat: "Math", desc: "Density and API gravity" },
  { name: "Z-Score Calculator", url: "z-score-calculator.html", icon: "&#128202;", cat: "Math", desc: "Normal distribution z-score" },
  { name: "Pipe Flow Calculator", url: "pipe-flow-calculator.html", icon: "&#128200;", cat: "Math", desc: "Fluid flow rate and pressure" },
  { name: "Unit Converter", url: "unit-converter.html", icon: "&#128208;", cat: "Convert", desc: "All units in one place", badge: "hot" },
  { name: "Length Converter", url: "length-converter.html", icon: "&#128208;", cat: "Convert", desc: "Meters feet inches miles" },
  { name: "Weight Converter", url: "weight-converter.html", icon: "&#9878;", cat: "Convert", desc: "Kg pounds stone converter" },
  { name: "Temperature Converter", url: "temperature-converter.html", icon: "&#127777;", cat: "Convert", desc: "Celsius Fahrenheit Kelvin", badge: "top" },
  { name: "Speed Converter", url: "speed-converter.html", icon: "&#128663;", cat: "Convert", desc: "Km/h mph m/s converter" },
  { name: "Volume Calculator", url: "volume-calculator.html", icon: "&#128208;", cat: "Convert", desc: "Volume of any 3D shape" },
  { name: "Area Calculator", url: "area-calculator.html", icon: "&#128208;", cat: "Convert", desc: "Area of any 2D shape" },
  { name: "Pressure Converter", url: "pressure-converter.html", icon: "&#127754;", cat: "Convert", desc: "PSI bar pascal converter" },
  { name: "Energy Converter", url: "energy-converter.html", icon: "&#9889;", cat: "Convert", desc: "Joules calories kWh converter" },
  { name: "Data Converter", url: "data-converter.html", icon: "&#128187;", cat: "Convert", desc: "Bytes KB MB GB TB converter" },
  { name: "Digital Storage Converter", url: "digital-storage-converter.html", icon: "&#128187;", cat: "Convert", desc: "Digital storage units" },
  { name: "Time Unit Converter", url: "time-unit-converter.html", icon: "&#128336;", cat: "Convert", desc: "Seconds minutes hours days" },
  { name: "Angle Converter", url: "angle-converter.html", icon: "&#128208;", cat: "Convert", desc: "Degrees radians gradians" },
  { name: "Speed Distance Time Calculator", url: "speed-distance-time-calculator.html", icon: "&#128663;", cat: "Convert", desc: "Speed distance time formula" },
  { name: "Force Converter", url: "force-converter.html", icon: "&#9889;", cat: "Convert", desc: "Newton pound-force converter" },
  { name: "Power Unit Converter", url: "power-unit-converter.html", icon: "&#9889;", cat: "Convert", desc: "Watts HP BTU converter" },
  { name: "Cooking Converter", url: "cooking-converter.html", icon: "&#127859;", cat: "Convert", desc: "Cups tablespoons ml oz" },
  { name: "Currency Inflation Calculator", url: "currency-inflation-calculator.html", icon: "&#128178;", cat: "Convert", desc: "Inflation adjusted value" },
  { name: "Date Calculator", url: "date-calculator.html", icon: "&#128197;", cat: "DateTime", desc: "Days between two dates", badge: "hot" },
  { name: "Age Difference Calculator", url: "age-difference-calculator.html", icon: "&#127874;", cat: "DateTime", desc: "Age gap between two people" },
  { name: "Add Days Calculator", url: "add-days-calculator.html", icon: "&#128197;", cat: "DateTime", desc: "Add or subtract days from date" },
  { name: "Days Until Calculator", url: "days-until-calculator.html", icon: "&#128197;", cat: "DateTime", desc: "How many days until event" },
  { name: "Working Days Calculator", url: "working-days-calculator.html", icon: "&#128197;", cat: "DateTime", desc: "Business days between dates" },
  { name: "Time Between Dates Calculator", url: "time-between-dates-calculator.html", icon: "&#128336;", cat: "DateTime", desc: "Exact time gap calculator" },
  { name: "Time Zone Converter", url: "time-zone-converter.html", icon: "&#127760;", cat: "DateTime", desc: "World clock converter" },
  { name: "Countdown Calculator", url: "countdown-calculator.html", icon: "&#128197;", cat: "DateTime", desc: "Countdown to any event" },
  { name: "Anniversary Calculator", url: "anniversary-calculator.html", icon: "&#128140;", cat: "DateTime", desc: "Next anniversary date finder" },
  { name: "Week Number Calculator", url: "week-number-calculator.html", icon: "&#128197;", cat: "DateTime", desc: "What week of year is it" },
  { name: "Birth Year Calculator", url: "birth-year-calculator.html", icon: "&#127874;", cat: "DateTime", desc: "Year of birth from age" },
  { name: "Age on Planet Calculator", url: "age-on-planet-calculator.html", icon: "&#127988;", cat: "DateTime", desc: "Your age on other planets" },
  { name: "Pet Age Calculator", url: "pet-age-calculator.html", icon: "&#128049;", cat: "DateTime", desc: "Dog and cat age in human years" },
  { name: "Grade Calculator", url: "grade-calculator.html", icon: "&#127891;", cat: "Education", desc: "Final grade calculator", badge: "hot" },
  { name: "GPA Calculator", url: "gpa-calculator.html", icon: "&#127891;", cat: "Education", desc: "Semester and cumulative GPA", badge: "top" },
  { name: "Percentage Calculator", url: "percentage-off-calculator.html", icon: "&#128290;", cat: "Education", desc: "Percentage off and increase" },
  { name: "CGPA to Percentage", url: "cgpa-to-percentage-calculator.html", icon: "&#127891;", cat: "Education", desc: "CGPA to marks percentage" },
  { name: "GPA to Percentage", url: "gpa-to-percentage.html", icon: "&#127891;", cat: "Education", desc: "GPA to percentage conversion" },
  { name: "GPA College Calculator", url: "gpa-calculator-college.html", icon: "&#127891;", cat: "Education", desc: "US college GPA calculator" },
  { name: "Exam Score Calculator", url: "exam-score-calculator.html", icon: "&#128221;", cat: "Education", desc: "Exam marks percentage" },
  { name: "Study Hours Calculator", url: "study-hours-calculator.html", icon: "&#128218;", cat: "Education", desc: "Study time planner" },
  { name: "Reading Time Calculator", url: "reading-time-calculator.html", icon: "&#128218;", cat: "Education", desc: "How long to read a book" },
  { name: "Word Count Calculator", url: "word-count-calculator.html", icon: "&#128221;", cat: "Education", desc: "Words characters pages" },
  { name: "Percentage Change Calculator", url: "percentage-change-calculator.html", icon: "&#128290;", cat: "Education", desc: "Increase decrease percentage" },
  { name: "Square Footage Calculator", url: "square-footage-calculator.html", icon: "&#127968;", cat: "Home", desc: "Room and floor sq ft", badge: "hot" },
  { name: "Tile Calculator", url: "tile-calculator.html", icon: "&#127968;", cat: "Home", desc: "Tiles needed for floor/wall" },
  { name: "Paint Calculator", url: "paint-calculator.html", icon: "&#127912;", cat: "Home", desc: "Paint needed for room" },
  { name: "Concrete Calculator", url: "concrete-calculator.html", icon: "&#127959;", cat: "Home", desc: "Concrete volume and bags" },
  { name: "Brick Wall Calculator", url: "brick-wall-calculator.html", icon: "&#127959;", cat: "Home", desc: "Bricks needed for wall" },
  { name: "Flooring Calculator", url: "flooring-calculator.html", icon: "&#127968;", cat: "Home", desc: "Flooring material quantity" },
  { name: "Roof Pitch Calculator", url: "roof-pitch-calculator.html", icon: "&#127968;", cat: "Home", desc: "Roof angle and slope" },
  { name: "Stair Calculator", url: "stair-calculator.html", icon: "&#127968;", cat: "Home", desc: "Stair rise run dimensions" },
  { name: "Fence Calculator", url: "fence-calculator.html", icon: "&#127968;", cat: "Home", desc: "Fencing material estimate" },
  { name: "Mulch Calculator", url: "mulch-calculator.html", icon: "&#127807;", cat: "Home", desc: "Garden mulch quantity" },
  { name: "Gravel Calculator", url: "gravel-calculator.html", icon: "&#127959;", cat: "Home", desc: "Gravel and stone estimate" },
  { name: "Drywall Calculator", url: "drywall-calculator.html", icon: "&#127968;", cat: "Home", desc: "Drywall sheets needed" },
  { name: "Concrete Volume Calculator", url: "concrete-volume-calculator.html", icon: "&#127959;", cat: "Home", desc: "Concrete pour calculator" },
  { name: "Aspect Ratio Calculator", url: "aspect-ratio-calculator.html", icon: "&#128208;", cat: "Home", desc: "Screen aspect ratio" },
  { name: "Land Area Calculator", url: "land-area-calculator.html", icon: "&#127968;", cat: "Home", desc: "Land area in acres and sqft" },
  { name: "Paint Coverage Calculator", url: "paint-coverage-calculator.html", icon: "&#127912;", cat: "Home", desc: "Paint gallons coverage" },
  { name: "Paint Cost Calculator", url: "paint-cost-calculator.html", icon: "&#127912;", cat: "Home", desc: "Total painting project cost" },
  { name: "Electricity Usage Calculator", url: "electricity-usage-calculator.html", icon: "&#9889;", cat: "Home", desc: "Appliance power consumption" },
  { name: "Electricity Bill Calculator", url: "electricity-bill-calculator.html", icon: "&#9889;", cat: "Home", desc: "Monthly electricity cost" },
  { name: "Electricity Unit Calculator", url: "electricity-unit-calculator.html", icon: "&#9889;", cat: "Home", desc: "kWh unit calculation" },
  { name: "Electricity Saving Calculator", url: "electricity-saving-calculator.html", icon: "&#9889;", cat: "Home", desc: "LED and appliance savings" },
  { name: "Solar Power Calculator", url: "solar-power-calculator.html", icon: "&#9728;", cat: "Home", desc: "Solar panel output kWh" },
  { name: "Solar Savings Calculator", url: "solar-savings-calculator.html", icon: "&#9728;", cat: "Home", desc: "Solar panel ROI and payback" },
  { name: "Random Password Generator", url: "random-password-generator.html", icon: "&#128274;", cat: "Tech", desc: "Secure password creator", badge: "hot" },
  { name: "IP Subnet Calculator", url: "ip-subnet-calculator.html", icon: "&#127760;", cat: "Tech", desc: "Network subnet mask calculator" },
  { name: "Bandwidth Calculator", url: "bandwidth-calculator.html", icon: "&#128187;", cat: "Tech", desc: "Network bandwidth estimator" },
  { name: "Download Time Calculator", url: "download-time-calculator.html", icon: "&#128190;", cat: "Tech", desc: "File download time estimator" },
  { name: "Color Code Converter", url: "color-code-converter.html", icon: "&#127912;", cat: "Tech", desc: "HEX RGB HSL color codes" },
  { name: "Pixel Density Calculator", url: "pixel-density-calculator.html", icon: "&#128248;", cat: "Tech", desc: "Screen PPI and DPI" },
  { name: "Aspect Ratio Calculator (Screen)", url: "aspect-ratio-calculator.html", icon: "&#128249;", cat: "Tech", desc: "Monitor aspect ratio" },
  { name: "Hash Value Calculator", url: "hash-value-calculator.html", icon: "&#128274;", cat: "Tech", desc: "MD5 SHA hash generator" },
  { name: "Fuel Cost Calculator", url: "fuel-cost-calculator.html", icon: "&#9981;", cat: "Travel", desc: "Road trip fuel cost", badge: "hot" },
  { name: "Fuel Efficiency Calculator", url: "fuel-efficiency-calculator.html", icon: "&#128663;", cat: "Travel", desc: "MPG and km/L converter" },
  { name: "Flight Time Calculator", url: "flight-time-calculator.html", icon: "&#9992;", cat: "Travel", desc: "Flight hours and distance" },
  { name: "Travel Budget Calculator", url: "travel-budget-calculator.html", icon: "&#9992;", cat: "Travel", desc: "Trip cost planner" },
  { name: "Carbon Footprint Calculator", url: "carbon-footprint-calculator.html", icon: "&#127807;", cat: "Travel", desc: "CO2 emissions calculator", badge: "new" },
  { name: "Water Footprint Calculator", url: "water-footprint-calculator.html", icon: "&#128167;", cat: "Travel", desc: "Personal water usage" },
  { name: "Horsepower Calculator", url: "horsepower-calculator.html", icon: "&#128663;", cat: "Travel", desc: "Engine horsepower formula" },
  { name: "Engine Displacement Calculator", url: "engine-displacement-calculator.html", icon: "&#128663;", cat: "Travel", desc: "Engine CC and displacement" },
  { name: "Nautical Mile Calculator", url: "nautical-mile-calculator.html", icon: "&#9875;", cat: "Travel", desc: "Sea distance and knots" },
  { name: "Tip Calculator", url: "tip-calculator.html", icon: "&#128176;", cat: "Travel", desc: "Restaurant tip splitter", badge: "hot" },
  { name: "Tip Calculator UK", url: "tip-calculator-uk.html", icon: "&#128176;", cat: "Travel", desc: "UK gratuity calculator" },
  { name: "Bill Split Calculator", url: "bill-split-calculator.html", icon: "&#128176;", cat: "Travel", desc: "Split restaurant bill easily" },
  { name: "Love Calculator", url: "love-calculator.html", icon: "&#10084;", cat: "Fun", desc: "Love compatibility percentage", badge: "hot" },
  { name: "Love Compatibility Calculator", url: "love-compatibility-calculator.html", icon: "&#10084;", cat: "Fun", desc: "Zodiac love match score" },
  { name: "Lucky Number Calculator", url: "lucky-number-calculator.html", icon: "&#127922;", cat: "Fun", desc: "Numerology lucky number" },
  { name: "Name Value Calculator", url: "name-value-calculator.html", icon: "&#128290;", cat: "Fun", desc: "Numerology name value" },
  { name: "Zodiac Sign Calculator", url: "zodiac-sign-calculator.html", icon: "&#11088;", cat: "Fun", desc: "Find your zodiac sign" },
  { name: "Age on Planet Calculator", url: "age-on-planet-calculator.html", icon: "&#127988;", cat: "Fun", desc: "Your age on Mars Saturn" },
  { name: "Random Number Generator", url: "random-number-generator.html", icon: "&#127922;", cat: "Fun", desc: "Generate lucky numbers" },
  { name: "Recipe Scaling Calculator", url: "recipe-scaling-calculator.html", icon: "&#127859;", cat: "Fun", desc: "Scale recipe up or down" },
  { name: "Horsepower Calculator", url: "horsepower-calculator.html", icon: "&#128663;", cat: "Fun", desc: "Car horsepower estimator" },
  { name: "Tide Calculator", url: "tide-calculator.html", icon: "&#127754;", cat: "Fun", desc: "Ocean tide predictor" },
  { name: "Power Consumption Calculator", url: "power-consumption-calculator.html", icon: "&#9889;", cat: "Other", desc: "Device watt-hour cost" },
  { name: "Minutes to Hours Calculator", url: "minutes-to-hours-calculator.html", icon: "&#128336;", cat: "Other", desc: "Time conversion calculator" },
  { name: "Percentage Off Calculator", url: "percentage-off-calculator.html", icon: "&#127991;", cat: "Other", desc: "Discount amount calculator" },
  { name: "Z Score Calculator", url: "z-score-calculator.html", icon: "&#128202;", cat: "Other", desc: "Statistics z-score tool" },

  // Social Media - Instagram
  { name: "Instagram Engagement Rate Calculator", url: "instagram-engagement-rate-calculator.html", icon: "&#128247;", cat: "Social", desc: "Calculate your IG engagement rate", badge: "hot" },
  { name: "Instagram Engagement Per Post", url: "instagram-engagement-per-post-calculator.html", icon: "&#128247;", cat: "Social", desc: "Avg engagement per Instagram post" },
  { name: "Instagram Reach Rate Calculator", url: "instagram-reach-rate-calculator.html", icon: "&#128247;", cat: "Social", desc: "What % of followers see your posts" },
  { name: "Instagram Growth Rate Calculator", url: "instagram-growth-rate-calculator.html", icon: "&#128200;", cat: "Social", desc: "Track Instagram follower growth", badge: "new" },
  { name: "Instagram Influencer Earnings", url: "instagram-influencer-earnings-calculator.html", icon: "&#128176;", cat: "Social", desc: "Estimate Instagram sponsored post rate", badge: "hot" },
  { name: "Instagram Reels Earnings", url: "instagram-reels-earnings-calculator.html", icon: "&#127909;", cat: "Social", desc: "Reels monetization estimator", badge: "new" },

  // Social Media - YouTube
  { name: "YouTube Engagement Rate Calculator", url: "youtube-engagement-rate-calculator.html", icon: "&#127909;", cat: "Social", desc: "YouTube likes/comments vs views" },
  { name: "YouTube Money Calculator", url: "youtube-money-calculator.html", icon: "&#128176;", cat: "Social", desc: "Estimate YouTube channel earnings", badge: "hot" },
  { name: "YouTube CPM Calculator", url: "youtube-cpm-calculator.html", icon: "&#128200;", cat: "Social", desc: "YouTube cost per mille ad rate", badge: "hot" },
  { name: "YouTube RPM Calculator", url: "youtube-rpm-calculator.html", icon: "&#128200;", cat: "Social", desc: "Revenue per 1000 YouTube views", badge: "hot" },
  { name: "YouTube Growth Rate Calculator", url: "youtube-growth-rate-calculator.html", icon: "&#128200;", cat: "Social", desc: "YouTube subscriber growth tracker" },
  { name: "YouTube Shorts Earnings", url: "youtube-shorts-earnings-calculator.html", icon: "&#127909;", cat: "Social", desc: "Shorts monetization estimator", badge: "new" },
  { name: "YouTube Watch Time Calculator", url: "youtube-watch-time-calculator.html", icon: "&#9201;", cat: "Social", desc: "4000 hours monetization tracker" },
  { name: "YouTube Retention Rate Calculator", url: "youtube-retention-rate-calculator.html", icon: "&#128200;", cat: "Social", desc: "Audience retention analysis" },
  { name: "YouTube Channel Growth Projection", url: "youtube-channel-growth-projection-calculator.html", icon: "&#128200;", cat: "Social", desc: "Project subscriber milestones" },
  { name: "Views to Subscribers Ratio", url: "views-to-subscribers-ratio-calculator.html", icon: "&#127909;", cat: "Social", desc: "YouTube subscriber conversion rate" },
  { name: "YouTube Thumbnail CTR Calculator", url: "youtube-thumbnail-ctr-calculator.html", icon: "&#128249;", cat: "Social", desc: "Click-through rate for thumbnails" },

  // Social Media - TikTok
  { name: "TikTok Engagement Rate Calculator", url: "tiktok-engagement-rate-calculator.html", icon: "&#127925;", cat: "Social", desc: "TikTok likes/comments/shares rate", badge: "hot" },
  { name: "TikTok Earnings Calculator", url: "tiktok-earnings-calculator.html", icon: "&#128176;", cat: "Social", desc: "TikTok creator fund income", badge: "hot" },
  { name: "TikTok Virality Score Calculator", url: "tiktok-virality-score-calculator.html", icon: "&#128293;", cat: "Social", desc: "Is your TikTok going viral?" },
  { name: "TikTok Growth Rate Calculator", url: "tiktok-growth-rate-calculator.html", icon: "&#128200;", cat: "Social", desc: "TikTok follower growth tracker" },

  // Social Media - Twitter & LinkedIn
  { name: "Twitter (X) Engagement Rate", url: "twitter-engagement-rate-calculator.html", icon: "&#128038;", cat: "Social", desc: "Tweet engagement rate calculator" },
  { name: "Tweet Engagement Calculator", url: "tweet-engagement-calculator.html", icon: "&#128038;", cat: "Social", desc: "Single tweet metrics analyzer" },
  { name: "Twitter Growth Rate Calculator", url: "twitter-growth-rate-calculator.html", icon: "&#128200;", cat: "Social", desc: "Twitter follower growth tracker" },
  { name: "LinkedIn Engagement Rate", url: "linkedin-engagement-rate-calculator.html", icon: "&#128188;", cat: "Social", desc: "LinkedIn post engagement rate", badge: "hot" },
  { name: "LinkedIn Post Performance", url: "linkedin-post-performance-calculator.html", icon: "&#128202;", cat: "Social", desc: "LinkedIn content performance score" },

  // Creator Economy / Monetization
  { name: "Influencer Earnings Per Post", url: "influencer-earnings-per-post-calculator.html", icon: "&#128176;", cat: "Social", desc: "Sponsored post rate calculator", badge: "hot" },
  { name: "Brand Deal Rate Calculator", url: "brand-deal-rate-calculator.html", icon: "&#129534;", cat: "Social", desc: "Content creator brand deal pricing", badge: "new" },
  { name: "AdSense RPM Calculator", url: "adsense-rpm-calculator.html", icon: "&#128176;", cat: "Social", desc: "Google AdSense earnings estimator", badge: "hot" },
  { name: "Affiliate Earnings Calculator", url: "affiliate-earnings-calculator.html", icon: "&#128200;", cat: "Social", desc: "Affiliate marketing income estimator" },
  { name: "Social Media ROI Calculator", url: "social-media-roi-calculator.html", icon: "&#128200;", cat: "Social", desc: "Marketing ROI and ROAS calculator" },
  { name: "Website Traffic to Revenue", url: "website-traffic-to-revenue-calculator.html", icon: "&#128200;", cat: "Social", desc: "Website monetization estimator" },
  { name: "Follower to Income Calculator", url: "follower-to-income-calculator.html", icon: "&#128176;", cat: "Social", desc: "What your followers are worth" },
  { name: "Micro Influencer Rate Calculator", url: "micro-influencer-rate-calculator.html", icon: "&#128247;", cat: "Social", desc: "Nano and micro influencer pricing" },
  { name: "Virality Score Calculator", url: "virality-score-calculator.html", icon: "&#128293;", cat: "Social", desc: "Social media viral coefficient" },
  { name: "Follower to Engagement Ratio", url: "follower-to-engagement-ratio-calculator.html", icon: "&#128290;", cat: "Social", desc: "Ghost follower detector" },
  { name: "Content Performance Score", url: "content-performance-score-calculator.html", icon: "&#128202;", cat: "Social", desc: "Overall content effectiveness score" },
  { name: "Post Frequency Impact Calculator", url: "post-frequency-impact-calculator.html", icon: "&#128197;", cat: "Social", desc: "Optimal posting frequency finder" },

  // AI & Modern Tools
  { name: "AI Token Cost Calculator", url: "ai-token-cost-calculator.html", icon: "&#129302;", cat: "AI Tools", desc: "ChatGPT, Claude, Gemini API costs", badge: "hot" },
  { name: "API Cost Calculator", url: "api-cost-calculator.html", icon: "&#128187;", cat: "AI Tools", desc: "Monthly API usage cost estimator", badge: "new" },
  { name: "SaaS Pricing Calculator", url: "saas-pricing-calculator.html", icon: "&#128200;", cat: "AI Tools", desc: "MRR, ARR, LTV and churn metrics", badge: "hot" },
  { name: "Content Generation Cost", url: "content-generation-cost-calculator.html", icon: "&#128221;", cat: "AI Tools", desc: "AI vs human writer cost comparison", badge: "new" },
];

/* ── Dark Mode ── */
const themeToggle = document.getElementById('themeToggle');
const themeIcon   = document.getElementById('themeIcon');

function initTheme() {
  const saved = localStorage.getItem('SuperCalc-theme') || 'light';
  applyTheme(saved);
}

function applyTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  if (themeIcon) themeIcon.className = theme === 'dark' ? 'bi bi-sun-fill' : 'bi bi-moon-fill';
  localStorage.setItem('SuperCalc-theme', theme);
}

function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme');
  applyTheme(current === 'dark' ? 'light' : 'dark');
}

if (themeToggle) themeToggle.addEventListener('click', toggleTheme);

/* ── Search ── */
function initSearch() {
  const inputs = document.querySelectorAll('.search-input, .hero-search-input');
  inputs.forEach(input => {
    const dropdown = input.nextElementSibling;
    if (!dropdown) return;

    input.addEventListener('input', () => {
      const q = input.value.trim().toLowerCase();
      if (q.length < 2) { dropdown.classList.remove('show'); return; }

      const results = ALL_CALCULATORS.filter(c =>
        c.name.toLowerCase().includes(q) ||
        c.cat.toLowerCase().includes(q) ||
        c.desc.toLowerCase().includes(q)
      ).slice(0, 8);

      dropdown.innerHTML = results.length
        ? results.map(c => `
            <div class="search-item hero-search-item" onclick="location.href='${c.url}'">
              <span class="calc-icon">${c.icon}</span>
              <div>
                <div class="calc-name">${highlight(c.name, q)}</div>
                <div class="calc-cat">${c.cat} • ${c.desc}</div>
              </div>
            </div>`).join('')
        : `<div class="search-item" style="color:var(--text-muted)">No results for "${q}"</div>`;

      dropdown.classList.add('show');
    });

    document.addEventListener('click', e => {
      if (!input.contains(e.target)) dropdown.classList.remove('show');
    });

    input.addEventListener('keydown', e => {
      if (e.key === 'Escape') { dropdown.classList.remove('show'); input.blur(); }
    });
  });
}

function highlight(text, q) {
  const re = new RegExp(`(${q})`, 'gi');
  return text.replace(re, '<mark style="background:rgba(79,70,229,0.15);color:var(--primary);border-radius:2px;padding:0 2px">$1</mark>');
}

/* ── FAQ Accordion ── */
function initFAQ() {
  document.querySelectorAll('.faq-question').forEach(btn => {
    btn.addEventListener('click', () => {
      const answer = btn.nextElementSibling;
      const isOpen = btn.classList.contains('open');

      document.querySelectorAll('.faq-question.open').forEach(b => {
        b.classList.remove('open');
        b.nextElementSibling.style.maxHeight = null;
      });

      if (!isOpen) {
        btn.classList.add('open');
        answer.style.maxHeight = answer.scrollHeight + 'px';
      }
    });
  });
}

/* ── Copy to Clipboard ── */
function copyResult(text) {
  navigator.clipboard.writeText(text).then(() => showToast('✓ Copied to clipboard!'));
}

/* ── WhatsApp Share ── */
function shareWhatsApp(text) {
  const url = encodeURIComponent(window.location.href);
  const msg = encodeURIComponent(text + '\n\nCalculated at: ' + window.location.href);
  window.open(`https://wa.me/?text=${msg}`, '_blank');
}

/* ── Toast Notification ── */
function showToast(msg, duration = 3000) {
  const container = document.querySelector('.toast-container') || createToastContainer();
  const toast = document.createElement('div');
  toast.className = 'toast-msg';
  toast.textContent = msg;
  container.appendChild(toast);
  setTimeout(() => toast.remove(), duration);
}

function createToastContainer() {
  const el = document.createElement('div');
  el.className = 'toast-container';
  document.body.appendChild(el);
  return el;
}

/* ── Back to Top ── */
function initBackToTop() {
  const btn = document.getElementById('backToTop');
  if (!btn) return;
  window.addEventListener('scroll', () => {
    btn.classList.toggle('show', window.scrollY > 400);
  });
  btn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
}

/* ── Reveal on Scroll ── */
function initReveal() {
  const elements = document.querySelectorAll('.reveal');
  if (!elements.length) return;
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });
  elements.forEach(el => observer.observe(el));
}

/* ── Format Numbers ── */
function formatNum(num, decimals = 2) {
  if (isNaN(num)) return '0';
  return new Intl.NumberFormat('en-IN', {
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals
  }).format(num);
}

function formatCurrency(num, symbol = '₹') {
  return symbol + formatNum(num);
}

function formatCurrencyUS(num) {
  return '$' + formatNum(num);
}

/* ── Print Result ── */
function printResult() {
  window.print();
}

/* ── Active Nav Link ── */
function setActiveNav() {
  const page = location.pathname.split('/').pop();
  document.querySelectorAll('.nav-link').forEach(a => {
    a.classList.toggle('active', a.getAttribute('href') === page);
  });
}

/* ── Category Filter (Homepage) ── */
function initCategoryFilter() {
  const pills = document.querySelectorAll('.cat-pill[data-filter]');
  const sections = document.querySelectorAll('.calc-section[data-cat]');

  pills.forEach(pill => {
    pill.addEventListener('click', () => {
      pills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      const filter = pill.dataset.filter;

      sections.forEach(sec => {
        if (filter === 'all' || sec.dataset.cat === filter) {
          sec.style.display = 'block';
        } else {
          sec.style.display = 'none';
        }
      });
    });
  });
}

/* ── Number Formatting for Inputs ── */
function addCommas(num) {
  return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}

function removeCommas(str) {
  return str.replace(/,/g, '');
}

/* ── Smooth Scroll for Anchor Links ── */
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const target = document.querySelector(a.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

/* ── Init Everything ── */
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initSearch();
  initFAQ();
  initBackToTop();
  initReveal();
  setActiveNav();
  initCategoryFilter();
});

