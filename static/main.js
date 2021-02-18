const fixedNav = document.querySelector('.fixed-nav');
const topBar = document.querySelector('.top-bar');
const fixedNavItem = document.querySelectorAll('.fixed-nav__items__item');
const fixedNavItems = document.querySelector('.fixed-nav__items');
const Body = document.querySelector('body');
const mainMenuItems = document.querySelector('.main__menu__items')

function dropDownMenu (event, index, text) {
    const dropDown1 = document.createElement('ul');
    dropDown1.setAttribute('class', 'drop-down');
    dropDown1.innerHTML = text
    fixedNavItem[index].appendChild(dropDown1)
    const Rect = event.target.getBoundingClientRect()
    dropDown1.style.position = 'fixed';
    dropDown1.style.left = Rect.x +'px';
    dropDown1.style.top = Rect.bottom -20 + 'px';
    dropDown1.style.width = Rect.width + 'px';   
    fixedNavItem[index].addEventListener('mouseleave', event => {
        const dropDown1 = document.querySelector('.drop-Down')
        dropDown1 && dropDown1.remove()
    })
}
window.addEventListener('scroll', () => {
    if (window.scrollY==0) {
        fixedNav.style.top = 30 +'px';
    } else {
        fixedNav.style.top = 0;
    }
    if ((window.scrollY + window.innerHeight) > mainMenuItems.getBoundingClientRect().top+100) {
        mainMenuItems.style.transform = 'translateY(-20px)'
        mainMenuItems.style.opacity = '1'
        mainMenuItems.style.transition = 'all ease-in 0.3s';

    }
})

fixedNavItems.addEventListener('mouseover', event => {
    if (event.target.id == 'nav_item1') {
        const index = 0;
        const innerHTML = `
        <li class='drop-down-item'>인사말</li>
        <hr>
        <li class='drop-down-item'>오시는 길</li>
        `
        dropDownMenu(event, index, innerHTML)
    }
    if (event.target.id == 'nav_item5') {
        const index = 4;
        const innerHTML = `
        <li class='drop-down-item'>공지사항</li>
        <hr>
        <li class='drop-down-item'>자료실</li>
        <hr>
        <li class='drop-down-item'>자유게시판</li>
        `
        dropDownMenu(event, index, innerHTML)
    }
})


