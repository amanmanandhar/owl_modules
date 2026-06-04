/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class CounterApp extends Component{
    static  template = "counter_app.Counting";
    setup() {
        this.state = useState({
                counter: 0,
        });
    }
    increment(){
        this.state.counter++;
    }
    decrement(){
        this.state.counter--;
    }
}
registry.category("actions").add('counter_app', CounterApp)