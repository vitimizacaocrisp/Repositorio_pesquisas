// js/script.js

// Este arquivo pode ser usado para adicionar interatividade ao seu site.
// Por exemplo, você pode adicionar um botão de "voltar ao topo" ou animações.

document.addEventListener('DOMContentLoaded', () => {
    // Exemplo: console.log para verificar se o JS está carregado
    console.log('Script JavaScript carregado com sucesso!');

    //Se quiser adicionar um "scroll to top" button, aqui seria o lugar:
    const scrollToTopButton = document.createElement('button');
    scrollToTopButton.textContent = '⬆️ Topo';
    scrollToTopButton.style.position = 'fixed';
    scrollToTopButton.style.bottom = '20px';
    scrollToTopButton.style.right = '20px';
    scrollToTopButton.style.padding = '10px 15px';
    scrollToTopButton.style.backgroundColor = 'var(--primary-color)';
    scrollToTopButton.style.color = 'white';
    scrollToTopButton.style.border = 'none';
    scrollToTopButton.style.borderRadius = '5px';
    scrollToTopButton.style.cursor = 'pointer';
    scrollToTopButton.style.display = 'none'; // Hidden by default
    document.body.appendChild(scrollToTopButton);

    window.addEventListener('scroll', () => {
        if (window.scrollY > 200) { // Show button after scrolling 200px
            scrollToTopButton.style.display = 'block';
        } else {
            scrollToTopButton.style.display = 'none';
        }
    });

    scrollToTopButton.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
});