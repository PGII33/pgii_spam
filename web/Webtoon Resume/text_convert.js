
// Cette fonction permet de séparer du texte brut en catégories et en texte
function genererResume(texteBrut) {
    const lignes = texteBrut.split('\n');
    let resume = '<p>';

    for (const ligne of lignes) {
        // Détecter la catégorie et le texte associé
        const match = ligne.match(/(.*?):(.*)/);
        const is_link = ligne.match(/https/);
        if (is_link) {
            const categorie = match[1].trim();
            const texte = match[2].trim();
            resume += `<strong>${categorie} </strong>: <a href="${texte}">${texte}</a><br><br>`;
        } else
        if (match) {
            const categorie = match[1].trim();
            const texte = match[2].trim();
            resume += `<strong>${categorie} </strong>: ${texte}<br><br>`;
        }
    }
    
    resume += '</p>';

    return resume;
}

// Cette fonction permet le filtrage par genre
function filtrerParGenre() {
    const genreSelectionne = document.getElementById('genreFilter').value;
    const elementsWebtoon = document.getElementsByClassName('toggle-text');

    for (const element of elementsWebtoon) {
        if (genreSelectionne === 'tous' || element.classList.contains(genreSelectionne)) {
            element.style.display = 'block';
        } else {
            element.style.display = 'none';
        }
    }
}

// Déclaration des variables
let texteBrut = ""; // Le texte brut à convertir
let resumeWebtoon = ""; // La version html de ce texte

// The World After The Fall
texteBrut = `
Titre : The World After The Fall
Genre : Action
Statut : En cours
Nombre de chapitres : 85 chap
Taille d'un chapitre : Moyen / Long
Description : Lorsque l’apocalypse a éclaté, Jaehwan a été convoqué par la « Tour des cauchemars »...
Avis Personnel : Pas un simple système de tour le plus basique, on voit vraiment la façon de penser du personnage qui évolue...
Lien : https://www.webtoons.com/fr/action/the-world-after-the-fall/list?title_no=4193
Dernière date d'édition : 9/11/23
`;
resumeWebtoon = genererResume(texteBrut);
document.getElementById('The_World_After_the_Fall').innerHTML = resumeWebtoon;

// Villian To Kill
texteBrut = `
Titre : Villain To Kill
Genre : Action
Statut : En Cours
Nombre de chapitres : 112
Taille d'un chapitre : Moyen
Description : Cassian est un héros légendaire, un « psyker » de première classe qui a perdu la vie, injustement accusé du meurtre de son collègue. À son réveil, il se retrouve dans le corps d’un jeune élève et découvre qu’il est devenu un de ces « vilains » qu’il chassait dans sa vie précédente...! Cassian devra désormais compter sur « Moros » une mystérieuse créature, pour combattre le désir destructif qui s’empare constamment de son corps de vilain, afin de pouvoir se venger de ceux qui l’ont trahi dans sa vie passée. « Puisque c'est comme ça, je deviendrai le plus puissant des vilains à ma manière ! »
Avis Personnel : Ici encore sur un monde avec des ranks, mais finalement assez différent, je propose d'en lire un peu pour comprendre. Mais notre héro n'est pas un gentil, mais pas un méchant. Sa situation ambigüe est sympa à lire et peu de webtoon lui ressemble. Je le recommande (il y a plus de chapitre en anglais).
Lien : https://www.webtoons.com/fr/action/villaintokill/list?title_no=3443
Dernière date d'édition : 14/11/23
`;
resumeWebtoon = genererResume(texteBrut);
document.getElementById('Villain_To_Kill').innerHTML = resumeWebtoon;

// Verification du fonctionnement
console.log(resumeWebtoon)