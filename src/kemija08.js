const readline = require("readline");
const rl = readline.createInterface(process.stdin, process.stdout);

rl.question("", (line) => {
  for (let c of "aeiou") {
    const regex = new RegExp(`${c}p${c}`, "g");
    line = line.replace(regex, c);
  }
  console.log(line);
});
