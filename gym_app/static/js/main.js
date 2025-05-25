console.log('This is JS from your page!!')

let timer;
let isRunning = false;
let timeLeft = 0;

const timerDisplay = document.getElementById('timer');
const startBtn = document.getElementById('startBtn');
const pauseBtn = document.getElementById('pauseBtn');
const resetBtn = document.getElementById('resetBtn');
const minutesInput = document.getElementById('minutes');

function updateDisplay(seconds) {
    const mins = Math.floor(seconds / 60).toString().padStart(2, '0');
    const secs = (seconds % 60).toString().padStart(2, '0');
    timerDisplay.textContent = `${mins}:${secs}`;
}

function startTimer() {
    if (!isRunning) {
        if (timeLeft === 0) {
            timeLeft = parseInt(minutesInput.value) * 60;
        }
        isRunning = true;
        timer = setInterval(() => {
            timeLeft--;
            updateDisplay(timeLeft);

            if (timeLeft <= 0) {
                clearInterval(timer);
                isRunning = false;
                // Play a sound or show alert when timer ends
                alert('Time is up!');
            }
        }, 1000);
    }
}

function pauseTimer() {
    clearInterval(timer);
    isRunning = false;
}

function resetTimer() {
    pauseTimer();
    timeLeft = 0;
    updateDisplay(timeLeft);
    minutesInput.value = 5;
}

startBtn.addEventListener('click', startTimer);
pauseBtn.addEventListener('click', pauseTimer);
resetBtn.addEventListener('click', resetTimer);

// Initialize display
updateDisplay(0);