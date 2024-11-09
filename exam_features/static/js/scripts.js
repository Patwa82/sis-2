document.addEventListener('DOMContentLoaded', function () {
    console.log("Examination Features JS Loaded.");

    // Form validation for the file upload
    const examForm = document.querySelector('form');
    if (examForm) {
        examForm.addEventListener('submit', function (e) {
            const examFileInput = document.querySelector('input[type="file"]');
            const examFile = examFileInput.files[0];

            if (!examFile) {
                alert("Please upload the exam file before submitting.");
                e.preventDefault();
            }
        });
    }

    // Timer functionality for exams (client-side timer for demo purposes)
    const examStartTimeElement = document.getElementById('exam-start-time');
    const examEndTimeElement = document.getElementById('exam-end-time');
    const timerElement = document.getElementById('timer');

    if (examStartTimeElement && examEndTimeElement && timerElement) {
        const startTime = new Date(examStartTimeElement.innerText);
        const endTime = new Date(examEndTimeElement.innerText);
        const now = new Date();

        if (now >= startTime && now <= endTime) {
            const timeRemaining = Math.floor((endTime - now) / 1000); // Time remaining in seconds
            updateTimer(timeRemaining);

            const countdownInterval = setInterval(() => {
                if (timeRemaining <= 0) {
                    clearInterval(countdownInterval);
                    alert("Exam time is over.");
                } else {
                    updateTimer(--timeRemaining);
                }
            }, 1000);
        }
    }

    function updateTimer(timeRemaining) {
        const minutes = Math.floor(timeRemaining / 60);
        const seconds = timeRemaining % 60;
        timerElement.innerText = `Time Remaining: ${minutes}m ${seconds}s`;
    }
});
