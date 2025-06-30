// Create Dynamic Events by using Eventing Functions
// Example Combat Alert
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