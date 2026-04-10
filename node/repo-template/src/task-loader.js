const fs = require('fs');

function loadConfig(file) {
  const raw = fs.readFileSync(file, 'utf8');
  return JSON.parse(raw);
}

module.exports = { loadConfig };
