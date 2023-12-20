// tempo.js
let username = localStorage.getItem('username') || 'default';
let horaAtual = localStorage.getItem(`${username}_horaAtual`) || 22;
let minutoAtual = localStorage.getItem(`${username}_minutoAtual`) || 0;

function passouMinutos(minutos) {
  minutoAtual = Number(minutoAtual) + minutos;
  while (minutoAtual >= 60) {
    horaAtual = Number(horaAtual) + 1;
    minutoAtual -= 60;
  }
  // Se a hora atual for 24 ou mais, subtraia 24
  if (horaAtual >= 24) {
    horaAtual -= 24;
  }
  // Armazene a hora e os minutos atuais no localStorage
  localStorage.setItem(`${username}_horaAtual`, horaAtual);
  localStorage.setItem(`${username}_minutoAtual`, minutoAtual);
  atualizarRelogio();
}

function atualizarRelogio() {
  const relogio = document.querySelector('.relogio');
  relogio.textContent = `${horaAtual.toString().padStart(2, '0')}:${minutoAtual.toString().padStart(2, '0')}`;
}

function resetarTempo() {
  horaAtual = 22;
  minutoAtual = 0;
  // Armazene a hora e os minutos atuais no localStorage
  localStorage.setItem(`${username}_horaAtual`, horaAtual);
  localStorage.setItem(`${username}_minutoAtual`, minutoAtual);
  atualizarRelogio();
}
