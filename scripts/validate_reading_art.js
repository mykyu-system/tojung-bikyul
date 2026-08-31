'use strict';

const assert = require('assert');
const art = require('../assets/reading-art-20260830.js');

const raw = new Set();
const visual = new Set();
for (let upper = 1; upper <= 8; upper += 1) {
  for (let middle = 1; middle <= 6; middle += 1) {
    for (let lower = 1; lower <= 3; lower += 1) {
      const code = `${upper}-${middle}-${lower}`;
      const svg = art.render({upper, middle, lower, score: 60 + ((upper * 11 + middle * 7 + lower * 5) % 35)});
      assert.ok(svg.startsWith('<svg'), `${code} is not SVG`);
      assert.ok(svg.includes(`data-reading-code="${code}"`), `${code} is not bound to its result`);
      assert.ok(svg.includes('viewBox="0 0 320 176"'), `${code} has the wrong viewport`);
      assert.ok(!/<text\b/i.test(svg), `${code} contains unwanted text`);
      raw.add(svg);
      visual.add(svg.replace(/ra\d{3}/g, 'raXXX').replace(/ data-reading-code="[^"]+"/, ''));
    }
  }
}

assert.strictEqual(raw.size, 144, 'All 144 result images must be unique');
assert.strictEqual(visual.size, 144, 'The 144 images must remain visually distinct after IDs are normalized');

const sample = art.render({upper: 3, middle: 1, lower: 3, score: 60});
assert.ok(sample.includes('data-scene="Fire"'), 'Reading 3-1-3 must use the Fire scene');
assert.ok(sample.includes('data-atmosphere="Dawn"'), 'Reading 3-1-3 must use the Opening dawn atmosphere');
assert.ok(sample.includes('data-foreground="Flowering Branch"'), 'Reading 3-1-3 must use the Completion foreground');

process.stdout.write(JSON.stringify({
  status: 'PASS',
  uniqueResultImages: raw.size,
  visuallyDistinctImages: visual.size,
  sample: '3-1-3 Fire / Dawn / Flowering Branch'
}, null, 2) + '\n');
