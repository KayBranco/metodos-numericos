document.getElementById('methodForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const method = document.getElementById('method').value;
    const func = document.getElementById('function').value;
    const a = document.getElementById('a').value;
    const b = document.getElementById('b').value;

    fetch('/calculate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ method: method, function: func, a: a, b: b })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = `Raiz encontrada: ${data.result}`;

        // Gera o gráfico
        const trace = {
            x: data.x_values,
            y: data.y_values,
            mode: 'lines+markers',
            type: 'scatter'
        };
        
        const layout = {
            title: 'Gráfico da Função',
            xaxis: { title: 'x' },
            yaxis: { title: 'f(x)' }
        };

        Plotly.newPlot('plot', [trace], layout);
    });
});
