'use strict';

const fs = require('fs');
const path = require('path');
const assert = require('assert');
const engine = require('../assets/fortune-engine-20260830.js');

const ROOT = path.resolve(__dirname, '..');
const readJson = relative => JSON.parse(fs.readFileSync(path.join(ROOT, relative), 'utf8'));
const source = readJson('Mykyu-system_TOJEONG_100_FINAL.json');
const manifest = readJson('data/en/manifest.json');
const calculation = { solar_to_lunar: {}, lunar_to_solar: {}, month_days: {} };

for (const file of manifest.calendarFiles) {
  const part = readJson('data/en/' + file);
  Object.assign(calculation.solar_to_lunar, part.solarToLunar || {});
  Object.assign(calculation.lunar_to_solar, part.lunarToSolar || {});
  Object.assign(calculation.month_days, part.monthDays || {});
}

const krStem = ['갑', '을', '병', '정', '무', '기', '경', '신', '임', '계'];
const krBranch = ['자', '축', '인', '묘', '진', '사', '오', '미', '신', '유', '술', '해'];
const enToKr = new Map(Array.from({ length: 60 }, (_, i) => [engine.CYCLE[i], krStem[i % 10] + krBranch[i % 12]]));

let dayChecks = 0;
for (const [solar, lunar] of Object.entries(source.calculation.solar_to_lunar)) {
  const [year, month, day] = solar.split('-').map(Number);
  assert.strictEqual(enToKr.get(engine.dayGanji(year, month, day)), lunar.dayGanji, 'Day pillar mismatch at ' + solar);
  dayChecks += 1;
}

for (const sample of source.calculation.validation_examples || []) {
  const [birthYear, birthMonth, birthDay] = sample.birth_lunar;
  const result = engine.calculateReading({
    targetYear: sample.target,
    birth: { y: birthYear, m: birthMonth, d: birthDay, leap: false },
    calculation,
    cycleReference: manifest.cycleReference
  });
  assert.strictEqual(result.code.replaceAll('-', ''), sample.expected_gua, 'Official sample mismatch');
}

const expectedBranches = ['Yin', 'Mao', 'Chen', 'Si', 'Wu', 'Wei', 'Shen', 'You', 'Xu', 'Hai', 'Zi', 'Chou'];
for (let month = 1; month <= 12; month += 1) {
  assert.strictEqual(engine.monthGanji(2026, month).split('-')[1], expectedBranches[month - 1], 'Month branch mismatch');
}

const codes = new Set();
let birthChecks = 0;
let adjustedBirthdays = 0;
for (const [solar, lunar] of Object.entries(calculation.solar_to_lunar)) {
  if (Number(solar.slice(0, 4)) > 2026) continue;
  const result = engine.calculateReading({
    targetYear: 2026,
    birth: { y: Number(lunar.y), m: Number(lunar.m), d: Number(lunar.d), leap: Boolean(lunar.leap) },
    calculation,
    cycleReference: manifest.cycleReference
  });
  assert.match(result.code, /^[1-8]-[1-6]-[1-3]$/, 'Invalid 144-reading code');
  codes.add(result.code);
  adjustedBirthdays += result.targetBirthday.adjusted ? 1 : 0;
  birthChecks += 1;
}

assert.strictEqual(codes.size, 144, 'Not all 144 readings are reachable');
assert.strictEqual(adjustedBirthdays, 327, 'Unexpected missing-day adjustment count');
assert.throws(() => engine.calculateReading({
  targetYear: 2026,
  birth: { y: 2027, m: 1, d: 1, leap: false },
  calculation,
  cycleReference: manifest.cycleReference
}), /Birth year/);

const report = {
  status: 'PASS',
  officialExamples: (source.calculation.validation_examples || []).length,
  dayPillarChecks: dayChecks,
  targetYearBirthChecks: birthChecks,
  adjustedDay30Birthdays: adjustedBirthdays,
  reachableReadings: codes.size
};

process.stdout.write(JSON.stringify(report, null, 2) + '\n');
