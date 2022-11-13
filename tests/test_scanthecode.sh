#!/bin/bash
rosservice call /display/update_scanthecode_state \
'{
    task_id: 5,
    data: [321]
}'