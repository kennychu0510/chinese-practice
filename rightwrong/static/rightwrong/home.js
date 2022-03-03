const words = document.querySelectorAll('td');
words.forEach(element => {
    element.style.cursor = "pointer";
});

const wordPair = document.querySelectorAll('tr')
wordPair.forEach(element => {
    let rightWord = element.querySelector('td');
    let wrongWord = element.querySelector('td:last-child');
    const id = parseInt(element.querySelector('input').value);

    let changed = false;

    if (Math.floor(Math.random() * 3) + 1 === 1) {
        temp = rightWord.innerHTML;
        rightWord.innerHTML = wrongWord.innerHTML;
        wrongWord.innerHTML = temp;
        changed = true;
    }

    let finalRightWord;
    let finalWrongWord;
    if (changed) {
        finalRightWord = element.querySelector('td:last-child');
        finalWrongWord = element.querySelector('td');

    } else {
        finalRightWord = element.querySelector('td');
        finalWrongWord = element.querySelector('td:last-child');
    };

    // Retreive score on page


    // when right word is clicked
    finalRightWord.onclick = function () {
        fetch(`/${id}`, {
            method: 'PUT',
            body: JSON.stringify({
                correct: true
            })
        });
        finalRightWord.className = "table-success";

        // Updates score when correct word is clicked
        let score = parseInt(document.querySelector("#score").innerHTML);
        score++;
        document.querySelector("#score").innerHTML = score;

        // Disable button after one click
        finalRightWord.onclick = null;
        finalWrongWord.onclick = null;
        finalRightWord.style.cursor = "auto";
        finalWrongWord.style.cursor = "auto";
    };

    // when wrong word is clicked
    finalWrongWord.onclick = function () {
        fetch(`/${id}`, {
            method: 'PUT',
            body: JSON.stringify({
                correct: false
            })
        });
        finalWrongWord.className = "table-danger";

        // Disable button after one click
        finalWrongWord.onclick = null;
        finalRightWord.onclick = null;
        finalWrongWord.style.cursor = "auto";
        finalRightWord.style.cursor = "auto";
    }
});

// refresh page when New is selected
document.querySelector('#refresh').onclick = () => window.location.reload();

// redirect to statistics
