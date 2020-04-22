import fetch from 'isomorphic-unfetch';

export async function getSampleContent() {
  const response = await fetch('https://jsonplaceholder.typicode.com/todos');
  const body = await response.json();

  if (response.status !== 200) throw Error(body.message);

  return body;
}