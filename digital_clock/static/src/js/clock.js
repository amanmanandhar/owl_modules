/** @odoo-module **/

import { Component, useState, onMounted, onWillUnmount } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class DigitalClock extends Component {
    static template = 'digital_clock.DigitalClockTemplate';
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

registry.category("public_components").add("digital_clock.DigitalClock", DigitalClock);