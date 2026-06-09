/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { registry } from "@web/core/registry";

export class UserList extends Component {
    static template = "user_list_orm.Template";
    setup(){
        this.orm = useService("orm");
        this.state = useState({
            users: [],
        });
    }
    async loadEmployees(){
        this.state.users = await this.orm.searchRead("res.users",[],["name","email"]);
    }
}
registry.category('public_components').add('user_list_view', UserList)