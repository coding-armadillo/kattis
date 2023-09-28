const readline = require("readline");
const rl = readline.createInterface(process.stdin, process.stdout);

rl.question("", (a) => {
  console.log(4 * Math.sqrt(parseInt(a)));
});
