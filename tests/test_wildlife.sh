#!/bin/bash
rostopic pub -1 /dji_m210/task/wildlife bb_msgs/Wildlife \
'{
    crocodile: {latitude: -33.724640, longitude: 150.671923},
    platypus: {latitude: -33.723745, longitude: 150.670337},
    turtle: {latitude: -33.724385, longitude: 150.669799}
}'