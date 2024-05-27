chrome.runtime.onMessage.addListener((message, sender) => {
  (async () => {

    // Kiểm tra xem đã đăng nhập 
    if (message.type === 'sets_side_panel') { 
      const { path } = message;
      await chrome.sidePanel.setOptions({
        path: path,
        enabled: true
      });
    } else if (message.type === 'open_side_panel') { 
      await chrome.sidePanel.open({tabId: sender.tab.id});
    } else if (message.type === 'close_side_panel') { 
      await chrome.sidePanel.setOptions({
        enabled: false
      });
      await new Promise(resolve => setTimeout(resolve, 100));
      await chrome.sidePanel.setOptions({
        enabled: true
      });
    }
  })();
});


let recorder;
let chunks = []; 
function saveToFile(blob, name) {
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement("a");
  document.body.appendChild(a);
  a.style = "display: none";
  a.href = url;
  a.download = name;
  a.click();
  URL.revokeObjectURL(url);
  a.remove();
  chunks = [];
}

const start = (streamId) => {
  navigator.mediaDevices.getUserMedia({
    audio: false,
    video: {
      mandatory: {
        chromeMediaSource: "tab",
        chromeMediaSourceId: streamId
      }
    }
  })
    .then((stream) => {
      recorder = new MediaRecorder(stream);
      chunks = [];
      recorder.ondataavailable = (e) => {
        chunks.push(e.data);
      }; 
      recorder.start();
    });
}

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  switch (message.type) {
    case "start":
      start(message.streamId);
      break;
    case "stop":
      recorder.stop();
      break;
    case "download":
      if (chunks.length > 0) {
        const blob = new Blob(chunks, { type: 'audio/webm' });
        saveToFile(blob, "test.webm");
      } 
      break;
  }

  return true;
});