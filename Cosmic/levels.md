# Levels

Levels are stored in a file in /levels/

- Premade levels are stored in /levels/default
- User generated levels are stored in /levels/user

## SYNTAX

Levels are stored in the file with text encoding

Each level consists of multiple events (enemy spawning, switch level type, etc.) each of which is represented by a single line in the level file.

Each event has 5 arguments, seperated by `|`. These arguments are all of type `int`

```

{EVENT TYPE}|{X_COORD*}|{Y_COORD*}|{HEALTH*}|{DELAY_TIMER}

(arguments indicated by * are optional for some event types and can be left as 0)
```



## EVENTS

|Event          | Arguments     |               |               |               |               | Notes     |  
|---------------|---------------|---------------|---------------|---------------|---------------|-----------|
|               | {EVENT_TYPE}  | {X_COORD}     | {Y_COORD}     | {HEALTH}      | {DELAY_TIMER} |                           |
|               |               |               |               |               |               |                           |
| EMPTY         | 0             | N             | N             | N             | Y             | Level is empty. May be used to end game          |
| ENEMY         | 1             | Y             | Y             | Y             | Y             | Spawns an enemy at the specified coordinates with health {HEALTH} (recommended value = 1)|
| ENEMY_RANDX   | 2             | N             | Y             | Y             | Y             | Spawns an enemy at the specifed Y coordinate, with a randomized x coordinate with health {HEALTH} (recommended value = 1)|
| BOSS          | 3             | Y             | Y             | Y             | Y             | Spawns a boss at the specified coordinates, with health {HEALTH} (recommended value = 50). Refer to [BOSS](#boss)|
| BOSS_RANDX    | 4             | N             | Y             | Y             | Y             | Spawns a boss at the specified Y coordinate, a randomized x coordinate, with health {HEALTH} (recommended value = 50). Refer to [BOSS](#boss)|
| BOSS_BG       | 5             | N             | N             | N             | Y             | Switch the background to the boss' (not recommended unless BOSS or BOSS_RANDX is active, as enemies will appear invisible)|
| NORMAL_BG     | 6             | N             | N             | N             | Y             | Switch the background back to normal |
| ENDLESS       | 7             | N             | N             | N             | N             | Set the game to endless mode, pausing event execution. |
| NEXT_LVL      | 8             | N             | N             | N             | Y             | Initialize the next level. See [LEVEL PROGRESSION](#level-progression) |
| WAIT_EMPTY    | 9             | N             | N             | N             | N             | Waits until all enemies are cleared from the screen. |
| COUNTDOWN     | 100           | N             | N             | N             | N             | Not to be used in level file. Indicates that DELAY_TIMER is > 0 (The game is counting down to execute the next event)|

### HIGH SCORE

The high score (event 42) is and exception to the normal event syntax. It uses X_coord as a counter to store the high score. It must be positioned in the first line of the level file.

## LEVEL PROGRESSION

Level names play a role in how levels are progressed. They must be named with a trailing number indicating the level number, preceded by an underscore (`_`). Levels start indexing at 1.

Whenever event `NEXT_LVL` is called, the level number is incremented by 1 and the corresponding level file opened and ran.

For example in `My Level_1` `NEXT_LVL` will cause `My Level_2` to be opened and ran, followed by `My Level_3` etc., until `EMPTY` or `ENDLESS` events occur

## BOSS

The boss can be spawned one or multiple time in a level. The events `BOSS` or `BOSS_RANDX` can be used. These events will pause event execution until the boss is defeated. Before `BOSS` or `BOSS_RANDX` is called, `WAIT_EMPTY` should be called  to ensure that no enemies remain, followed by `BOSS_BG`. After `BOSS` or `BOSS_RANDX`, `NORMAL_BG` should be called  to set the background back to normal.