/** @odoo-module **/

import { mount } from "@odoo/owl";
import { DigitalClock } from "./clock";

function startClock() {
    const el = document.getElementById("clock_root");

    if (el) {
        mount(DigitalClock, el);
    }
}

startClock();