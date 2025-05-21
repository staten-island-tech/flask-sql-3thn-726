window.onload = () => {
    const bubbles = document.querySelectorAll('.bubble');
    bubbles.forEach(bubble => {
        bubble.style.left = Math.random() * 90 + '%';
        bubble.style.top = Math.random() * 90 + '%';
    });
};
