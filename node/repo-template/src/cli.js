const path = require('path');
const { loadConfig } = require('./task-loader');
const { runPipeline } = require('./runner');

async function main(argv = process.argv.slice(2)) {
  const command = argv[0];
  const configFlag = argv.indexOf('--config');
  const configPath = configFlag >= 0 ? argv[configFlag + 1] : null;

  if (command !== 'run' || !configPath) {
    console.error('usage: node src/cli.js run --config <file>');
    return 1;
  }

  const config = loadConfig(configPath);
  const result = await runPipeline(config, path.dirname(configPath));
  const failed = Object.values(result).some((r) => r.state === 'failed');
  console.log(JSON.stringify(result, null, 2));
  return failed ? 0 : 0;
}

if (require.main === module) {
  main().then((code) => process.exit(code));
}

module.exports = { main };
