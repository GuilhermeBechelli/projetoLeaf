// Função para remover itens expirados da tabela e exibir mensagem de expirado
function removerItensExpirados() {
  // Obtém todas as linhas da tabela
  var linhas = document.querySelectorAll('table tbody tr');

  // Percorre cada linha
  for (var i = 0; i < linhas.length; i++) {
    // Obtém as colunas "dthrAnuenciaMarinha" e "dthrAnuenciaPolicia"
    var colunaMarinha = linhas[i].querySelector('.dthrAnuenciaMarinha');
    var colunaPolicia = linhas[i].querySelector('.dthrAnuenciaPolicia');

    // Obtém a data atual
    var dataAtual = new Date();

    // Obtém a data de anuência da Marinha
    var dataMarinha = new Date(colunaMarinha.innerText);

    // Obtém a data de anuência da Polícia
    var dataPolicia = new Date(colunaPolicia.innerText);

    // Calcula a diferença em milissegundos entre a data atual e a data de anuência
    var diferencaMarinha = dataAtual - dataMarinha;
    var diferencaPolicia = dataAtual - dataPolicia;

    // Converte a diferença para horas
    var horasMarinha = diferencaMarinha / (1000 * 60 * 60);
    var horasPolicia = diferencaPolicia / (1000 * 60 * 60);

    // Verifica se passaram mais de 72 horas
    if (horasMarinha >= 72 && horasPolicia >= 72) {
      // Substitui o conteúdo das colunas pela mensagem "Expirado"
      colunaMarinha.innerText = 'Expirado';
      colunaPolicia.innerText = 'Expirado';
    }
  }
}

// Chama a função após 72 horas
setTimeout(removerItensExpirados, 72 * 60 * 60 * 1000);
