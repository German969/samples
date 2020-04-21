import React from "react";

export default class Home extends React.Component {
    constructor() {
        super();
        this.state = {
            subtitle: "This is the Home Page!"
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