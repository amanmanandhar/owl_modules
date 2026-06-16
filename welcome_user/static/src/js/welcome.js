/** @odoo-module **/

import { registry } from "@web/core/registry";

const welcomeService = {
    dependencies: ["action"],

    async start(env, { action }) {
        setTimeout(() => {
            action.doAction("welcome_user.action_welcome");
        }, 2000);
    },
};

registry.category("services").add("welcome_popup", welcomeService);