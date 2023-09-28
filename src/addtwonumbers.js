const readline = require("readline");
const rl = readline.createInterface(process.stdin, process.stdout);

rl.question("", (line) => {
  [a, b] = line
    .trim()
    .split(" ")
    .map((e) => parseInt(e));
  console.log(a + b);
});
