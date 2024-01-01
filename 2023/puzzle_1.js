const data = await Deno.readTextFile("puzzle_1.txt");

const sum_part1 = data.split("\n").reduce((sum, line) => {
  const regexp = /\d/g;
  const digits = [...line.matchAll(regexp)];
  return sum + (digits.length ? +(digits.at(0) + digits.at(-1)) : 0);
}, 0);

console.log(`sum of all of the calibration values: ${sum_part1}`);

// deno-fmt-ignore
const numbers = [
  "1","2", "3", "4", "5", "6", "7", "8", "9",
  "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
];

let sum_part2 = 0;

data.split("\n").forEach((line) => {
  let num_ix1 = -1;
  let num_ix2 = -1;

  for (let line_ix = 0; line_ix < line.length; line_ix++) {
    // for (const [num_ix, num] of numbers.entries()) { // slower
    for (let num_ix = 0, num; (num = numbers[num_ix]); num_ix++) { // faster
      if (line.slice(line_ix, line_ix + num.length) === num) {
        if (num_ix1 === -1) {
          num_ix1 = num_ix;
        }
        num_ix2 = num_ix;
      }
    }
  }

  if (num_ix1 >= 0 && num_ix2 >= 0) {
    sum_part2 += ((num_ix1 % 9 + 1) * 10) + (num_ix2 % 9 + 1);
  }
});

console.log(`sum of all of the calibration values: ${sum_part2}`);
