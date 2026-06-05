/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import {DigitalClock} from "../../../../digital_clock/static/src/js/clock";

export class TodoApp extends Component {
    static template = 'todo_app.TodoAppTemplate';
    setup(){
        this.state = useState({
            task: "",
            todos: [],
        });
    }
    addTask(){
        if(!this.state.task.trim()){
            return;
        }
        this.state.todos.push({
            id: Date.now(),
            name: this.state.task,
        });
        this.state.task = "";
    }
    deleteTask = (id) => {
        this.state.todos = this.state.todos.filter(
            (todo) => todo.id !== id
        );
    }
}
registry.category('public_components').add("todo_app.TodoApp", TodoApp);