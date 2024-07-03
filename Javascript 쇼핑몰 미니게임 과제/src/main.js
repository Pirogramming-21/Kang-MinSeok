function loadItems() {
    return fetch('data/data/json')
    .then(response => response.json())
    .then(json => json.items);
}
function displayItems (items){
    const container = document.querySelector('.items');
    container.innerHTML = items.map(item => createHTMLString(item)).join('');
}

function createHTMLString(item){
    return `
        <li class="item">
            <img src="${item.image}" alt="${item.type}" class="item__thumbnail" >
            <span class="item__description">${item.gender}, ${item.size}</span>
        </li>
        `;
}

function onButtonClick(event, items) {
    const dataset = event.target.dataset;
    const key = event.target.key;
    const value = event.target.value;

    if(key == null || value == null){
        return;
    }

    const filtered = items.filter(item => item[key] === value);
    displayItems(filtered);

}

function setEventListners (items) {
    const logo = document.querySelector('.logo');
    const buttons = document.querySelector('.buttons');
    logo.addEventListener('click', () => displayItems(itmes));
    buttons.addEventListener('click', () => onButtonClick(event, items));
}

//main
loadItems()
.then(items => {
    displayItems(items);
    setEventListners(items);
})
.catch(console.log);