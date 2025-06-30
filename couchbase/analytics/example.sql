-- Create example Analytics Dataset for Players
-- Execute in Analytics Editor
CREATE DATASET players_ds ON `galactic-dominion`.`game_data`.`players`;

-- Run Leaderboard Query
-- Return Top 2 Players by Credits
SELECT username, player_id, resources.credits AS credits
FROM players_ds
ORDER BY resources.credits DESC
LIMIT 2;

-- Return top player by total resources (credits, metals and crystals)
SELECT 
  username, 
  player_id,
  resources.credits,
  resources.metal,
  resources.crystals,
  (resources.credits + resources.metal + resources.crystals) AS total_resources
FROM players_ds
ORDER BY total_resources DESC
LIMIT 1;