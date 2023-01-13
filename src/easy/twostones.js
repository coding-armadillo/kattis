const readline = require("readline");
const rl = readline.createInterface(process.stdin, process.stdout);

rl.question("", (n) => {
  if (parseInt(n) % 2) {
    console.log("Alice");
  } else {
    console.log("Bob");
  }
});
