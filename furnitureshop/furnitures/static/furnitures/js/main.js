// const ph0t0 = document.getElementByClass('ph0t0');
// const wrdandpht = ph0t0.wrdandpht;

// function checkAndRemove() {
//     if (wrdandpht.length > 2) {
//         for (let i = 2; i < wrdandpht.length; i++) {
//           wrdandpht[i].remove();
//         }
//     }
// }

// checkAndRemove();

const items = document.querySelectorAll('.wrdandpht .image');
items.forEach((image, index) => {
  if (index >= 3) {
    image.style.display = 'none';
  }
});