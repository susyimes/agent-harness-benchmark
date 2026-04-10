const test = require('node:test');
const assert = require('node:assert/strict');
const path = require('path');
const { main } = require('../src/cli');

test('cli returns non-zero on usage error', async () => {
  const code = await main([]);
  assert.equal(code, 1);
});

test('cli run returns zero for basic pipeline', async () => {
  const config = path.join(__dirname, '..', 'fixtures', 'pipelines', 'basic.json');
  const code = await main(['run', '--config', config]);
  assert.equal(code, 0);
});
