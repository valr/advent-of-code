const data = await Deno.readTextFile("puzzle_1.txt");

const sum_part1 = data.split("\n").reduce((sum, line) => {
  const regexp = /\d/g;
  const digits = [...line.matchAll(regexp)];
  return sum + (digits.length ? +(digits.at(0) + digits.at(-1)) : 0);
}, 0);

console.log(`sum of all of the calibration values: ${sum_part1}`);

// deno-fmt-ignore
const numbers =
  [ "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ];

let sum_part2 = 0;

data.split("\n").forEach((line) => {
  const number = numbers
    .map((num) => {
      return [line.indexOf(num), line.lastIndexOf(num)];
    })
    .reduce((res, num, num_ix) => {
      if (num[0] >= 0 && num[0] < res.min_val) {
        res.min_val = num[0];
        res.min_ix = num_ix;
      }
      if (num[1] >= 0 && num[1] > res.max_val) {
        res.max_val = num[1];
        res.max_ix = num_ix;
      }
      return res;
    }, { min_val: Infinity, min_ix: -1, max_val: -Infinity, max_ix: -1 });

  sum_part2 += ((number.min_ix % 9 + 1) * 10) + (number.max_ix % 9 + 1);
});

console.log(`sum of all of the calibration values: ${sum_part2}`);
