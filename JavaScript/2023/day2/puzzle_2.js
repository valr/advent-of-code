const data = await Deno.readTextFile("puzzle_2.txt");

// parsing

const games = data.split("\n").map((line) => {
  const [idline, setline] = line.split(": ");
  const game = setline.split("; ").map((set) => {
    return set.split(", ").reduce((obj, str) => {
      obj[str.split(" ")[1]] = parseInt(str.split(" ")[0]);
      return obj;
    }, {});
  });
  game.unshift(parseInt(idline.split(" ")[1]));
  return game;
});

// part one

const sum_game_ids = games.reduce((sum, game) => {
  return game.slice(1).every((set) => {
    return (
      (set.red === undefined || set.red <= 12) &&
      (set.green === undefined || set.green <= 13) &&
      (set.blue === undefined || set.blue <= 14)
    );
  })
    ? sum + game[0]
    : sum;
}, 0);

console.log(`sum of game ids: ${sum_game_ids}`);

// part two

const sum_power_sets = games.reduce((sum, game) => {
  const set = game.slice(1).reduce((res, set) => {
    ["red", "green", "blue"].forEach((color) => {
      res[color] = Math.max(res[color], set[color] ?? 0);
    });
    return res;
  }, { red: 0, green: 0, blue: 0 });
  return sum + Object.values(set).reduce((a, b) => a * b);
}, 0);

console.log(`sum of power of sets: ${sum_power_sets}`);
