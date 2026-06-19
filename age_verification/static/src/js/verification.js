/** @odoo-module **/

import { Component, useState, mount } from "@odoo/owl";

console.log("AGE VERIFICATION JS LOADED");

export class AgeVerification extends Component {
    static template = "age_verification.AgeVerificationTemplate";

    setup() {
        console.log("COMPONENT SETUP");

        this.state = useState({
            showModal: localStorage.getItem("age_verified") !== "true",
        });
    }

    allowEntry() {
        console.log("ALLOW CLICKED");

        localStorage.setItem("age_verified", "true");
        this.state.showModal = false;
    }

    denyEntry() {
        console.log("DENY CLICKED");

        window.location.href = "https://www.google.com";
    }
}

async function start() {
    try {
        console.log("START CALLED");

        let root = document.getElementById("age_verification_root");

        if (!root) {
            root = document.createElement("div");
            root.id = "age_verification_root";
            document.body.appendChild(root);
            console.log("ROOT CREATED");
        }

        await mount(AgeVerification, {
            target: root,
        });

        console.log("COMPONENT MOUNTED");
    } catch (error) {
        console.error("AGE VERIFICATION ERROR:", error);
    }
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
} else {
    start();
}