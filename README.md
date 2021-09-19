# Hockey-Statistics-Web-Application

This is a project from CS 1520, Programming Languages for Web Applications. I created a hockey statistics web application where hockey teams are generated, their average goals scored are calculated, and the team with the highest average goals scored is found. The latter two statistics are then printed into the console. 

Because there is not a UI to this project, I have not included a live version. 

### :warning: The following files have my original code:
1. [backend/hockey.py](https://github.com/val-l-hosler/Hockey-Statistics-Web-Application/blob/main/backend/hockey.py)
2. [js_frontend/js_frontend.js](https://github.com/val-l-hosler/Hockey-Statistics-Web-Application/blob/main/js_frontend/js_frontend.js)
3. [wasm_frontend/src/lib.rs](https://github.com/val-l-hosler/Hockey-Statistics-Web-Application/blob/main/wasm_frontend/src/lib.rs)

### 🧰 Tech Stack 
1. Flask
2. JavaScript (ES6) (including the fetch API, async/await, and functional programming)
3. JSON
4. Python
5. Rust
6. WebAssembly

### :memo: The project had the following specifications:

1. Due to the large number of languages, tools, and technologies to be used in
	this project, you are provided with a large amount of skeleton code. Here,
	we will overview the project directory, and detail the changes you will 
	be required to make. In the root of your repository you will find the
	following:
	
	1. The `backend/` directory:
		* This is a Flask application that will serve as the backend of your
			web app, generating hockey stats and making them available as a
			RESTful API.
		* You will need to modify `backend/hockey.py` to provide additional
			Flask routes:
			* `/teams`: Performing a `GET` on this route should return a
				list of teams in the league (as a JSON array of strings).
				You should serve data on 12 different teams:
				* meerkats
				* elephants
				* antelopes
				* seals
				* seagulls
				* starfish
				* deer
				* rabbits
				* squirrels
				* flamingos
				* salamanders
				* cranes
			* `/teams/team_name`: For each of the preceeding 12 team
				names, you should return a list of players and the stats
				for each player (all randomly generated). Specifically, a
				`GET` on this route should return a JSON array of objects.
				Each object should have the following attributes:
				* `name`: The player's name, a randomly generated string 4-8 characters long
				* `position`: They player's position.
					* `"D"` for defenseman
					* `"LW"` for left wing
					* `"RW"` for right wing
					* `"C"` for center 
					* For each team, you should generate 6 defensemen, and 3
						players for each other position (you will be ignoring
						goalie stats for this project)
				* `goals`: The number of goals scored by this player as an integer
				* `assists`: The nubmer of assistes from this player as an integer
			* You do not need to support other routes or HTTP methods for
				this project. Because all data will be randomly generated,
				you do not need to use SQLAlchemy or store any data in a
				database. However, you should use the team name as a random
				seed so that `GET`s to the same route (e.g.,
				`/teams/meerkats`) will return the same values (even after
				stopping/restarting the server!)
			* Attempting to `GET` any `/teams/team_name` not returned by
				a `GET` to `/teams` should result in a `404` (e.g., if a
				`GET` to `/teams` did not include the name `mice`, 
				attempting a `GET` on `/teams/mice` should result in a
				`404`).
			* You should not modify any other files in this directory aside
				from `backend/hockey.py`!
	1. The `js_frontend/` directory:
		* This folder should contain a single `.js` file: 
			`js_frontend/js_frontend.js`. You should modify this file to provide
			implementations of two functions:
			* `process_all_teams(func)`: This function should `fetch` stats
				on all of the teams from the backend, and then pass a
				single JS Array of Objects as an argument to `func`. Each
				Object should have two attributes:
				* `name`: the team's name (e.g., `"meerkats"`)
				* `players`: a JS Array of Player Objects (as described
					in the backend section)
			* `js_avg_goals(results)`: This function should process data
				gathered by `process_all_teams`. Specifically, it should 
				determine which team had the highest average goals scored,
				and log that result to the console (both the team name and
				the average).
			* Note that this file is imported as a JS module, so these
				functions need to be exported (e.g., `process_all_teams`
				should be defined as: `export function process_all_teams(func) { ... }`
			* In order to collect the stats from all teams into a single
				Array, you may find the `Promise.all()` method useful.
			* `process_all_teams` should determine the teams available via
				a `GET` to the `/teams` route on the backend (i.e., you 
				should not hard-code this function to fetch the 12 team
				names listed above).
	1. The `wasm_frontend/` directory:
		* This folder is a Cargo project generated by `wasm-pack`. You will
			need to have `wasm-pack` installed to build this project. You do
			not need to create a new `wasm-pack` project, it has already
			been initialized for you, but as you can see, the `Makefile` uses
			`wasm-pack` to compile your Rust code.
		* You will need to modify `wasm_frontend/src/lib.rs` to provide an 
			implementation of `wasm_avg_goals(results: &JsValue)`. This
			function should mirror the functionality of `js_avg_goals`, just
			in Rust instead of JavaScript.
	1. The `Makefile`:
		* As you can see, the Makefile does the work of compiling your WASM
			binary and bridge code, copying the WASM and JS frontends to the
			Flask app's `static` directory, and starting the Flask app.
		* You should be able to compile and run your project by running 
			`make run` in the root of your repository
		* You should *not* modify the `Makefile`

1. You must build your website using JavaScript, Rust, JSON, AJAX, Python, and
	Flask.

<em>Note: The project specifications were written by my professor, Dr. Farnan.</em>
