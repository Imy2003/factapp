// static/invoices/modal.js
document.addEventListener('DOMContentLoaded', function() {
    const modalButtons = document.querySelectorAll('.modal-button');
    const modals = document.querySelectorAll('.modal');
  
    modalButtons.forEach(button => {
      button.addEventListener('click', () => {
        const targetModal = document.querySelector(button.dataset.modalTarget);
        modals.forEach(modal => modal.classList.remove('show'));
        targetModal.classList.add('show');
      });
    });
  
    modals.forEach(modal => {
      modal.addEventListener('click', event => {
        if (event.target === modal) {
          modal.classList.remove('show');
        }
      });
    });
  });
  const menuBtn = document.querySelector('.menu-btn');
  const hiddenMenu = document.querySelector('.hidden-menu');
  
  menuBtn.addEventListener('click', () => {
    hiddenMenu.classList.toggle('menu-open');
  });
  