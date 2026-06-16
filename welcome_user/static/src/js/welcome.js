import { registry } from "@web/core/registry";

registry.category('services').add('welcome_popup'), {
    dependencies: ['action'],
    start(env, { action }){
        setTimeout(()=>{
            action.doAction('welcome_user.action_welcome');
        }, 2000)
    }
}

