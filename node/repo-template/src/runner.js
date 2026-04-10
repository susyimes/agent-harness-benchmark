const { spawn } = require('child_process');
const path = require('path');
const { pickReadyTasks } = require('./scheduler');

function runCommand(task, cwd) {
  return new Promise((resolve, reject) => {
    const child = spawn(process.execPath, [task.script], { cwd, stdio: 'pipe' });
    let stderr = '';
    child.stderr.on('data', (d) => {
      stderr += d.toString();
    });
    child.on('error', reject);
    child.on('close', (code) => {
      if (code === 0) resolve({ ok: true });
      else reject(new Error(stderr || `exit ${code}`));
    });
  });
}

async function runPipeline(config, rootDir) {
  const states = {};
  const tasks = config.tasks || [];
  for (let i = 0; i < tasks.length; i++) {
    const ready = pickReadyTasks(tasks, states);
    if (ready.length === 0) break;
    const task = ready[0];
    const cwd = path.resolve(rootDir, task.cwd || '.');
    try {
      await runCommand(task, cwd);
      states[task.id] = { state: 'success', attempts: 1 };
    } catch (err) {
      states[task.id] = { state: 'failed', attempts: 1, error: String(err.message || err) };
    }
  }
  return states;
}

module.exports = { runPipeline };
