import { useState, useEffect, Component } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class ThrottleDebouceDemo extends Component{
    static template = 'throttle_debounce.ThrottleDebounceDemoTemplate';
    setup(){
        this.state = useState({
            text: '',
            mode: 'throttle',
            call: 0,
        });
        this.lastThrottleRun = 0;
        useEffect(
            () => {
                if (this.state.mode === "throttle") {
                    this.runThrottle();
                } else {
                    return this.runDebounce();
                }
            },
            () => [this.state.text, this.state.mode]
        );
    }
    runThrottle(){
        const now = Date.now();
        if (now - this.lastThrottleRun > 1000){
            this.lastThrottleRun = now;
            this.fakeApiCall();
        }
    }
    runDebounce(){
        const timer = setTimeout(()=>{
            this.fakeApiCall();
        }, 1000);
    }
    fakeApiCall(){
        this.state.calls++;
        console.log(`[${this.state.mode.toUpperCase()}] API Call:`,
        this.state.text
        );
    }
    onInput(ev){
        this.state.text = ev.target.value;
    }
    setThrottle(){
        this.state.mode = "throttle";
    }
    setDebounce(){
        this.state.mode = 'Debounce';
    }
}
registry.category('public_components').add('throttle_example',ThrottleDebouceDemo)