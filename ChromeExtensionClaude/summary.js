chrome.storage.local.get('history', function(data) {
    const history = data.history || [];
    const latestSummary = history[history.length - 1];

    if (latestSummary) {
        document.getElementById('url').textContent = `URL: ${latestSummary.url}`;
        document.getElementById('summary').textContent = `Summary: ${latestSummary.summary}`;
    }
});