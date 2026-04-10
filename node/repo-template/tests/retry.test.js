const test = require('node:test');
const assert = require('node:assert/strict');
const path = require('path');
const fs = require('fs');
const { loadConfig } = require('../src/task-loader');
const { runPipeline } = require('../src/runner');

test('flaky pipeline should eventually succeed with retries', async () => {
  const marker = path.join(__dirname, '..', 'fixtures', 'workspace', 'project-a', '.flaky-count');
  if (fs.existsSync(marker)) fs.unlinkSync(marker);
  const configPath = path.join(__dirname, '..', 'fixtures', 'pipelines', 'retry.json');
  const config = loadConfig(configPath);
  const result = await runPipeline(config, path.dirname(configPath));
  assert.equal(result.flaky.state, 'success');
});
