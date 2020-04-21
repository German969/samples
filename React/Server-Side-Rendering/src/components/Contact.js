import React from "react";
import Helmet from "react-helmet";

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
            <Helmet>
              <title>Contact Page</title>
              <meta name="description" content="This is a proof of concept for React SSR" />
            </Helmet>
        );
    }
}