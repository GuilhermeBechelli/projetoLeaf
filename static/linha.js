function marcarLinha(linha) {
    // Remove a marcação de todas as linhas da tabela
    var linhas = linha.parentNode.getElementsByTagName("tr");
    for (var i = 0; i < linhas.length; i++) {
      linhas[i].classList.remove("marcada");
    }
  
    // Adiciona a marcação na linha clicada
    linha.classList.add("marcada");
  }
