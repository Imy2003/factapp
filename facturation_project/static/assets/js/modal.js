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
  


  document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("search-input");
    const tableBody = document.getElementById("table-body");

    searchInput.addEventListener("input", function () {
        const searchText = searchInput.value.toLowerCase();

        // Filtrer les lignes du tableau en fonction du texte saisi
        const rows = tableBody.getElementsByTagName("tr");
        for (const row of rows) {
            const cells = row.getElementsByTagName("td");
            let shouldDisplay = false;
            for (const cell of cells) {
                if (cell.textContent.toLowerCase().includes(searchText)) {
                    shouldDisplay = true;
                    break;
                }
            }
            row.style.display = shouldDisplay ? "" : "none";
        }
    });
});
