-- An Index will limit the data scan area. 
-- Your queries will have to scan less data to find results.
-- This improves both Query cost and performance.

-- Create index on owner_player_id for fast lookups (planets, fleets and star_systems)
CREATE INDEX idx_planets_owner_player_id
ON `galactic-dominion`.`game_data`.`planets`(owner_player_id);

CREATE INDEX idx_fleets_owner_player_id
ON `galactic-dominion`.`game_data`.`fleets`(owner_player_id);

CREATE INDEX idx_star_systems_owner_player_id
ON `galactic-dominion`.`game_data`.`star_systems`(owner_player_id);

-- Create index on player_id for players collection (for joins and lookups)
CREATE INDEX idx_players_player_id
ON `galactic-dominion`.`game_data`.`players`(player_id);

-- Create index on status for sessions and combats
CREATE INDEX idx_sessions_status
ON `galactic-dominion`.`game_data`.`sessions`(status);

CREATE INDEX idx_combats_status
ON `galactic-dominion`.`game_data`.`combats`(status);

-- Create index on system_id for star_systems and planets
CREATE INDEX idx_star_systems_system_id
ON `galactic-dominion`.`game_data`.`star_systems`(system_id);

CREATE INDEX idx_planets_system_id
ON `galactic-dominion`.`game_data`.`planets`(system_id);

-- Create index on player_id for resources
CREATE INDEX idx_resources_player_id
ON `galactic-dominion`.`game_data`.`resources`(player_id);

-- Create index on diplomacy.allies for array search
CREATE INDEX idx_players_diplomacy_allies
ON `galactic-dominion`.`game_data`.`players`(DISTINCT ARRAY ally FOR ally IN diplomacy.allies END);

-- Create index on technology_ids for UNNEST queries
CREATE INDEX idx_players_technology_ids
ON `galactic-dominion`.`game_data`.`players`(DISTINCT ARRAY tech_id FOR tech_id IN technology_ids END);

-- Create index on tech_id for technologies
CREATE INDEX idx_technologies_tech_id
ON `galactic-dominion`.`game_data`.`technologies`(tech_id);