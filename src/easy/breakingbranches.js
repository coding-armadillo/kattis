const readline = require("readline");
const rl = readline.createInterface(process.stdin, process.stdout);

rl.question("", (n) => {
  if (parseInt(n) % 2) {
    console.log("Bob");
  } else {
    console.log("Alice");
    console.log(1);
  }
});
