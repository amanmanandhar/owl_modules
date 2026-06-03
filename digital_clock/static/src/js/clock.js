/** @odoo-module **/

import { Component, useState, onMounted, onWillUnmount } from "@odoo/owl";

export class DigitalClock extends Component {
    setup() {
        this.state = useState({
            time: new Date().toLocaleTimeString(),
        });

        let timer;

        onMounted(() => {
            timer = setInterval(() => {
                this.state.time = new Date().toLocaleTimeString();
            }, 1000);
        });

        onWillUnmount(() => {
            clearInterval(timer);
        });
    }
}

DigitalClock.template = "digital_clock.DigitalClock";