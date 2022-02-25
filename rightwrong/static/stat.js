const words = document.querySelectorAll('tr:not(:first-child)');

words.forEach(word => {

    const attempts = parseInt(word.querySelector('#attempts').innerHTML);
    const corrects = parseInt(word.querySelector('#corrects').innerHTML);
    let percentage = corrects / attempts * 100;
    if (isNaN(percentage)) {
        percentage = 0;
    }
    word.querySelector('#percentage').innerHTML = Math.round(percentage);
})
