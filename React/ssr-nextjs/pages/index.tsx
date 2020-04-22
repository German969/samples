// add links in index.tsx
import Link from 'next/link';

const Index = () => (
  <div>
    <p>SSR with Next.js+ react + redux + redux-saga + jest</p>
    { /*static link*/ }
    <Link href="about">
      <a>About</a>
    </Link>
    { /*dynamic link*/ }
    <Link href="/product/[id]" as={`/product/${1}`}>
      <a>Product 1</a>
    </Link>
  </div>
);

export default Index;