(function() {
  'use strict';

  // Função para alternar o tema
  function setTheme(themeName) {
    localStorage.setItem('theme', themeName);
    document.documentElement.setAttribute('data-bs-theme', themeName);
  }

  // Função para alternar entre light e dark
  function toggleTheme() {
    if (localStorage.getItem('theme') === 'dark') {
      setTheme('light');
    } else {
      setTheme('dark');
    }
  }

  // Verifique se o usuário já tem uma preferência de tema salva
  (function () {
    if (localStorage.getItem('theme') === 'dark') {
      setTheme('dark');
    } else {
      setTheme('light');
    }
  })();

  // Adiciona evento ao botão de alternância de tema
  document.getElementById('bd-theme').addEventListener('click', function() {
    toggleTheme();
  });
})();
