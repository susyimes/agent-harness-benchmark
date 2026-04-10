const fs = require('fs');
const path = require('path');
const marker = path.join(__dirname, '..', '.flaky-count');
let count = 0;
if (fs.existsSync(marker)) count = Number(fs.readFileSync(marker, 'utf8'));
count += 1;
fs.writeFileSync(marker, String(count));
if (count === 1) {
  console.error('first run fails');
  process.exit(1);
}
process.exit(0);
