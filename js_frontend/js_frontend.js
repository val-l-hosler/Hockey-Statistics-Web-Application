export function process_all_teams(func) {
    fetch(("/teams"))
    .then((response) => {
        return response.json();
    }).then((data) => {
        const teams = data.map(async (name) => {
            const response = await fetch("/teams/" + name);

            if (!response.ok) {
                throw new Error("The following error has occurred: " + response.status);
            }

            const players = await response.json();
            return {"name": name, "players": players};
        });

        return Promise.all(teams);
    }).then((data) => {
        const teams_arr = [];

        for (let i = 0; i < data.length; i++) {
            teams_arr.push(data[i]);
        }

        return Promise.resolve(teams_arr);
    }).then((data) => func(data))
    .catch(() => {
        console.log("Error fetching teams.")
    });
}

export function js_avg_goals(results) {
    const teams = results.map(results => results["name"]);
    const players = results.map(results => results["players"]);
    const team_avg_goals = [];

    for (let i = 0; i < players.length; i++) {
        team_avg_goals.push({
            "name": teams[i],
            "avg_goals": (players[i].reduce((total, team) => total + team.goals, 0) / 15)
        });
    }

    // Returns the team with the highest average goals
    const highest_avg_goals = team_avg_goals.reduce((previous, current) => previous.avg_goals > current.avg_goals ? previous : current);
    console.log("Team with the highest avg goals scored: " + highest_avg_goals.name);
    console.log("Avg goals scored: " + highest_avg_goals.avg_goals);
}
