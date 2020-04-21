import React from "react";

export default class About extends React.Component {
    constructor() {
        super();
        this.state = {
            subtitle: "About us!"
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