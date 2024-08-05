import * as influxdb from "@komminarlabs/influxdb3";

export const database = new influxdb.Database("signals", {
    name: "signals",
    retentionPeriod: 604800,
});

export const databaseId = database.id;

console.log(`Database ID: {databaseId}`);
