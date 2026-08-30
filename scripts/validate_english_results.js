'use strict';

const fs = require('fs');
const path = require('path');
const assert = require('assert');

const ROOT = path.resolve(__dirname, '..');
const readJson = relative => JSON.parse(fs.readFileSync(path.join(ROOT, relative), 'utf8'));
const manifest = readJson('data/en/manifest.json');
const readings = manifest.guaFiles.flatMap(file => readJson('data/en/' + file));
const annualFields = ['summary', 'money', 'career', 'relationship', 'health'];
const detailFields = ['investment', 'job_change', 'promotion_exam', 'real_estate', 'document_contract', 'children_family', 'social', 'accident', 'travel_move', 'final'];

assert.strictEqual(manifest.version, '2.0.0-verified');
assert.strictEqual(readings.length, 144);
assert.strictEqual(new Set(readings.map(g => g.code)).size, 144);
assert.ok(new Set(readings.map(g => g.name)).size >= 100, 'Traditional reading names were not preserved');

for (const field of annualFields) {
  assert.strictEqual(new Set(readings.map(g => g[field])).size, 144, field + ' must be unique for every reading');
}
for (const field of detailFields) {
  assert.strictEqual(new Set(readings.map(g => g.detailed[field])).size, 144, 'detailed.' + field + ' must be unique for every reading');
}

const months = readings.flatMap(g => g.months.map(month => ({ ...month, code: g.code })));
assert.strictEqual(months.length, 1728);
for (const field of ['flow', 'money', 'caution']) {
  assert.strictEqual(new Set(months.map(month => month[field])).size, 1728, 'monthly ' + field + ' must be unique');
}
for (const reading of readings) {
  assert.strictEqual(reading.months.length, 12);
  assert.strictEqual(new Set(reading.months.map(month => month.flow)).size, 12);
  assert.strictEqual(new Set(reading.months.map(month => month.money)).size, 12);
  assert.strictEqual(new Set(reading.months.map(month => month.caution)).size, 12);
}

const scoreSequences = new Set(readings.map(g => g.months.map(month => month.score).join(',')));
assert.strictEqual(scoreSequences.size, 144, 'Monthly score sequence must differ for every reading');
assert.ok(months.every(month => month.score >= 48 && month.score <= 96), 'Monthly scores must stay in range');

const serialized = JSON.stringify(readings);
assert.ok(!serialized.includes('This reading emphasizes careful timing'), 'Generic placeholder survived');
assert.ok(!serialized.includes('This area benefits from careful timing'), 'Generic area placeholder survived');
assert.ok(!serialized.includes('Theme"'), 'Generic keyword survived');

const report = {
  status: 'PASS',
  readings: readings.length,
  annualUniquePerField: Object.fromEntries(annualFields.map(field => [field, new Set(readings.map(g => g[field])).size])),
  detailedUniquePerField: Object.fromEntries(detailFields.map(field => [field, new Set(readings.map(g => g.detailed[field])).size])),
  monthlyEntries: months.length,
  monthlyUniquePerField: Object.fromEntries(['flow', 'money', 'caution'].map(field => [field, new Set(months.map(month => month[field])).size])),
  uniqueMonthlyScoreSequences: scoreSequences.size,
  monthlyScoreRange: [Math.min(...months.map(month => month.score)), Math.max(...months.map(month => month.score))],
  genericPlaceholders: 0
};

process.stdout.write(JSON.stringify(report, null, 2) + '\n');
