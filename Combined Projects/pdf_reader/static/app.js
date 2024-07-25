function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

function formatSummary(summary) {
    return `<div class="result">
        <p><strong>Ответ:</strong> ${capitalizeFirstLetter(summary)}</p>
    </div>`;
}

function submitQuery() {
    const fileInput = document.getElementById('pdfFile');
    const queryInput = document.getElementById('query');
    const responseArea = document.getElementById('responseArea');

    const file = fileInput.files[0];
    const query = queryInput.value;

    if (!file || !query) {
        responseArea.textContent = "Please upload a PDF file and enter a query.";
        return;
    }

    const formData = new FormData();
    formData.append('file', file);
    formData.append('query', query);

    fetch('/analyze', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            responseArea.textContent = 'Error: ' + data.error;
        } else {
            responseArea.innerHTML = formatSummary(data.summary);
        }
    })
    .catch(error => {
        responseArea.textContent = 'Error: ' + error.message;
    });
}