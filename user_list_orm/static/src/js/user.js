/** @odoo-module **/

import { Component, useState, onWillStart } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { registry } from "@web/core/registry";

export class UserList extends Component {
    static template = "user_list_orm.Template";
    setup(){
        this.orm = useService("orm");
        this.notification = useService("notification");
        this.state = useState({
            users: [],
            editingUser: null,
        });
        onWillStart(async ()=>{
           await this.loadEmployees();
        });
    }
    async loadEmployees(){
        this.state.users = await this.orm.searchRead("res.users",[],["name","email","share"]);
    }
    async deleteUser(user){
        if(!user.share){
            this.notification.add("Cannot delete the internal user",{
                type: "danger",
            });
            return;
        }
        await this.orm.unlink('res.users',[user.id]);
        this.notification.add("User deleted successfully",{
            type: "success",
        });
        await this.loadEmployees()
    }
    editUser(user){
        this.state.editingUser = { ...user };
    }
    async saveUser(user){
        await this.orm.write('res.users',[this.state.editingUser.id], {
            name: this.state.editingUser.name,
            email: this.state.editingUser.email,
        });
        this.notification.add("User saved successfully",{
            type: "success",
        })
        this.state.editingUser = null;
        await this.loadEmployees();
    }
}
registry.category('public_components').add('user_list_view', UserList)