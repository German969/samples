function transpose(a) {

  let i, j, t = [];

  for(i=0; i<3; i++) {

    t[i] = [];

    for(j=0; j<3; j++) {
      t[i][j] = a[j][i];
    }
  }

  return t;
}

function traverseDiag(array){
  //[[1,2,3],[4,5,6],[7,8,9]]

    let t = [[],[],[]];

    i = 0;

    for (let k = 0; k <= 2 * (array.length - 1); k++) {
    //de 0 hasta 4
    //En que filas me muevo
    let yMin = Math.max(0, k - array.length + 1);
    let yMax = Math.min(array.length - 1, k);
    // 0,0 0,1 0,2 1,2 2,2

    for (let y = yMin; y <= yMax; y++) {
        //0,1
        //x -> 1-0
        //x -> 1-1
        //array(0,1), array(1,0)
        let x = k - y;
        console.log(array[y][x]);

        let x2 = k == 0 || k == 4 ? k : k-1;
        let y2 = i % 3;

        t[x2][y2] = array[y][x];

    }

    return t;
}}

function traverseDiagReverse(array){
  for (let k = 0; k <= 2 * (array.length - 1); k++) {
    let yMin = Math.max(0, k - array.length + 1);
    let yMax = Math.min(array.length - 1, k);
    for (let y = yMin; y <= yMax; y++) {
        let x = k - y;
        console.log(array[y][x]);
    }
    console.log('--');
}