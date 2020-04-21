import React from 'react';
import { act, render, cleanup, waitForElementToBeRemoved, waitForElement } from '@testing-library/react';
import axios from 'axios';
import uuid from 'uuid/v4';
import App from './App';

// Define a factory function to simplify
// stubbing out Gif data in the test
function Gif({ title, imageURL }) {
  return {
    id: uuid(),
    images: {
      fixed_width: {
        url: imageURL
      }
    },
    title
  };
}

const stubbedGifs = [
  Gif({
    title: 'Sad Gif',
    imageURL: '//media2.giphy.com.media/sad.gif'
  }),
  Gif({
    title: 'Funny Gif',
    imageURL: '//media2.giphy.com.media/funny.gif'
  }),
  Gif({
    title: 'Animated Gif',
    imageURL: '//media2.giphy.com.media/animated.gif'
  })
];

beforeEach(() => {
  axios.get = jest.fn(() => Promise.resolve({data: {data: stubbedGifs}}));
});

afterEach(cleanup);

describe('Gif Generator', () => {
  it('should display loading text while fetching', async () => {
    await act(async () => {
      const { getByText } = render(<App />);

      expect(getByText('...Loading')).toBeDefined();
    });
  });

  it('should remove loading text after receiving gifs', async () => {
    const { getByText } = render(<App />);

    await waitForElementToBeRemoved(() => getByText('...Loading'));
    // Removal is the final state of the component, all states are updated, no act needed
    // Using act will be better for test maintainability
  });

  it('should display the trnding gifs received from Giphy API', async () => {
    await act(async () => { // Here we can omit the act also
      const { getByAltText } = render(<App />);

      await waitForElement(() => getByAltText(stubbedGifs[0].title))
      getByAltText(stubbedGifs[1].title);
      getByAltText(stubbedGifs[2].title);
    });
  });
});
