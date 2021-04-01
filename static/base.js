const menuList = document.querySelector('#fixed-nav__items1');
const menuItem1 = document.querySelector("#fixed-nav__menu1");
const menuItem2 = document.querySelector("#fixed-nav__menu2");
const menuItem3 = document.querySelector("#fixed-nav__menu3");
const menuItem4 = document.querySelector("#fixed-nav__menu4");
const menuItem5 = document.querySelector("#fixed-nav__menu5");

console.log(menuList)
const LinktoPage = function (event) {
    if (document.body.clientWidth<720) {
        
    } else if (event.target==menuItem1) {
        location.href = '/company/introduction/'
    } else if (event.target==menuItem2) {
        location.href = '/business/coast/'
    } else if (event.target==menuItem4) {
        location.href = '/board/notice/'
    } 
}
menuList.addEventListener('click', LinktoPage)


