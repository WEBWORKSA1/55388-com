/* 55388.com — Number engine (numerology, angel numbers, Chinese luck, tools). Pure functions, no network. */
(function (root) {
  const D = () => root.N55_DATA;
  const MASTER = [11, 22, 33];
  const digitSum = n => String(n).replace(/\D/g, "").split("").reduce((a, b) => a + (+b), 0);
  function reduce(n, keepMaster = true) {
    n = Math.abs(+n);
    while (n > 9 && !(keepMaster && MASTER.includes(n))) n = digitSum(n);
    return n;
  }
  function lifePath(y, m, d) {
    const parts = [reduce(m), reduce(d), reduce(digitSum(y))];
    const total = parts.reduce((a, b) => a + b, 0);
    return { number: reduce(total), steps: `${m} → ${parts[0]}, ${d} → ${parts[1]}, ${y} → ${parts[2]}; ${parts.join(" + ")} = ${total} → ${reduce(total)}` };
  }
  const LETTERS = { a:1,j:1,s:1,b:2,k:2,t:2,c:3,l:3,u:3,d:4,m:4,v:4,e:5,n:5,w:5,f:6,o:6,x:6,g:7,p:7,y:7,h:8,q:8,z:8,i:9,r:9 };
  const VOWELS = "aeiou";
  function nameNumbers(name) {
    const clean = (name || "").toLowerCase().normalize("NFD").replace(/[^a-z]/g, "");
    let all = 0, v = 0, c = 0;
    for (const ch of clean) { const val = LETTERS[ch] || 0; all += val; if (VOWELS.includes(ch)) v += val; else c += val; }
    return { expression: reduce(all), soulUrge: reduce(v), personality: reduce(c), letters: clean.length };
  }
  function personalYear(m, d, year) { return reduce(reduce(m) + reduce(d) + reduce(digitSum(year)), false); }
  function universalDay(date = new Date()) { return reduce(digitSum(`${date.getFullYear()}${date.getMonth() + 1}${date.getDate()}`), true); }
  function seeded(seed) { let s = seed % 2147483647; if (s <= 0) s += 2147483646; return () => (s = s * 16807 % 2147483647) / 2147483647; }
  function numberOfTheDay(date = new Date()) {
    const key = +(`${date.getFullYear()}${String(date.getMonth() + 1).padStart(2, "0")}${String(date.getDate()).padStart(2, "0")}`);
    const list = D().featured; const r = seeded(key)();
    return { angel: list[Math.floor(r * list.length)], universal: universalDay(date) };
  }

  function pattern(s) {
    const u = new Set(s);
    if (s.length > 1 && u.size === 1) return { key: "repeating", label: "Repeating number", text: `Every digit is ${s[0]}, so the energy of ${s[0]} is amplified ${s.length}× — this is the clearest, loudest form of the message.` };
    if (s.length > 2 && s === [...s].reverse().join("")) return { key: "palindrome", label: "Mirror / palindrome", text: "It reads the same forwards and backwards — a sign of reflection: what you send out comes back to you." };
    if (s.length % 2 === 0 && s.length >= 4 && s.slice(0, s.length / 2) === s.slice(s.length / 2)) return { key: "double", label: "Double sequence", text: `The pair ${s.slice(0, s.length / 2)} repeats — a nudge to notice a cycle that is replaying in your life.` };
    const asc = [...s].every((c, i, a) => i === 0 || +c === +a[i - 1] + 1), desc = [...s].every((c, i, a) => i === 0 || +c === +a[i - 1] - 1);
    if (s.length > 2 && asc) return { key: "ascending", label: "Ascending sequence", text: "The digits climb step by step — progress, momentum and a clear next step." };
    if (s.length > 2 && desc) return { key: "descending", label: "Descending sequence", text: "The digits count down — release, simplification and letting go of excess." };
    if (s.length >= 4 && /^(\d)\1(\d)\2$/.test(s)) return { key: "pairs", label: "Paired digits", text: `Two pairs (${s[0]}${s[0]} and ${s[2]}${s[2]}) — two areas of life asking to be balanced.` };
    return { key: "mixed", label: "Mixed sequence", text: "A mixed sequence is read in layers: the first digits show the cause, the middle digits the core message, the last digits the likely outcome." };
  }
  function analyze(input) {
    const s = String(input).replace(/\D/g, "").slice(0, 12);
    if (!s) return null;
    const data = D(), counts = {};
    for (const c of s) counts[c] = (counts[c] || 0) + 1;
    const dominant = Object.entries(counts).sort((a, b) => b[1] - a[1] || +b[0] - +a[0])[0][0];
    const sum = digitSum(s), root = reduce(sum);
    const uniq = [...new Set(s)];
    return {
      number: s, sum, root, pattern: pattern(s), dominant, uniq,
      rootInfo: data.digits[root] || data.masters[root],
      digitInfo: uniq.map(d => ({ d, n: counts[d], ...data.digits[d] })),
      layers: s.length >= 3 ? { cause: s[0], core: s.slice(1, -1), outcome: s[s.length - 1] } : null,
      curated: data.featured.includes(s)
    };
  }
  function chinese(input) {
    const s = String(input).replace(/\D/g, "").slice(0, 20);
    if (!s) return null;
    const cd = D().chinese;
    const digits = [...s].map(d => ({ d, ...cd.digits[d] }));
    let score = digits.reduce((a, x) => a + x.score, 0) / digits.length;
    const combos = [];
    for (const c of cd.combos) if (s.includes(c.n)) { combos.push(c); score += c.bonus; }
    if (s.endsWith("8")) score += 5; if (s.endsWith("4")) score -= 5;
    score = Math.max(1, Math.min(100, Math.round(score)));
    const verdict = score >= 85 ? "Exceptionally auspicious" : score >= 70 ? "Very lucky" : score >= 55 ? "Balanced / neutral-positive" : score >= 40 ? "Mixed" : "Traditionally unlucky";
    return { number: s, digits, combos, score, verdict };
  }
  const ONES = ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"];
  const TENS = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"];
  const SCALES = ["","thousand","million","billion","trillion","quadrillion"];
  function chunk(n) {
    let out = [];
    if (n >= 100) { out.push(ONES[Math.floor(n / 100)] + " hundred"); n %= 100; if (n) out.push("and"); }
    if (n >= 20) { out.push(TENS[Math.floor(n / 10)] + (n % 10 ? "-" + ONES[n % 10] : "")); }
    else if (n > 0 || !out.length) out.push(ONES[n]);
    return out.join(" ");
  }
  function toWords(numStr, opts = {}) {
    let s = String(numStr).trim().replace(/,/g, ""); if (!/^-?\d+(\.\d+)?$/.test(s)) return null;
    const neg = s.startsWith("-"); if (neg) s = s.slice(1);
    let [intPart, dec = ""] = s.split(".");
    intPart = intPart.replace(/^0+(?=\d)/, "");
    if (intPart.length > 18) return "Number too large (max 18 digits).";
    let n = BigInt(intPart), words = [];
    if (n === 0n) words = ["zero"];
    let i = 0;
    while (n > 0n) { const c = Number(n % 1000n); if (c) words.unshift(chunk(c).replace(/^and /, "") + (SCALES[i] ? " " + SCALES[i] : "")); n /= 1000n; i++; }
    let text = words.join(" ");
    if (!opts.uk) text = text.replace(/ and /g, " ");
    if (opts.cheque) {
      const cents = (dec + "00").slice(0, 2);
      text = `${text} ${opts.currency || "dollars"} and ${cents}/100`;
    } else if (dec) text += " point " + [...dec].map(d => ONES[+d]).join(" ");
    if (neg) text = "minus " + text;
    if (opts.case === "upper") text = text.toUpperCase();
    else if (opts.case === "title") text = text.replace(/\b[a-z]/g, c => c.toUpperCase());
    else if (opts.case === "sentence") text = text[0].toUpperCase() + text.slice(1);
    return text;
  }
  function pick(count, max, exclude = [], rng = Math.random) {
    const out = new Set(exclude.length ? [] : []);
    const pool = Array.from({ length: max }, (_, i) => i + 1);
    for (let i = pool.length - 1; i > 0; i--) { const j = Math.floor(secureRand() * (i + 1)); [pool[i], pool[j]] = [pool[j], pool[i]]; }
    pool.slice(0, count).forEach(x => out.add(x));
    return [...out].sort((a, b) => a - b);
  }
  function secureRand() { if (root.crypto && crypto.getRandomValues) { const a = new Uint32Array(1); crypto.getRandomValues(a); return a[0] / 4294967296; } return Math.random(); }
  function randInt(min, max) { return Math.floor(secureRand() * (max - min + 1)) + min; }
  function compatibility(a, b) {
    const groups = [[1, 5, 7], [2, 4, 8], [3, 6, 9]];
    const base = x => (x > 9 ? reduce(x, false) : x);
    const A = base(a), B = base(b);
    let score = 60;
    if (A === B) score = 78;
    else if (groups.some(g => g.includes(A) && g.includes(B))) score = 90;
    else if ((A + B) % 3 === 0) score = 72;
    else if (Math.abs(A - B) === 4) score = 52;
    if (MASTER.includes(a) || MASTER.includes(b)) score += 4;
    return Math.min(99, score);
  }
  root.N55 = { reduce, digitSum, lifePath, nameNumbers, personalYear, universalDay, numberOfTheDay, analyze, chinese, toWords, pick, randInt, compatibility, secureRand };
})(window);
