// parsing

const array = (await Deno.readTextFile("puzzle_3.txt")).split("\n");

// part one

const sum_adjacent_symbol = array.reduce((sum, row, row_ix, arr) => {
  return sum +
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
          .replace(/[0-9.]/g, "");
      })
      .reduce((sum_match, match) => {
        return sum_match + parseInt(match[0]);
      }, 0);
}, 0);

console.log(`sum of numbers adjacent to a symbol: ${sum_adjacent_symbol}`);
