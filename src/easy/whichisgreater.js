const readline = require("readline");
const rl = readline.createInterface(process.stdin, process.stdout);

rl.question("", (line) => {
  [a, b] = line
    .trim()
    .split(" ")
    .map((e) => parseInt(e));
  if (a > b) {
    console.log(1);
  } else {
    console.log(0);
  }
});
