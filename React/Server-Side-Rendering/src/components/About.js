import React from "react";
import Helmet from "react-helmet";

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
            <Helmet>
              <title>About Page</title>
              <meta name="description" content="This is a proof of concept for React SSR" />
            </Helmet>
        );
    }
}