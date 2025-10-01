# write a for loop and run the crew for 5 times
for i in {0..20}
do
    echo "Running crew for PLAYER_ID=$i"
    PLAYER_ID=$i uv run crewai run
    sleep 1m
done