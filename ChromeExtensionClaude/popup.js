document.addEventListener('DOMContentLoaded', function() {
    const historyList = document.getElementById('historyList');
    const clearDataButton = document.getElementById('clearData');
    const sendHistoryButton = document.getElementById('sendHistory'); // New button
    const prompt= document.getElementById('prompt'); // prompt

    clearDataButton.addEventListener('click', function() {
        chrome.storage.local.set({ history: [] }, function() {
            historyList.innerHTML = '';
        });
    });

    sendHistoryButton.addEventListener('click', function() {
        chrome.runtime.sendMessage({ action: 'sendHistory' }, function(response) {
            console.log('Stored history sent to webhook');
            // Handle response if needed
        });
    });

    chrome.storage.local.get('history', function(data) {
        const history = data.history || [];
        history.forEach(function(item) {
            const li = document.createElement('li');
            li.textContent = `URL: ${item.url}`;
            historyList.appendChild(li);
        });
    });
    document.getElementById('textInput').addEventListener('input', function(event) {
        // Retrieve the value of the textbox
        var textValue = event.target.value;

        // Store the value in Chrome storage
        chrome.storage.sync.set({ 'textboxValue': textValue }, function() {
            // Notify the user that the value has been saved
            console.log('Value saved to Chrome storage:', textValue);
        });
    });
    chrome.storage.sync.get('textboxValue', function(data) {
        var lastPrompt = data.textboxValue;
        console.log(lastPrompt)
        if (lastPrompt) {
            document.getElementById('textInput').value = lastPrompt;
        } else {
            document.getElementById('textInput').value = "Summarized what I worked today?";
        }
    });
});


