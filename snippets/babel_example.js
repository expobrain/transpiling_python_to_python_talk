// Original ES7+ code
[1, 2, 3].map(n => n ** 2);

// ..is translated into ES5 code
[1, 2, 3].map(function(n) {
  return n ** 2;
});
