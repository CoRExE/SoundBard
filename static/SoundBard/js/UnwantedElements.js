// Sélection de l'élément à supprimer
const unwantedElement = document.querySelector('input[pseudo="file-selector-button"]');

// Vérification si l'élément existe
if (unwantedElement) {
    // Suppression de l'élément
    unwantedElement.remove();
}
