-- Once Function is deployed
-- Insert a new combat document 
-- Check Alerts collection: "A new conflict has started in the Galaxy!"
INSERT INTO `galactic-dominion`.`game_data`.`combats` (KEY, VALUE)
VALUES (
  "combat::test1",
  {
    "combat_id": "combat::test1",
    "system_id": "system::alpha",
    "participants": [
      { "player_id": "player::123", "fleet_ids": ["fleet::a1"] },
      { "player_id": "player::456", "fleet_ids": ["fleet::b2"] }
    ],
    "start_time": "2025-06-28T12:00:00Z",
    "status": "ongoing"
  }
);