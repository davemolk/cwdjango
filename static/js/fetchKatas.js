document.getElementById('getC#').addEventListener('click', getKatas);
document.getElementById('getC++').addEventListener('click', getKatas);
document.getElementById('getGo').addEventListener('click', getKatas);
document.getElementById('getJava').addEventListener('click', getKatas);
document.getElementById('getJavaScript').addEventListener('click', getKatas);
document.getElementById('getPHP').addEventListener('click', getKatas);
document.getElementById('getPython').addEventListener('click', getKatas);
document.getElementById('getRuby').addEventListener('click', getKatas);
document.getElementById('getRust').addEventListener('click', getKatas);
document.getElementById('getScala').addEventListener('click', getKatas);
document.getElementById('getTypeScript').addEventListener('click', getKatas);


function getKatas(){
    fetch(`https://www.codewars.com/api/v1/users/davemolk/code-challenges/completed?`)
    .then(res => res.json())
    .then(data => {
        console.log('data', data);
        let output = '<h2 class="mb-4">Katas</h2>';
        data.data.forEach(kata => {
            output += `
                <ul class='list-group mb-3'>
                    <li class="list-group-item">ID: ${kata.id}</li>
                </ul>
                `
        })
        document.getElementById('output').innerHTML = output;
    })
}