const readline = require("readline");
const rl = readline.createInterface(process.stdin, process.stdout);

rl.question("", (line) => {
  if (line.includes("ss")) {
    console.log("hiss");
  } else {
    console.log("no hiss");
  }
});
