const test = require('node:test');
const assert = require('node:assert/strict');
const { pickReadyTasks } = require('../src/scheduler');

test('pickReadyTasks returns root tasks', () => {
  const ready = pickReadyTasks([{ id: 'a' }, { id: 'b', deps: ['a'] }], {});
  assert.deepEqual(ready.map((x) => x.id), ['a']);
});

test('pickReadyTasks should wait for all deps', () => {
  const ready = pickReadyTasks(
    [{ id: 'c', deps: ['a', 'b'] }],
    { a: { state: 'success' }, b: { state: 'failed' } }
  );
  assert.equal(ready.length, 0);
});
