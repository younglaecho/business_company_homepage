const menuList = document.querySelector("#fiexed-nav__items")
const menuItem1 = document.querySelector("#fiexed-nav__menu1")
const menuItem2 = document.querySelector("#fiexed-nav__menu2")
const menuItem3 = document.querySelector("#fiexed-nav__menu3")
const menuItem4 = document.querySelector("#fiexed-nav__menu4")
const menuItem5 = document.querySelector("#fiexed-nav__menu5")

const LinktoPage = function (event) {
    if (document.body.clientWidth<720) {
        
    } else if (event.target==menuItem1) {
        console.log(event.target)
        location.href = '/company/introduction/'
    } else if (event.target==menuItem2) {
        location.href = '/business/coast/'
    } else if (event.target==menuItem3) {
        location.href = '/qanda/'
    } else if (event.target==menuItem4) {
        location.href = '/board/notice/'
    } else if (event.target==menuItem5) {
        location.href = '/recruit/'
    }
}
menuList.addEventListener('click', LinktoPage(evnet))


