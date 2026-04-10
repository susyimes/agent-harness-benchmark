const test = require('node:test');
const assert = require('node:assert/strict');
const { execFile } = require('node:child_process');
const path = require('path');

test('cli integration basic pipeline', async () => {
  const cli = path.join(__dirname, '..', '..', 'src', 'cli.js');
  const config = path.join(__dirname, '..', '..', 'fixtures', 'pipelines', 'basic.json');
  const { stdout } = await new Promise((resolve, reject) => {
    execFile(process.execPath, [cli, 'run', '--config', config], { cwd: path.join(__dirname, '..', '..') }, (err, stdout, stderr) => {
      if (err) return reject(err);
      resolve({ stdout, stderr });
    });
  });
  const data = JSON.parse(stdout);
  assert.equal(data.ok.state, 'success');
});
