
$files = @(
  'index.html','emi-calculator.html','gst-calculator.html','bmi-calculator.html',
  'age-calculator.html','percentage-calculator.html','sip-calculator.html',
  'income-tax-calculator.html','calorie-calculator.html','compound-interest-calculator.html',
  'tip-calculator.html','about.html','privacy.html','terms.html',
  'js\main.js','js\calc-engine.js','manifest.json'
)

$win1252 = [System.Text.Encoding]::GetEncoding(1252)
$utf8 = New-Object System.Text.UTF8Encoding($false) # no BOM

foreach ($f in $files) {
  if (-not (Test-Path $f)) { continue }
  $content = [System.IO.File]::ReadAllText($f, $utf8)
  try {
    $bytes = $win1252.GetBytes($content)
    $fixed = $utf8.GetString($bytes)
    [System.IO.File]::WriteAllText($f, $fixed, $utf8)
    Write-Host "Fixed: $f"
  } catch {
    Write-Host "Skip: $f - $_"
  }
}
Write-Host "Done."
