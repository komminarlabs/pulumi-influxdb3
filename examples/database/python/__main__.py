"""A Python Pulumi program"""

import komminarlabs_influxdb3 as influxdb3

database = influxdb3.Database(
    "signals",
    name="signals",
    retention_period=604800,
)
