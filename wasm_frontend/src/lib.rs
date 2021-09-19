mod utils;

use wasm_bindgen::prelude::*;
use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize)]
pub struct Players {
    name: String,
    position: String,
    goals: i32,
    assists: i32,
}

#[derive(Serialize, Deserialize)]
pub struct Team {
    name: String,
    players: Vec<Players>,
}

#[wasm_bindgen]
pub fn wasm_avg_goals(results: &JsValue) {
    // I added the match statement just in case the results are not the expected type for whatever reason
    match results.into_serde::<Vec<Team>>() {
        Ok(_) => {
            let rust_results = results.into_serde::<Vec<Team>>().unwrap();
            let mut team_name: String = "".to_string();
            let mut max_average = 0.0;
            let mut sum = 0.0;

            // Iterates through the Team(s)
            for i in 0..rust_results.len() {
                // Iterates through the Team's Players
                for j in 0..rust_results[i].players.len() {
                    sum = sum + rust_results[i].players[j].goals as f64;
                }

                sum = sum / 15.0;

                if sum > max_average {
                    max_average = sum;
                    team_name = rust_results[i].name.clone();
                }

                sum = 0.0;
            }

            web_sys::console::log_2(&"Team with the highest avg goals scored:".into(), &team_name.into());
            web_sys::console::log_2(&"Avg goals scored:".into(), &max_average.into());
        }
        Err(_) => web_sys::console::log_1(&"Could not parse the JS results into Rust".into())
    }
}
