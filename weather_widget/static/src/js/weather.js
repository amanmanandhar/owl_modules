/** @odoo-module **/

import { Component, useState } from "@odoo/owl";

export class Weather extends Component {
    setup() {
        this.state = useState({
            city: "",
            temp: null,
            condition: "",
        });
    }

    async getWeather() {
        const city = this.state.city;

        const data = {
            Kathmandu: { temp: 22, condition: "Cloudy" },
            Delhi: { temp: 30, condition: "Sunny" },
            London: { temp: 15, condition: "Rainy" },
        };

        if (data[city]) {
            this.state.temp = data[city].temp;
            this.state.condition = data[city].condition;
        } else {
            this.state.temp = "N/A";
            this.state.condition = "Not Found";
        }
    }
}
Weather.template = "weather_widget.Weather";