import React from "react";

export default class Contact extends React.Component {
    constructor() {
        super();
        this.state = {
            subtitle: "Send us a message!"
        };
    }

    render() {
        return (
            <div>
                <h2>{ this.state.subtitle }</h2>
            </div>
        );
    }
}