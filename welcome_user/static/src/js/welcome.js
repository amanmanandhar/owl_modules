/** @odoo-module **/

import { registry } from "@web/core/registry";
import { rpc } from "@web/core/network/rpc";

const welcomeService = {
    dependencies: ["action"],

    async start(env, { action }) {
        const showWelcome = await rpc('/welcome_user/check', {});
        if (showWelcome) {
            setTimeout(() => {
                action.doAction("welcome_user.action_welcome");
            }, 2000);
        }
    },
};

registry.category("services").add("welcome_popup", welcomeService);