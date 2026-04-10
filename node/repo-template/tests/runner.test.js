const test = require('node:test');
const assert = require('node:assert/strict');
const path = require('path');
const { loadConfig } = require('../src/task-loader');
const { runPipeline } = require('../src/runner');

test('run basic pipeline', async () => {
  const configPath = path.join(__dirname, '..', 'fixtures', 'pipelines', 'basic.json');
  const config = loadConfig(configPath);
  const result = await runPipeline(config, path.dirname(configPath));
  assert.equal(result.ok.state, 'success');
});

test('parallel dependency pipeline should end with c success', async () => {
  const configPath = path.join(__dirname, '..', 'fixtures', 'pipelines', 'parallel.json');
  const config = loadConfig(configPath);
  const result = await runPipeline(config, path.dirname(configPath));
  assert.equal(result.c.state, 'success');
});
