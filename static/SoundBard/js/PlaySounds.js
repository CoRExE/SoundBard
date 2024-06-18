document.querySelectorAll('.sound-button').forEach(button => {
    button.addEventListener('click', () => {
        const soundId = button.value;
        const audio = document.getElementById('audio' + soundId);
        if (audio.readyState >= 2) { // Check if audio is loaded and ready to play
            audio.play();
        } else {
            console.error('Audio is not ready to play');
        }
    });
});

console.log('PlaySounds.js loaded');

function playSound(soundId) {
    const audio = document.getElementById('audio' + soundId);
    if (audio.readyState >= 2) { // Check if audio is loaded and ready to play
        audio.play();
    } else {
        console.error('Audio is not ready to play');
    }
}

function stopSound(soundId) {
    const audio = document.getElementById('audio' + soundId);
    audio.pause();
    audio.currentTime = 0;
}

function stopAllSounds() {
    document.querySelectorAll('.sound-button').forEach(button => {
        const soundId = button.value;
        stopSound(soundId);
    });
}