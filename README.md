# Letters-Cubes Helper
This is a tool to help solve a kids game

In this game, each player roll 7 dices with letters on them, and the goal is to arrange words out of them

Words can be arrange in a row:

![use1](https://github.com/kfirkrak/letters-game/blob/main/game_example1.png)

We can also arrange them vertically:

![use1](https://github.com/kfirkrak/letters-game/blob/main/game_example2.png)
![use1](https://github.com/kfirkrak/letters-game/blob/main/game_example3.png)

The game is over once all the letters has been chosen, each as a part of some word on the board:

![use1](https://github.com/kfirkrak/letters-game/blob/main/game_example4.png)

### Programming tools
To solve this problem I've used the following key ideas:
- Random
  - In the function ```roll_a_dice(num=7, on=False)``` which simulate a single dice roll for us
- combinatorics
  - ```subset(roll)``` which generate each possible subset of a givin dice roll
  - ```every_combination(lists)``` sorting out the **unique** subsets
## Example of usage
In order to run a single turn we'll call the function:
```
single_turn()
```
This function simulate a single dice roll, and prints a list of all the Hebrew words we can generate from those letters:

![use](https://github.com/kfirkrak/letters-game/blob/main/exemple1.png)

After seeing this list, the first player can choose one of the 5 letter words and place it on the board:

![use](https://github.com/kfirkrak/letters-game/blob/main/usage1.png)

Thus the second player can choose on of the 3 letter words to place the remaining 2 letters:

![use](https://github.com/kfirkrak/letters-game/blob/main/usage2.png)

And the second player would win this round

## Game analysis
We can use this code to generate new insights on this game

The main tool I wrote for that is the function ```analyze_game(times)```

This function's input is the number of games we wish to run, and it's output is statistical data gathered from those round

![use](https://github.com/kfirkrak/letters-game/blob/main/longest1000rolls.png)

From this pie chart we can deduce that it is not so likely to win this game on the first round, the probability of finishing a game in one round is about 10%
moreover is it very unlikely that we won't be able to find a word shorter than 5 letters, since for 4 letter the chances are 2.3% and after running 1000 games we can see clearly that it was always possible to find a 4-letter word to place.
* So the best strategy for the first player would be to place **the shortest word**, so that the other player wont be able to finish the board
* While the best strategy second player if to **maximize** the word he's placing

![use](https://github.com/kfirkrak/letters-game/blob/main/letters1000rolls.png)

From this bar graph we can see that the cubes are pretty fair, with a slight deviation for the two most common vowels
