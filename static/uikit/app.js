
// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  // hljs.highlightAll();
});

console.log('JS loaded')
let alertWrapper = document.querySelector('.alert')
let alertClose = document.querySelector('.alert__close')

if (alertWrapper) {
  console.log('JS loaded')
  alertClose.addEventListener('click', () =>
    alertWrapper.style.display = 'none'
  )
}