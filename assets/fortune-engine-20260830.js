(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  if (root) root.TojungEngine = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';

  const STEM = ['Jia', 'Yi', 'Bing', 'Ding', 'Wu', 'Ji', 'Geng', 'Xin', 'Ren', 'Gui'];
  const BRANCH = ['Zi', 'Chou', 'Yin', 'Mao', 'Chen', 'Si', 'Wu', 'Wei', 'Shen', 'You', 'Xu', 'Hai'];
  const CYCLE = Array.from({ length: 60 }, (_, i) => STEM[i % 10] + '-' + BRANCH[i % 12]);
  const MONTH_START_STEM = { 0: 2, 5: 2, 1: 4, 6: 4, 2: 6, 7: 6, 3: 8, 8: 8, 4: 0, 9: 0 };

  function remainder(n, modulus) {
    const value = Number(n) % modulus;
    return value === 0 ? modulus : value;
  }

  function yearGanji(year) {
    return CYCLE[((Number(year) - 4) % 60 + 60) % 60];
  }

  function monthGanji(year, lunarMonth) {
    const month = Number(lunarMonth);
    if (!Number.isInteger(month) || month < 1 || month > 12) throw new Error('Invalid lunar month.');
    const yearStem = ((Number(year) - 4) % 60 + 60) % 60 % 10;
    const stem = (MONTH_START_STEM[yearStem] + month - 1) % 10;
    // Traditional month branches begin with Yin (寅) in lunar month 1.
    const branch = (month + 1) % 12;
    return STEM[stem] + '-' + BRANCH[branch];
  }

  function dayGanji(year, month, day) {
    const a = Math.floor((14 - Number(month)) / 12);
    const y = Number(year) + 4800 - a;
    const m = Number(month) + 12 * a - 3;
    const jdn = Number(day) + Math.floor((153 * m + 2) / 5) + 365 * y + Math.floor(y / 4) - Math.floor(y / 100) + Math.floor(y / 400) - 32045;
    return CYCLE[((jdn + 49) % 60 + 60) % 60];
  }

  function solarKey(value) {
    if (!value) return '';
    if (typeof value === 'string') return value.slice(0, 10);
    if (typeof value === 'object') {
      const year = value.y ?? value.year;
      const month = value.m ?? value.month;
      const day = value.d ?? value.day;
      if (year && month && day) {
        return String(year).padStart(4, '0') + '-' + String(month).padStart(2, '0') + '-' + String(day).padStart(2, '0');
      }
      for (const key of ['solar', 'solar_date', 'date']) if (value[key]) return solarKey(value[key]);
    }
    return '';
  }

  function resolveTargetLunarBirthday(calculation, targetYear, birth) {
    const month = Number(birth.m);
    const requestedDay = Number(birth.d);
    const monthDays = Number(calculation.month_days[targetYear + '-' + month]);
    if (!Number.isInteger(monthDays) || monthDays < 29 || monthDays > 30) throw new Error('Target lunar month length could not be resolved.');
    const effectiveDay = Math.min(requestedDay, monthDays);
    const leap = birth.leap ? 1 : 0;
    const keys = [
      targetYear + '-' + month + '-' + requestedDay + '-' + leap,
      targetYear + '-' + month + '-' + requestedDay + '-0'
    ];
    if (effectiveDay !== requestedDay) {
      keys.push(targetYear + '-' + month + '-' + effectiveDay + '-' + leap);
      keys.push(targetYear + '-' + month + '-' + effectiveDay + '-0');
    }
    let value = null;
    let matchedKey = '';
    for (const key of [...new Set(keys)]) {
      if (calculation.lunar_to_solar[key]) {
        value = calculation.lunar_to_solar[key];
        matchedKey = key;
        break;
      }
    }
    const solar = solarKey(value);
    if (!solar) throw new Error('Target lunar birthday could not be resolved.');
    return { solar, monthDays, requestedDay, effectiveDay, adjusted: effectiveDay !== requestedDay, matchedKey };
  }

  function calculateReading(options) {
    const targetYear = Number(options.targetYear);
    const birth = options.birth || {};
    const calculation = options.calculation || {};
    const cycleReference = options.cycleReference || {};
    if (!Number.isInteger(targetYear)) throw new Error('Invalid reading year.');
    if (!Number.isInteger(Number(birth.y)) || Number(birth.y) > targetYear) throw new Error('Birth year must not be later than the reading year.');
    if (!Number.isInteger(Number(birth.m)) || Number(birth.m) < 1 || Number(birth.m) > 12) throw new Error('Invalid lunar birth month.');
    if (!Number.isInteger(Number(birth.d)) || Number(birth.d) < 1 || Number(birth.d) > 30) throw new Error('Invalid lunar birth day.');

    const age = targetYear - Number(birth.y) + 1;
    const yearPillar = yearGanji(targetYear);
    const yearReference = cycleReference[yearPillar];
    const monthPillar = monthGanji(targetYear, birth.m);
    const monthReference = cycleReference[monthPillar];
    const targetBirthday = resolveTargetLunarBirthday(calculation, targetYear, birth);
    if (!yearReference || !monthReference) throw new Error('Cycle reference could not be resolved.');

    const parts = targetBirthday.solar.split('-').map(Number);
    const dayPillar = dayGanji(parts[0], parts[1], parts[2]);
    const dayReference = cycleReference[dayPillar];
    if (!dayReference) throw new Error('Day-cycle reference could not be resolved.');

    const upper = remainder(age + Number(yearReference.yearNumber), 8);
    const middle = remainder(targetBirthday.monthDays + Number(monthReference.monthNumber), 6);
    const lower = remainder(Number(birth.d) + Number(dayReference.dayNumber), 3);
    const code = upper + '-' + middle + '-' + lower;
    return {
      targetYear,
      age,
      yearPillar,
      yearReference,
      monthPillar,
      monthReference,
      dayPillar,
      dayReference,
      monthDays: targetBirthday.monthDays,
      targetBirthday,
      upper,
      middle,
      lower,
      code
    };
  }

  return Object.freeze({
    STEM,
    BRANCH,
    CYCLE,
    remainder,
    yearGanji,
    monthGanji,
    dayGanji,
    solarKey,
    resolveTargetLunarBirthday,
    calculateReading
  });
});
