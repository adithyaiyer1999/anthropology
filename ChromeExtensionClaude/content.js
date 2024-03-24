// function extractTextContent(node) {
//     if (node.nodeType === Node.TEXT_NODE) {
//         return node.textContent;
//     } else {
//         let text = '';
//         for (let i = 0; i < node.childNodes.length; i++) {
//             text += extractTextContent(node.childNodes[i]);
//         }
//         return text;
//     }
// }
//
// const textContent = extractTextContent(document.body); //---> working one

let prompt = '';
chrome.storage.sync.get('textboxValue', function(data) {
    prompt = data.textboxValue || ''; // Retrieve prompt from the saved sync variable
    chrome.runtime.sendMessage({ action: 'storeData', url: window.location.href, prompt_text: prompt });
});

// chrome.runtime.sendMessage({ action: 'storeData', url: window.location.href, content: textContent });
// chrome.runtime.sendMessage({ action: 'storeData', url: window.location.href, content: textContent }); ---> working one
// chrome.runtime.sendMessage({ action: 'storeData', url: window.location.href, content: textContent ,prompt_text: document.getElementById('textInput').value});

// Listen for messages from the popup script
// chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
//     if (message.action === 'storeData') {
//         const textContent = extractTextContent(document.body);
//         const prompt = ; // Retrieve prompt from the text input field
//         chrome.runtime.sendMessage({ action: 'storeData', url: window.location.href, content: textContent, prompt: prompt });
//     }
// });


// content.js

// function extractTextContent(node) {
//     if (node.nodeType === Node.TEXT_NODE) {
//         return node.textContent;
//     } else {
//         let text = '';
//         for (let i = 0; i < node.childNodes.length; i++) {
//             text += extractTextContent(node.childNodes[i]);
//         }
//         return text;
//     }
// }
//
// chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
//     if (message.action === 'sendPrompt') {
//         const textContent = extractTextContent(document.body);
//         const prompt = message.prompt; // Retrieve prompt value from the message
//         chrome.runtime.sendMessage({ action: 'storeData', url: window.location.href, content: textContent, prompt: prompt });
//     }
// });

