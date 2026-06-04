/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class CounterApp extends Component{
    static template = "website_counter_owl.CounterTemplate"
    setup(){
        this.state = useState({
            count:0,
        });
    }
    increment(){
        this.state.count++;
    }
    decrement(){
        this.state.count--;
    }
}
registry.category("public_components").add("website_counter_owl.CounterApp",CounterApp)