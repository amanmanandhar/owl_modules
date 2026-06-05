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
            editingId: null,
        });
    }
    addTask() {
    if (!this.state.task.trim()) {
        return;
    }

    if (this.state.editingId !== null) {
        const index = this.state.todos.findIndex(
            todo => todo.id === this.state.editingId
        );

        if (index !== -1) {
            this.state.todos[index].name = this.state.task;
        }

        this.state.editingId = null;
    } else {
        this.state.todos.push({
            id: Date.now(),
            name: this.state.task,
        });
    }

    this.state.task = "";
}
    editTask(id){
        const todo = this.state.todos.find(
            (todo) => todo.id === id
        );
        if (todo){
            this.state.task = todo.name;
            this.state.editingId = id;
        }
    }
    deleteTask = (id) => {
        this.state.todos = this.state.todos.filter(
            (todo) => todo.id !== id
        );
    }
}
registry.category('public_components').add("todo_app.TodoApp", TodoApp);