document.addEventListener('DOMContentLoaded', function() {
    const paginaAtual = window.location.pathname.split('/').pop(); // Obtém o nome da página atual
    const usuario = localStorage.getItem('username'); // Obtém o nome de usuário do localStorage
  
    if (usuario) {
      // Salva a página atual associada ao nome de usuário no localStorage
      localStorage.setItem(`${usuario}_pagina_atual`, paginaAtual);
    }
  });
  