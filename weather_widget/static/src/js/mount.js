/** @odoo-module **/

import { App } from "@odoo/owl";
import { Weather } from "./weather";

async function startWeather() {
    const el = document.getElementById("weather_root");
    if (el) {
        const res = await fetch("/weather_widget/static/src/xml/weather.xml");
        const templateContent = await res.text();
        const app = new App(Weather, {
            templates: templateContent,
            env: {},
        });
        await app.mount(el);
    }
}
startWeather();