const test = require('node:test');
const assert = require('node:assert/strict');
const path = require('path');
const { loadConfig } = require('../src/task-loader');
const { runPipeline } = require('../src/runner');

test('timeout pipeline should fail', async () => {
  const configPath = path.join(__dirname, '..', 'fixtures', 'pipelines', 'timeout.json');
  const config = loadConfig(configPath);
  const result = await runPipeline(config, path.dirname(configPath));
  assert.equal(result.slow.state, 'failed');
});
