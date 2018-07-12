document.getElementById("language").onchange = function() {myFuntion()};
let formLanguage = document.getElementById("form-language")

function myFuntion() {
    formLanguage.submit();
};

const quantity = document.getElementById("id_quantity");

const cartPrice = document.getElementById("cartPrice");
const cartTotal = document.getElementById("cartTotal");
const cartForm = document.getElementById("cartForm");
const orderQuantity = document.getElementById("orderQuantity");
const orderTotal = document.getElementById("orderTotal");
const orderBtn = document.getElementById("orderBtn");

let changeTotal = function(event) {
    orderQuantity.innerHTML = quantity.value;
    const price = parseFloat(cartPrice.innerHTML);
    const cantidad = parseFloat( quantity.value);
    const total = isNaN(price * cantidad) ? 0 : price * cantidad;

    cartTotal.innerHTML = total;
    orderTotal.innerHTML = total;
}
quantity.addEventListener('change', changeTotal);
quantity.addEventListener('keyup', changeTotal);

orderBtn.addEventListener('click', function() {
    cartForm.submit();
})