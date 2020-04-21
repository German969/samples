import express from "express";
import path from "path";

import React from "react";
import { renderToString } from "react-dom/server";
import Layout from "./components/Layout";

import { StaticRouter } from "react-router-dom";

import { Provider as ReduxProvider } from "react-redux";
import createStore, { initializeSession } from "./store";

const app = express();

app.use( express.static( path.resolve( __dirname, "../dist" ) ) );

app.get( "/*", ( req, res ) => {
  const context = {}; // Track potential redirects while rendering DOM (3XX res)
  const store = createStore(); // If we need to render parts of the DOM based on this state

  store.dispatch(initializeSession());

  const jsx = ( 
    <ReduxProvider store={ store }>
      <StaticRouter context={ context } location={ req.url }>
        <Layout />
      </StaticRouter>
    </ReduxProvider>
  );
  const reactDom = renderToString( jsx );

  const reduxState = store.getState();

  res.writeHead(200, { "Content-Type": "text/html" });
  res.end(htmlTemplate(reactDom, reduxState));
});

app.listen(2048);

function htmlTemplate(reactDom, reduxState) {
  return `
      <!DOCTYPE html>
      <html>
      <head>
          <meta charset="utf-8">
          <title>React SSR</title>
      </head>
        
      <body>
          <div id="app">${ reactDom }</div>
          <script>
            window.REDUX_DATA = ${ JSON.stringify(reduxState) }
          </script>
          <script src="./app.bundle.js"></script>
      </body>
      </html>
  `;
}
