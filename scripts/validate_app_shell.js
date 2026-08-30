'use strict';

const fs = require('fs');
const path = require('path');
const assert = require('assert');

const ROOT = path.resolve(__dirname, '..');
const read = relative => fs.readFileSync(path.join(ROOT, relative), 'utf8');
const app = read('english-app7.html');
const wrapper = read('english.html');

assert.ok(app.includes('assets/fortune-engine-20260830.js?v=1'), 'Verified engine is not loaded');
assert.ok(app.includes('ENGINE.calculateReading({targetYear:TARGET_YEAR'), 'UI does not call the verified engine');
assert.ok(!app.includes("BRANCH[m-1]"), 'Old month-branch calculation survived');
assert.ok(app.indexOf('fortune-engine-20260830.js') < app.indexOf("const ENGINE=window.TojungEngine"), 'Engine must load before the app');

const inlineScripts = [...app.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/gi)].map(match => match[1]).filter(Boolean);
assert.ok(inlineScripts.length >= 1, 'No inline application script found');
for (const script of inlineScripts) new Function(script);

assert.ok(wrapper.includes('english-app7.html?v=20260830-verified1'), 'Wrapper cache key was not updated');
for (const file of ['blogger.html', 'blogger-english.html']) {
  assert.ok(read(file).includes('english.html?v=blogger-verified-20260830'), file + ' cache key was not updated');
}
assert.ok(read('blogger-post-final.html').includes('english.html?v=20260830-verified1'), 'Blogger post cache key was not updated');

process.stdout.write(JSON.stringify({
  status: 'PASS',
  inlineScriptsParsed: inlineScripts.length,
  verifiedEngineLinked: true,
  wrapperCacheUpdated: true,
  bloggerRoutesUpdated: 3
}, null, 2) + '\n');
