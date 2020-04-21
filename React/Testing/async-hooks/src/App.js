import React from 'react';
import axios from 'axios';
import './App.css';

function useGiphyAPI() {
  const [gifs, setGifs] = React.useState(null);

  React.useEffect(() => {
    // Basic implementation to handle race conditions
    // When component might unmount before API call finishes
    // https://overreacted.io/a-complete-guide-to-useeffect/#speaking-of-race-conditions
    let isStopped = false;

    if (!isStopped) {
      const url = `http://api.giphy.com/v1/gifs/trending?api_key=${process.env.REACT_APP_GIPHY_API_KEY}&limit=3`;

      const getGifs = async () => {
        try {
          const { data: { data: gifs } } = await axios.get(url);

          if (!isStopped && gifs) {
            setGifs(gifs);
          }
        } catch (error) {
          console.log(error)
        }
      }

      getGifs();
    }

    return () => {
      isStopped = true;
    }
  }, []);

  return [gifs];
}

function App() {
  const [gifs] = useGiphyAPI();

  return (
    <>
      {
        gifs ? gifs.map(gif => (
          <img
            key={gif.id}
            src={gif.images.fixed_width.url}
            alt={gif.title}
          />
        )) : <p>...Loading</p>
      }
    </>
  );
}

export default App;
