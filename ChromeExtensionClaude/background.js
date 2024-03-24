// chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
//     if (message.action === 'storeData') {
//         chrome.storage.local.get('history', function(result) {
//             var history = result.history || [];
//             history.push({ url: message.url, content:message.content });
//             chrome.storage.local.set({ history: history });
//
//             const apiKey = 'Claude-API'; // Replace with your actual Claude API key
//             const url = 'https://www.anthropic.com/api/';
//             console.log(message)
//             console.log(message.content)
//             // var sanitizedContent = message.content.replace(/[^\w\s]/gi, '');
//
//             // console.log(sanitizedContent)
//
//             fetch('https://webhook.site/01f90e51-9dd3-4253-ac73-97e5c30cea9b', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json'
//                 },
//                 body: JSON.stringify({
//                     url: message.url,
//                     content: message.content
//                 })
//             })
//                 .then(response => response.text())
//
//         });
//     }
// });

chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
    if (message.action === 'storeData') {
        // Store data in chrome.storage.local as before
        chrome.storage.local.get('history', function(result) {
            var history = result.history || [];
            // history.push({ url: message.url, content: message.content, });
            history.push({ url: message.url, prompt:message.prompt_text });
            chrome.storage.local.set({ history: history });
        });

    } else if (message.action === 'sendHistory') {
        // Send stored history to webhook
        chrome.storage.local.get('history', function(result) {
            const history = result.history || [];
            const finaldata = {"username":"Sainu","urls_and_summaries":history}
            fetch('http://localhost:8000/api/projects/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                // body: JSON.stringify(history)
                body: JSON.stringify(finaldata)
            })
                .then(response => response.text())
        });
    }
});

// chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
//     if (message.action === 'storeData') {
//         chrome.storage.local.get('history', function(result) {
//             var history = result.history || [];
//             history.push({ url: message.url, content: message.content });
//             chrome.storage.local.set({ history: history });
//         });
//     } else if (message.action === 'sendHistory') {
//         chrome.storage.local.get(['history', 'prompt'], function(result) {
//             const history = result.history || [];
//             const prompt = result.prompt || ''; // Extract prompt from storage
//             const dataToSend = { history: history, prompt: prompt }; // Include prompt and history in the data
//             console.log(dataToSend)
//             fetch('https://webhook.site/f17dfe18-5fd3-4429-9d51-ee725ce055df', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json'
//                 },
//                 body: JSON.stringify(dataToSend)
//             })
//                 .then(response => response.text())
//                 .then(data => {
//                     console.log('Webhook response:', data);
//                 });
//         });
//     }
// });



