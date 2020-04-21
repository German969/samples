import React from "react";
import { useSelector } from 'react-redux';
// import { fetchData } from "../store"; // If we need to fetch data in the server
// fetchData is a Redux Thunk action

function Home () {
  const state = useSelector(state => state);
  console.log(state);

  // const { circuits } = this.props;

  return (
    <div>
      <h2>This is the Home Page!</h2>
      <p>LoggedIn: {'' + state.loggedIn}</p>
    </div>
  );
}

// Home.serverFetch = fetchData; // static declaration of data requirements

export default Home;