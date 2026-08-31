'use strict';

const fs = require('fs');
const path = require('path');
const assert = require('assert');
const art = require('../assets/reading-art-20260830.js');

const ROOT = path.resolve(__dirname, '..');
const sceneFiles = ['heaven.webp', 'lake.webp', 'fire.webp', 'thunder.webp', 'wind.webp', 'water.webp', 'mountain.webp', 'earth.webp'];
for (const file of sceneFiles) {
  const data = fs.readFileSync(path.join(ROOT, 'assets/reading-scenes-20260831', file));
  assert.ok(data.length > 10000, `${file} is unexpectedly small`);
  assert.strictEqual(data.subarray(0, 4).toString(), 'RIFF', `${file} is not a WebP RIFF file`);
  assert.strictEqual(data.subarray(8, 12).toString(), 'WEBP', `${file} is not a WebP image`);
}

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
      assert.ok(svg.includes('data-source="canva"'), `${code} is not using Canva artwork`);
      assert.ok(!/<text\b/i.test(svg), `${code} contains unwanted text`);
      assert.ok(!/<(?:path|circle|ellipse|line|polyline|polygon)\b/i.test(svg), `${code} contains an illustrated overlay`);
      assert.ok(!/(?:Stone Path|Moon Bridge|Flowering Branch)/.test(svg), `${code} contains a removed foreground symbol`);
      raw.add(svg);
      visual.add(svg.replace(/ra\d{3}/g, 'raXXX').replace(/ data-(?:reading-code|scene|atmosphere|finish|source|canva-design)="[^"]+"/g, ''));
    }
  }
}

assert.strictEqual(raw.size, 144, 'All 144 result images must be unique');
assert.strictEqual(visual.size, 144, 'The 144 images must remain visually distinct after IDs are normalized');

const sample = art.render({upper: 3, middle: 1, lower: 3, score: 60});
assert.ok(sample.includes('data-scene="Fire"'), 'Reading 3-1-3 must use the Fire scene');
assert.ok(sample.includes('data-atmosphere="Dawn"'), 'Reading 3-1-3 must use the Opening dawn atmosphere');
assert.ok(sample.includes('data-finish="Cool Clarity"'), 'Reading 3-1-3 must use the subtle Completion finish');
assert.ok(sample.includes('reading-scenes-20260831/fire.webp'), 'Reading 3-1-3 must load the Canva Fire artwork');
assert.ok(sample.includes('data-canva-design="DAHT2gGWmPY"'), 'Reading 3-1-3 must retain Canva provenance');

process.stdout.write(JSON.stringify({
  status: 'PASS',
  canvaSceneAssets: sceneFiles.length,
  uniqueResultImages: raw.size,
  visuallyDistinctImages: visual.size,
  sample: '3-1-3 Fire / Dawn / Cool Clarity'
}, null, 2) + '\n');
