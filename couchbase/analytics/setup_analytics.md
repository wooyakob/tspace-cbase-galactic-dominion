## 1. Create Analytics Dataset for Players
1. Open the **Couchbase Web Console** and go to the **Analytics** tab.
2. In the Analytics Query Editor, run:
   ```sql
   CREATE DATASET players_ds ON `galactic-dominion`.`game_data`.`players`;
3. Run Queries in analytics/example.sql. 

Analytics queries do not impact operational game performance and are ideal for leaderboards and reporting. 