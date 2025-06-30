-- Execute SQL++ / N1QL Queries using Python SDK in run-query.py 
-- or under Query in Couchbase Server UI

-- List all planets with owner player ID and username
SELECT p.name AS planet_name, p.owner_player_id, pl.username AS owner_username
FROM `galactic-dominion`.`game_data`.`planets` p
LEFT JOIN `galactic-dominion`.`game_data`.`players` pl
ON p.owner_player_id = pl.player_id;

-- List all fleets and their owners
SELECT f.fleet_id, f.owner_player_id, pl.username AS owner_username
FROM `galactic-dominion`.`game_data`.`fleets` f
LEFT JOIN `galactic-dominion`.`game_data`.`players` pl
ON f.owner_player_id = pl.player_id;

-- Find all players allied with a specific player
SELECT p.username, p.player_id
FROM `galactic-dominion`.`game_data`.`players` p
WHERE ANY ally IN p.diplomacy.allies SATISFIES ally = "player::123" END;

-- Get all resources for a specific player
SELECT r.*
FROM `galactic-dominion`.`game_data`.`resources` r
WHERE r.player_id = "player::123";

-- List all technologies a player has
SELECT p.username, t.name AS technology_name
FROM `galactic-dominion`.`game_data`.`players` p
UNNEST p.technology_ids AS tech_id
JOIN `galactic-dominion`.`game_data`.`technologies` t
ON tech_id = t.tech_id
WHERE p.player_id = "player::123";

-- Find all ongoing combats and participants
SELECT c.combat_id, c.system_id, c.status, c.participants
FROM `galactic-dominion`.`game_data`.`combats` c
WHERE c.status = "ongoing";

-- Show all planets in a given star system
SELECT p.name AS planet_name, s.name AS system_name
FROM `galactic-dominion`.`game_data`.`planets` p
JOIN `galactic-dominion`.`game_data`.`star_systems` s
ON p.system_id = s.system_id
WHERE s.name = "Alpha Centauri";

-- Show all sessions and their players
SELECT s.session_id, s.status, s.players
FROM `galactic-dominion`.`game_data`.`sessions` s;