import React from "react";
import { useSelector } from 'react-redux';

function Home () {
  const state = useSelector(state => state);
  console.log(state);

  return (
    <div>
      <h2>This is the Home Page!</h2>
      <p>LoggedIn: {'' + state.loggedIn}</p>
    </div>
  );
}

export default Home;