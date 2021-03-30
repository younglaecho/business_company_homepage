const fixedNav = document.querySelector('.fixed-nav');
const topBar = document.querySelector('.top-bar');
const fixedNavItem = document.querySelectorAll('.fixed-nav__items__item');
const fixedNavItems = document.querySelector('.fixed-nav__items');
const Body = document.querySelector('body');
const mainMenuItems = document.querySelector('.main__menu__items')


let index_mainImage = 1

const mainImage1 = document.querySelector('.main__sliding-image1')
const mainImage2 = document.querySelector('.main__sliding-image2')
const mainImage3 = document.querySelector('.main__sliding-image3')
const changeImage = function() {
    // console.log('time')
    if (index_mainImage== 1) {
        mainImage1.style.display = 0
        mainImage2.style.opacity = 1
        mainImage3.style.opacity = 0
    }
    if (index_mainImage== 2) {
        mainImage1.style.opacity = 0
        mainImage2.style.opacity = 0
        mainImage3.style.opacity = 1
    }
    if (index_mainImage== 3) {
        mainImage1.style.opacity = 1
        mainImage2.style.opacity = 0
        mainImage3.style.opacity = 0
        index_mainImage = 0
    }
    // mainImage.style.transform = "translateX("+(-100*index_mainImage)+"vw)"

    // if (index_mainImage==3) {
    //     mainImage.style.transform = "translateX(0vw)"
    //     index_mainImage = 0
    // }
    index_mainImage = index_mainImage + 1
}

let fadeTime = setInterval(changeImage,5000)

const mainButton = document.querySelector('.main__menu__buttonbox')
const business1 = document.querySelector('.main__menu__items__item1')
const business2 = document.querySelector('.main__menu__items__item2')
const business3 = document.querySelector('.main__menu__items__item3')
const business4 = document.querySelector('.main__menu__items__item4')
const business5 = document.querySelector('.main__menu__items__item5')
const businessButton1 = document.querySelector('.main__menu__button1')
const businessButton2 = document.querySelector('.main__menu__button2')
const businessButton3 = document.querySelector('.main__menu__button3')
const businessButton4 = document.querySelector('.main__menu__button4')
const businessButton5 = document.querySelector('.main__menu__button5')

mainButton.addEventListener('mouseover', event => {
    console.log(event.target)
    if (event.target.classList.contains('main__menu__button1')) {
        business1.style.opacity = 1
        business2.style.opacity = 0
        business3.style.opacity = 0
        business4.style.opacity = 0
        business5.style.opacity = 0
    }
    if (event.target.classList.contains('main__menu__button2')) {
        business1.style.opacity = 0
        business2.style.opacity = 1
        business3.style.opacity = 0
        business4.style.opacity = 0
        business5.style.opacity = 0

    }
    if (event.target.classList.contains('main__menu__button3')) {
        business1.style.opacity = 0
        business2.style.opacity = 0
        business3.style.opacity = 1
        business4.style.opacity = 0
        business5.style.opacity = 0

    }
    if (event.target.classList.contains('main__menu__button4')) {
        business1.style.opacity = 0
        business2.style.opacity = 0
        business3.style.opacity = 0
        business4.style.opacity = 1
        business5.style.opacity = 0

    }
    if (event.target.classList.contains('main__menu__button5')) {
        business1.style.opacity = 0
        business2.style.opacity = 0
        business3.style.opacity = 0
        business4.style.opacity = 0
        business5.style.opacity = 1

    }
})

// const changeBusiness = function() {
//     if (index_business== 1) {
//         business1.style.opacity = 0
//         business2.style.opacity = 1
//         business3.style.opacity = 0
//         business4.style.opacity = 0
//     }
//     if (index_business== 2) {
//         business1.style.opacity = 0
//         business2.style.opacity = 0
//         business3.style.opacity = 0
//         business4.style.opacity = 1
//     }
//     if (index_business== 3) {
//         business1.style.opacity = 1
//         business2.style.opacity = 0
//         business3.style.opacity = 0
//         business4.style.opacity = 0
//     }
//     if (index_business== 4) {
//         business1.style.opacity = 1
//         business2.style.opacity = 0
//         business3.style.opacity = 0
//         business4.style.opacity = 0
//     }
//     index_business = index_business + 1
// }

// function dropDownMenu (event, index, text) {
//     const dropDown1 = document.createElement('ul');
//     dropDown1.setAttribute('class', 'drop-down');
//     dropDown1.innerHTML = text
//     fixedNavItem[index].appendChild(dropDown1)
//     const Rect = event.target.getBoundingClientRect()
//     dropDown1.style.position = 'fixed';
//     dropDown1.style.left = Rect.x +'px';
//     dropDown1.style.top = Rect.bottom -20 + 'px';
//     dropDown1.style.width = Rect.width + 'px';   
//     fixedNavItem[index].addEventListener('mouseleave', event => {
//         const dropDown1 = document.querySelector('.drop-Down')
//         dropDown1 && dropDown1.remove()
//     });
// }



window.addEventListener('scroll', () => {
    // if (window.scrollY==0) {
    //     fixedNav.style.top = 30 +'px';
    // } else {
    //     fixedNav.style.top = 0;
    // }
    if ((window.scrollY + window.innerHeight) > mainMenuItems.getBoundingClientRect().top+100) {
        mainMenuItems.style.transform = 'translateY(-20px)'
        mainMenuItems.style.opacity = '1'
        mainMenuItems.style.transition = 'all ease-in 0.3s';
    }
})


// fixedNavItems.addEventListener('mouseover', event => {
//     if (event.target.id == 'nav_item1') {
//         const index = 0;
//         const innerHTML = `
//         <li class='drop-down-item'><a href="/introduction">인사말</a></li>
//         <hr>
//         <li class='drop-down-item'>오시는 길</li>
//         `
//         dropDownMenu(event, index, innerHTML)
//     }
//     if (event.target.id == 'nav_item5') {
//         const index = 3;
//         const innerHTML = `
//         <li class='drop-down-item'>공지사항</li>
//         <hr>
//         <li class='drop-down-item'>자료실</li>
//         <hr>
//         <li class='drop-down-item'>자유게시판</li>
//         `
//         dropDownMenu(event, index, innerHTML)
//     }
// })

// const scrollUnit = window.innerHeight * 8/9
// const toggleButton1 = document.querySelector('.toggle__button1') 
// const toggleButton2 = document.querySelector('.toggle__button2') 
// const toggleButton3 = document.querySelector('.toggle__button3')

// toggleButton1.addEventListener('click', () => {
//     window.scrollTo({
//         top:0,
//         behavior: 'smooth'
//     })
// })

// toggleButton2.addEventListener('click', () => {
//     window.scrollTo({
//         top:  scrollUnit,
//         behavior: 'smooth'
//     })
// })

// toggleButton3.addEventListener('click', () => {
//     window.scrollTo({
//         top: scrollUnit*2,
//         behavior: 'smooth'
//     })
// })

