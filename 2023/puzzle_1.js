const data = await Deno.readTextFile("puzzle_1.txt");

const sum_part1 = data.split("\n").reduce((sum, line) => {
  const regexp = /\d/g;
  const digits = [...line.matchAll(regexp)];
  return sum + (digits.length ? +(digits.at(0) + digits.at(-1)) : 0);
}, 0);

console.log(`sum of all of the calibration values: ${sum_part1}`);

// deno-fmt-ignore
const numbers =
  { "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9 };

let sum_part2 = 0;

data.split("\n").forEach((line) => {
  const number = Object.keys(numbers)
    .map((num) => {
      return [line.indexOf(num), line.lastIndexOf(num), numbers[num]];
    })
    .reduce((res, num) => {
      const [num_min_ix, num_max_ix, num_val] = num;

      if (num_min_ix >= 0 && num_min_ix < res.min_ix) {
        res = { ...res, min_ix: num_min_ix, min_val: num_val };
      }
      if (num_max_ix >= 0 && num_max_ix > res.max_ix) {
        res = { ...res, max_ix: num_max_ix, max_val: num_val };
      }

      return res;
    }, { min_ix: Infinity, min_val: 0, max_ix: -Infinity, max_val: 0 });

  sum_part2 += number.min_val * 10 + number.max_val;
});

console.log(`sum of all of the calibration values: ${sum_part2}`);
