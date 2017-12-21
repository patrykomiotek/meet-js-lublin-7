const math = require('mathjs');

const print = (msg) => console.log(msg);

const a = math.matrix([[1, 2], [3, 4]]);
const b = math.matrix([[2, 3], [3, 4]]);

print(math.multiply(a, b));
