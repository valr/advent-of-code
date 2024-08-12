const data = (await Deno.readTextFile("puzzle_3.txt")).split("\n");

// part one

const sum_adjacent_symbol = data.reduce((sum, row, row_ix, arr) => {
  return sum + row
    .matchAll(/\d+/g)
    .filter((match) => {
      return arr
        .slice(
          Math.max(row_ix - 1, 0),
          Math.min(row_ix + 2, arr.length),
        )
        .map((row) =>
          row.slice(
            Math.max(match.index - 1, 0),
            Math.min(match.index + match[0].length + 1, row.length),
          )
        )
        .join("")
        .replace(/[0-9.]/g, "");
    })
    .reduce((sum_match, match) => {
      return sum_match + parseInt(match[0]);
    }, 0);
}, 0);

console.log(`sum of numbers adjacent to a symbol: ${sum_adjacent_symbol}`);

// part two

data.forEach((row, row_ix, arr) => {
  row
    .matchAll(/\d+/g)
    .filter((match) => {
      return arr
        .slice(
          Math.max(row_ix - 1, 0),
          Math.min(row_ix + 2, arr.length),
        )
        .map((row) =>
          row.slice(
            Math.max(match.index - 1, 0),
            Math.min(match.index + match[0].length + 1, row.length),
          )
        )
        .join("")
        .includes("*");
    })
    .forEach((match) => {
      // store all numbers together with indexes of '*'

      // is it possible to have it indexed by indexes of '*' ?
      // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map
      console.log(match);
    });
});

// console.log(`sum of the gear ratios: ${sum_gear_ratios}`);
