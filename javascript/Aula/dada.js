let sequencia = [0, 1];
n = 8

  for (let i = 2; i < n; i++) {
    let proximo = sequencia[i - 1] + sequencia[i - 2];
    sequencia.push(proximo);
    console.log(sequencia)
    
  }