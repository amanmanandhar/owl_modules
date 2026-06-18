/** @odoo-module **/

import { Component, useState, mount } from "@odoo/owl";

export class AgeVerification extends Component {
    static template = 'age_verification.AgeVerificationTemplate';
    setup(){
        this.state = useState({
            showModal: localStorage.getItem("age_verified") !== "true",
        });
    }
    allowEntry(){
        localStorage.setItem("age_verified", 'true');
        this.state.showModal = false;
    }
    denyEntry(){
        window.location.href = "https://www.google.com";
    }
}
document.addEventListener("DOMContentLoaded", async () => {
    const root = document.createElement('div');
    root.id = 'age_verification_root';
    document.body.appendChild(root);
    await mount(AgeVerification, root)
});