const videoElement = document.getElementById('video');

// Access the user's camera
navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    // Attach the video stream to the video element
    videoElement.srcObject = stream;
    videoElement.play();
  })
  .catch(err => {
    console.error('Error accessing user media', err);
  });
