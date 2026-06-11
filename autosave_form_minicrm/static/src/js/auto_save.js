/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { useService } from "@web/core/utils/hook";
import { registry } from "@web/core/registry";

export class AutoSaveForm extends Component {
    static template = 'autosave_form_minicrm.AutoSaveFormTemplate';
    setup(){
        this.orm = useService('orm');
        this.state = useState({
            id: "",
            name: "",
            email: "",
            phone: "",
            saveStatus: "",
        });
        this.saveTimeout = null;
    }
    onInput(field, ev){
        this.state[field] = ev.target.value;
        clearTimeout(this.saveTimeout);
        this.saveTimeout = setTimeout(() => {
            this.autoSave();},1000);
    }
    async autoSave(){
        try {
            this.state.saveStatus = "saving...";
            const vals = {
                name: this.state.name,
                email: this.state.email,
                phone: this.state.phone,
            };
            if (this.state.id) {
                await this.orm.write(
                    'crm.lead',
                    [this.state.id],
                    vals
                );
            } else {
                this.state.id = await this.orm.create(
                    'crm.lead',
                    [vals]
                );
            }
            this.state.saveStatus = "Saved";
        } catch (error) {
            console.error(error);
            this.state.saveStatus = "Failed";
        }
    }
}
registry.category('public_components').add('auto_save_form', AutoSaveForm);