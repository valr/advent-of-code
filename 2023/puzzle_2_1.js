// day 2 - part 1

const data = await Deno.readTextFile("puzzle_2.txt");

const sum_game_id = data.split("\n").reduce((sum, line) => {
  const [game, set_line] = line.split(": ");

  const sets = set_line.split("; ").map((set) => {
    return set.split(", ").reduce((obj, str) => {
      obj[str.split(" ")[1]] = parseInt(str.split(" ")[0]);
      return obj;
    }, {});
  });

  return sets.every((set) => {
      return (
        // game possible with only 12 red cubes, 13 green cubes, and 14 blue cubes
        (set.red === undefined || set.red <= 12) &&
        (set.green === undefined || set.green <= 13) &&
        (set.blue === undefined || set.blue <= 14)
      );
    })
    ? sum + parseInt(game.split(" ")[1])
    : sum;
}, 0);

console.log(`sum of game ids: ${sum_game_id}`);
