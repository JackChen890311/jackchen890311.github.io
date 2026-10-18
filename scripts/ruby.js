hexo.extend.tag.register('ruby', function (args) {
  const [base, reading] = args;
  return `<ruby>${base}<rp>(</rp><rt>${reading}</rt><rp>)</rp></ruby>`;
});