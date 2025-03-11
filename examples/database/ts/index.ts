import * as influxdb3 from "@komminarlabs/influxdb3";

export const database = new influxdb3.Database("signals", {
    name: "signals",
    retentionPeriod: 604800,
});

export const databaseId = database.id;

console.log(`Database ID: {databaseId}`);
