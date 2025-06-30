# Setting Up a Couchbase Eventing Function: Combat Alert
This guide shows you how to create an Eventing function in Couchbase that writes an alert to the `game_events.alerts` collection whenever a new combat document is created or updated.
---
## Step-by-Step Instructions
### 1. Prepare Collections
Make sure these exist in your `galactic-dominion` bucket:
- **Scope:** `game_data`
  - **Collection:** `combats`
Create new scope and collection:
- **Scope:** `game_events`
  - **Collection:** `alerts`
---
### 2. Create the Eventing Function
1. Go to the **Eventing** section in CB Server UI.
2. Click **Add Function**.
#### Fill out the form:
- **Function Scope:**  
  - Bucket: `galactic-dominion`  
  - Scope: `game_data`
- **Listen To Location:**  
  - Bucket: `galactic-dominion`  
  - Scope: `game_data`  
  - Collection: `combats`
- **Eventing Storage:**  
  - Bucket: `galactic-dominion`  
  - Scope: `game_events`  
  - Collection: `alerts`
- **Function Name:**  
  - `combat_alerts`
- **Deployment Feed Boundary:**  
  - `Everything` (default)
---
### 3. Add Bindings
Under **Bindings**, add:
- **Binding type:** Bucket alias  
  - **Alias:** `alerts`  
  - **Bucket:** `galactic-dominion`  
  - **Scope:** `game_events`  
  - **Collection:** `alerts`  
  - **Access:** Read/Write
---
### 4. Add the Function Code
Click **Next: Add Code** and paste the following:
```javascript
function OnUpdate(doc, meta) {
    if (meta.id.startsWith("combat::")) {
        var alert = {
            type: "combat_alert",
            combat_id: meta.id,
            system_id: doc.system_id,
            participants: doc.participants,
            status: doc.status,
            timestamp: new Date().toISOString(),
            message: "A new conflict has started in the galaxy!"
        };
        // Write to alerts collection in game_events scope
        alerts[meta.id] = alert;
    }
}
```
---
### 5. Save and Deploy
- Click **Save and Return**.
- Click **Deploy** to activate the function.
---
**Done!**  
Now, whenever a combat document is created or updated, an alert will be written to the `game_events.alerts` collection.