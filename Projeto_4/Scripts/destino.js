const user = localStorage.getItem('username');
let horaAtualizada = localStorage.getItem(`${user}_horaAtual`);
let caminho_morte = localStorage.getItem(`${user}_caminho_morte`);
let caminho_fugi = localStorage.getItem(`${user}_caminho_fugi`);

console.log('horaAtual:', horaAtualizada);
console.log('caminho_morte:', caminho_morte);
console.log('caminho_fugi:', caminho_fugi);

if (horaAtualizada >= 20) {
    if (caminho_morte === 'desbloqueado' || caminho_fugi === 'desbloqueado') {
        let timeoutId = setTimeout(() => {
            console.log('Redirecionando para cena_final1.html');
            window.location.href = '../cena_final1.html';
        }, 10000);

        window.addEventListener('hashchange', function() {
            console.log('Evento hashchange disparado');
            console.log('URL atual:', window.location.href);
            if (window.location.href.endsWith('html_salvo1') || window.location.href.endsWith('html_salvo2')) {
                console.log('Cancelando redirecionamento');
                clearTimeout(timeoutId);
            }
        }, false);
    } else {
        console.log('Redirecionando para cena_final1.html');
        window.location.href = '../cena_final1.html';
    }
}
