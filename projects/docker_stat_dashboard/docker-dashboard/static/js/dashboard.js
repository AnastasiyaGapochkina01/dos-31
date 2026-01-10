const eventSource = new EventSource('/events');

eventSource.onmessage = function(event) {
    const containers = JSON.parse(event.data);
    updateContainers(containers);
};

function updateContainers(containers) {
    const containerDiv = document.getElementById('containers');
    containerDiv.innerHTML = '';
    
    containers.forEach(container => {
        const div = document.createElement('div');
        div.className = 'container';
        div.innerHTML = `
            <a href="/container/${container.Id}">${container.Names[0]}</a>
            <span class="status ${container.State}"></span>
        `;
        containerDiv.appendChild(div);
    });
}

function generateReport() {
    fetch('/report', { method: 'POST' })
        .then(response => response.json())
        .then(data => alert('Report generation started'));
}